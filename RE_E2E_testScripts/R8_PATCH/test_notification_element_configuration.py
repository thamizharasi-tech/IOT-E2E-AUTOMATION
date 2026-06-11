import json
import time
from datetime import timezone
import random

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.vehicle_state import *
from C2CModules.commandControl_modules import *
from C2CModules.telemetry_modules import *
from C2CModules.notifications import *
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_vehConf_ERT:

    def test_pos_notification_add_new_element(self):

        # Read testdata from excel sheet
        dict = read_api_data_from_excel(self, "Notification", "Notification_addNewElement")

        alertAttributeName = str(dict["alertAttributeName"])
        modelCode = str(dict["modelCode"])
        eventType = str(dict["eventType"])
        attributeName = str(dict["attributeName"])
        attributeDisplayName = str(dict["attributeDisplayName"])
        elementId = str(dict["elementId"])
        unit = str(dict["unit"])
        dataType = str(dict["dataType"])
        active = str(dict["active"])

        print("=================Test data=================")
        print("Alert Attribute Name: ", alertAttributeName)
        print("Model Code: ", modelCode)
        print("Event Type: ", eventType)
        print("Attribute Name: ", attributeName)
        print("Attribute Display Name: ", attributeDisplayName)
        print("Element Id: ", elementId)
        print("Unit: ", unit)
        print("Data Type: ", dataType)
        print("Active: ", active)


        notification_attribute(self, alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
                               elementId, unit, dataType, active, "save_notification_attribute")

    def test_pos_notification_update_element(self):

        # Read testdata from excel sheet
        dict = read_api_data_from_excel(self, "Notification", "Notification_updateElement")

        alertAttributeName = str(dict["alertAttributeName"])
        modelCode = str(dict["modelCode"])
        eventType = str(dict["eventType"])
        attributeName = str(dict["attributeName"])
        attributeDisplayName = str(dict["attributeDisplayName"])
        elementId = str(dict["elementId"])
        unit = str(dict["unit"])
        dataType = str(dict["dataType"])
        active = str(dict["active"])

        print("=================Test data=================")
        print("Alert Attribute Name: ", alertAttributeName)
        print("Model Code: ", modelCode)
        print("Event Type: ", eventType)
        print("Attribute Name: ", attributeName)
        print("Attribute Display Name: ", attributeDisplayName)
        print("Element Id: ", elementId)
        print("Unit: ", unit)
        print("Data Type: ", dataType)
        print("Active: ", active)


        notification_attribute(self, alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
                               elementId, unit, dataType, active, "update_notification_attribute")

    def test_pos_notification_delete_element(self):

        # Read testdata from excel sheet
        dict = read_api_data_from_excel(self, "Notification", "Notification_updateElement")

        alertAttributeName = str(dict["alertAttributeName"])
        modelCode = str(dict["modelCode"])
        eventType = str(dict["eventType"])
        attributeName = str(dict["attributeName"])
        attributeDisplayName = str(dict["attributeDisplayName"])
        elementId = str(dict["elementId"])
        unit = str(dict["unit"])
        dataType = str(dict["dataType"])
        active = str(dict["active"])

        notification_attribute(self, alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
                               elementId, unit, dataType, active, "delete_notification_attribute")

