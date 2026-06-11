import logging
import subprocess
import time
import pytest
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from C2CModules.e2e_testData import *
from C2CModules.packageController_modules import packageController_packageAllDetails, read_packageId, \
    packageController_packageUpgrade, packageController_packageAssignmentDetails, read_packageStatus_byPackageId, \
    read_packageStatus_byTrackingId
from C2CModules.primary_IVI_device_modules import getVIN, get_SystemId, pull_logs_from_IVI_device, \
    pull_files_from_primary_IVI, pull_stability_logs_from_primary_IVI
from C2CModules.testResults import testResult
from utils.customlogger import LogGen

i = 0
OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
sched = BlockingScheduler()
self= ''
@pytest.mark.positive
def testmy_interval_job():
    # Get vin & systemId from device
    vin = getVIN(self, OnboardingType, chipsetType)
    systemId = get_SystemId(self, OnboardingType, chipsetType)
    LogGen.loggen()

    # Verify package upgrade status
    response = packageController_packageAssignmentDetails(self, systemId)

    # Get package id & status'
    packageId = 102
    status = read_packageStatus_byPackageId(self, response, packageId)
    print(status)

    print("Package Id: ", packageId)
    print("Package status: ", status)
    if status == "SUCCESS":
        packageId = 103

    try:
        print("--------------------------------------------------------------")
        print("Initiate Package Upgrade OR Assign 'Value' Package to Vehicle via API ")
        print("--------------------------------------------------------------")
        # Initiate Package Upgrade request
        response = packageController_packageUpgrade(self, systemId, vin, packageId)

        #pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
        pull_stability_logs_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
        if response['message'] == 'Vehicle Package Mapping already exist':
            print("=====================================")

            print("--------------------------------------------------------------")
            print("Verify package status : ")
            print("--------------------------------------------------------------")
            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId)

            # Get package id & status'
            status = read_packageStatus_byPackageId(self, response, packageId)

            print("Package Id: ", packageId)
            print("Package status: ", status)

            if status == "SUCCESS":
                testResult(self, "passed",
                           "'Value' package status should be set to 'SUCCESS'",
                           "'Value' package status is set to 'SUCCESS'")
            elif status != "SUCCESS":
                testResult(self, "failed",
                           "Package status should be set to 'SUCCESS'",
                           "Package status is not set to 'SUCCESS'")
        else:
            # Get package tracking id'
            packageTrackingId = response["responseData"]["packageTrackingId"]

            print("Package Tracking ID : ", packageTrackingId)
            testResult(self, "passed",
                       "Initiate package upgrade or Assign 'Value' package to Vehicle via API",
                       "Package Upgrade is initiated successfully ")

            print("--------------------------------------------------------------")
            print("Verify package status : ")
            print("--------------------------------------------------------------")

            for i in range(20):
                # Verify package upgrade status
                response = packageController_packageAssignmentDetails(self, systemId)

                # Get package id & status'
                pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")

                packageId, status = read_packageStatus_byTrackingId(self, response, packageTrackingId)
                if status != "SUCCESS" or status == "IN_PROGRESS" or status == 'RECEIVED':
                    time.sleep(30)
                    pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
                    pull_stability_logs_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
                else:
                    break

            #pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
            pull_stability_logs_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")

            if status == "SUCCESS":
                print("Upgraded Package Id: ", packageId)
                print("Upgraded Package status: ", status)
                if packageId == '102':
                    testResult(self, "passed",
                               "Vehicle should be mapped to 'Value' package",
                               "Vehicle is mapped to 'Value' package successfully")
                    logging.info('Passed')
                elif packageId == '103':
                    testResult(self, "passed",
                               "Vehicle should be mapped to 'Elite' package",
                               "Vehicle is mapped to 'Elite' package successfully")
                    logging.info('Passed')
            elif status != "SUCCESS":
                print("Vehicle is mapped to - Package Id: ", packageId)
                print("Vehicle Package status: ", status)
                if packageId == '102':
                    testResult(self, "failed",
                               "Vehicle should be mapped to 'Value' package",
                               "Vehicle is not mapped to 'Value' package successfully")
                    logging.error('Failed')
                elif packageId == '103':
                    testResult(self, "failed",
                               "Vehicle should be mapped to 'Elite' package",
                               "Vehicle is not mapped to 'Elite' package successfully")
                    logging.error('Failed')
        i = i+1
        print(i)
        logging.info(i)
    except:
        packageTrackingId = ''
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
        pull_stability_logs_from_primary_IVI(self, OnboardingType, chipsetType, "stability_logs")
        testResult(self, "failed",
                   "Initiate package upgrade via API",
                   "Something went wrong while initiating package upgrade via API")
        logging.error('Failed')
        assert False

    print("--------------------------------------------------------------")

sched.add_job(testmy_interval_job, 'interval', seconds=900)
sched.start()
