import json
import os, sys, datetime, time, subprocess, inspect, logging
from pathlib import Path

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir)

from C2CModules.logManager_modules import *
from C2CModules.e2e_testData import *
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

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
            dict1 = read_api_data_from_excel(self, "Mahindra", "add_user")
            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                system_id = str(dict1["SystemId"])
                device_id = str(dict1["deviceId"])
                vin = str(dict1["vin"])

                # List of users
                selectedUsers = str(dict1["selectedUsers"]).split(',')

                # Call api reusable model
                response_body = logManager_add_user(self, system_id, device_id, vin, selectedUsers)

                if response_body['message'] == "Success":
                    testResult(self, "passed", "users details added successfully",
                               "users details added successfully")
                    self.result.set_result(TestResults.passed)

                elif response_body['message'] != "Success":
                    testResult(self, "failed", "users details added successfully",
                               "users details are not added successfully   " + " Reason for failure is : " +
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