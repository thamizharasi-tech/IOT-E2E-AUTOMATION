import json
import os, sys, datetime, time, subprocess, inspect, logging
import requests

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from C2CModules.token_generation import *

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

            mahindra_token_gen_reus_mod(self, "API_Data", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_CreateIncident", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFileDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_SearchCriteria", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_AllVehicleDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_FetchAllUserDetailsDesc", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_FetchAllActiveVehicles", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_DownloadUrl", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_FetchAllUserDetailsAsc", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_VehicleDetailsInTable", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_VehicleDetailsAsc", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_VehicleDetailsDesc", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_FetchAllUserDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogsVehicleBased", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC001", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC002", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC003", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC004", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC005", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC006", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC007", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFilesTC008", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_IncidentDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_UserDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_UserDetails_SearchBy", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ForgotPassword", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_User_Login", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_User_Signup", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ApproveUser", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_DisableUser", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_AddUser", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_UpdateIncidentDetails", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_Check_DownloadURL_IsExist", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFileDetails_SortBy", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_AddVehicles", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_IncidentDetails_SearchCriteria", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFileDetails_SearchCriteria", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFileDetailsASC", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_LogFileDetailsDESC", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ViewLogTC001", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ViewLogTC002", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ViewLogTC003", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ViewLogTC004", "Mahindra_getToken")
            mahindra_update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_ViewLogTC005", "Mahindra_getToken")

            self.result.set_result(TestResults.passed)

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            self.result.set_result(TestResults.failed)

    def cleanup(self):
        pass


if __name__ == '__main__':
    test = Test()
    test.run()