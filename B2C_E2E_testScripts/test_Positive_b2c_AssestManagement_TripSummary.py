import os,sys,datetime,time,subprocess,inspect,logging
import shutil

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from C2CModules.e2e_testData import *
from C2CModules.fms_modules import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.vehicle_metadata import vehicle_update_vehicle_meta_data
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
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
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "DeviceOnboarding")
        try:
            shutil.rmtree('C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\Trip_waypoints')
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
        pass

    def execute(self):

        # ===========================================================================================
        # Update vehicle meta
        # ===========================================================================================

        vin = getVIN(self, OnboardingType, chipsetType)
        model = getModel(self, deviceType, OnboardingType)
        engineType = 2
        print("VIN :", vin)
        # print("Device Model :", model)
        print("Engine Type :", engineType)
        vehicle_update_vehicle_meta_data(self, vin, model, engineType)

        # ===========================================================================================
        # Run telemetry stub on device for trip waypoint
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run trip start stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_start')

        print("Trip start/run process is completed, verify logs for telemetry details : ")
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
        
        i=0
        while i<=2:        
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
            i=i+1
        
        
        if tripId == "":
            testResult(self, "failed", "Trip should start on device ", "Either trip is not started or device logs are not updated. pls refer device logs in detail ")
            

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
            print("Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
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
            print("Either trip is not started or device logs are not updated or logs have been rotated. pls refer device logs in detail")
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
                print("Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
                testResult(self, "verificationFailed", "Trip should stop on device ",
                           "Either trip is not stopped or device logs are not updated or have been rotated. pls refer device logs in detail ")

        time.sleep(60)
        print("----------------------------------------------------------")

        
        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        # tripId = get_tridId_from_log(self)

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")
        time.sleep(120)
        value = value1 = ""

        print("----------------------------------------------------------")
        time.sleep(120)

        i = 0
        print('===', tripId)
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

            value = "FAIL"
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

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip start odo meter value
        actual_tripStart_odometer = response_body["responseData"]["data"][0]["trip"]["tripStart"]["odometer"]

        print(f"Trip Start - Odometer value configured in stub : -> ' {b2c_trip_start_odometer_value} ' ")
        print(f"Trip Start - Odometer value stored in cloud : -> ' {actual_tripStart_odometer} ' ")
        if float(actual_tripStart_odometer) == b2c_trip_start_odometer_value:
            testResult(self, "passed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripStart_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["fuelLevel"]

        print(f"Trip Start - Fuel level value configured in stub : -> ' {b2c_trip_start_fuelLevel_value_ev} ' ")
        print(f"Trip Start - Fuel level value stored in cloud : -> ' {actual_tripStart_fuelLevel} ' ")
        if float(actual_tripStart_fuelLevel) == b2c_trip_start_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripStart_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripStart"]["batteryLevel"]

        print(f"Trip Start - Battery level value configured in stub : -> ' {b2c_trip_start_batteryLevel_value_ev} ' ")
        print(f"Trip Start - Battery level value stored in cloud : -> ' {actual_tripStart_batteryLevel} ' ")
        if float(actual_tripStart_batteryLevel) == b2c_trip_start_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
            value = "FAIL"

        print("----------------------------------------------------------")
        # validate trip end odo meter value
        actual_tripEnd_odometer = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["odometer"]
        print(f"Trip End - Odometer level value configured in stub : -> ' {b2c_trip_end_odometer_value} ' ")
        print(f"Trip End - Odometer level value stored in cloud : -> ' {actual_tripEnd_odometer} ' ")

        if float(actual_tripEnd_odometer) == b2c_trip_end_odometer_value:
            testResult(self, "passed",
                       "Trip End - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Odometer value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Start - Odometer value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip Start - Odometer value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip start fuel level value
        actual_tripEnd_fuelLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"]["fuelLevel"]
        print(f"Trip End - Fuel level value configured in stub : -> ' {b2c_trip_end_fuelLevel_value_ev} ' ")
        print(f"Trip End - Fuel level value stored in cloud : -> ' {actual_tripEnd_fuelLevel} ' ")

        if float(actual_tripEnd_fuelLevel) == b2c_trip_end_fuelLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Fuel level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip start battery level value
        actual_tripEnd_batteryLevel = response_body["responseData"]["data"][0]["trip"]["tripEnd"][
            "batteryLevel"]
        print(f"Trip End - Battery level value configured in stub : -> ' {b2c_trip_end_batteryLevel_value_ev} ' ")
        print(f"Trip End - Battery level value stored in cloud : -> ' {actual_tripEnd_batteryLevel} ' ")

        if float(actual_tripEnd_batteryLevel) == b2c_trip_end_batteryLevel_value_ev:
            testResult(self, "passed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip End - Battery level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Trip End - Battery level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "stub & device/cloud logs for detailed info")

            value = "FAIL"
        print("----------------------------------------------------------")

        # Calculations :

        # read trip start & end time
        actual_trip_startTime = \
            response_body["responseData"]["data"][0]["trip"]["tripStart"]["time"]
        actual_trip_endTime = \
            response_body["responseData"]["data"][0]["trip"]["tripEnd"]["time"]

        # Calculate trip distance for validation :
        trip_distance = calculate_trip_distance(self, b2c_trip_start_odometer_value, b2c_trip_end_odometer_value) * 1000
        
        # print(b2c_trip_start_odometer_value, b2c_trip_end_odometer_value, trip_distance)
        
        # Calculate trip fuel usage for validation :
        trip_fuel_usage = calculate_fuel_consumed(self, b2c_trip_start_fuelLevel_value_ev,
                                                  b2c_trip_end_fuelLevel_value_ev)
        

        if engineType ==2:
            trip_co2_emission = 0
        

        # Calculate trip duration for validation :
        trip_duration = calculate_trip_duration(self, actual_trip_startTime, actual_trip_endTime)

        # Calculate trip average speed for validation :
        trip_average_speed = calculate_average_speed(self, trip_distance, trip_duration)

        # Calculate trip battery consumed for validation :
        trip_battery_consumed = calculate_battery_consumed(self, b2c_trip_start_batteryLevel_value_ev,
                                                           b2c_trip_end_batteryLevel_value_ev)

        # Calculate trip battery efficiency for validation :
        trip_battery_efficiency = calculate_trip_battery_efficiency(self, trip_distance, trip_battery_consumed)

        # Validations:

        # validate trip_summary_tripFuelEfficiency_value_ev
        if engineType !=2:
            
            # Calculate trip fuel usage for validation :
            trip_fuel_usage = calculate_fuel_consumed(self, b2c_trip_start_fuelLevel_value_ev,
                                                  b2c_trip_end_fuelLevel_value_ev)
                                                  
            trip_co2_emission = calculate_CO2_emission(self, trip_fuel_usage, b2c_trip_Fuel_Constant_ev)
            
            # Calculate trip fuel efficiency for validation :
            trip_fuel_efficiency = calculate_trip_fuel_efficiency(self, trip_distance, trip_fuel_usage)
            
            actual_trip_summary_tripFuelEfficiency_value_ev = \
                response_body["responseData"]["data"][0]["trip"]["tripSummary"]["tripFuelEfficiency"]
    
            print(f"Trip Summary - Trip Fuel Efficiency calculated based on stub values : -> ' {trip_fuel_efficiency} ' ")
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
    
                value = "FAIL"
            print("----------------------------------------------------------")
            
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
    
                value = "FAIL"
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

            value = "FAIL"
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

            value = "FAIL"
        
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

            value = "FAIL"
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

            value = "FAIL"
        print("----------------------------------------------------------")
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
            value = "FAIL"

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

            value = "FAIL"
        print("----------------------------------------------------------")
        # validate trip_summary_maxSpeed_value_ev
        actual_trip_summary_maxSpeed_value_ev = \
            response_body["responseData"]["data"][0]["trip"]["tripSummary"]["maxSpeed"]

        print(
            f"Trip Summary - Max Speed configured in stub : -> ' {b2c_trip_summary_maxSpeed_value_ev} ' ")
        print(
            f"Trip Summary - Max Speed value stored in cloud : -> ' {actual_trip_summary_maxSpeed_value_ev} ' ")

        if float(actual_trip_summary_maxSpeed_value_ev) == float(b2c_trip_summary_maxSpeed_value_ev):
            testResult(self, "passed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is correct & stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Summary - Max Speed should be calculated based on trip start & trip end",
                       "Trip Summary - Max Speed value is incorrect or not stored in the Cloud DB. pls refer "
                       "stub & device/cloud for detailed info")
        
            value = "FAIL"
        print("----------------------------------------------------------")
        
        if value == "FAIL":
            self.result.set_result(TestResults.failed)
            assert False

        elif value != "FAIL":
            assert True
            self.result.set_result(TestResults.passed)
        time.sleep(10)

    def cleanup(self):
        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")
        pass       
        


if __name__ == '__main__':
    test = Test()
    test.run()

