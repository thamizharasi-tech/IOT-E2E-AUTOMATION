import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random

import pytest

from C2CModules.e2e_testData import *
from C2CModules.vehicleGrouping import *
from C2CModules.testResults import testResult
from datetime import datetime, timedelta

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_vehicleGrouping:

    def test1_create_vehicle_group_single_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Create Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group creation with all the required parameters
        """
        print("\n------------------VEHICLE GROUP CREATION - SINGLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                      criteria2_operator, criteria2_value, criteria2_key, option, tc)

        print("\n------------------------------END------------------------------\n")

    def test2_update_vehicle_group_single_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Edit/Update Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group update with all the required parameters
        """
        print("\n------------------VEHICLE GROUP UPDATE - SINGLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        groupName = ''
        desc = "Update existing group"
        criteria1_operator = "in"
        criteria1_value = "Suv"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "update_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        # call reusable module
        vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                      criteria2_operator, criteria2_value, criteria2_key, option, tc)

        print("\n------------------------------END------------------------------\n")

    def test3_delete_vehicle_group_single_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Delete Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group delete
        """
        print("\n------------------VEHICLE GROUP DELETE - SINGLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # call reusable module
        delete_vehicle_group(self)

        print("\n------------------------------END------------------------------\n")

    def test4_create_vehicle_group_multiple_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Create Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group creation with all the required parameters
        """
        print("\n------------------VEHICLE GROUP CREATION - MULTIPLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "multiple_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        # call reusable module
        vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                      criteria2_operator, criteria2_value, criteria2_key, option, tc)

        print("\n------------------------------END------------------------------\n")

    def test5_update_vehicle_group_multiple_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Edit/Update Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group update with all the required parameters
        """
        print("\n------------------VEHICLE GROUP UPDATE - MULTIPLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        groupName = ''
        desc = "Update existing group"
        criteria1_operator = "in"
        criteria1_value = "Suv"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "multiple_criteria"  # options : single_criteria or multiple_criteria
        tc = "update_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        # call reusable module
        vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                      criteria2_operator, criteria2_value, criteria2_key, option, tc)

        print("\n------------------------------END------------------------------\n")

    def test6_delete_vehicle_group_multiple_criteria(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Delete Vehicle Group functionality. (positive scenario)
        :return: return test status
        Vehicle group delete
        """
        print("\n------------------VEHICLE GROUP DELETE - MULTIPLE CRITERIA------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # call reusable module
        delete_vehicle_group(self)

        print("\n------------------------------END------------------------------\n")

    ## Negative Test Script ##
class Test_vehicleGrouping_Neg:

    def test1_negative_VehicleGrouping_createGroup_invalid_duplicate_groupName(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Vehicle Group already exist with given name" and \
                response_body["errors"][0]["errorCode"] == "13226":
            testResult(self, "passed",
                       "Create vehicle group API should throw proper error message for duplicate group name",
                       "Create vehicle group API is throwing proper error message")
            assert True
        else:
            testResult(self, "failed",
                       "Create vehicle group API should throw proper error message for duplicate group name",
                       "Create vehicle group API is not throwing proper error message")
            assert False

        print("----------------------------------------------------------")

    def test2_negative_VehicleGrouping_createGroup_emptyGroupName(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        #groupName = 'Group_' + str(msg_id)
        groupName = ""
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "GroupName is Null/Empty or contains only spaces" and \
                response_body["errors"][0]["errorCode"] == "13225":
            testResult(self, "passed",
                       " Create Vehicle group API should throw proper error message for empty group name",
                       "Create Vehicle group API is throwing proper error message for empty group name")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle group API should throw proper error message for empty group name",
                       "Create Vehicle group API is not throwing proper error message for empty group name")
            assert False

        print("----------------------------------------------------------")

    def test3_negative_VehicleGrouping_createGroup_nonExisting_criteriaValue(self):

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = 1234
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Value List can contain only 'String' Valuesmodel" and \
                response_body["errors"][0]["errorCode"] == "13230":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria value",
                       "Create Vehicle grouping API is throwing proper error message for non-exist criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria value",
                       "Create Vehicle grouping API is not throwing proper error message for non-exist criteria value")
            assert False

        print("----------------------------------------------------------")

    def test4_negative_VehicleGrouping_createGroup_nonExisting_criteriaOperator(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "xyz"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Operator xyz is not permmited for Key Name 'model'" and \
                response_body["errors"][0]["errorCode"] == "13234":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria operator",
                       "Create Vehicle grouping API is throwing proper error message for non-exist criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria operator",
                       "Create Vehicle grouping API is not throwing proper error message for non-exist criteria operator")
            assert False

        print("----------------------------------------------------------")

    def test5_negative_VehicleGrouping_createGroup_nonExisting_criteriaKey(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "ssd"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No Mapping present for Key Name 'ssd'" and \
                response_body["errors"][0]["errorCode"] == "13235":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria key",
                       "Create Vehicle grouping API is throwing proper error message for non-exist criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for non-exist criteria key",
                       "Create Vehicle grouping API is not throwing proper error message for non-exist criteria key")
            assert False

        print("----------------------------------------------------------")

    def test6_negative_VehicleGrouping_createGroup_invalid_keyCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "ssd"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No Mapping present for Key Name 'ssd'" and \
                response_body["errors"][0]["errorCode"] == "13235":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria key",
                       "Create Vehicle grouping API is throwing proper error message for invalid criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria key",
                       "Create Vehicle grouping API is not throwing proper error message for invalid criteria key")
            assert False

        print("----------------------------------------------------------")

    def test7_negative_VehicleGrouping_createGroup_invalid_operatorCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "dfd"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Operator dfd is not permmited for Key Name 'model'" and \
                response_body["errors"][0]["errorCode"] == "13234":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria operator",
                       "Create Vehicle grouping API is throwing proper error message for invalid criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria operator",
                       "Create Vehicle grouping API is not throwing proper error message for invalid criteria operator")
            assert False

        print("----------------------------------------------------------")

    def test8_negative_VehicleGrouping_createGroup_invalid_valueCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = 123
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Value List can contain only 'String' Valuesmodel" and \
                response_body["errors"][0]["errorCode"] == "13230":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria value",
                       "Create Vehicle grouping API is throwing proper error message for invalid criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for invalid criteria value",
                       "Create Vehicle grouping API is not throwing proper error message for invalid criteria value")
            assert False

        print("----------------------------------------------------------")

    def test9_negative_VehicleGrouping_createGroup_empty_operatorCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = ""
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Operator is Null/Empty or contains only spaces for key : model" and \
                response_body["errors"][0]["errorCode"] == "13234":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria operator",
                       "Create Vehicle grouping API is throwing proper error message for empty criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria operator",
                       "Create Vehicle grouping API is not throwing proper error message for empty criteria operator")
            assert False

        print("----------------------------------------------------------")

    def test10_negative_VehicleGrouping_createGroup_empty_keyCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = ""
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Key Name is Null/Empty or contains only spaces" and \
                response_body["errors"][0]["errorCode"] == "13234":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria key",
                       "Create Vehicle grouping API is throwing proper error message for empty criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria key",
                       "Create Vehicle grouping API is not throwing proper error message for empty criteria key")
            assert False

        print("----------------------------------------------------------")

    def test11_negative_VehicleGrouping_createGroup_empty_valueCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = ""
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Value in value list is Null/Empty or contains only spaces for key : model" and \
                response_body["errors"][0]["errorCode"] == "13237":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria value",
                       "Create Vehicle grouping API is throwing proper error message for empty criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for empty criteria value",
                       "Create Vehicle grouping API is not throwing proper error message for empty criteria value")
            assert False

        print("----------------------------------------------------------")

    def test12_negative_VehicleGrouping_createGroup_empty_description(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = ""
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Description is Null/Empty or contains only spaces" and \
                response_body["errors"][0]["errorCode"] == "13227":
            testResult(self, "passed",
                       "Create Vehicle grouping API should throw proper error message for empty description",
                       "Create Vehicle grouping API is throwing proper error message for empty description")
            assert True
        else:
            testResult(self, "failed",
                       "Create Vehicle grouping API should throw proper error message for empty description",
                       "Create Vehicle grouping API is not throwing proper error message for empty description")
            assert False

        print("----------------------------------------------------------")

    ## Fetch Api
    #Pass
    def test13_negative_VehicleGrouping_fetchGroup_invalid_keyCriteria(self):
        print("----------------------------------------------------------")


        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "xyz"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Key Not Found for keyName: xyz" and \
                response_body["errors"][0]["errorCode"] == "13243":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria key",
                       "Fetch Vehicle group API is throwing proper error message for invalid criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria key",
                       "Fetch Vehicle group API is not throwing proper error message for invalid criteria key")
            assert False

        print("----------------------------------------------------------")

    #Pass
    def test14_negative_VehicleGrouping_fetchGroup_invalid_valueCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "in"
        criteria1_value = "sdsd"
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 404:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No criteria found for filter with keyId: 6" and \
                response_body["errors"][0]["errorCode"] == "13244":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria value",
                       "Fetch Vehicle group API is throwing proper error message for invalid criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria value",
                       "Fetch Vehicle group API is not throwing proper error message for invalid criteria value")
            assert False

        print("----------------------------------------------------------")

    #Pass
    def test15_negative_VehicleGrouping_fetchGroup_invalid_operatorCriteria(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet

        criteria1_operator = "innn"
        criteria1_value = "2"
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 404:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No criteria found for filter with keyId: 6" and \
                response_body["errors"][0]["errorCode"] == "13244":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria operator",
                       "Fetch Vehicle group API is throwing proper error message for invalid criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria operator",
                       "Fetch Vehicle group API is not throwing proper error message for invalid criteria operator")
            assert False

        print("----------------------------------------------------------")

    #Pass
    def test16_negative_VehicleGrouping_fetchGroup_empty_keyCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "in"
        criteria1_value = "sdsd"
        criteria1_key = ""
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Key name cannot be null or empty" and \
                response_body["errors"][0]["errorCode"] == "13240":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for empty criteria key",
                       "Fetch Vehicle group API is throwing proper error message for invalid criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for invalid criteria key",
                       "Fetch Vehicle group API is not throwing proper error message for invalid criteria key")
            assert False

        print("----------------------------------------------------------")

    #pass
    def test17_negative_VehicleGrouping_fetchGroup_empty_valueCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "in"
        criteria1_value = ""
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 404:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No criteria found for filter with keyId: 6" and \
                response_body["errors"][0]["errorCode"] == "13244":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for empty criteria value",
                       "Fetch Vehicle group API is throwing proper error message for empty criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for empty criteria value",
                       "Fetch Vehicle group API is not throwing proper error message for empty criteria value")
            assert False

        print("----------------------------------------------------------")

    #pass
    def test18_negative_VehicleGrouping_fetchGroup_empty_operatorCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = ""
        criteria1_value = "2"
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Operator cannot be null or empty" and \
                response_body["errors"][0]["errorCode"] == "13241":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for empty criteria operator",
                       "Fetch Vehicle group API is throwing proper error message for empty criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for empty criteria operator",
                       "Fetch Vehicle group API is not throwing proper error message for empty criteria operator")
            assert False

        print("----------------------------------------------------------")

    # Pass
    def test19_negative_VehicleGrouping_fetchGroup_nonexisting_keyCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "eq"
        criteria1_value = "2"
        criteria1_key = "abc"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Key Not Found for keyName: abc" and \
                response_body["errors"][0]["errorCode"] == "13243":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria key",
                       "Fetch Vehicle group API is throwing proper error message for non-exist criteria key")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria key",
                       "Fetch Vehicle group API is not throwing proper error message for non-exist criteria key")
            assert False

        print("----------------------------------------------------------")

    #pass
    def test20_negative_VehicleGrouping_fetchGroup_nonexisting_operatorCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "abc"
        criteria1_value = "2"
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 404:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No criteria found for filter with keyId: 6" and \
                response_body["errors"][0]["errorCode"] == "13244":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria operator",
                       "Fetch Vehicle group API is throwing proper error message for non-exist criteria operator")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria operator",
                       "Fetch Vehicle group API is not throwing proper error message for non-exist criteria operator")
            assert False

        print("----------------------------------------------------------")

    def test21_negative_VehicleGrouping_fetchGroup_nonexisting_valueCriteria(self):
        print("----------------------------------------------------------")

        criteria1_operator = "in"
        criteria1_value = "abc"
        criteria1_key = "engineType"
        offset = "0"
        limit = "100"

        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)

        # Verify command & control response
        response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                                 criteria1_value, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 404:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "No criteria found for filter with keyId: 6" and \
                response_body["errors"][0]["errorCode"] == "13244":
            testResult(self, "passed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria value",
                       "Fetch Vehicle group API is throwing proper error message for non-exist criteria value")
            assert True
        else:
            testResult(self, "failed",
                       "Fetch Vehicle group API should throw proper error message for non-exist criteria value",
                       "Fetch Vehicle group API is not throwing proper error message for non-exist criteria value")
            assert False

        print("----------------------------------------------------------")

    def test22_negative_VehicleGrouping_fetchGroup_nonexisting_groupName(self):
        print("----------------------------------------------------------")

        groupName = "abcrer"
        offset = "0"
        limit = "100"

        print('groupName : ', groupName)
        print('offset : ', offset)
        print('limit : ', limit)

        # Verify command & control response
        response = fetch_vehicle_group_details_with_pagination(self, groupName, offset, limit, "valid")

        # Validate response status code
        if response.status_code == 204:
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    #pass
    def test23_negative_VehicleGrouping_deleteGroup_nonexisting_group(self):
        print("----------------------------------------------------------")


        groupName = "GRP-RE123X"

        print('groupName : ', groupName)

        # Verify command & control response
        response = vehicle_group_deletion(self, groupName, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0][
            "message"] == "Given groupname not found" and \
                response_body["errors"][0]["errorCode"] == "15534":
            testResult(self, "passed",
                       "Delete Vehicle group API should throw proper error message for non-exist group",
                       "Delete Vehicle group API is throwing proper error message for non-exist group")
            assert True
        else:
            testResult(self, "failed",
                       "Delete Vehicle group API should throw proper error message for non-exist group",
                       "Delete Vehicle group API is not throwing proper error message for non-exist group")
            assert False

        print("----------------------------------------------------------")

    #Pass
    def test24_negative_VehicleGrouping_deleteGroup_groupName_already_deleted(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Verify command & control response
        response = vehicle_group_deletion(self, groupName, "valid")

        response = vehicle_group_deletion(self, groupName, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0][
            "message"] == "Given groupname not found" and \
                response_body["errors"][0]["errorCode"] == "15534":
            testResult(self, "passed",
                       "Delete Vehicle Grouping API should throw proper error message to delete the already deleted group",
                       "Delete Vehicle Grouping API is throwing proper error message to delete the already deleted grou")
            assert True
        else:
            testResult(self, "failed",
                       "Delete Vehicle Grouping API should throw proper error message to delete the already deleted grou",
                       "Delete Vehicle Grouping API is not throwing proper error message to delete the already deleted grou")
            assert False

        print("----------------------------------------------------------")

    def test25_negative_VehicleGrouping_deleteGroup_fetch_details_for_deleted_group(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Verify command & control response
        response = vehicle_group_deletion(self, groupName, "valid")


        # Fetch vehicle group
        response = fetch_vehicle_group_details_with_pagination(self, groupName, '0', '100', "valid")
        if response.status_code == 204:
            assert True

        else:
            print("Status code is not 204. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    ## Update Api

    def test26_negative_VehicleGrouping_updateGroup_empty_groupName(self):

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        groupName = ""
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 204:
            assert True

        else:
            print("Status code is not 204. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    def test27_negative_VehicleGrouping_updateGroup_alreadyexists_groupName(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True

        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        if response_body["message"] == "Data Updated Successfully":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    def test28_negative_VehicleGrouping_updateGroup_empty_description(self):

        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        desc = ""
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True

        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        if response_body["message"] == "Data Updated Successfully":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    def test29_negative_VehicleGrouping_updateGroup_empty_value(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        criteria1_value = ""
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13237" and response_body["errors"][0]["message"] == "Value in value list is Null/Empty or contains only spaces for key : model":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    def test30_negative_VehicleGrouping_updateGroup_empty_Keycriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        criteria1_key = ""
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13234" and response_body["errors"][0][
            "message"] == "Key Name is Null/Empty or contains only spaces":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    def test31_negative_VehicleGrouping_updateGroup_invalid_valueCriteria(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        criteria1_value = 123
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13230" and response_body["errors"][0][
            "message"] == "Value List can contain only 'String' Valuesmodel":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    def test32_negative_VehicleGrouping_updateGroup_nonexisting_key(self):
        print("----------------------------------------------------------")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])

        groupName = 'Group_' + str(msg_id)
        desc = "Create new group"
        criteria1_operator = "in"
        criteria1_value = "Adp"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "ACTIVE"
        criteria2_key = "lifeCycleState"
        option = "single_criteria"  # options : single_criteria or multiple_criteria
        tc = "create_vehicle_group"  # tc : create_vehicle_group or update_vehicle_group

        print('groupName : ', groupName)
        print('desc : ', desc)
        print('criteria1_operator : ', criteria1_operator)
        print('criteria1_value : ', criteria1_value)
        print('criteria1_key : ', criteria1_key)
        print('criteria2_operator : ', criteria2_operator)
        print('criteria2_value : ', criteria2_value)
        print('criteria2_key : ', criteria2_key)

        # Verify command & control response
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, "valid")

        criteria1_key = "1234@@"
        # Verify command & control response
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13235" and response_body["errors"][0][
            "message"] == "No Mapping present for Key Name '1234@@'":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")
