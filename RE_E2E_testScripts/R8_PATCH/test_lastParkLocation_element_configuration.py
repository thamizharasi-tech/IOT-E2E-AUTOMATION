import pytest

from C2CModules.telemetry_modules import *
from C2CModules.primary_IVI_device_modules import *
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_LastParkLocation:

    def test1_positive_lastPark_location_save_telemetry_elements(self):

        print("----------------------------------------------------------")

        # Expected parameters
        parameter1 = {"attributeName": "GPS_SIGNAL_STRENGTH", "modelCode": "1234", "elementId": 554745871,
                      "eventType": 1234, "values": "NA", "idName": "AL_GPS_SIGNAL_STRENGTH", "unit": "NA"}
        parameter2 = {"attributeName": "NETWORK_OP_NAME", "modelCode": "1234", "elementId": 554745872,
                      "eventType": 1234, "values": "NA", "idName": "AL_NETWORK_OP_NAME", "unit": "NA"}
        parameter3 = {"attributeName": "LATITUDE", "modelCode": "1234", "elementId": 559940097, "eventType": 1234,
                      "values": "", "idName": "AL_GPS_STATUS", "unit": ""}
        parameter4 = {"attributeName": "GPS_STATUS", "modelCode": "1234", "elementId": 554745870, "eventType": 1234,
                      "values": "", "idName": "AL_GPS_STATUS", "unit": ""}
        parameter5 = {"attributeName": "LONGITUDE", "modelCode": "1234", "elementId": 559940098, "eventType": 1234,
                      "values": "", "idName": "AL_LONGITUDE", "unit": ""}
        parameter6 = {"attributeName": "DIRECTION", "modelCode": "1234", "elementId": 559940100, "eventType": 1234,
                      "values": "", "idName": "AL_BEARING", "unit": ""}
        parameter7 = {"attributeName": "ALTITUDE", "modelCode": "1234", "elementId": 559940099, "eventType": 1234,
                      "values": "", "idName": "AL_ALTITUDE", "unit": ""}
        parameter8 = {"attributeName": "GPS_SPEED", "modelCode": "1234", "elementId": 559942149, "eventType": 1234,
                      "values": "", "idName": "AL_VELOCITY", "unit": ""}
        parameter9 = {"attributeName": "PDOP", "modelCode": "1234", "elementId": 559988760, "eventType": 1234,
                      "values": "", "idName": "AL_PDOP", "unit": ""}
        parameter10 = {"attributeName": "HDOP", "modelCode": "1234", "elementId": 559988761, "eventType": 1234,
                       "values": "", "idName": "AL_HDOP", "unit": ""}
        parameter11 = {"attributeName": "GPSFIX", "modelCode": "1234", "elementId": 559988762, "eventType": 1234,
                       "values": "", "idName": "AL_GPS_FIX", "unit": ""}
        parameter12 = {"attributeName": "LATDIR", "modelCode": "1234", "elementId": 554745874, "eventType": 1234,
                       "values": "", "idName": "AL_LAT_DIR", "unit": ""}
        parameter13 = {"attributeName": "LONGDIR", "modelCode": "1234", "elementId": 554745875, "eventType": 1234,
                       "values": "", "idName": "AL_LONG_DIR", "unit": ""}
        parameter14 = {"attributeName": "TIMESTAMP", "modelCode": "1234", "elementId": 559988753, "eventType": 1234,
                       "values": "", "idName": "AL_TIMESTAMP", "unit": ""}
        parameter15 = {"attributeName": "IGNITION", "modelCode": "1234", "elementId": 557875730, "eventType": 1234,
                       "values": "", "idName": "Vehicle_Mode__Vehicle_Mode_Lvl_1_RX_V", "unit": ""}

        print("Parameter-1: ", parameter1)
        print("Parameter-1: ", parameter2)
        print("Parameter-1: ", parameter3)
        print("Parameter-1: ", parameter4)
        print("Parameter-1: ", parameter5)
        print("Parameter-1: ", parameter6)
        print("Parameter-1: ", parameter7)
        print("Parameter-1: ", parameter8)
        print("Parameter-1: ", parameter9)
        print("Parameter-1: ", parameter10)
        print("Parameter-1: ", parameter11)
        print("Parameter-1: ", parameter12)
        print("Parameter-1: ", parameter13)
        print("Parameter-1: ", parameter14)
        print("Parameter-1: ", parameter15)

        lastPark_location_save_telemetry_elements(self, parameter1, parameter2, parameter3, parameter4, parameter5,
                                                  parameter6, parameter7, parameter8, parameter9, parameter10,
                                                  parameter11, parameter12, parameter13, parameter14, parameter15)

    def test2_positive_lastPark_location_update_telemetry_elements(self):

        print("----------------------------------------------------------")

        # Test data
        elementId = "559941197"
        attributeName = "LATITUDE"
        modelCode = "1234"
        eventType = "1234"
        values = "NA"
        idName = "AL_LATITUDE"
        unit = "NA"

        print("Element Id: ", elementId)
        print("Attribute Name: ", attributeName)
        print("Model Code: ", modelCode)
        print("Event Type: ", eventType)
        print("Values: ", values)
        print("Id Name: ", idName)
        print("Unit: ", unit)

        lastPark_location_update_telemetry_elements(self, elementId, attributeName, modelCode, eventType, values,
                                                    idName, unit)

    def test3_positive_lastPark_location_delete_telemetry_elements(self):

        print("----------------------------------------------------------")

        # Test data
        attributeName = "LATITUDE"
        modelCode = "1234"

        print("Attribute Name: ", attributeName)
        print("Model Code: ", modelCode)

        lastPark_location_delete_telemetry_elements(self, attributeName, modelCode)

