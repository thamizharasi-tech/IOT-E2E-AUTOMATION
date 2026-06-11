import inspect
import logging
import os
import sys
import time


sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from C2CModules.e2e_testData import *
from C2CModules.fms_modules import get_tridId_from_log, assetManagement_trip_waypoints_by_tripid, \
    assetManagement_latest_trip_meta, assetManagement_latest_trip_details, assetManagement_trip_info_by_tripId, \
    read_tripId_from_Trip_waypoints
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notification_message
from C2CModules.primary_IVI_device_modules import *
from C2CModules.vehicle_metadata import vehicle_update_vehicle_meta_data

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi

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
    
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Update vehicle meta
        # ===========================================================================================

        vin = getVIN(self, OnboardingType, chipsetType)
        vehicle_update_vehicle_meta_data(self, vin, "demovehicle", "2")

        # ===========================================================================================
        # Run telemetry stub on device for trip waypoint
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, trip_waypoint_stub_option)
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify trip messages in log file
        # ===========================================================================================

        # Get trip Id

        # ===========================================================================================
        # Pull logs for Trip Id
        # ===========================================================================================
        print("Pull/Fetch device logs for Trip Id : ")

        i = 0
        while i <= 2:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)
            if tripId != '':
                break
            else:
                ("Trip Id not found in c2c logs, thus fetching 'Trip_Waypoints' folder to host machine for trip file")
                tripId = read_tripId_from_Trip_waypoints(self, OnboardingType, chipsetType, 'Trip_waypoints')
                if tripId != '':
                    break
                else:
                    time.sleep(10)
            i = i + 1

        if tripId == "":
            testResult(self, "failed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        # telemetry - trip start = "event_type": 4005

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        ls = verify_message_in_log(self, trip_start_reason_code, trip_start_reason_code)

        if trip_start_reason_code in str(ls[0]):
            print(f"Trip is started with ' {trip_start_reason_code} ' ")
            testResult(self, "passed", "Trip should start on device ",
                       "Trip is started and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:

                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_start_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip start event type code should be present in the telemetry message published to the cloud",
                               "Trip start event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_start_event_type_code not in msg_body_data:
                    testResult(self, "failed",
                               "Trip start event type code should be present in the telemetry message published to the cloud",
                               "Trip start event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        # tripId = get_tridId_from_log(self)
        if str(ls[0]) == "Error":
            print(
                "Either trip is not started or device logs are not updated or logs have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated or have been rotated. pls refer device "
                       "logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run trip stub on device for trip stop
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run trip stop stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stop')

        print("Trip stop process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            time.sleep(60)
            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stop')
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

            if trip_stop_reason_code in str(ls[0]):
                print(
                    "Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
                testResult(self, "verificationFailed", "Trip should stop on device ",
                           "Either trip is not stopped or device logs are not updated or have been rotated. pls refer device logs in detail ")

        time.sleep(60)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(30)

        # tripId = get_tridId_from_log(self)
        # print(tripId)
        time.sleep(120)

        print("----------------------------------------------------------")

        i = 0
        while i in range(10):
            response_body = assetManagement_trip_waypoints_by_tripid(self, tripId)
            if response_body["responseData"]['message'] == "Trip summary details not exist":
                time.sleep(120)
            else:
                break

        assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")
        # validate trip Id
        actual_tripId = response_body["responseData"]['data']['tripId']
        actual_tripId1 = response_body["responseData"]["data"]["tripWaypointData"]["meta"]["tripId"]
        print(f"Trip Id stored in Cloud' {actual_tripId}, {actual_tripId1} ' ")

        if actual_tripId == tripId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is stored in cloud DB successfully")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is not stored in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # Validation of api response data

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # validate system id & trip Id mapping
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        actual_systemId = response_body["responseData"]['data']['systemId']
        print(f"Trip Id mapped to System Id in Cloud ' {actual_systemId} ' ")
        if actual_systemId == systemId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is mapped to device systemId in cloud DB")
        else:
            testResult(self, "failed",
                       "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")

        # validate rpm value
        actual_rpm = response_body["responseData"]['data']["tripWaypointData"]["tripWaypoints"][0]["rpm"]
        print(f"RPM value configured in stub ' {trip_waypoint_rpm_value} ' ")
        print(f"RPM value stored in Cloud ' {actual_rpm} ' ")

        if float(actual_rpm) == trip_waypoint_rpm_value:
            testResult(self, "passed",
                       "Trip Waypoint - RPM value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - RPM value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Trip Waypoint - RPM value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - RPM value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")

        print("----------------------------------------------------------")

        # validate speed value
        actual_speed = response_body["responseData"]['data']["tripWaypointData"]["tripWaypoints"][0]["speed"]
        print(f"Speed value configured in stub ' {trip_waypoint_speed_value } ' ")
        print(f"Speed value stored in Cloud ' {actual_speed} ' ")

        if float(actual_speed) == trip_waypoint_speed_value or float(actual_speed) == trip_waypoint_speed_value_1:
            testResult(self, "passed",
                       "Trip Waypoint - Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Trip Waypoint - Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
            self.result.set_result(TestResults.failed)

        
        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

    def cleanup(self):
        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")
        
        print("================Execution Ends================")        


if __name__ == '__main__':
    test = Test()
    test.run()

