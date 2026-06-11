import os, sys, datetime, time, subprocess, inspect, logging

from C2CModules.e2e_testData import *
from C2CModules.vehicleGrouping import *
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import *
from C2CModules.notifications import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_Alerts_Via_API:


    def test1_notifications_trigger_crash_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - crash via API functionality. (positive scenario)
        :return: return test status
        Validate crash Alert via POST API
        """
        print("\n------------------NOTIFICATION - CRASH ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")


        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", crash_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", crash_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", crash_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, crash_categoryId, messageId, modeId, priority,
                                             crash_propertyId,
                                             msgInfo_area, msgInfo_value_1, crash_notification_name, "valid")
        time.sleep(10)
        verify_notification_details_v3(self, systemId, crash_categoryName_v2, crash_notification_name_v2, notification_type, dt,
                                    dt1)

        print("\n------------------------------END------------------------------\n")

    def test2_notifications_trigger_tamper_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - tamper via API functionality. (positive scenario)
        :return: return test status
        Validate tamper Alert via POST API
        """
        print("\n------------------NOTIFICATION - TAMPER ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", tamper_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", tamper_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", tamper_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, tamper_categoryId, messageId, modeId, priority,
                                             tamper_propertyId,
                                             msgInfo_area, msgInfo_value_1, tamper_notification_name)
        time.sleep(60)
        verify_notification_details(self, systemId, tamper_categoryName_v2, tamper_notification_name_v2, notification_type, dt,
                                    dt1)

        print("\n------------------------------END------------------------------\n")

    def test3_notifications_trigger_sos_on_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - SOS ON alert via API functionality. (positive scenario)
        :return: return test status
        Validate SOS ON Alert via POST API
        """
        print("\n------------------NOTIFICATION - SOS ALERT ON VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", sos_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", sos_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", sos_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, sos_categoryId, messageId, modeId, priority, sos_propertyId,
                                             msgInfo_area, msgInfo_value_1, sos_notification_name)
        time.sleep(60)
        verify_notification_details(self, systemId, sos_categoryName, sos_notification_name, notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test4_notifications_trigger_sos_off_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - SOS OFF alert via API functionality. (positive scenario)
        :return: return test status
        Validate SOS OFF Alert via POST API
        """
        print("\n------------------NOTIFICATION - SOS OFF ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id
        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", sos_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", sos_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", sos_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_0)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, sos_categoryId, messageId, modeId, priority, sos_propertyId,
                                             msgInfo_area, msgInfo_value_0, sos_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, sos_categoryName, sos_notification_name, notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test5_notifications_trigger_vehicleState_on_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - vehicle state - ON via API functionality. (positive scenario)
        :return: return test status
        Validate vehicle state - ON Alert via POST API
        """
        print("\n------------------NOTIFICATION - VEHICLE STATE ON ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", vehicleState_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", vehicleState_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", vehicleState_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, vehicleState_categoryId, messageId, modeId, priority,
                                             vehicleState_propertyId,
                                             msgInfo_area, msgInfo_value_1, vehicleState_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, vehicleState_categoryName, vehicleState_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test6_notifications_trigger_vehicleState_off_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - vehicle state - OFF via API functionality. (positive scenario)
        :return: return test status
        Validate vehicle state - OFF Alert via POST API
        """
        print("\n------------------NOTIFICATION - VEHICLE STATE OFF ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", vehicleState_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", vehicleState_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", vehicleState_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_0)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, vehicleState_categoryId, messageId, modeId, priority,
                                             vehicleState_propertyId,
                                             msgInfo_area, msgInfo_value_0, vehicleState_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, vehicleState_categoryName, vehicleState_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test7_notifications_trigger_heat_and_cold_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Heat & Cold via API functionality. (positive scenario)
        :return: return test status
        Validate Heat & Cold Alert via POST API
        """
        print("\n------------------NOTIFICATION - HEAT & COLD ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", battery_heatCold_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", battery_heatCold_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", batteryHeatCold_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_0)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, battery_heatCold_categoryId, messageId, modeId, priority,
                                             batteryHeatCold_propertyId,
                                             msgInfo_area, msgInfo_value_0, battery_heatCold_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, battery_heatCold_categoryName, battery_heatCold_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test8_notifications_trigger_service_reminder_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Service Reminder via API functionality. (positive scenario)
        :return: return test status
        Validate Service Reminder Alert via POST API
        """
        print("\n------------------NOTIFICATION - SERVICE REMINDER ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", service_remainder_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", service_remainder_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", service_reminder_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", service_reminder_msgInfo_value)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, service_remainder_categoryId, messageId, modeId, priority,
                                             service_reminder_propertyId,
                                             msgInfo_area, service_reminder_msgInfo_value,
                                             service_remainder_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, service_remainder_categoryName, service_remainder_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test9_notifications_trigger_mode_change_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Mode Change via API functionality. (positive scenario)
        :return: return test status
        Validate  Mode Change Alert via POST API
        """
        print("\n------------------NOTIFICATION - MODE CHANGE ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", modeChange_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", modeChange_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", modeChange_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, modeChange_categoryId, messageId, modeId, priority,
                                             modeChange_propertyId,
                                             msgInfo_area, msgInfo_value_1, modeChange_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, modeChange_categoryName, modeChange_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test10_notifications_trigger_plugIn_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Plug In via API functionality. (positive scenario)
        :return: return test status
        Validate  Plug In Alert via POST API
        """
        print("\n------------------NOTIFICATION - PLUG IN ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")


        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", plugInOut_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", plugInOut_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", plugInOut_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, plugInOut_categoryId, messageId, modeId, priority,
                                             plugInOut_propertyId,
                                             msgInfo_area, msgInfo_value_1, plugInOut_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, plugInOut_categoryName, plugInOut_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test11_notifications_trigger_trip_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Trip via API functionality. (positive scenario)
        :return: return test status
        Validate  Trip Alert via POST API
        """
        print("\n------------------NOTIFICATION - TRIP ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", trip_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", trip_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, trip_categoryId, messageId, modeId, priority,
                                             trip_propertyId,
                                             msgInfo_area, msgInfo_value_1, trip_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, trip_categoryName, trip_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test12_notifications_trigger_towAway_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Tow Away via API functionality. (positive scenario)
        :return: return test status
        Validate  Tow Away Alert via POST API
        """
        print("\n------------------NOTIFICATION - TOW AWAY ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", towAway_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", towAway_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)
        print("Message Info Id : ", towAway_propertyId)
        print("Message Info Area: ", msgInfo_area)
        print("Message Info Value : ", msgInfo_value_1)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, towAway_categoryId, messageId, modeId, priority,
                                             towAway_propertyId,
                                             msgInfo_area, msgInfo_value_1, towAway_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, towAway_categoryName, towAway_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test13_notifications_trigger_dtc_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - DTC via API functionality. (positive scenario)
        :return: return test status
        Validate  DTC Alert via POST API
        """
        print("\n------------------NOTIFICATION - DTC ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", dtc_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", dtc_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, dtc_categoryId, messageId, modeId, priority,
                                             dtc_propertyId,
                                             msgInfo_area, msgInfo_value_1, dtc_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, dtc_categoryName, dtc_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test14_notifications_trigger_pinExpiry_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - PIN EXPIRY via API functionality. (positive scenario)
        :return: return test status
        Validate  PIn EXPIRY Alert via POST API
        """
        print("\n------------------NOTIFICATION - PIN EXPIRY ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", pinExpiry_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", pinExpiry_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, pinExpiry_categoryId, messageId, modeId, priority,
                                             dtc_propertyId,
                                             msgInfo_area, msgInfo_value_1, pinExpiry_notification_name)
        time.sleep(60)
        verify_notification_details(self, systemId, pinExpiry_categoryName, pinExpiry_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")

    def test15_notifications_trigger_geofence_alert_through_api(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Notification - Geofence via API functionality. (positive scenario)
        :return: return test status
        Validate  Geofence Alert via POST API
        """
        print("\n------------------NOTIFICATION - DEVICE GEOFENCE ALERT VIA API------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # read VIN & SystemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
        messageId = "38" + msg_id

        #systemId = "CROfKyxh_P9wM-qMpBYAc"

        print("System Id : ", systemId)
        print("Notification Name : ", geofence_notification_name)
        print("Notification Name : ", notification_type)
        print("Category Id : ", geofence_categoryId)
        print("Message Id : ", messageId)
        print("Mode Id : ", modeId)
        print("Priority : ", priority)

        # Call notification module
        trigger_alert_through_api_and_verify(self, systemId, geofence_categoryId, messageId, modeId, priority,
                                             towAway_propertyId,
                                             msgInfo_area, msgInfo_value_1, geofence_notification_name)
        time.sleep(10)
        verify_notification_details(self, systemId, geofence_categoryName, geofence_notification_name,
                                    notification_type, dt, dt1)

        print("\n------------------------------END------------------------------\n")