import inspect
import logging
import os
import sys
from pathlib import Path

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
sys.path.insert(0, parent_dir)


from C2CModules.sota_api_modules import SOTA_uploadPackage
from utils.XLUtils import read_api_data_from_excel

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test:

    def test_execute(self):
        try:
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                model = str(dict1["model"])
                system = str(dict1["system"])
                description = str(dict1["description"])
                isDiffImage = str(dict1["isDiffImage"])
                downloadConsent = str(dict1["downloadConsent"])
                installConsent = str(dict1["installConsent"])
                rebootConsent = str(dict1["rebootConsent"])
                packageName = str(dict1["packageName"])

                # Call api reusable model
                response = SOTA_uploadPackage(self, model, system, description, isDiffImage, downloadConsent,
                                          installConsent, rebootConsent, packageName, "empty_apiKey")

                response_body = response.json()
                if (response.status_code == 403):
                    if (response_body["message"] == "api keys are not matching..please provide valid key"):
                        assert True
                        # self.result.set_result(TestResults.passed)
                else:
                    # self.result.set_result(TestResults.failed)
                    assert False
                print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            # self.result.set_result(TestResults.failed)
            assert False


