import pytest

from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.e2e_testData import *
from C2CModules.notifications import notificationServiceController_details_by_systemId_Category
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile


class Test_RE_SP2_TamperingAlert:

    @pytest.mark.regression
    # Validate the notification message details of an invalid system ID
    def test1_negative_bikeSecuritySafety_tampering_alert_invalid_systemId(self):

        # invalid system Id
        systemId = "313a"
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "invalid")
        # parse api response into json
        response_body = response.json()

        if response_body["responseCode"] == 4001 and response_body[
            "responseMessage"] == "No data available in the database for the given combination":
            assert True
        else:
            assert False

    @pytest.mark.regression
    # Validate the notification message details with empty system ID
    def test2_negative_bikeSecuritySafety_tampering_alert_empty_systemId(self):

        # empty system Id
        systemId = ""
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "invalid")
        # parse api response into json
        response_body = response.json()

        if response_body["responseCode"] == 4001 and response_body[
            "responseMessage"] == "No data available in the database for the given combination":
            assert True
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  without category
    def test3_negative_bikeSecuritySafety_tampering_alert_without_category(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_category")
        if response.status_code == 400:
            assert True
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  with invalid category
    def test4_negative_bikeSecuritySafety_tampering_alert_invalid_category(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        invalid_tamper_categoryName = tamper_categoryName + "@"
        print("System Id : ", systemId)
        print("Invalid Category Name : ", invalid_tamper_categoryName)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId,
                                                                              invalid_tamper_categoryName,
                                                                              "invalid")
        if response.status_code == 202:

            # parse api response into json
            response_body = response.json()

            if response_body["responseCode"] == 4001 and response_body[
                "responseMessage"] == "No data available in the database for the given combination":
                assert True
            else:
                assert False
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details with empty page Number
    def test5_negative_bikeSecuritySafety_tampering_alert_empty_pageNo(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId,
                                                                              tamper_categoryName,
                                                                              "empty_pageNo")
        if response.status_code == 202:

            # parse api response into json
            response_body = response.json()

            if response_body["responseCode"] == 4001 and response_body[
                "responseMessage"] == "No data available in the database for the given combination":
                assert True
            else:
                assert False
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details with invalid page Number
    def test6_negative_bikeSecuritySafety_tampering_alert_invalid_pageNo(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId,
                                                                              tamper_categoryName,
                                                                              "invalid_pageNo")
        if response.status_code == 202:

            # parse api response into json
            response_body = response.json()

            if response_body["responseCode"] == 4001 and response_body[
                "responseMessage"] == "No data available in the database for the given combination":
                assert True
            else:
                assert False
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details with empty page size
    def test7_negative_bikeSecuritySafety_tampering_alert_empty_pageSize(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId,
                                                                              tamper_categoryName,
                                                                              "empty_pageSize")
        if response.status_code == 202:

            # parse api response into json
            response_body = response.json()

            if response_body["responseCode"] == 4001 and response_body[
                "responseMessage"] == "No data available in the database for the given combination":
                assert True
            else:
                assert False
        else:
            assert False

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details with invalid page size
    def test8_negative_bikeSecuritySafety_tampering_alert_invalid_pageSize(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId,
                                                                              tamper_categoryName,
                                                                              "invalid_pageSize")
        if response.status_code == 202:

            # parse api response into json
            response_body = response.json()

            if response_body["responseCode"] == 4001 and response_body[
                "responseMessage"] == "No data available in the database for the given combination":
                assert True
            else:
                assert False
        else:
            assert False

    @pytest.mark.regression
    # Validate the notification message details with empty x-requestor
    def test9_negative_bikeSecuritySafety_tampering_alert_empty_xRequestor(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "empty_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

    @pytest.mark.regression
    # Validate the notification message details with without x-requestor
    def test10_negative_bikeSecuritySafety_tampering_alert_no_xRequestor(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

    @pytest.mark.regression
    # Validate the notification message details with empty api-key
    def test11_negative_bikeSecuritySafety_tampering_alert_empty_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

    @pytest.mark.regression
    # Validate the notification message details with invalid api-key
    def test12_negative_bikeSecuritySafety_tampering_alert_invalid_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

    @pytest.mark.regression
    # Validate the notification message details with without api-key
    def test13_negative_bikeSecuritySafety_tampering_alert_no_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  without headers API key and x-requestor
    def test14_negative_bikeSecuritySafety_tampering_alert_no_xRequestor_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_x-requestor_and_no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor_and_no_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  with empty headers API key and x-requestor
    def test15_negative_bikeSecuritySafety_tampering_alert_empty_xRequestor_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "empty_x-requestor_and_empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor_and_empty_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  with empty x-requestor and invalid API key
    def test16_negative_bikeSecuritySafety_tampering_alert_empty_xRequestor_invalid_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "empty_x-requestor_and_invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor_and_invalid_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  with empty x-requestor and without header API key
    def test17_negative_bikeSecuritySafety_tampering_alert_empty_xRequestor_no_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "empty_x-requestor_and_no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor_and_no_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  without x-requestor and with invalid API key
    def test18_negative_bikeSecuritySafety_tampering_alert_no_xRequestor_invalid_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_x-requestor_and_invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor_and_invalid_apiKey")

    @pytest.mark.regression
    # Validate the  API to fetch the notification message details  without x-requestor and with empty API key
    def test19_negative_bikeSecuritySafety_tampering_alert_no_xRequestor_empty_apiKey(self):

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, tamper_categoryName,
                                                                              "no_x-requestor_and_empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor_and_empty_apiKey")
