import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random

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
        criteria1_value = "Cruiser"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "REGIONAL_ACTIVE"
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
        criteria1_value = "b2c"
        criteria1_key = "style"
        criteria2_operator = "eq"
        criteria2_value = "REGIONAL_ACTIVE"
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
        criteria1_value = "Cruiser"
        criteria1_key = "model"
        criteria2_operator = "eq"
        criteria2_value = "REGIONAL_ACTIVE"
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
        criteria1_value = "b2c"
        criteria1_key = "style"
        criteria2_operator = "eq"
        criteria2_value = "REGIONAL_ACTIVE"
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
