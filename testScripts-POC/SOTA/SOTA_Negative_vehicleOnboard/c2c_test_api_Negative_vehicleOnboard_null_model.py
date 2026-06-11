import json
import os, sys, datetime, time, subprocess, inspect, logging
import requests
import random
from datetime import datetime, timezone


from pathlib import Path
 
sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
sys.path.insert(0, parent_dir)


from C2CModules.sota_api_modules import SOTA_VehicleOnboard
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
            dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-VehicleOnboardnullmodel")
            if dict1['Flag'] == "Yes":
                model = str(dict1["model"])
                if model == "None":
                    model = None
                name = str(dict1["name"])
                partNo = str(dict1["partNo"])
                sn = str(dict1["sn"])
                vin = str(dict1["vins"])

                # Call api reusable model
                response = SOTA_VehicleOnboard(self, model, name, partNo, sn, vin)

                response_body = response.json()
                if (response.status_code == 400):
                    if (response_body["message"] == "model cannot be null or empty"):
                        self.result.set_result(TestResults.passed)
                else:
                    self.result.set_result(TestResults.failed)

                print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            self.result.set_result(TestResults.failed)

    def cleanup(self):
        pass


if __name__ == '__main__':
    test = Test()
    test.run()

