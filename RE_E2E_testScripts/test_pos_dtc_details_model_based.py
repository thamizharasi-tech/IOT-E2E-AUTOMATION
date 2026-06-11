import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random


from C2CModules.vehicle_diagnostic import DTC_get_dtc_details
from C2CModules.testResults import testResult
from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.vehicle_configurations import vehicleConfigurations_decision_table_for_rules

class Test_DTC:

    def test_positive_dtc_details(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            data_len = len(response_body["responseData"]["dtcDetails"])
            if data_len >= 1:
                for i in range(data_len):
                    dtcCode = response_body["responseData"]["dtcDetails"][i]["dtcCode"]
                    definition = response_body["responseData"]["dtcDetails"][i]["definition"]
                    causes = response_body["responseData"]["dtcDetails"][i]["causes"]
                    aids = response_body["responseData"]["dtcDetails"][i]["aids"]
                    priority = response_body["responseData"]["dtcDetails"][i]["priority"]
                    category = response_body["responseData"]["dtcDetails"][i]["category"]
                    summary = response_body["responseData"]["dtcDetails"][i]["summary"]
                    make = response_body["responseData"]["dtcDetails"][i]["make"]
                    model = response_body["responseData"]["dtcDetails"][i]["model"]
                    year = response_body["responseData"]["dtcDetails"][i]["year"]
                    faultSignalNameBySupplier = response_body["responseData"]["dtcDetails"][i]["faultSignalNameBySupplier"]
                    canSignalNameByRe = response_body["responseData"]["dtcDetails"][i]["canSignalNameByRe"]
                    checkedAt = response_body["responseData"]["dtcDetails"][i]["checkedAt"]
                    recoverable = response_body["responseData"]["dtcDetails"][i]["recoverable"]
                    faultTriggerCondition = response_body["responseData"]["dtcDetails"][i]["faultTriggerCondition"]
                    faultRecoveryConditions = response_body["responseData"]["dtcDetails"][i]["faultRecoveryConditions"]
                    faultGrade = response_body["responseData"]["dtcDetails"][i]["faultGrade"]
                    actionBy = response_body["responseData"]["dtcDetails"][i]["actionBy"]
                    action = response_body["responseData"]["dtcDetails"][i]["action"]


                    print("offset: ", offset)
                    print("limit: ", limit)
                    print("totalRecords: ", totalRecords)
                    print("dtcCode: ", dtcCode)
                    print("definition: ", definition)
                    print("causes: ", causes)
                    print("aids: ", aids)
                    print("priority: ", priority)
                    print("category: ", category)
                    print("summary: ", summary)
                    print("make: ", make)
                    print("model: ", model)
                    print("year: ", year)
                    print("faultSignalNameBySupplier: ", faultSignalNameBySupplier)
                    print("canSignalNameByRe: ", canSignalNameByRe)
                    print("checkedAt: ", checkedAt)
                    print("recoverable: ", recoverable)
                    print("faultTriggerCondition: ", faultTriggerCondition)
                    print("faultRecoveryConditions: ", faultRecoveryConditions)
                    print("faultGrade: ", faultGrade)
                    print("actionBy: ", actionBy)
                    print("action: ", action)
                    testResult(self, "passed",
                                   "DTC details should be fetched successfully",
                                   "DTC details fetched successfully")
                    assert True
                        # self.result.set_result(TestResults.passed)
                    break
            else:
                testResult(self, "failed",
                           "DTC details should be fetched successfully",
                           "Datalist is empty")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "DTC details should be fetched successfully",
                       "Failed to fetch dtc details")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_based_on_model(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "based_on_model")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            data_len = len(response_body["responseData"]["dtcDetails"])
            if data_len >= 1:
                for i in range(data_len):
                    dtcCode = response_body["responseData"]["dtcDetails"][i]["dtcCode"]
                    definition = response_body["responseData"]["dtcDetails"][i]["definition"]
                    causes = response_body["responseData"]["dtcDetails"][i]["causes"]
                    aids = response_body["responseData"]["dtcDetails"][i]["aids"]
                    priority = response_body["responseData"]["dtcDetails"][i]["priority"]
                    category = response_body["responseData"]["dtcDetails"][i]["category"]
                    summary = response_body["responseData"]["dtcDetails"][i]["summary"]
                    make = response_body["responseData"]["dtcDetails"][i]["make"]
                    model = response_body["responseData"]["dtcDetails"][i]["model"]
                    year = response_body["responseData"]["dtcDetails"][i]["year"]
                    faultSignalNameBySupplier = response_body["responseData"]["dtcDetails"][i][
                        "faultSignalNameBySupplier"]
                    canSignalNameByRe = response_body["responseData"]["dtcDetails"][i]["canSignalNameByRe"]
                    checkedAt = response_body["responseData"]["dtcDetails"][i]["checkedAt"]
                    recoverable = response_body["responseData"]["dtcDetails"][i]["recoverable"]
                    faultTriggerCondition = response_body["responseData"]["dtcDetails"][i]["faultTriggerCondition"]
                    faultRecoveryConditions = response_body["responseData"]["dtcDetails"][i]["faultRecoveryConditions"]
                    faultGrade = response_body["responseData"]["dtcDetails"][i]["faultGrade"]
                    actionBy = response_body["responseData"]["dtcDetails"][i]["actionBy"]
                    action = response_body["responseData"]["dtcDetails"][i]["action"]

                    print("offset: ", offset)
                    print("limit: ", limit)
                    print("totalRecords: ", totalRecords)
                    print("dtcCode: ", dtcCode)
                    print("definition: ", definition)
                    print("causes: ", causes)
                    print("aids: ", aids)
                    print("priority: ", priority)
                    print("category: ", category)
                    print("summary: ", summary)
                    print("make: ", make)
                    print("model: ", model)
                    print("year: ", year)
                    print("faultSignalNameBySupplier: ", faultSignalNameBySupplier)
                    print("canSignalNameByRe: ", canSignalNameByRe)
                    print("checkedAt: ", checkedAt)
                    print("recoverable: ", recoverable)
                    print("faultTriggerCondition: ", faultTriggerCondition)
                    print("faultRecoveryConditions: ", faultRecoveryConditions)
                    print("faultGrade: ", faultGrade)
                    print("actionBy: ", actionBy)
                    print("action: ", action)
                    testResult(self, "passed",
                               "DTC details should be fetched successfully",
                               "DTC details fetched successfully")
                    assert True
                    # self.result.set_result(TestResults.passed)
                    break
            else:
                testResult(self, "failed",
                           "DTC details should be fetched successfully",
                           "Datalist is empty")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "DTC details should be fetched successfully",
                       "Failed to fetch dtc details")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_based_on_model_dtcCode_make_priority(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "model_make_dtcCode_priority")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            data_len = len(response_body["responseData"]["dtcDetails"])
            if data_len >= 1:
                for i in range(data_len):
                    dtcCode = response_body["responseData"]["dtcDetails"][i]["dtcCode"]
                    definition = response_body["responseData"]["dtcDetails"][i]["definition"]
                    causes = response_body["responseData"]["dtcDetails"][i]["causes"]
                    aids = response_body["responseData"]["dtcDetails"][i]["aids"]
                    priority = response_body["responseData"]["dtcDetails"][i]["priority"]
                    category = response_body["responseData"]["dtcDetails"][i]["category"]
                    summary = response_body["responseData"]["dtcDetails"][i]["summary"]
                    make = response_body["responseData"]["dtcDetails"][i]["make"]
                    model = response_body["responseData"]["dtcDetails"][i]["model"]
                    year = response_body["responseData"]["dtcDetails"][i]["year"]
                    faultSignalNameBySupplier = response_body["responseData"]["dtcDetails"][i][
                        "faultSignalNameBySupplier"]
                    canSignalNameByRe = response_body["responseData"]["dtcDetails"][i]["canSignalNameByRe"]
                    checkedAt = response_body["responseData"]["dtcDetails"][i]["checkedAt"]
                    recoverable = response_body["responseData"]["dtcDetails"][i]["recoverable"]
                    faultTriggerCondition = response_body["responseData"]["dtcDetails"][i]["faultTriggerCondition"]
                    faultRecoveryConditions = response_body["responseData"]["dtcDetails"][i]["faultRecoveryConditions"]
                    faultGrade = response_body["responseData"]["dtcDetails"][i]["faultGrade"]
                    actionBy = response_body["responseData"]["dtcDetails"][i]["actionBy"]
                    action = response_body["responseData"]["dtcDetails"][i]["action"]

                    print("offset: ", offset)
                    print("limit: ", limit)
                    print("totalRecords: ", totalRecords)
                    print("dtcCode: ", dtcCode)
                    print("definition: ", definition)
                    print("causes: ", causes)
                    print("aids: ", aids)
                    print("priority: ", priority)
                    print("category: ", category)
                    print("summary: ", summary)
                    print("make: ", make)
                    print("model: ", model)
                    print("year: ", year)
                    print("faultSignalNameBySupplier: ", faultSignalNameBySupplier)
                    print("canSignalNameByRe: ", canSignalNameByRe)
                    print("checkedAt: ", checkedAt)
                    print("recoverable: ", recoverable)
                    print("faultTriggerCondition: ", faultTriggerCondition)
                    print("faultRecoveryConditions: ", faultRecoveryConditions)
                    print("faultGrade: ", faultGrade)
                    print("actionBy: ", actionBy)
                    print("action: ", action)
                    testResult(self, "passed",
                               "DTC details should be fetched successfully",
                               "DTC details fetched successfully")
                    assert True
                    # self.result.set_result(TestResults.passed)
                    break
            else:
                testResult(self, "failed",
                           "DTC details should be fetched successfully",
                           "Datalist is empty")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "DTC details should be fetched successfully",
                       "Failed to fetch dtc details")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_paginated(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "pagination")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            data_len = len(response_body["responseData"]["dtcDetails"])
            if data_len >= 1:
                for i in range(data_len):
                    dtcCode = response_body["responseData"]["dtcDetails"][i]["dtcCode"]
                    definition = response_body["responseData"]["dtcDetails"][i]["definition"]
                    causes = response_body["responseData"]["dtcDetails"][i]["causes"]
                    aids = response_body["responseData"]["dtcDetails"][i]["aids"]
                    priority = response_body["responseData"]["dtcDetails"][i]["priority"]
                    category = response_body["responseData"]["dtcDetails"][i]["category"]
                    summary = response_body["responseData"]["dtcDetails"][i]["summary"]
                    make = response_body["responseData"]["dtcDetails"][i]["make"]
                    model = response_body["responseData"]["dtcDetails"][i]["model"]
                    year = response_body["responseData"]["dtcDetails"][i]["year"]
                    faultSignalNameBySupplier = response_body["responseData"]["dtcDetails"][i][
                        "faultSignalNameBySupplier"]
                    canSignalNameByRe = response_body["responseData"]["dtcDetails"][i]["canSignalNameByRe"]
                    checkedAt = response_body["responseData"]["dtcDetails"][i]["checkedAt"]
                    recoverable = response_body["responseData"]["dtcDetails"][i]["recoverable"]
                    faultTriggerCondition = response_body["responseData"]["dtcDetails"][i]["faultTriggerCondition"]
                    faultRecoveryConditions = response_body["responseData"]["dtcDetails"][i]["faultRecoveryConditions"]
                    faultGrade = response_body["responseData"]["dtcDetails"][i]["faultGrade"]
                    actionBy = response_body["responseData"]["dtcDetails"][i]["actionBy"]
                    action = response_body["responseData"]["dtcDetails"][i]["action"]

                    print("offset: ", offset)
                    print("limit: ", limit)
                    print("totalRecords: ", totalRecords)
                    print("dtcCode: ", dtcCode)
                    print("definition: ", definition)
                    print("causes: ", causes)
                    print("aids: ", aids)
                    print("priority: ", priority)
                    print("category: ", category)
                    print("summary: ", summary)
                    print("make: ", make)
                    print("model: ", model)
                    print("year: ", year)
                    print("faultSignalNameBySupplier: ", faultSignalNameBySupplier)
                    print("canSignalNameByRe: ", canSignalNameByRe)
                    print("checkedAt: ", checkedAt)
                    print("recoverable: ", recoverable)
                    print("faultTriggerCondition: ", faultTriggerCondition)
                    print("faultRecoveryConditions: ", faultRecoveryConditions)
                    print("faultGrade: ", faultGrade)
                    print("actionBy: ", actionBy)
                    print("action: ", action)
                    testResult(self, "passed",
                               "DTC details should be fetched successfully",
                               "DTC details fetched successfully")
                    assert True
                    # self.result.set_result(TestResults.passed)
                    break
            else:
                testResult(self, "failed",
                           "DTC details should be fetched successfully",
                           "Datalist is empty")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "DTC details should be fetched successfully",
                       "Failed to fetch dtc details")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_invalid_offset(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "-1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "pagination")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["errorCode"] == "17007" or response_body["errors"][0]["errorCode"] == str(17007):
            if response_body["errors"][0]["message"] == "offset can not be less than 1 or negative":
                testResult(self, "passed",
                           "Error message should throw for invalid offset",
                           "Error message is throwing for invalid offset")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Error message should throw for invalid offset",
                           "Error message is not met the expected message")
                assert False
        elif response_body["errors"][0]["errorCode"] != "17007":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Error message should throw for invalid offset",
                       "Error code is not met the expected")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_invalid_limit(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "Adp"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "-10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "pagination")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["errorCode"] == "17015" or response_body["errors"][0]["errorCode"] == str(17015):
            if response_body["errors"][0]["message"] == "limit can not be less than 1 or negative":
                testResult(self, "passed",
                           "Error message should throw for invalid limit",
                           "Error message is throwing for invalid limit")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Error message should throw for invalid limit",
                           "Error message is not met the expected message")
                assert False
        elif response_body["errors"][0]["errorCode"] != "17007":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Error message should throw for invalid limit",
                       "Error code is not met the expected")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_invalid_filter(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "based_on_model")

        # Validate response status code
        assert (response.status_code == 204), "Status code is not 204. Rather found : " + str(response.status_code)
        if response.status_code != 204:
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_invalid_filter_combination(self):

        print("================================FETCH DTC DETAILS===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "model_make_dtcCode_priority")

        # Validate response status code
        assert (response.status_code == 204), "Status code is not 204. Rather found : " + str(response.status_code)
        if response.status_code != 204:
            # self.result.set_result(TestResults.failed)
            assert False

    def test_positive_dtc_details_invalid_apikey(self):

        print("================================FETCH DTC DETAILS - INVALID APIKEY===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "DTC Details API  should throw appropriate error message for invalid apikey.",
                   "DTC Details API showing/throwing appropriate error message for invalid apikey.")
        #self.result.set_result(TestResults.passed)

    def test_positive_dtc_details_empty_apikey(self):

        print("================================FETCH DTC DETAILS - EMPTY APIKEY===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "DTC Details API  should throw appropriate error message for empty apikey.",
                   "DTC Details API showing/throwing appropriate error message for empty apikey.")
        # self.result.set_result(TestResults.passed)

    def test_positive_dtc_details_no_apikey(self):

        print("================================FETCH DTC DETAILS - NO APIKEY===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "DTC Details API  should throw appropriate error message for no apikey.",
                   "DTC Details API showing/throwing appropriate error message for no apikey.")
        # self.result.set_result(TestResults.passed)

    def test_positive_dtc_details_empty_xrequestor(self):

        print("================================FETCH DTC DETAILS - EMPTY X_REQUESTOR===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "empty_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "DTC Details API  should throw appropriate error message for empty x-requestor.",
                   "DTC Details API showing/throwing appropriate error message for empty x-requestor.")
        # self.result.set_result(TestResults.passed)

    def test_positive_dtc_details_no_xrequestor(self):

        print("================================FETCH DTC DETAILS - WITHOUT X_REQUESTOR===================================")

        model = "xyz"
        make = "RE"
        dtcCode = "P1001"
        priority = "0"
        offset = "1"
        limit = "10"

        # call api reusable module
        response = DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, "no_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "DTC Details API  should throw appropriate error message for no x-requestor.",
                   "DTC Details API showing/throwing appropriate error message for no x-requestor.")
        # self.result.set_result(TestResults.passed)

class Test_Vehilce_Conf:

    def test_positive_vehicle_config_decision_table_for_rules(self):

        configType = "vehicle_configurations"

        response = vehicleConfigurations_decision_table_for_rules(self, configType, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Rule Creation Success.":

            if response_body["configurations"]:

                print("\n Rules for Vehicle Configurations: \n", response_body["configurations"])

                testResult(self, "passed","Decision table should be created for rules with ConfigType vehicle_configurations", "Decision table is created for rules with ConfigType vehicle_configurations")

                assert True

            else:

                print("Configurations are missing or empty.")

                assert False
        else:

            print("Response message is not expected , Rather than found:", response_body)

            assert False

    def test_positive_telemetry_config_decision_table_for_rules(self):

        configType = "telemetry"

        response = vehicleConfigurations_decision_table_for_rules(self, configType, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Rule Creation Success.":

            if response_body["configurations"]:

                print("\n Rules for Telemetry Configurations: \n", response_body["configurations"])

                testResult(self, "passed","Decision table should be created for rules with ConfigType telemetry", "Decision table is created for rules with ConfigType telemetry")

                assert True

            else:

                print("Configurations are missing or empty.")

                assert False
        else:

            print("Response message is not expected , Rather than found:", response_body)

            assert False

    def test_positive_remote_operation_config_decision_table_for_rules(self):

        configType = "remote_operations"

        response = vehicleConfigurations_decision_table_for_rules(self, configType, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Rule Creation Success.":

            if response_body["configurations"]:

                print("\n Rules for Remote Operations: \n", response_body["configurations"])

                testResult(self, "passed","Decision table should be created for rules with ConfigType remote operations", "Decision table is created for rules with ConfigType remote operations")

                assert True

            else:

                print("Configurations are missing or empty.")

                assert False
        else:

            print("Response message is not expected , Rather than found:", response_body)

            assert False

    def test_positive_alert_config_decision_table_for_rules(self):

        configType = "alert_configurations"

        response = vehicleConfigurations_decision_table_for_rules(self, configType, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Rule Creation Success.":

            if response_body["configurations"]:

                print("\n Rules for Alert Configurations: \n", response_body["configurations"])

                testResult(self, "passed","Decision table should be created for rules with ConfigType alert configurations", "Decision table is created for rules with ConfigType alert configurations")

                assert True

            else:

                print("Configurations are missing or empty.")

                assert False
        else:

            print("Response message is not expected , Rather than found:", response_body)

            assert False

    def test_positive_decision_table_for_rules_with_invalid_configType(self):

        configType = "xyz"

        response = vehicleConfigurations_decision_table_for_rules(self, configType, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["errorCode"] == "16051" and response_body["errors"][0]["message"] == "Invalid value for the configType.":

            assert True

        else:

            print("Response message is not expected , Rather than found:", response_body)

            assert False

