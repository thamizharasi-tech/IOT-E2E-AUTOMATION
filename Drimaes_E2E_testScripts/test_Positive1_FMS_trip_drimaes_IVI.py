import base64
import random
import time
import pytest

from C2CModules.e2e_testData import *
from C2CModules.fms_modules import get_tridId_from_log, assetManagement_trip_waypoints_by_tripid, \
    assetManagement_latest_trip_meta, assetManagement_latest_trip_details, assetManagement_trip_info_by_tripId, \
    calculate_trip_duration, calculate_average_speed, calculate_trip_batterySOClevel_efficiency, \
    calculate_batterySOClevel_consumed, calculate_trip_distance, calculate_fuel_consumed, calculate_CO2_emission, \
    calculate_trip_fuel_efficiency
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notification_message
from C2CModules.primary_IVI_device_modules import *
from C2CModules.vehicle_metadata import vehicle_update_vehicle_meta_data

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi


class Test1_FMS_trip:

    @pytest.mark.regression
    # Validate telemetry functionality.
    def test1_telemetry_trip_start(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_trip_start")
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
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
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

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")

        print("----------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry functionality.
    def test2_telemetry_trip_stop(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_trip_stop")
        time.sleep(60)

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
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - trip stop = "event_type": 4006

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not started/stopped or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_type_code, telemetry_msg_type_code)

        if telemetry_msg_type_code in str(ls[0]) and telemetry_msg_type_code in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:

                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_stop_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_stop_event_type_code not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")

        print("----------------------------------------------------------")

    def test3_trip_waypoint(self):

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")
        # telemetry - trip stop "event_type": 4006
        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start & stop - telemetry receive topic
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_recv_topic)

        if telemetry_recv_topic in str(ls[0]):
            print(f"Telemetry message published on ' {telemetry_recv_topic} '  topic")
            testResult(self, "passed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is published on telemetry recevive topic and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is not published on telemetry receive topic or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # telemetry - trip start & stop - message-type
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code)

        if telemetry_msg_type_code in str(ls[0]):
            print(f"Telemetry message published to cloud via ' {telemetry_msg_type_code} ' topic")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:
                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_stop_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_stop_event_type_code not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(30)

        tripId = get_tridId_from_log(self)
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
            testResult(self, "verificationFailed",
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
            testResult(self, "verificationFailed",
                       "Trip Waypoint - RPM value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - RPM value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")

        print("----------------------------------------------------------")

        # validate speed value
        actual_speed = response_body["responseData"]['data']["tripWaypointData"]["tripWaypoints"][0]["speed"]
        print(f"Speed value configured in stub ' {trip_waypoint_speed_value } ' ")
        print(f"Speed value stored in Cloud ' {actual_speed} ' ")

        if float(actual_speed) == trip_waypoint_speed_value :
            testResult(self, "passed",
                       "Trip Waypoint - Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Waypoint - Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Waypoint - Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

    def test4_trip_summary_engine_type_2(self):

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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, trip_summary_stub_option)
        time.sleep(10)

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")
        # telemetry - trip stop "event_type": 4006
        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start & stop - telemetry receive topic
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_recv_topic)

        if telemetry_recv_topic in str(ls[0]):
            print(f"Telemetry message published on ' {telemetry_recv_topic} '  topic")
            testResult(self, "passed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is published on telemetry recevive topic and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is not published on telemetry receive topic or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # telemetry - trip start & stop - message-type
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code)

        if telemetry_msg_type_code in str(ls[0]):
            print(f"Telemetry message published to cloud via ' {telemetry_msg_type_code} ' topic")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:
                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_stop_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_stop_event_type_code not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(120)

        tripId = get_tridId_from_log(self)

        print("----------------------------------------------------------")
        time.sleep(120)

        i = 0
        while i in range(10):
            response_body = assetManagement_trip_info_by_tripId(self, tripId)
            if response_body["responseData"]['message'] == "Trip summary details not exist":
                time.sleep(120)
            else:
                break

        # Validation of api response data

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")
        # validate trip Id
        actual_tripId = response_body["responseData"]["data"][0]["trip"]["meta"]["tripId"]
        print(f"Trip Id stored in Cloud' {actual_tripId} ' ")

        if actual_tripId == tripId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is stored in cloud DB successfully")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is not stored in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate system id & trip Id mapping
        actual_systemId = response_body["responseData"]["data"][0]["trip"]["meta"]["systemId"]
        print(f"Trip Id mapped to System Id in Cloud ' {actual_systemId} ' ")
        if actual_systemId == systemId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is mapped to device systemId in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate trip start odo meter value
        actual_tripStart_odometer = response_body["responseData"]["data"][0]["trip"]["tripStart"]["odometer"]

        print(f"Trip Start - Odometer value configured in stub ' {trip_start_odometer_value} ' ")
        print(f"Trip Start - Odometer value stored in cloud ' {actual_tripStart_odometer} ' ")
        if float(actual_tripStart_odometer) == trip_start_odometer_value:
            testResult(self, "passed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripStart_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["fuelLevel"]

        print(f"Trip Start - Fuel level value configured in stub ' {trip_start_fuelLevel_value_ev} ' ")
        print(f"Trip Start - Fuel level value stored in cloud ' {actual_tripStart_fuelLevel} ' ")
        if float(actual_tripStart_fuelLevel) == trip_start_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripStart_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["batteryLevel"]

        print(f"Trip Start - Battery level value configured in stub ' {trip_start_batteryLevel_value_ev} ' ")
        print(f"Trip Start - Battery level value stored in cloud ' {actual_tripStart_batteryLevel} ' ")
        if float(actual_tripStart_batteryLevel) == trip_start_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip end odo meter value
        actual_tripEnd_odometer = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["odometer"]
        print(f"Trip End - Odometer level value configured in stub ' {trip_end_odometer_value} ' ")
        print(f"Trip End - Odometer level value stored in cloud ' {actual_tripEnd_odometer} ' ")

        if float(actual_tripEnd_odometer) == trip_end_odometer_value:
            testResult(self, "passed",
                       "Trip End - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripEnd_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["fuelLevel"]
        print(f"Trip End - Fuel level value configured in stub ' {trip_end_fuelLevel_value_ev} ' ")
        print(f"Trip End - Fuel level value stored in cloud ' {actual_tripEnd_fuelLevel} ' ")

        if float(actual_tripEnd_fuelLevel) == trip_end_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripEnd_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"][
            "batteryLevel"]
        print(f"Trip End - Battery level value configured in stub ' {trip_end_batteryLevel_value_ev} ' ")
        print(f"Trip End - Battery level value stored in cloud ' {actual_tripEnd_batteryLevel} ' ")

        if float(actual_tripEnd_batteryLevel) == trip_end_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_tripFuelEfficiency_value_ev
        actual_trip_summary_tripFuelEfficiency_value_ev = response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripFuelEfficiency"]

        print(f"Trip Summary - Trip Fuel Efficiency value stored in cloud ' {actual_trip_summary_tripFuelEfficiency_value_ev} ' ")
        if float(actual_trip_summary_tripFuelEfficiency_value_ev) == trip_summary_tripFuelEfficiency_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Fuel Efficiency value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Fuel Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_co2Emission_value_ev
        actual_trip_summary_co2Emission_value_ev = \
        response_body["responseData"]["data"][0]["trip"]["tripSummary"]["co2Emission"]
        print(
            f"Trip Summary - CO2 Emission value stored in cloud ' {actual_trip_summary_co2Emission_value_ev} ' ")

        if float(actual_trip_summary_co2Emission_value_ev) == trip_summary_co2Emission_value_ev:
            testResult(self, "passed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_tripDistance_value_ev
        actual_trip_summary_tripDistance_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripDistance"]
        print(
            f"Trip Summary - Trip Distance value stored in cloud ' {actual_trip_summary_tripDistance_value_ev} ' ")

        if float(actual_trip_summary_tripDistance_value_ev) == trip_summary_tripDistance_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_fuelConsumed_value_ev
        actual_trip_summary_fuelConsumed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["fuelConsumed"]
        print(
            f"Trip Summary - Fuel Consumed value stored in cloud ' {actual_trip_summary_fuelConsumed_value_ev} ' ")

        if float(actual_trip_summary_fuelConsumed_value_ev) == trip_summary_fuelConsumed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Fuel Consumed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Fuel Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_tripDuration_value_ev
        actual_trip_summary_tripDuration_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripDuration"]
        print(
            f"Trip Summary - Trip Duration value stored in cloud ' {actual_trip_summary_tripDuration_value_ev} ' ")

        if float(actual_trip_summary_tripDuration_value_ev) == trip_summary_tripDuration_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_avgSpeed_value_ev
        actual_trip_summary_avgSpeed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["avgSpeed"]
        print(
            f"Trip Summary - Average Speed value stored in cloud ' {actual_trip_summary_avgSpeed_value_ev} ' ")

        if float(actual_trip_summary_avgSpeed_value_ev) == trip_summary_avgSpeed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_batteryConsumed_value_ev
        actual_trip_summary_batteryConsumed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["batteryConsumed"]
        print(
            f"Trip Summary - Battery Consumed value stored in cloud ' {actual_trip_summary_batteryConsumed_value_ev} ' ")

        if float(actual_trip_summary_batteryConsumed_value_ev) == trip_summary_batteryConsumed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Battery Consumed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Battery Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_tripBatteryEfficiency_value_ev
        actual_trip_summary_tripBatteryEfficiency_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripBatteryEfficiency"]

        print(
            f"Trip Summary - Trip Battery Efficiency value stored in cloud ' {actual_trip_summary_tripBatteryEfficiency_value_ev} ' ")

        if float(actual_trip_summary_tripBatteryEfficiency_value_ev) == trip_summary_tripBatteryEfficiency_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Battery Efficiency value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Battery Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_maxSpeed_value_ev
        actual_trip_summary_maxSpeed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["maxSpeed"]

        print(
            f"Trip Summary - Max Speed configured in stub ' {trip_summary_maxSpeed_value_ev} ' ")
        print(
            f"Trip Summary - Max Speed value stored in cloud ' {actual_trip_summary_maxSpeed_value_ev} ' ")

        if float(actual_trip_summary_maxSpeed_value_ev) == trip_summary_maxSpeed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speedvalue is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

    def test5_trip_notification(self):
        # ===========================================================================================
        # Initiate notification
        # ===========================================================================================
        print("Initiate notification via post api : ")
        print("----------------------------------------------------------")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
        print("Initiated message Id : ", msg_id)

        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        print(vin)

        response_body = notification_message(self, vin, systemId, msg_id)

        print("Notification is initiated")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify notification messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        ls = verify_message_in_log(self, notification_msg_type_code, notification_msg_type_code)

        if notification_msg_type_code in str(ls[0]):
            print(f"Notification message should be arrived from cloud ' {notification_msg_type_code} ' ")
            testResult(self, "passed", "Notification message should be arrived from cloud ",
                       "Notification message is arrived from cloud  and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:
                msg_body_data = decode_msg_body(str(ls[0]))
                ls1 = str(ls[0]).split('{"body_encoding_type":1},"body":')
                data = str(ls1[1])
                print(data)
                lenmax = len(data) - len(data) % 4
                decodedBytes = base64.b64decode(data[0:lenmax]).decode()

                msg_body_data = str(decodedBytes)
                print("Decoded message body :", msg_body_data)

                if msg_id in msg_body_data:
                    testResult(self, "passed",
                               "Message id should be present in the notification message arrived from the cloud",
                               "Message id is present in the notification message arrived from the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if msg_id not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Message id should be present in the notification message arrived from the cloud",
                               "Message id is not present in the notification message arrived from the cloud or device logs are not updated accordingly or device logs haven been rotated, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print(
                "Notification message is not arrived from cloud  and device logs are not updated accordingly or device logs have been rotated, pls refer "
                "device logs for detailed info")
            testResult(self, "verificationFailed", "Notification message should be arrived from cloud ",
                       "Notification message is not arrived from cloud  and device logs are not updated accordingly or device logs have been rotated, pls refer "
                       "device logs for detailed info")
        print("----------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry functionality.
    def test6_latest_trip_meta(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, trip_summary_stub_option)
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
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
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
                    testResult(self, "verificationFailed",
                               "Trip start event type code should be present in the telemetry message published to the cloud",
                               "Trip start event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(30)

        vin = getVIN(self, OnboardingType, chipsetType)

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        tripId = get_tridId_from_log(self)

        print("----------------------------------------------------------")

        i = 0
        while i in range(10):
            response_body = assetManagement_latest_trip_meta(self, vin, systemId, "Completed")
            if response_body["responseData"]['message'] == "Trip summary details not exist":
                time.sleep(120)
            else:
                break

        # Validation of api response data

        assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")
        # validate trip Id
        actual_tripId = response_body["responseData"]["data"]["trip"]["meta"]["tripId"]
        print(f"Trip Id stored in Cloud' {actual_tripId} ' ")

        if actual_tripId == tripId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is stored in cloud DB successfully")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is not stored in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate system id & trip Id mapping
        actual_systemId = response_body["responseData"]["data"]["trip"]["meta"]["systemId"]
        print(f"Trip Id mapped to System Id in Cloud ' {actual_systemId} ' ")
        if actual_systemId == systemId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is mapped to device systemId in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")

        # validate vin & trip Id mapping
        actual_vin = response_body["responseData"]["data"]["trip"]["meta"]["vin"]
        print(f"Trip Id mapped to System Id in Cloud ' {actual_systemId} ' ")
        if actual_vin == vin.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device VIN in cloud DB",
                       "Newly generated trip id is mapped to device VIN in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be mapped to device VIN in cloud DB",
                       "Newly generated trip id is not mapped to device VIN in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")

        # validate trip status
        actual_status = response_body["responseData"]["data"]["trip"]["meta"]["status"]
        print(f"Newly generated trip status in Cloud ' {actual_systemId} ' ")
        if actual_status == "Completed":
            testResult(self, "passed", "Newly generated trip status should be 'Completed' ",
                       "Newly generated trip status is 'Completed' ")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip status should be 'Completed'",
                       "Newly generated trip status is not 'Completed'. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")

        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

        print("----------------------------------------------------------")

    def test_try(self):
        assetManagement_trip_info_by_tripId(self, " sysd39b6e7e170811ee8f08_1688374980272")

    def test4_latest_trip_details(self):

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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, trip_summary_stub_option)
        time.sleep(10)

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")
        # telemetry - trip stop "event_type": 4006
        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start & stop - telemetry receive topic
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_recv_topic)

        if telemetry_recv_topic in str(ls[0]):
            print(f"Telemetry message published on ' {telemetry_recv_topic} '  topic")
            testResult(self, "passed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is published on telemetry recevive topic and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is not published on telemetry receive topic or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # telemetry - trip start & stop - message-type
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code)

        if telemetry_msg_type_code in str(ls[0]):
            print(f"Telemetry message published to cloud via ' {telemetry_msg_type_code} ' topic")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:
                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_stop_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_stop_event_type_code not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(120)

        tripId = get_tridId_from_log(self)

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        time.sleep(120)

        i = 0
        while i in range(10):
            response_body = assetManagement_latest_trip_details(self, vin, systemId, "Completed")
            if response_body["responseData"]['message'] == "Trip summary details not exist":
                time.sleep(120)
            else:
                break

        # Validation of api response data

        assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")
        # validate trip Id
        actual_tripId = response_body["responseData"]["data"]["trip"]["meta"]["tripId"]
        print(f"Trip Id stored in Cloud' {actual_tripId} ' ")

        if actual_tripId == tripId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is stored in cloud DB successfully")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is not stored in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate system id & trip Id mapping
        actual_systemId = response_body["responseData"]["data"]["trip"]["meta"]["systemId"]
        print(f"Trip Id mapped to System Id in Cloud ' {actual_systemId} ' ")
        if actual_systemId == systemId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is mapped to device systemId in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate trip start odo meter value
        actual_tripStart_odometer = response_body["responseData"]["data"]["trip"]["tripStart"]["odometer"]

        print(f"Trip Start - Odometer value configured in stub ' {trip_start_odometer_value} ' ")
        print(f"Trip Start - Odometer value stored in cloud ' {actual_tripStart_odometer} ' ")
        if float(actual_tripStart_odometer) == trip_start_odometer_value:
            testResult(self, "passed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripStart_fuelLevel = response_body["responseData"]["data"]["trip"]["tripStart"]["fuelLevel"]

        print(f"Trip Start - Fuel level value configured in stub ' {trip_start_fuelLevel_value_ev} ' ")
        print(f"Trip Start - Fuel level value stored in cloud ' {actual_tripStart_fuelLevel} ' ")
        if float(actual_tripStart_fuelLevel) == trip_start_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripStart_batteryLevel = response_body["responseData"]["data"]["trip"]["tripStart"]["batteryLevel"]

        print(f"Trip Start - Battery level value configured in stub ' {trip_start_batteryLevel_value_ev} ' ")
        print(f"Trip Start - Battery level value stored in cloud ' {actual_tripStart_batteryLevel} ' ")
        if float(actual_tripStart_batteryLevel) == trip_start_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip end odo meter value
        actual_tripEnd_odometer = response_body["responseData"]["data"]["trip"]["tripEnd"]["odometer"]
        print(f"Trip End - Odometer level value configured in stub ' {trip_end_odometer_value} ' ")
        print(f"Trip End - Odometer level value stored in cloud ' {actual_tripEnd_odometer} ' ")

        if float(actual_tripEnd_odometer) == trip_end_odometer_value:
            testResult(self, "passed",
                       "Trip End - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripEnd_fuelLevel = response_body["responseData"]["data"]["trip"]["tripEnd"]["fuelLevel"]
        print(f"Trip End - Fuel level value configured in stub ' {trip_end_fuelLevel_value_ev} ' ")
        print(f"Trip End - Fuel level value stored in cloud ' {actual_tripEnd_fuelLevel} ' ")

        if float(actual_tripEnd_fuelLevel) == trip_end_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")

        # validate trip start battery level value
        actual_tripEnd_batteryLevel = response_body["responseData"]["data"]["trip"]["tripEnd"][
            "batteryLevel"]
        print(f"Trip End - Battery level value configured in stub ' {trip_end_batteryLevel_value_ev} ' ")
        print(f"Trip End - Battery level value stored in cloud ' {actual_tripEnd_batteryLevel} ' ")

        if float(actual_tripEnd_batteryLevel) == trip_end_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_fuelConsumed_value_ev

        trip_summary_fuelConsumed_value_ev = float(trip_end_fuelLevel_value_ev - trip_start_fuelLevel_value_ev)

        actual_trip_summary_fuelConsumed_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["fuelConsumed"]
        print(
            f"Trip Summary - Fuel Consumed - calculation :  '{trip_end_fuelLevel_value_ev} - {trip_start_fuelLevel_value_ev} = {trip_summary_fuelConsumed_value_ev} ' ")

        print(
            f"Trip Summary - Fuel Consumed value stored in cloud ' {actual_trip_summary_fuelConsumed_value_ev} ' ")


        if float(actual_trip_summary_fuelConsumed_value_ev) == trip_summary_fuelConsumed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Fuel Consumed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Fuel Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_co2Emission_value_ev


        trip_summary_co2Emission_value_ev = trip_summary_fuelConsumed_value_ev * trip_Fuel_Constant_ev  # Fuel Constant

        actual_trip_summary_co2Emission_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["co2Emission"]

        print(
            f"Trip Summary - CO2 Emission - calculation :  ' {trip_summary_fuelConsumed_value_ev} * {trip_Fuel_Constant_ev} = {trip_summary_co2Emission_value_ev} ' ")

        print(
            f"Trip Summary - CO2 Emission value stored in cloud ' {actual_trip_summary_co2Emission_value_ev} ' ")

        if float(actual_trip_summary_co2Emission_value_ev) == trip_summary_co2Emission_value_ev:
            testResult(self, "passed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_tripDistance_value_ev
        trip_summary_tripDistance_value_ev = float(trip_end_odometer_value - trip_start_odometer_value)

        actual_trip_summary_tripDistance_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["tripDistance"]

        print(
            f"Trip Summary - Trip Distance - calculation :  ' {trip_end_odometer_value} - {trip_start_odometer_value } = {trip_summary_tripDistance_value_ev} ' ")
        print(
            f"Trip Summary - Trip Distance value stored in cloud ' {actual_trip_summary_tripDistance_value_ev} ' ")

        if float(actual_trip_summary_tripDistance_value_ev) == trip_summary_tripDistance_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")


        # validate trip_summary_tripFuelEfficiency_value_ev

        #trip_summary_tripFuelEfficiency_value_ev = float(trip_summary_tripDistance_value_ev / trip_summary_fuelConsumed_value_ev)

        actual_trip_summary_tripFuelEfficiency_value_ev = response_body["responseData"]["data"]["trip"]["tripSummary"]["tripFuelEfficiency"]

        print(
            f"Trip Summary - Trip Fuel Efficiency - calculation : ' {trip_summary_tripDistance_value_ev} /  {trip_summary_fuelConsumed_value_ev} = {trip_summary_tripFuelEfficiency_value_ev} ' ")

        print(f"Trip Summary - Trip Fuel Efficiency value stored in cloud ' {actual_trip_summary_tripFuelEfficiency_value_ev} ' ")
        if float(actual_trip_summary_tripFuelEfficiency_value_ev) == trip_summary_tripFuelEfficiency_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Fuel Efficiency value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Fuel Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_tripDuration_value_ev
        actual_trip_startTime = \
            response_body["responseData"]["data"]["trip"]["tripStart"]["time"]
        actual_trip_endTime = \
            response_body["responseData"]["data"]["trip"]["tripEnd"]["time"]

        trip_summary_tripDuration_value_ev = float((actual_trip_endTime - actual_trip_startTime) / 3600000)

        actual_trip_summary_tripDuration_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["tripDuration"]

        print(
            f"Trip Summary - Trip Duration value - calculation : ' (( {actual_trip_endTime} - {actual_trip_startTime} ) / 3600000 ) =  {trip_summary_tripDuration_value_ev} ' ")
        print(
            f"Trip Summary - Trip Duration value stored in cloud ' {actual_trip_summary_tripDuration_value_ev} ' ")


        if float(actual_trip_summary_tripDuration_value_ev) == trip_summary_tripDuration_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_avgSpeed_value_ev

        trip_summary_avgSpeed_value_ev = float(trip_summary_tripDistance_value_ev/trip_summary_tripDuration_value_ev)
        actual_trip_summary_avgSpeed_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["avgSpeed"]
        print(
            f"Trip Summary - Average Speed - calculation :  ' {trip_summary_tripDistance_value_ev} / {trip_summary_tripDuration_value_ev} = {trip_summary_avgSpeed_value_ev} ' ")

        print(
            f"Trip Summary - Average Speed value stored in cloud ' {actual_trip_summary_avgSpeed_value_ev} ' ")

        if float(actual_trip_summary_avgSpeed_value_ev) == trip_summary_avgSpeed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_batteryConsumed_value_ev

        trip_summary_batteryConsumed_value_ev = float((trip_end_batteryLevel_value_ev - trip_end_batteryLevel_value_ev)/1000)
        actual_trip_summary_batteryConsumed_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["batteryConsumed"]
        print(
            f"Trip Summary - Battery Consumed - calculation : '(( {trip_end_batteryLevel_value_ev} - {trip_end_batteryLevel_value_ev} ) / 1000) =  {trip_summary_batteryConsumed_value_ev} ' ")

        print(
            f"Trip Summary - Battery Consumed value stored in cloud ' {actual_trip_summary_batteryConsumed_value_ev} ' ")

        if float(actual_trip_summary_batteryConsumed_value_ev) == trip_summary_batteryConsumed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Battery Consumed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                       "Trip Summary - Battery Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        # validate trip_summary_tripBatteryEfficiency_value_ev
        try:
            trip_summary_tripBatteryEfficiency_value_ev1 = float(trip_summary_tripDistance_value_ev)/float(trip_summary_batteryConsumed_value_ev)

        except:
            trip_summary_tripBatteryEfficiency_value_ev1 = trip_summary_tripBatteryEfficiency_value_ev

        actual_trip_summary_tripBatteryEfficiency_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["tripBatteryEfficiency"]

        print(
            f"Trip Summary - Trip Battery Efficiency - calculation '  {trip_summary_tripDistance_value_ev} - {trip_summary_batteryConsumed_value_ev} = {trip_summary_tripBatteryEfficiency_value_ev1} ' ")

        print(
            f"Trip Summary - Trip Battery Efficiency value stored in cloud ' {actual_trip_summary_tripBatteryEfficiency_value_ev} ' ")

        if float(actual_trip_summary_tripBatteryEfficiency_value_ev) == trip_summary_tripBatteryEfficiency_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Battery Efficiency value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Battery Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_maxSpeed_value_ev
        actual_trip_summary_maxSpeed_value_ev = \
            response_body["responseData"]["data"]["trip"]["tripSummary"]["maxSpeed"]

        print(
            f"Trip Summary - Max Speed configured in stub ' {trip_summary_maxSpeed_value_ev} ' ")
        print(
            f"Trip Summary - Max Speed value stored in cloud ' {actual_trip_summary_maxSpeed_value_ev} ' ")

        if float(actual_trip_summary_maxSpeed_value_ev) == trip_summary_maxSpeed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

    def test_try(self):
        calculate_trip_duration(self)

    def test4_trip_summary(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Update vehicle meta
        # ===========================================================================================

        vin = getVIN(self, OnboardingType, chipsetType)
        model = getModel(self, OnboardingType, chipsetType)
        engineType = get_engineType(self, OnboardingType, chipsetType)
        print("VIN : ", vin)
        print("Model : ", model)
        print("Engine Type : ", engineType)

        vehicle_update_vehicle_meta_data(self, vin, model, engineType)

        # ===========================================================================================
        # Run telemetry stub on device for trip waypoint
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, trip_summary_stub_option)
        time.sleep(10)

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
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")
        # telemetry - trip stop "event_type": 4006
        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start & stop - telemetry receive topic
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_recv_topic)

        if telemetry_recv_topic in str(ls[0]):
            print(f"Telemetry message published on ' {telemetry_recv_topic} '  topic")
            testResult(self, "passed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is published on telemetry recevive topic and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published- on telemetry receive topic ",
                       "Telemetry message is not published on telemetry receive topic or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # telemetry - trip start & stop - message-type
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code)

        if telemetry_msg_type_code in str(ls[0]):
            print(f"Telemetry message published to cloud via ' {telemetry_msg_type_code} ' topic")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            print("c2c logs line data : => ", ls[0])

            try:
                msg_body_data = decode_msg_body(str(ls[0]))

                if trip_stop_event_type_code in msg_body_data:
                    testResult(self, "passed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                               "device logs for detailed info")
                if trip_stop_event_type_code not in msg_body_data:
                    testResult(self, "verificationFailed",
                               "Trip stop event type code should be present in the telemetry message published to the cloud",
                               "Trip stop event type code is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                               "device logs for detailed info")
            except:
                print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print("Either trip is not started or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(120)
        value = value1 = ""

        tripId = get_tridId_from_log(self)

        print("----------------------------------------------------------")
        time.sleep(120)

        i = 0
        while i in range(10):
            response_body = assetManagement_trip_info_by_tripId(self, tripId)
            if response_body["responseData"]['message'] == "Trip summary details not exist":
                time.sleep(120)
            else:
                break

        # Validation of api response data

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")
        # validate trip Id
        actual_tripId = response_body["responseData"]["data"][0]["trip"]["meta"]["tripId"]
        print(f"Trip Id stored in Cloud : ->' {actual_tripId} ' ")

        if actual_tripId == tripId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is stored in cloud DB successfully")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be stored in cloud DB",
                       "Newly generated trip id is not stored in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate system id & trip Id mapping
        actual_systemId = response_body["responseData"]["data"][0]["trip"]["meta"]["systemId"]
        print(f"Trip Id mapped to System Id in Cloud : -> ' {actual_systemId} ' ")
        if actual_systemId == systemId.replace('\n', ''):
            testResult(self, "passed", "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is mapped to device systemId in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip id should be mapped to device systemId in cloud DB",
                       "Newly generated trip id is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        print("----------------------------------------------------------")
        # validate trip start odo meter value
        actual_tripStart_odometer = response_body["responseData"]["data"][0]["trip"]["tripStart"]["odometer"]

        print(f"Trip Start - Odometer value configured in stub : -> ' {trip_start_odometer_value} ' ")
        print(f"Trip Start - Odometer value stored in cloud : -> ' {actual_tripStart_odometer} ' ")
        if float(actual_tripStart_odometer) == trip_start_odometer_value:
            testResult(self, "passed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripStart_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["fuelLevel"]

        print(f"Trip Start - Fuel level value configured in stub : -> ' {trip_start_fuelLevel_value_ev} ' ")
        print(f"Trip Start - Fuel level value stored in cloud : -> ' {actual_tripStart_fuelLevel} ' ")
        if float(actual_tripStart_fuelLevel) == trip_start_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripStart_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["batterySocLevel"]

        print(
            f"Trip Start - Battery SOC level value configured in stub : -> ' {trip_start_batterySOCLevel_value_ev} ' ")
        print(f"Trip Start - Battery SOC level value stored in cloud : -> ' {actual_tripStart_batteryLevel} ' ")
        if float(actual_tripStart_batteryLevel) == trip_start_batterySOCLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Battery SOC level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery SOC level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Battery SOC level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery SOC level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
            value = "FAIL"

        print("----------------------------------------------------------")
        # validate trip end odo meter value
        actual_tripEnd_odometer = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["odometer"]
        print(f"Trip End - Odometer level value configured in stub : -> ' {trip_end_odometer_value} ' ")
        print(f"Trip End - Odometer level value stored in cloud : -> ' {actual_tripEnd_odometer} ' ")

        if float(actual_tripEnd_odometer) == trip_end_odometer_value:
            testResult(self, "passed",
                       "Trip End - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripEnd_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["fuelLevel"]
        print(f"Trip End - Fuel level value configured in stub : -> ' {trip_end_fuelLevel_value_ev} ' ")
        print(f"Trip End - Fuel level value stored in cloud : -> ' {actual_tripEnd_fuelLevel} ' ")

        if float(actual_tripEnd_fuelLevel) == trip_end_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripEnd_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"][
            "batterySocLevel"]
        print(f"Trip End - Battery SOC level value configured in stub : -> ' {trip_end_batterySOCLevel_value_ev} ' ")
        print(f"Trip End - Battery SOC level value stored in cloud : -> ' {actual_tripEnd_batteryLevel} ' ")

        if float(actual_tripEnd_batteryLevel) == trip_end_batterySOCLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Battery SOC level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery SOC level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Battery SOC level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery SOC level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

        print("----------------------------------------------------------")

        # Calculations :

        # read trip start & end time
        actual_trip_startTime = \
            response_body["responseData"]["data"][0]["trip"]["tripStart"]["time"]
        actual_trip_endTime = \
            response_body["responseData"]["data"][0]["trip"]["tripEnd"]["time"]

        # Calculate trip distance for validation :
        trip_distance = calculate_trip_distance(self, trip_start_odometer_value, trip_end_odometer_value)

        # Calculate trip fuel usage for validation :
        trip_fuel_usage = calculate_fuel_consumed(self, trip_start_fuelLevel_value_ev, trip_end_fuelLevel_value_ev)

        # Calculate trip C02 emission for validation :
        trip_co2_emission = calculate_CO2_emission(self, trip_fuel_usage, trip_Fuel_Constant_ev)

        # Calculate trip fuel efficiency for validation :
        trip_fuel_efficiency = calculate_trip_fuel_efficiency(self, trip_distance, trip_fuel_usage)

        # Calculate trip duration for validation :
        trip_duration = calculate_trip_duration(self, actual_trip_startTime, actual_trip_endTime)

        # Calculate trip average speed for validation :
        trip_average_speed = calculate_average_speed(self, trip_distance, trip_duration)

        # Calculate trip battery consumed for validation :
        trip_battery_consumed = calculate_batterySOClevel_consumed(self, trip_start_batterySOCLevel_value_ev,
                                                                   trip_end_batterySOCLevel_value_ev)

        # Calculate trip battery efficiency for validation :
        trip_battery_efficiency = calculate_trip_batterySOClevel_efficiency(self, trip_distance, trip_battery_consumed)

        # Validations:

        if engineType == '0':
            # validate trip_summary_tripFuelEfficiency_value_ev
            actual_trip_summary_tripFuelEfficiency_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripFuelEfficiency"]

            print(
                f"Trip Summary - Trip Fuel Efficiency calculated based on stub values : -> ' {trip_fuel_efficiency} ' ")
            print(
                f"Trip Summary - Trip Fuel Efficiency value stored in cloud : -> ' {actual_trip_summary_tripFuelEfficiency_value_ev} ' ")

            if float(actual_trip_summary_tripFuelEfficiency_value_ev) == trip_fuel_efficiency:
                testResult(self, "passed",
                           "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Fuel Efficiency value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Fuel Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")

            print("----------------------------------------------------------")
        # validate trip_summary_co2Emission_value_ev
        actual_trip_summary_co2Emission_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["co2Emission"]

        print(
            f"Trip Summary - CO2 Emission calculated based on stub values : -> ' {trip_co2_emission} ' ")
        print(
            f"Trip Summary - CO2 Emission value stored in cloud : -> ' {actual_trip_summary_co2Emission_value_ev} ' ")

        if float(actual_trip_summary_co2Emission_value_ev) == trip_co2_emission:
            testResult(self, "passed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - CO2 Emission should be calculated based on trip start & trip end",
                       "Trip Summary - CO2 Emission value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")
        # validate trip_summary_tripDistance_value_ev
        actual_trip_summary_tripDistance_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripDistance"]

        print(
            f"Trip Summary - Trip Distance calculated based on stub values : -> ' {trip_distance} ' ")
        print(
            f"Trip Summary - Trip Distance value stored in cloud : -> ' {actual_trip_summary_tripDistance_value_ev} ' ")

        if float(actual_trip_summary_tripDistance_value_ev) == trip_distance:
            testResult(self, "passed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Distance value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

            value == "FAIL"
        print("----------------------------------------------------------")

        if engineType == '0':
            # validate trip_summary_fuelConsumed_value_ev
            actual_trip_summary_fuelConsumed_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["fuelConsumed"]
            print(
                f"Trip Summary - Fuel Consumed calculated based on stub values : -> ' {trip_fuel_usage} ' ")
            print(
                f"Trip Summary - Fuel Consumed value stored in cloud : -> ' {actual_trip_summary_fuelConsumed_value_ev} ' ")

            if float(actual_trip_summary_fuelConsumed_value_ev) == trip_fuel_usage:
                testResult(self, "passed",
                           "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Fuel Consumed value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Fuel Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")

            print("----------------------------------------------------------")
        # validate trip_summary_tripDuration_value_ev
        actual_trip_summary_tripDuration_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripDuration"]
        print(
            f"Trip Summary - Trip Duration calculated based on stub values : -> ' {trip_duration} ' ")
        print(
            f"Trip Summary - Trip Duration value stored in cloud : -> ' {actual_trip_summary_tripDuration_value_ev} ' ")

        if float(actual_trip_summary_tripDuration_value_ev) == trip_duration:
            testResult(self, "passed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationPassed",
                       "Trip Summary - Trip Duration should be calculated based on trip start & trip end",
                       "Trip Summary - Trip Duration value is correct and stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

            value == "FAIL"
        print("----------------------------------------------------------")
        # validate trip_summary_avgSpeed_value_ev
        actual_trip_summary_avgSpeed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["avgSpeed"]
        print(
            f"Trip Summary - Average Speed calculated based on stub values : -> ' {trip_average_speed} ' ")
        print(
            f"Trip Summary - Average Speed value stored in cloud : -> ' {actual_trip_summary_avgSpeed_value_ev} ' ")

        if float(actual_trip_summary_avgSpeed_value_ev) == trip_average_speed:
            testResult(self, "passed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Average Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Average Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

            value == "FAIL"
        print("----------------------------------------------------------")
        if engineType == 2 or engineType == "2":
            # validate trip_summary_batteryConsumed_value_ev
            actual_trip_summary_batteryConsumed_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["batteryConsumed"]
            print(
                f"Trip Summary - Battery Consumed calculated based on stub values : -> ' {trip_battery_consumed} ' ")
            print(
                f"Trip Summary - Battery Consumed value stored in cloud : -> ' {actual_trip_summary_batteryConsumed_value_ev} ' ")

            if float(actual_trip_summary_batteryConsumed_value_ev) == trip_battery_consumed:
                testResult(self, "passed",
                           "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Battery Consumed value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Battery Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Battery Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
                value1 = "FAIL"

            print("----------------------------------------------------------")
            # validate trip_summary_tripBatteryEfficiency_value_ev
            actual_trip_summary_tripBatteryEfficiency_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripBatteryEfficiency"]

            print(
                f"Trip Summary - Trip Battery Efficiency calculated based on stub values : -> ' {trip_battery_efficiency} ' ")
            print(
                f"Trip Summary - Trip Battery Efficiency value stored in cloud : -> ' {actual_trip_summary_tripBatteryEfficiency_value_ev} ' ")

            if float(actual_trip_summary_tripBatteryEfficiency_value_ev) == trip_battery_efficiency:
                testResult(self, "passed",
                           "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Battery Efficiency value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Trip Battery Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Battery Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")

                value == "FAIL"
            print("----------------------------------------------------------")

        if engineType == 0 or engineType == "0":
            # validate trip_summary_fuelConsumed_value_ev
            actual_trip_summary_fuelConsumed_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["fuelConsumed"]
            print(
                f"Trip Summary - Fuel Consumed value stored in cloud ' {actual_trip_summary_fuelConsumed_value_ev} ' ")

            if float(actual_trip_summary_fuelConsumed_value_ev) == trip_summary_fuelConsumed_value_ev:
                testResult(self, "passed",
                           "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Fuel Consumed value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Fuel Consumed should be calculated based on trip start & trip end",
                           "Trip Summary - Fuel Consumed value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
                value == "FAIL"

            print("----------------------------------------------------------")

            # validate trip_summary_tripfuelEfficiency_value_ev
            actual_trip_summary_tripFuelEfficiency_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripFuelEfficiency"]

            print(
                f"Trip Summary - Trip Battery Efficiency calculated based on stub values : -> ' {trip_fuel_efficiency} ' ")
            print(
                f"Trip Summary - Trip Battery Efficiency value stored in cloud : -> ' {actual_trip_summary_tripFuelEfficiency_value_ev} ' ")

            if float(actual_trip_summary_tripFuelEfficiency_value_ev) == trip_fuel_efficiency:
                testResult(self, "passed",
                           "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Fuel Efficiency value is correct & stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Summary - Trip Fuel Efficiency should be calculated based on trip start & trip end",
                           "Trip Summary - Trip Fuel Efficiency value is incorrect or not stored in the Cloud DB. pls refer "
                           "stub & device/cloud for detailed info")

                value == "FAIL"
            print("----------------------------------------------------------")

        # validate trip_summary_maxSpeed_value_ev
        actual_trip_summary_maxSpeed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["maxSpeed"]

        print(
            f"Trip Summary - Max Speed configured in stub : -> ' {trip_summary_maxSpeed_value_ev} ' ")
        print(
            f"Trip Summary - Max Speed value stored in cloud : -> ' {actual_trip_summary_maxSpeed_value_ev} ' ")

        if float(actual_trip_summary_maxSpeed_value_ev) == trip_summary_maxSpeed_value_ev:
            testResult(self, "passed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speedvalue is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")

        print("----------------------------------------------------------")

        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

        time.sleep(10)

        print("----------------------------------------------------------")
        if value == "FAIL" and value1 == "FAIL":
            testResult(self, "failed",
                       "Trip Summary - should be calculated based on trip start & trip end data",
                       "Trip Summary - details are not correct. pls refer "
                       "stub & device/cloud for detailed info")
            #self.result.set_result(TestResults.failed)