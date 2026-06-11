
from C2CModules.e2e_testData import *
from C2CModules.packageController_modules import packageController_packageUpgrade, packageController_packageAllDetails, \
    read_packageId, packageController_packageAssignmentDetails, read_packageStatus_byTrackingId, \
    read_packageStatus_byPackageId
from C2CModules.primary_IVI_device_modules import *

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test1_PackageControll:

    def test1_packageUpgrade_Value(self):
        # ===========================================================================================
        # Initiate Package Upgrade via API
        # ===========================================================================================
        try:
            print("--------------------------------------------------------------")
            print("Get 'Value' package Id to assign it to vehicle")
            print("--------------------------------------------------------------")

            # Get vin & systemId from device
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            packageId = read_packageId(self, response, "Value")

            print("Package Id for 'Value' Package : ", packageId)

            testResult(self, "passed",
                       "Get package id for 'Value' Package to upgrade",
                       "All package details are listed and package id for 'Value' is fetched successfully ")
        except:
            testResult(self, "failed",
                       "Get package id for 'Value' Package to upgrade",
                       "Something went wrong while fetching all package details")

        try:
            print("--------------------------------------------------------------")
            print("Initiate Package Upgrade OR Assign 'Value' Package to Vehicle via API ")
            print("--------------------------------------------------------------")
            # Initiate Package Upgrade request
            response = packageController_packageUpgrade(self, systemId, vin, packageId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            if response['message'] == 'Vehicle Package Mapping already exist':
                print(" => Vehicle is already mapped to 'Value' package, hence skipping this step")

                print("--------------------------------------------------------------")
                print("Verify package status : ")
                print("--------------------------------------------------------------")
                # Verify package upgrade status
                response = packageController_packageAssignmentDetails(self, systemId, "valid")

                # Validate response status code
                if response.status_code == 200:
                    print("API response status code is :", str(response.status_code))
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Status code is not 200. Rather found : " + str(response.status_code))
                    # self.result.set_result(TestResults.failed)
                    assert False

                # parse api response into json
                response = response.json()

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
                    response = packageController_packageAssignmentDetails(self, systemId, "valid")

                    # Validate response status code
                    if response.status_code == 200:
                        print("API response status code is :", str(response.status_code))
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Status code is not 200. Rather found : " + str(response.status_code))
                        # self.result.set_result(TestResults.failed)
                        assert False

                    # parse api response into json
                    response = response.json()

                    # Get package id & status'

                    packageId, status = read_packageStatus_byTrackingId(self, response, packageTrackingId)
                    if status != "SUCCESS" or status == "IN_PROGRESS" or status == 'RECEIVED':
                        time.sleep(30)
                    else:
                        break

                if status == "SUCCESS":
                    print("Upgraded Package Id: ", packageId)
                    print("Upgraded Package status: ", status)
                    testResult(self, "passed",
                               "Vehicle should be mapped to 'Value' package",
                               "Vehicle is mapped to 'Value' package successfully")
                elif status != "SUCCESS":
                    print("Vehicle is mapped to - Package Id: ", packageId)
                    print("Vehicle Package status: ", status)
                    testResult(self, "failed",
                               "Vehicle should be mapped to 'Value' package",
                               "Vehicle is not mapped to 'Value' package successfully")
        except:
            packageTrackingId = ''
            testResult(self, "failed",
                       "Initiate package upgrade via API",
                       "Something went wrong while initiating package upgrade via API")

        print("--------------------------------------------------------------")

    def test2_packageUpgrade_Elite(self):
        # ===========================================================================================
        # Initiate Package Upgrade via API
        # ===========================================================================================
        try:
            print("--------------------------------------------------------------")
            print("Get 'Elite' package Id to assign it to vehicle")
            print("--------------------------------------------------------------")

            # Get vin & systemId from device
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            packageId = read_packageId(self, response, "Elite")

            print("Package Id for 'Elite' Package : ", packageId)

            testResult(self, "passed",
                       "Get package id for 'Elite' Package to upgrade",
                       "All package details are listed and package id for 'Elite' is fetched successfully ")
        except:
            testResult(self, "failed",
                       "Initiate package upgrade or assign desired package to vehicle via API",
                       "Something went wrong while assigning package to vehicle via API")

        try:
            print("--------------------------------------------------------------")
            print("Initiate Package Upgrade OR Assign 'Elite' Package to Vehicle via API ")
            print("--------------------------------------------------------------")
            # Initiate Package Upgrade request
            response = packageController_packageUpgrade(self, systemId, vin, packageId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            if response['message'] == 'Vehicle Package Mapping already exist':
                print(" => Vehicle is already mapped to 'Elite' package, hence skipping this step")

                print("--------------------------------------------------------------")
                print("Verify package status : ")
                print("--------------------------------------------------------------")

                # Verify package upgrade status
                response = packageController_packageAssignmentDetails(self, systemId, "valid")

                # Validate response status code
                if response.status_code == 200:
                    print("API response status code is :", str(response.status_code))
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Status code is not 200. Rather found : " + str(response.status_code))
                    # self.result.set_result(TestResults.failed)
                    assert False

                # parse api response into json
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                print("Package Id: ", packageId)
                print("Package status: ", status)

                if status == "SUCCESS":
                    testResult(self, "passed",
                               "'Elite' package status should be set to 'SUCCESS'",
                               "'Elite package status is set to 'SUCCESS'")
                elif status != "SUCCESS":
                    testResult(self, "failed",
                               "Package status should be set to 'SUCCESS'",
                               "Package status is not set to 'SUCCESS'")
            else:
                # Get package tracking id'
                packageTrackingId = response["responseData"]["packageTrackingId"]

                print("Package Tracking ID : ", packageTrackingId)
                testResult(self, "passed",
                           "Initiate package upgrade or Assign 'Elite' package to Vehicle via API",
                           "Package Upgrade is initiated successfully ")

                print("--------------------------------------------------------------")
                print("Verify package status : ")
                print("--------------------------------------------------------------")

                # Verify package upgrade status
                for i in range(20):

                    response = packageController_packageAssignmentDetails(self, systemId, "valid")

                    # Validate response status code
                    if response.status_code == 200:
                        print("API response status code is :", str(response.status_code))
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Status code is not 200. Rather found : " + str(response.status_code))
                        # self.result.set_result(TestResults.failed)
                        assert False

                    # parse api response into json
                    response = response.json()

                    # Get package id & status'

                    packageId, status = read_packageStatus_byTrackingId(self, response, packageTrackingId)
                    if status != "SUCCESS" or status == 'IN_PROGRESS' or status == 'RECEIVED':
                        time.sleep(30)
                    else:
                        break

                if status == "SUCCESS" :
                    print("Upgraded Package Id: ", packageId)
                    print("Upgraded Package status: ", status)
                    testResult(self, "passed",
                               "Vehicle should be mapped to 'Elite' package",
                               "Vehicle is mapped to 'Elite' package successfully")
                elif status != "SUCCESS":
                    print("Vehicle is mapped to - Package Id: ", packageId)
                    print("Vehicle Package status: ", status)
                    testResult(self, "failed",
                               "Vehicle should be mapped to 'Elite' package",
                               "Vehicle is not mapped to 'Elite' package successfully")
        except:
            packageTrackingId = ''
            testResult(self, "failed",
                       "Initiate package upgrade or assign desired package to vehicle via API",
                       "Something went wrong while assigning package to vehicle via API")

        print("--------------------------------------------------------------")

    def test3_packageUpgrade_Essential(self):
        # ===========================================================================================
        # Initiate Package Upgrade via API
        # ===========================================================================================
        try:
            print("--------------------------------------------------------------")
            print("Get 'Essential' package Id to assign it to vehicle")
            print("--------------------------------------------------------------")

            # Get vin & systemId from device
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            packageId = read_packageId(self, response, "Essential")

            print("Package Id for 'Essential' Package : ", packageId)

            testResult(self, "passed",
                       "Get package id for 'Essential' Package to upgrade",
                       "All package details are listed and package id for 'Essential' is fetched successfully ")
        except:
            testResult(self, "failed",
                       "Get package id for 'Essential' Package to upgrade",
                       "Something went wrong while fetching all package details")

        try:
            print("--------------------------------------------------------------")
            print("Initiate Package Upgrade OR Assign 'Essential' Package to Vehicle via API ")
            print("--------------------------------------------------------------")

            # Initiate Package Upgrade request
            response = packageController_packageUpgrade(self, systemId, vin, packageId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("API response status code is :", str(response.status_code))
                # self.result.set_result(TestResults.passed)
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                # self.result.set_result(TestResults.failed)
                assert False

            # parse api response into json
            response = response.json()

            if response['message'] == 'Vehicle Package Mapping already exist':
                print(" => Vehicle is already mapped to 'Essential' package, hence skipping this step")

                print("--------------------------------------------------------------")
                print("Verify package status : ")
                print("--------------------------------------------------------------")
                # Verify package upgrade status
                response = packageController_packageAssignmentDetails(self, systemId, "valid")

                # Validate response status code
                if response.status_code == 200:
                    print("API response status code is :", str(response.status_code))
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Status code is not 200. Rather found : " + str(response.status_code))
                    # self.result.set_result(TestResults.failed)
                    assert False

                # parse api response into json
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                print("Package Id: ", packageId)
                print("Package status: ", status)

                if status == "SUCCESS":
                    testResult(self, "passed",
                               "'Essential' package status should be set to 'SUCCESS'",
                               "'Essential' package status is set to 'SUCCESS'")
                elif status != "SUCCESS":
                    testResult(self, "failed",
                               "Package status should be set to 'SUCCESS'",
                               "Package status is not set to 'SUCCESS'")
            else:
                # Get package tracking id'
                packageTrackingId = response["responseData"]["packageTrackingId"]

                print("Package Tracking ID : ", packageTrackingId)
                testResult(self, "passed",
                           "Initiate package upgrade or Assign 'Essential package to Vehicle via API",
                           "Package Upgrade is initiated successfully ")

                print("--------------------------------------------------------------")
                print("Verify package status : ")
                print("--------------------------------------------------------------")

                for i in range(20):
                    # Verify package upgrade status
                    response = packageController_packageAssignmentDetails(self, systemId, "valid")

                    # Validate response status code
                    if response.status_code == 200:
                        print("API response status code is :", str(response.status_code))
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Status code is not 200. Rather found : " + str(response.status_code))
                        # self.result.set_result(TestResults.failed)
                        assert False

                    # parse api response into json
                    response = response.json()

                    # Get package id & status'

                    packageId, status = read_packageStatus_byTrackingId(self, response, packageTrackingId)
                    if status != "SUCCESS" or status == "IN_PROGRESS" or status == 'RECEIVED':
                        time.sleep(30)
                    else:
                        break

                if status == "SUCCESS":
                    print("Upgraded Package Id: ", packageId)
                    print("Upgraded Package status: ", status)
                    testResult(self, "passed",
                               "Vehicle should be mapped to 'Essential' package",
                               "Vehicle is mapped to 'Essential' package successfully")
                elif status != "SUCCESS":
                    print("Vehicle is mapped to - Package Id: ", packageId)
                    print("Vehicle Package status: ", status)
                    testResult(self, "failed",
                               "Vehicle should be mapped to 'Essential' package",
                               "Vehicle is not mapped to 'Essential' package successfully")
        except:
            packageTrackingId = ''
            testResult(self, "failed",
                       "Initiate package upgrade or assign desired package to vehicle via API",
                       "Something went wrong while assigning package to vehicle via API")

        print("--------------------------------------------------------------")

