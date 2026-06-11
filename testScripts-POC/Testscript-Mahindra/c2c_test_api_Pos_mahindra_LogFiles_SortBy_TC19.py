import json
import os, sys, datetime, time, subprocess, inspect, logging
import requests
import random
from datetime import datetime, timezone

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from C2CModules.logManager_modules import *
from C2CModules.e2e_testData import *
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel, save_data_in_excel

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

try:
    from axiom.ttypes import *
except:
    from Axiom.ttypes import *
from axiom_framework.tests.base import Test as Base
from axiom_framework.results.base import TestResults


class Test(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self):
        pass

    def execute(self):
        try:
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            dict1 = read_api_data_from_excel(self, "Mahindra", "log_file_details_sort_by_tc19")
            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                system_id = str(dict1["SystemId"])
                sort_by = str(dict1["sortBy"])

                # Call api reusable model
                response_body = logManager_log_files_sort_by(self, system_id, sort_by)

                if response_body['message'] == "Success":
                    testResult(self, "passed", "log file details fetched successfully",
                               "log file details fetched successfully")
                    self.result.set_result(TestResults.passed)
                elif response_body['message'] != "Success":
                    testResult(self, "failed", "log file details fetched successfully",
                               "log file details not fetched successfully   " + " Reason for failure is : " +
                               response_body["message"])
                    self.result.set_result(TestResults.failed)

                else:
                    print("Something went wrong")
                print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            self.result.set_result(TestResults.failed)

    def cleanup(self):
        pass


if __name__ == '__main__':
    test = Test()
    test.run()