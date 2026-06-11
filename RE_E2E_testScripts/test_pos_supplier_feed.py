import json
import time
from datetime import timezone, datetime
import random

from C2CModules.e2e_testData import *

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_supplierFeed:

    def test1_supplier_feed(self):

        print("\n------------------------------START------------------------------\n")

        """

        This test is validating the Supplier Feed functionality. (positive scenario)

        :return: return test status

        Validate Supplier Feed

        """
        print("=========GENERATE AND UPDATE IMEI AND ICCID IN CSV========")
        imei = "IMEI" + str(random.randint(1, 1000))
        iccid = "ICCID" + str(random.randint(1, 1000))

        print("IMEI: ", imei)
        print("ICCID: ", iccid)

        write_to_csv(self, imei, iccid)

        print("\n------------------SUPPLIER FEED------------------\n")

        print("----------------------------------------------------------")

        utc_time = datetime.now()

        dt = utc_time.strftime("%Y-%m-%d_%H_%M")

        dt1 = utc_time.strftime("%Y-%m-%d_%H")

        print("Current date & time :", dt)

        print("----------------------------------------------------------")

        response = supplier_feed(self, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            if response_body["message"] == "Supplier feed Saved Successfully":
                if response_body["supplierFeed"][0]["iccid"] == iccid:
                    if response_body["supplierFeed"][0]["mnoStatus"] == "Success":
                        trackingId = response_body["supplierFeed"][0]["trackingId"]
                        testResult(self, "passed",

                                   "Validate that Supplier feed saved successfully",

                                   "Supplier feed saved successfully, pls refer api response for detailed info")

            else:

                testResult(self, "failed",

                       "Validate that Supplier feed is saved successfully",

                       "Supplier feed is not saved, pls refer api response for detailed info")

        elif response.status_code == 400:

            # Validate response body

            if response_body["errors"][0]["message"] == "device imei is already exits":

                testResult(self, "passed",

                       "Validate that Supplier feed is saved or already exists in DB",

                       "Supplier feed is already exits, pls refer api response for detailed info")

            else:

                testResult(self, "failed",

                       "Validate that Supplier feed is saved successfully",

                       "Supplier feed is not saved or does not exits, pls refer api response for detailed info")

        else:

            testResult(self, "failed",

                   "Validate that Supplier feed is saved successfully",

                   "Supplier data is not saved, pls refer api response for detailed info")

        # verify supplier feed status on the cloud side
        response = supplier_feed_status(self, trackingId, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data fetched successfully":
            if response_body["supplierFeed"][0]["mnoStatus"] == "Success" and response_body["supplierFeed"][0]["iccid"] == iccid:
                trackingId_actual = response_body["supplierFeed"][0]["trackingId"]
                if trackingId == trackingId_actual:
                    testResult(self, "passed", "Supplier Feed data should be saved successfully",
                               "Supplier Feed data saved successfully")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Data fetched successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Supplier Feed data should be saved successfully",
                       "Supplier Feed data failed to save" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False