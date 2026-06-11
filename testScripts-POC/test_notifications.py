import random

import pytest

from C2CModules.notifications import notification_createBroadcastGroup, \
    notification_broadcastMessage, notification_message_new, notification_message
from C2CModules.primary_IVI_device_modules import getVIN, get_SystemId
from utils.XLUtils import read_api_data_from_excel
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset, b2c_ivi_chipset

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Notifications:

    # Notification_message
    @pytest.mark.Smoke
    def test1_positive_notification_msg(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            message = str(dict1["Message"])

            print("Initiate notification via post api : ")
            print("VIN :", vin)
            print("System Id :", systemId)
            print("Message :", message)
            print("---------------------------------------")

            # Call notification reusable module
            response = notification_message(self, vin, systemId, message)

            print("Notification is initiated")

            print("----------------------------")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # ===========================================================================================
            # Initiate notification
            # ===========================================================================================

            print("Initiate notification via post api : ")
            print("---------------------------------------")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            print("Initiated message Id : ", msg_id)

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("VIN :", vin)
            print("System Id :", systemId)
            print("Message :", msg_id)

            response_body = notification_message(self, vin, systemId, msg_id)

            print("Notification is initiated")

            print("---------------------------")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast
    @pytest.mark.Smoke
    def test2_positive_notification_createBroadcastGroup(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            groupName = 'broadcast_group' + str(msg_id)

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "valid")

        # Validate response code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message
    @pytest.mark.Smoke
    def test3_positive_notification_broadcastMessage(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "broadcast_msg_title"
            message = "Message is broadcast"

        # Call subscribe reusable module
        # groupName= "%2B"
        response = notification_broadcastMessage(self, groupName, title, message, "valid")

        # Validate response code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")

        print("----------------------------------------------------------")

    # - Negative TCs
    # Notification - Group Broadcast - duplicate group name
    @pytest.mark.Smoke
    def test1_negative_notification_createBroadcastGroup_duplicate_groupName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_with_duplicate_groupName")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast123"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "valid")

        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "valid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11115")
        assert ("Group name and system id is already exit" in response_body["errors"][0]["message"])

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - invalid VIN
    @pytest.mark.Smoke
    def test2_negative_notification_createBroadcastGroup_invalid_VIN(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_with_invalid_VIN")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = "VIn123"
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11115")
        assert ("Group name and system id is already exit" in response_body["errors"][0]["message"])

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - empty VIN
    @pytest.mark.Smoke
    def test3_negative_notification_createBroadcastGroup_empty_VIN(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_with_empty_VIN")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ""
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = ""
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - without VIN field
    @pytest.mark.Smoke
    def test4_negative_notification_createBroadcastGroup_without_VIN_field(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_without_VIN_field")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid_without_VIN_field")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - with invalid system id
    @pytest.mark.Smoke
    def test5_negative_notification_createBroadcastGroup_with_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_with_invalid_systemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6109")
        assert (response_body["errors"][0]["message"] == "Given system id length is not valid")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - with empty system id
    @pytest.mark.Smoke
    def test6_negative_notification_createBroadcastGroup_with_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_with_empty_systemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6109" or response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given system id length is not valid" or response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty" )
        # assert (response_body["errors"][1]["errorCode"] == "6112")
        # assert (response_body["errors"][1]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - with incorrect system id
    @pytest.mark.Smoke
    def test7_negative_notification_createBroadcastGroup_with_incorrect_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_with_incorrect_systemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6109" or response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given system id length is not valid" or response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - without system id field
    @pytest.mark.Smoke
    def test8_negative_notification_createBroadcastGroup_without_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_without_systemId_field")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid_without_systemId_field")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6109" or response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given system id length is not valid" or
                response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - without groupname field
    @pytest.mark.Smoke
    def test9_negative_notification_createBroadcastGroup_without_groupName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_without_groupName_field")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid_without_groupName_field")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11113")
        assert (response_body["errors"][0]["message"] == "Group name cannot be null or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - with empty groupname
    @pytest.mark.Smoke
    def test10_negative_notification_createBroadcastGroup_with_empty_groupName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_with_empty_groupName")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
            if groupName == "None":
                groupName = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = ""

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11113")
        assert (response_body["errors"][0]["message"] == "Group name cannot be null or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - without group field
    @pytest.mark.Smoke
    def test11_negative_notification_createBroadcastGroup_without_group(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup_without_group_field")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid_without_group_field")

        # Validate response code
        assert (response.status_code == 500), "Status code is not 500. Rather found : " + str(
            response.status_code)

        print("----------------------------------------------------------")

    # Notification - Group Broadcast - without vin & system field
    @pytest.mark.Smoke
    def test12_negative_notification_createBroadcastGroup_without_vinSystem_field(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_without_vinSystemId_field")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName,
                                                     "invalid_without_vinSystemId_field")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "6112")
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Notification - Group Broadcast with existing systemId & group Name
    @pytest.mark.Smoke
    def test13_positive_notification_createBroadcastGroup_with_existing_vinSystemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification",
                                         "Notification_createBroadcastGroup_with_existing_vinSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response_1 = notification_createBroadcastGroup(self, systemId, vin, groupName, "valid")

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "valid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11115")
        assert ("Group name and system id is already exit" in response_body["errors"][0]["message"])

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  invalid group name
    @pytest.mark.Smoke
    def test14_negative_notification_broadcastMessage_invalid_groupName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage_invalid_groupName")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "#$"
            title = "broadcast_msg_title"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11114")
        assert (response_body["errors"][0]["message"] == "Group name is not valid")

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  empty group name
    @pytest.mark.Smoke
    def test15_negative_notification_broadcastMessage_empty_groupName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage_empty_groupName")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            if groupName == "None":
                groupName = ""
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = ""
            title = "broadcast_msg_title"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "invalid")

        # Validate response code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["errors"][0]["errorCode"] == "11114")
        assert (response_body["errors"][0]["message"] == "Group name is not valid")

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  empty title
    @pytest.mark.Smoke
    def test16_negative_notification_broadcastMessage_empty_title(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage_empty_title")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            if title == "None":
                title = ""
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = ""
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "invalid")

        # Validate response code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  empty message
    @pytest.mark.Smoke
    def test17_negative_notification_broadcastMessage_empty_message(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage_empty_message")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
            if message == "None":
                message = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = ""

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "invalid")

        # Validate response code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")
        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  invalid apiKey
    @pytest.mark.Smoke
    def test18_negative_notification_broadcastMessage_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "invalid_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  empty apiKey
    @pytest.mark.Smoke
    def test19_negative_notification_broadcastMessage_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "empty_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  no apiKey
    @pytest.mark.Smoke
    def test20_negative_notification_broadcastMessage_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "no_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  empty x-requestor
    @pytest.mark.Smoke
    def test19_negative_notification_broadcastMessage_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "empty_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # Notification -  Broadcast Message -  no x-requestor
    @pytest.mark.Smoke
    def test20_negative_notification_broadcastMessage_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_broadcastMessage")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            groupName = str(dict1["groupName"])
            title = str(dict1["title"])
            message = str(dict1["Message"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            groupName = "%2B"
            title = "Message Broadcast"
            message = "Message is broadcast"

        # Call subscribe reusable module
        response = notification_broadcastMessage(self, groupName, title, message, "no_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # Notification -  Create Broadcast Group -  invalid apiKey
    @pytest.mark.Smoke
    def test21_negative_notification_createBroadcastGroup_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "invalid_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  Create Broadcast Group -  empty apiKey
    @pytest.mark.Smoke
    def test22_negative_notification_createBroadcastGroup_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "empty_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  Create Broadcast Group -  no apiKey
    @pytest.mark.Smoke
    def test23_negative_notification_createBroadcastGroup_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "no_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # Notification -  Create Broadcast Group -  empty x-requestor
    @pytest.mark.Smoke
    def test24_negative_notification_createBroadcastGroup_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "empty_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # Notification -  Create Broadcast Group -  no x-requestor
    @pytest.mark.Smoke
    def test25_negative_notification_createBroadcastGroup_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_createBroadcastGroup")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            groupName = str(dict1["groupName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            groupName = "broadcast_group"

        # Call subscribe reusable module
        response = notification_createBroadcastGroup(self, systemId, vin, groupName, "no_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # Notification_message
    @pytest.mark.Smoke
    def test26_negative_notification_empty_message(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_empty_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            if msg_id == "None":
                msg_id = ""
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = ""

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)
        print("Message :", msg_id)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "message cannot be empty"

    @pytest.mark.Smoke
    def test27_negative_notification_without_message_field(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_without_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = ""

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_without_message_field")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "message cannot be empty"

    @pytest.mark.Smoke
    def test28_negative_notification_message_exceeds_maxlength(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message_exceeds_maxlenth")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "abcdabcdkjsjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "message length cannot be more than 500"

    @pytest.mark.Smoke
    def test29_negative_Notification_empty_source(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_empty_source")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
            if source == "None":
                source = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = ""
            msg_id = "123456"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "source cannot be empty"

    @pytest.mark.Smoke
    def test30_negative_notification_without_source_field(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_without_source")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_without_source_field")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "source cannot be empty"

    @pytest.mark.Smoke
    def test31_negative_notification_without_vin_field(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_without_vin")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_without_vin_field")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # VIN is an optional parameter, thus give success response
        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

    @pytest.mark.Smoke
    def test32_negative_notification_invalid_vin(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_invalid_vin")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = "vin123"
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # VIN is an optional parameter, thus give success response
        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

    @pytest.mark.Smoke
    def test33_negative_notification_empty_vin(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_empty_vin")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == "None":
                vin =""
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = ""
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # VIN is an optional parameter, thus give success response
        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

    @pytest.mark.Smoke
    def test34_negative_notification_without_systemId_field(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_without_systemId")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_without_systemId_field")

        # Validate response status code
        assert (response.status_code == 500), "Status code is not 500. Rather found : " + str(response.status_code)

    @pytest.mark.Smoke
    def test35_negative_notification_invalid_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_invalid_systemId")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = "sys123"
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert "Vehicle does not exist for system id" in response_body["responseData"]["message"]

    @pytest.mark.Smoke
    def test36_negative_notification_empty_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_empty_systemId")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId =""
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = ""
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert "Vehicle does not exist for system id" in response_body["responseData"]["message"]

    @pytest.mark.Smoke
    def test37_negative_notification_without_target_field(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_without_target")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_without_target_field")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert response_body["responseCode"] == "4001"
        assert response_body["responseData"]["message"] == "target cannot be null"

    # Notification -  message -  invalid apiKey
    @pytest.mark.Smoke
    def test38_negative_notification_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "invalid_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  message -  empty apiKey
    @pytest.mark.Smoke
    def test39_negative_notification_createBroadcastGroup_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "empty_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # Notification -  message -  no apiKey
    @pytest.mark.Smoke
    def test40_negative_notification_createBroadcastGroup_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "no_apiKey")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # Notification -  message -  empty x-requestor
    @pytest.mark.Smoke
    def test41_negative_notification_createBroadcastGroup_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "empty_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # Notification -  message -  no x-requestor
    @pytest.mark.Smoke
    def test42_negative_notification_createBroadcastGroup_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification", "Notification_message")
        message = str(dict1["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            systemId = str(dict1["systemId"])
            msg_id = str(dict1["Message"])
            source = str(dict1["Source"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            source = "DA"
            msg_id = "1234"

        print("VIN :", vin)
        print("System Id :", systemId)
        print("Source :", source)

        # Call notification message reusable module
        response = notification_message_new(self, vin, systemId, msg_id, source, "no_x-requestor")

        # Validate response code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")
