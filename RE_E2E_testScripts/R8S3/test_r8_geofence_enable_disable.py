import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.e2e_testData import *
from C2CModules.vehicle_state import *
from C2CModules.geofence import *
from C2CModules.notifications import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_geofence_precondition1:

    def test_pos_save_geofence_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        cloudEnv = read_cloud_env(self)
        action = "geofence_config_update"

        # Define state preconditions in one line
        statePreconditions1 = {"attribute": "ignition", "operator": "eq", "value": ["ON"]}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                               "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
        statePreconditions3 = {"attribute": "parkMode", "operator": "eq", "value": ["OFF"]} if cloudEnv not in [
            "GCP-QA3", "DM1"] else None

        print("----------------------------------------------------------")
        print(f"Model: {model}")
        print(f"Action: {action}")
        print(f"statePreconditions-1: {statePreconditions1}")
        print(f"statePreconditions-2: {statePreconditions2}")
        print(f"statePreconditions-3: {statePreconditions3}")
        print("----------------------------------------------------------")

        geofence_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, "save_precondition")

    def test_pos_update_geofence_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        cloudEnv = read_cloud_env(self)
        action = "geofence_config_update"

        # Define state preconditions in one line
        statePreconditions1 = {"attribute": "ignition", "operator": "eq", "value": ["ON"]}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                               "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
        statePreconditions3 = {"attribute": "parkMode", "operator": "eq", "value": ["OFF"]} if cloudEnv not in [
            "GCP-QA3", "DM1"] else None

        print("----------------------------------------------------------")
        print(f"Model: {model}")
        print(f"Action: {action}")
        print(f"statePreconditions-1: {statePreconditions1}")
        print(f"statePreconditions-2: {statePreconditions2}")
        print(f"statePreconditions-3: {statePreconditions3}")
        print("----------------------------------------------------------")

        geofence_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2,
                              statePreconditions3, "update_precondition")

class Test_R8S3_Circle_Geofence_disable:

    def test_create_circle_geofence(self):

        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        geometryType = "circle"
        cloudEnv = read_cloud_env(self)
        if cloudEnv in r8_patch4_sp17_envs:
            radius = "500"
        else:
            radius = "150"
        lat = "28.61370736476138"
        long = "77.22751858264235"
        isActive = "true"
        tolerance = "0"
        type1 = "PERSONAL"
        poiFlag = "False"
        tag = "office"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"
        systemId = read_vehicleJsonFile(self, "system_id")

        create_circle_polygon_geofence(self, onboardingType, chipsetType, name, geometryType, radius, long, lat, isActive,
                               tolerance, type1, poiFlag, tag, notification, isEdgeEnabled, ruleId,
                               ruleExpression,"circle")

    def test_create_circle_geofence_disable(self):
        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        isActive = "true"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed&gt;50"
        systemId = read_vehicleJsonFile(self, "system_id")

        # Geofence enable/disable
        geofence_enable_disable(
            self,
            systemId,
            notification,
            isEdgeEnabled,
            ruleId,
            isActive,
            ruleExpression,
            name,
            "disable",
            "disable"
        )

        # Trigger Alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date &amp; time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_circle_alert_entry')

            print("Location stub start/run process is completed, verify logs for trip &amp; telemetry details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")
            pull_logs_from_IVI_device(self, onboardingType, chipsetType)
            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_in_alert_text, geo_in_alert_text)

            if geo_in_alert_text in str(ls[0]):
                print(f" =&gt; Aert is triggered/generated when a vehicle entered the circular geofence")
                print("c2c logs line data : =&gt; ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" =&gt; Aert is triggered/generated when a vehicle entered the circular geofence")
            testResult(
                self,
                "passed",
                "Validate if an alert is triggered/generated when a vehicle enters the circular geofence",
                "Aert is triggered/generated when a vehicle entered the circular geofence, pls refer device logs for "
                "detailed info"
            )
            print("c2c logs line data : =&gt; ", ls[0])

        if str(ls[0]) == "Error":
            print(
                " =&gt; Failed to trigger Alert when a vehicle entered the circular geofence. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Validate if an alert is generated when a vehicle enters the circular geofence",
                "Aert is not triggered/generated when a vehicle entered the circular geofence, pls refer device logs for "
                "detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status &amp; response for single systemId &amp; eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(
            self,
            systemId,
            geofence_entry_categoryName,
            geofence_entry_notification_name,
            notification_type,
            dt,
            dt1,
            "disable"
        )

        print("----------------------------------------------------------")

        # Trigger exit alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date &amp; time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_circle_alert_exit')

            print("Location stub start/run process is completed, verify logs for trip &amp; telemetry details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")
            pull_logs_from_IVI_device(self, onboardingType, chipsetType)
            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_in_alert_text, geo_in_alert_text)

            if geo_in_alert_text in str(ls[0]):
                print(f" =&gt; Aert is triggered/generated when a vehicle exit the circular geofence")
                print("c2c logs line data : =&gt; ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" =&gt; Aert is triggered/generated when a vehicle exited the circular geofence")
            testResult(
                self,
                "passed",
                "Validate if an alert is triggered/generated when a vehicle exits the circular geofence",
                "Aert is triggered/generated when a vehicle exited the circular geofence, pls refer device logs for "
                "detailed info"
            )
            print("c2c logs line data : =&gt; ", ls[0])

        if str(ls[0]) == "Error":
            print(
                " =&gt; Failed to trigger Alert when a vehicle exited the circular geofence. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Validate if an alert is generated when a vehicle exits the circular geofence",
                "Aert is not triggered/generated when a vehicle exited the circular geofence, pls refer device logs for "
                "detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status &amp; response for single systemId &amp; eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(
            self,
            systemId,
            geofence_exit_categoryName,
            geofence_exit_notification_name,
            notification_type,
            dt,
            dt1,
            "disable"
        )

        print("----------------------------------------------------------")

    def test_create_circle_geofence_enable(self):

        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        isActive = "true"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"
        systemId = read_vehicleJsonFile(self, "system_id")

        # Geofence enable/disable

        geofence_enable_disable(self, systemId, notification, isEdgeEnabled, ruleId, isActive,
                                ruleExpression, name, "enable", "enable")

        # Trigger Alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_circle_alert_entry')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_in_alert_text, geo_in_alert_text)

            if geo_in_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle entered the circular geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle entered the circular geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle enters the circular geofence",
                       "Aert is triggered/generated when a vehicle entered the circular geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle entered the circular geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle enters the circular geofence",
                       "Aert is not triggered/generated when a vehicle entered the circular geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(self, systemId, geofence_entry_categoryName, geofence_entry_notification_name,
                                       notification_type, dt, dt1, "alert_trigger_from_device")

        print("----------------------------------------------------------")

        # Trigger exit alert

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_circle_alert_exit')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_in_alert_text, geo_in_alert_text)

            if geo_in_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle exit the circular geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle exited the circular geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle exits the circular geofence",
                       "Aert is triggered/generated when a vehicle exited the circular geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle exited the circular geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle exits the circular geofence",
                       "Aert is not triggered/generated when a vehicle exited the circular geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(self, systemId, geofence_exit_categoryName, geofence_exit_notification_name,
                                       notification_type, dt, dt1, "alert_trigger_from_device")

        print("----------------------------------------------------------")

    def test_circle_geofence_delete(self):
        print("----------------------------------------------------------")
        print("Fetch newly created geofence details")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        offset = "1"
        limit = "10"
        isActive = "true"

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["geofences"])
            for i in range(data_len):
                isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                actual_Id = response_body["responseData"]["geofences"][i]["id"]
                actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                if isEdgeEnabled == 1 or isEdgeEnabled == "1":
                    actual_Id = response_body["responseData"]["geofences"][i]["id"]
                    actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                    break

            # Call api reusable module to delete geofence
            response = geofence_deleteGeofence_by_vehicleMappingId(self, actual_Id, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)
            if response.status_code != 200:
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Geofence deletion Initiated in the device":
                # vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
                message = response_body["message"]
                print("----------------------------------------------------------")
                # print('Vehicle Mapping Id : ', vehicleMappingId)
                print('Message : ', message)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully",
                           "Geofence deletion is initiated in the device and unmapped from Vehicle successfully ")
                #self.result.set_result(TestResults.passed)
            elif response_body["message"] != "Geofence deletion Initiated in the device":
                # print(response_body["responseData"]["message"])
                testResult(self, "failed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                           "Failed to initiate geofence deletion in the device or failed to delete geofence in the device or failed to unmap Geofence from Vehicle " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                #self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong")
                #self.result.set_result(TestResults.failed)

            print("----------------------------------------------------------")
            print("Validation of Geofence Deletion at Device:")
            print("----------------------------------------------------------")
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the geofence Deletion message is received from cloud
            conf_msg = 'configuration data ='
            msgType_16650 = '"message_type": 16650'
            msg_266 = 'Message type: 266 : Encoding type : 2'
            flush_msg = "Flush geofence table success"
            msg_268 = 'Message type: 268 : Encoding type : 2'
            msg_267 = 'Message type: 267 : Encoding type : 1'
            delete_action = '"action": "delete"'
            success_status = '"status": 0'

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, conf_msg,
                                       conf_msg)

            if conf_msg in str(ls[0]):
                print(
                    f" => Device received required geofence details such as geoId from cloud for circular geofence "
                    f"deletion successfully ")
                testResult(self, "passed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device received required geofence details such as geoId from cloud for circular geofence deletion successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive required geofence details such as geoId from cloud for circular geofenc deletion.")
                testResult(self, "verificationFailed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device failed to receive required geofence details such as geoId from cloud for circular geofence deletion , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, delete_action,
                                       success_status)
            if delete_action in str(ls[0]):
                print(f" => GeoId is deleted successfully on device")
                testResult(self, "passed",
                           "Validate that geofence is deleted successfully on device",
                           "geofence is deleted successfully on device, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(f" => Failed to delete geofence on device")
                testResult(self, "verificationFailed",
                           "Validate that geofence is deleted successfully on device",
                           "Failed to delete geofence on device or logs are not updated with required text , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msgType_16650,
                                       msgType_16650)
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_266,
                                       msg_266)

            if msg_266 in str(ls[0]):
                print(
                    f" => Device received Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "passed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device received Geofence deletion request message from cloud post mapping to vehicle using POST API successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "verificationFailed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API, or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_267,
                                       msg_267)

            if msg_267 in str(ls[0]):
                print(
                    f" => Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, flush_msg,
                                       flush_msg)
            if msg_268 in str(ls[0]):
                print(f" => Device failed to flush/update geofence table successfully")
                testResult(self, "passed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device flushed/updated geofence table successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device failed to flush/update geofence table or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_268,
                                       msg_268)

            if msg_268 in str(ls[0]):
                print(f" => Device responded back/sends response message to cloud successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device responded back/sends response message to cloud successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device failed to respond back/send response message to cloud or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                       "Failed to fetch geofence details for deletion " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            #self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
        print("Validation of Geofence Deletion at Cloud:")
        print("----------------------------------------------------------")

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        # assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code == 200:
            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                geofences = response_body["responseData"]["geofences"]
                found = False

                for geofence in geofences:
                    actual_Id_del = geofence["id"]

                    # Check for matching ID and validate device status
                    if actual_Id == actual_Id_del:
                        found = True
                        if "deviceStatus" in geofence:
                            device_status = geofence["deviceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == 9:  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                        elif "geofenceStatus" in geofence:
                            device_status = geofence["geofenceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == "DELETED":  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                            break
                if not found:
                    print(f"Error: Geofence ID '{actual_Id}' not found in response data.")
                    testResult(self, "passed",
                               "Validate Geofence deletion from Cloud DB",
                               f"Geofence ID '{actual_Id}' is not present in the Cloud DB.")
            else:
                print(f"Unexpected response message: {response_body['message']}")
                testResult(self, "failed",
                           "Validate Geofence deletion from Cloud DB",
                           f"Unexpected response message: {response_body['message']}")
        elif response.status_code == 204:
            testResult(self, "passed",
                       "Validate Geofence deletion from Cloud DB",
                       "No geofence data returned")
        else:
            print(f"Error: Unable to process the request. Status Code: {response.status_code}")
            testResult(self, "failed",
                       "Validate Geofence deletion from Cloud DB",
                       f"Unexpected status code: {response.status_code}")
        print("----------------------------------------------------------")

class Test_R8S3_Polygon_Geofence_disable:

    def test_create_polygon_geofence(self):

        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        geometryType = "polygon"
        cloudEnv = read_cloud_env(self)
        if cloudEnv in r8_patch4_sp17_envs:
            radius = "500"
        else:
            radius = "150"
        lat = "28.61370736476138"
        long = "77.22751858264235"
        isActive = "true"
        tolerance = "0"
        type1 = "PERSONAL"
        poiFlag = "False"
        tag = "office"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"
        systemId = read_vehicleJsonFile(self, "system_id")

        create_circle_polygon_geofence(self, onboardingType, chipsetType, name, geometryType, radius, long, lat, isActive,
                               tolerance, type1, poiFlag, tag, notification, isEdgeEnabled, ruleId,
                               ruleExpression,"polygon")

    def test_create_polygon_geofence_disable(self):
        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        isActive = "true"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed&gt;50"
        systemId = read_vehicleJsonFile(self, "system_id")

        # Geofence enable/disable
        geofence_enable_disable(
            self,
            systemId,
            notification,
            isEdgeEnabled,
            ruleId,
            isActive,
            ruleExpression,
            name,
            "disable",
            "disable"
        )

        # Trigger Alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date &amp; time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_entry')

            print("Location stub start/run process is completed, verify logs for trip &amp; telemetry details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")
            pull_logs_from_IVI_device(self, onboardingType, chipsetType)
            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_in_alert_text, geo_polygon_in_alert_text)

            if geo_polygon_in_alert_text in str(ls[0]):
                print(f" =&gt; Aert is triggered/generated when a vehicle entered the polygon geofence")
                print("c2c logs line data : =&gt; ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_polygon_in_alert_text in str(ls[0]):
            print(f" =&gt; Aert is triggered/generated when a vehicle entered the polygon geofence")
            testResult(
                self,
                "passed",
                "Validate if an alert is triggered/generated when a vehicle enters the polygon geofence",
                "Aert is triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                "detailed info"
            )
            print("c2c logs line data : =&gt; ", ls[0])

        if str(ls[0]) == "Error":
            print(
                " =&gt; Failed to trigger Alert when a vehicle entered the polygon geofence. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Validate if an alert is generated when a vehicle enters the polygon geofence",
                "Aert is not triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                "detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status &amp; response for single systemId &amp; eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(
            self,
            systemId,
            geofence_entry_categoryName,
            geofence_entry_notification_name,
            notification_type,
            dt,
            dt1,
            "disable"
        )

        print("----------------------------------------------------------")

        # Trigger exit alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date &amp; time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_exit')

            print("Location stub start/run process is completed, verify logs for trip &amp; telemetry details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")
            pull_logs_from_IVI_device(self, onboardingType, chipsetType)
            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_out_alert_text, geo_polygon_out_alert_text)

            if geo_polygon_out_alert_text in str(ls[0]):
                print(f" =&gt; Aert is triggered/generated when a vehicle exit the polygon geofence")
                print("c2c logs line data : =&gt; ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_polygon_out_alert_text in str(ls[0]):
            print(f" =&gt; Aert is triggered/generated when a vehicle exited the polygon geofence")
            testResult(
                self,
                "passed",
                "Validate if an alert is triggered/generated when a vehicle exits the polygon geofence",
                "Aert is triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                "detailed info"
            )
            print("c2c logs line data : =&gt; ", ls[0])

        if str(ls[0]) == "Error":
            print(
                " =&gt; Failed to trigger Alert when a vehicle exited the polygon geofence. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Validate if an alert is generated when a vehicle exits the polygon geofence",
                "Aert is not triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                "detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status &amp; response for single systemId &amp; eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(
            self,
            systemId,
            geofence_exit_categoryName,
            geofence_exit_notification_name,
            notification_type,
            dt,
            dt1,
            "disable"
        )

        print("----------------------------------------------------------")

    def test_create_polygon_geofence_enable(self):

        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        isActive = "true"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"
        systemId = read_vehicleJsonFile(self, "system_id")

        # Geofence enable/disable

        geofence_enable_disable(self, systemId, notification, isEdgeEnabled, ruleId, isActive,
                                ruleExpression, name, "enable", "enable")

        # Trigger Alert
        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_entry')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_in_alert_text, geo_polygon_in_alert_text)

            if geo_polygon_in_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle entered the polygon geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_polygon_in_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle entered the polygon geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle enters the polygon geofence",
                       "Aert is triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle entered the polygon geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle enters the polygon geofence",
                       "Aert is not triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(self, systemId, geofence_entry_categoryName, geofence_entry_notification_name,
                                       notification_type, dt, dt1, "alert_trigger_from_device")

        print("----------------------------------------------------------")

        # Trigger exit alert

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_exit')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_out_alert_text, geo_polygon_out_alert_text)

            if geo_polygon_out_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle exit the polygon geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle exited the polygon geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle exits the polygon geofence",
                       "Aert is triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle exited the polygon geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle exits the polygon geofence",
                       "Aert is not triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v3(self, systemId, geofence_exit_categoryName, geofence_exit_notification_name,
                                       notification_type, dt, dt1, "alert_trigger_from_device")

        print("----------------------------------------------------------")

    def test_polygon_geofence_delete(self):
        print("----------------------------------------------------------")
        print("Fetch newly created geofence details")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        offset = "1"
        limit = "10"
        isActive = "true"

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["geofences"])
            for i in range(data_len):
                isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                actual_Id = response_body["responseData"]["geofences"][i]["id"]
                actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                if isEdgeEnabled == 1 or isEdgeEnabled == "1":
                    actual_Id = response_body["responseData"]["geofences"][i]["id"]
                    actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                    break

            # Call api reusable module to delete geofence
            response = geofence_deleteGeofence_by_vehicleMappingId(self, actual_Id, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)
            if response.status_code != 200:
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Geofence deletion Initiated in the device":
                # vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
                message = response_body["message"]
                print("----------------------------------------------------------")
                # print('Vehicle Mapping Id : ', vehicleMappingId)
                print('Message : ', message)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully",
                           "Geofence deletion is initiated in the device and unmapped from Vehicle successfully ")
                #self.result.set_result(TestResults.passed)
            elif response_body["message"] != "Geofence deletion Initiated in the device":
                # print(response_body["responseData"]["message"])
                testResult(self, "failed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                           "Failed to initiate geofence deletion in the device or failed to delete geofence in the device or failed to unmap Geofence from Vehicle " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                #self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong")
                #self.result.set_result(TestResults.failed)

            print("----------------------------------------------------------")
            print("Validation of Geofence Deletion at Device:")
            print("----------------------------------------------------------")
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the geofence Deletion message is received from cloud
            conf_msg = 'configuration data ='
            msgType_16650 = '"message_type": 16650'
            msg_266 = 'Message type: 266 : Encoding type : 2'
            flush_msg = "Flush geofence table success"
            msg_268 = 'Message type: 268 : Encoding type : 2'
            msg_267 = 'Message type: 267 : Encoding type : 1'
            delete_action = '"action": "delete"'
            success_status = '"status": 0'

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, conf_msg,
                                       conf_msg)

            if conf_msg in str(ls[0]):
                print(
                    f" => Device received required geofence details such as geoId from cloud for circular geofence "
                    f"deletion successfully ")
                testResult(self, "passed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device received required geofence details such as geoId from cloud for circular geofence deletion successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive required geofence details such as geoId from cloud for circular geofenc deletion.")
                testResult(self, "verificationFailed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device failed to receive required geofence details such as geoId from cloud for circular geofence deletion , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, delete_action,
                                       success_status)
            if delete_action in str(ls[0]):
                print(f" => GeoId is deleted successfully on device")
                testResult(self, "passed",
                           "Validate that geofence is deleted successfully on device",
                           "geofence is deleted successfully on device, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(f" => Failed to delete geofence on device")
                testResult(self, "verificationFailed",
                           "Validate that geofence is deleted successfully on device",
                           "Failed to delete geofence on device or logs are not updated with required text , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msgType_16650,
                                       msgType_16650)
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_266,
                                       msg_266)

            if msg_266 in str(ls[0]):
                print(
                    f" => Device received Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "passed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device received Geofence deletion request message from cloud post mapping to vehicle using POST API successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "verificationFailed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API, or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_267,
                                       msg_267)

            if msg_267 in str(ls[0]):
                print(
                    f" => Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, flush_msg,
                                       flush_msg)
            if msg_268 in str(ls[0]):
                print(f" => Device failed to flush/update geofence table successfully")
                testResult(self, "passed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device flushed/updated geofence table successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device failed to flush/update geofence table or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_268,
                                       msg_268)

            if msg_268 in str(ls[0]):
                print(f" => Device responded back/sends response message to cloud successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device responded back/sends response message to cloud successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device failed to respond back/send response message to cloud or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                       "Failed to fetch geofence details for deletion " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            #self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
        print("Validation of Geofence Deletion at Cloud:")
        print("----------------------------------------------------------")

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        # assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code == 200:
            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                geofences = response_body["responseData"]["geofences"]
                found = False

                for geofence in geofences:
                    actual_Id_del = geofence["id"]

                    # Check for matching ID and validate device status
                    if actual_Id == actual_Id_del:
                        found = True
                        if "deviceStatus" in geofence:
                            device_status = geofence["deviceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == 9:  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                        elif "geofenceStatus" in geofence:
                            device_status = geofence["geofenceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == "DELETED":  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                            break
                if not found:
                    print(f"Error: Geofence ID '{actual_Id}' not found in response data.")
                    testResult(self, "passed",
                               "Validate Geofence deletion from Cloud DB",
                               f"Geofence ID '{actual_Id}' is not present in the Cloud DB.")
            else:
                print(f"Unexpected response message: {response_body['message']}")
                testResult(self, "failed",
                           "Validate Geofence deletion from Cloud DB",
                           f"Unexpected response message: {response_body['message']}")
        elif response.status_code == 204:
            testResult(self, "passed",
                       "Validate Geofence deletion from Cloud DB",
                       "No geofence data returned")
        else:
            print(f"Error: Unable to process the request. Status Code: {response.status_code}")
            testResult(self, "failed",
                       "Validate Geofence deletion from Cloud DB",
                       f"Unexpected status code: {response.status_code}")
        print("----------------------------------------------------------")

class Test_R8S3_Polygon_Geofence:

    def test_create_polygon_geofence(self):
        print("----------------------------------------------------------")
        print("Geofence - Cloud Precondition")
        print("----------------------------------------------------------")

        # Set ignition ON via stub
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'ignition_on_alert')
        time.sleep(5)

        print("----------------------------------------------------------")
        print("* * * * * * * * GET CURRENT VEHICLE MODE * * * * * * * * *")
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if ignition == "ON" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE"]:
            testResult(self, "passed",
                       "Cloud precondition should satisfy to create the geofence",
                       "Cloud precondition is satisfied to create the geofence")
            assert True
        else:
            testResult(self, "failed",
                       "Cloud precondition should satisfy to create the geofence",
                       "Cloud precondition is not satisfied to create the geofence")
            assert False

        print("----------------------------------------------------------")
        print("Create new geofence with predefined input/data")
        print("----------------------------------------------------------")

        msg_id = str(random.randint(10, 9999)).zfill(6)
        name = f"Geofence{msg_id}"
        geometryType = "polygon"
        radius = "150"
        lat = "28.61370736476138"
        long = "77.22751858264235"
        isActive = "true"
        tolerance = "0"
        type1 = "PERSONAL"
        poiFlag = "False"
        tag = "office"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"

        # Create geofence
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "polygon_geofence")

        assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
        response_body = response.json()

        if response_body["message"] == "Data Saved Successfully":
            geoId = response_body["responseData"]["geoId"]
            print("----------------------------------------------------------")
            print("Geofence Id:", geoId)
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "New geofence should be created successfully",
                       "New geofence is created successfully")
        else:
            testResult(self, "failed",
                       "New geofence should be created successfully",
                       f"New geofence is not created. Reason: {response_body['responseData']['message']}")
            assert False

        print("----------------------------------------------------------")
        print("Map Geofence with Vehicle")
        print("----------------------------------------------------------")

        # Map geofence to vehicle
        response = geofence_map_geofence_to_vehicle(
            self, geoId, notification, isEdgeEnabled, ruleId,
            isActive, ruleExpression, systemId, "valid"
        )

        assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
        response_body = response.json()

        mapping_msg = response_body["geofenceMappings"][0]["message"]
        if mapping_msg == "Geofence creation Initiated in the device":
            vehicleMappingId = response_body["geofenceMappings"][0]["vehicleMappingId"]
            print("----------------------------------------------------------")
            print("Vehicle Mapping Id:", vehicleMappingId)
            print("Message:", mapping_msg)
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                       "Geofence creation is initiated and mapped to Vehicle successfully")
        else:
            testResult(self, "failed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                       f"Failed to initiate or map geofence. Reason: {mapping_msg}")
            assert False
        print("----------------------------------------------------------")
        print("Validation of Geofence Creation at Device:")
        print("----------------------------------------------------------")

        # Pull logs for validation
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # Define expected log messages
        conf_msg = "configuration data ="
        msgType_16650 = '"message_type": 16650'
        msg_266 = "Message type: 266 : Encoding type : 2"
        flush_msg = "Flush geofence table success"
        msg_268 = "Message type: 268 : Encoding type : 2"
        msg_267 = "Message type: 267 : Encoding type : 1"

        # Validate geofence configuration message
        ls = verify_message_in_log(self, conf_msg, conf_msg)
        if conf_msg in str(ls[0]):
            print("=> Device received required geofence details from cloud successfully")
            testResult(self, "passed",
                       "Device should receive geofence details from cloud",
                       "Device received geofence details successfully. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> Device failed to receive geofence details from cloud")
            testResult(self, "verificationFailed",
                       "Device should receive geofence details from cloud",
                       "Device failed to receive geofence details. Refer to device logs.")

        print("----------------------------------------------------------")

        # Validate geoId presence
        ls = verify_message_in_log(self, geoId, geoId)
        if geoId in str(ls[0]):
            print("=> GeoId is present and matches POST API creation")
            testResult(self, "passed",
                       "GeoId should match POST API creation",
                       "GeoId matches POST API creation. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> GeoId is missing or mismatched")
            testResult(self, "verificationFailed",
                       "GeoId should match POST API creation",
                       "GeoId missing or mismatched. Refer to device logs.")

        print("----------------------------------------------------------")

        # Validate geofence creation request message
        ls = verify_message_in_log(self, msg_266, msg_266)
        if msg_266 in str(ls[0]):
            print("=> Device received geofence creation request from cloud")
            testResult(self, "passed",
                       "Device should receive geofence creation request from cloud",
                       "Device received geofence creation request successfully. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> Device failed to receive geofence creation request")
            testResult(self, "verificationFailed",
                       "Device should receive geofence creation request from cloud",
                       "Device failed to receive geofence creation request. Refer to device logs.")

        print("----------------------------------------------------------")

        # Validate acknowledgement message
        ls = verify_message_in_log(self, msg_267, msg_267)
        if msg_267 in str(ls[0]):
            print("=> Device sent acknowledgement to cloud")
            testResult(self, "passed",
                       "Device should send acknowledgement to cloud",
                       "Device sent acknowledgement successfully. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> Device failed to send acknowledgement to cloud")
            testResult(self, "verificationFailed",
                       "Device should send acknowledgement to cloud",
                       "Device failed to send acknowledgement. Refer to device logs.")

        print("----------------------------------------------------------")

        # Validate geofence table flush
        ls = verify_message_in_log(self, flush_msg, flush_msg)
        if msg_268 in str(ls[0]):
            print("=> Device flushed geofence table successfully")
            testResult(self, "passed",
                       "Device should flush geofence table",
                       "Device flushed geofence table successfully. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> Device failed to flush geofence table")
            testResult(self, "verificationFailed",
                       "Device should flush geofence table",
                       "Device failed to flush geofence table. Refer to device logs.")

        print("----------------------------------------------------------")

        # Validate final response message
        ls = verify_message_in_log(self, msg_268, msg_268)
        if msg_268 in str(ls[0]):
            print("=> Device sent final response to cloud")
            testResult(self, "passed",
                       "Device should send final response to cloud",
                       "Device sent final response successfully. Refer to device logs.")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("=> Device failed to send final response to cloud")
            testResult(self, "verificationFailed",
                       "Device should send final response to cloud",
                       "Device failed to send final response. Refer to device logs.")

        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("Cloud Side Validations: Fetch Geofence List to verify newly created geofence details")
        print("----------------------------------------------------------")

        # Call API reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, "1", "10", isActive, "valid")

        # Validate response status code
        assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            geofences = response_body["responseData"]["geofences"]
            found = False

            for geofence in geofences:
                isEdgeEnabled = geofence["isEdgeEnabled"]
                actual_geoId = geofence["geofence"]["geoId"]

                if actual_geoId == geoId and str(isEdgeEnabled) == "1":
                    found = True

                    if "deviceStatus" in geofence:
                        device_status = geofence["deviceStatus"]
                        if str(device_status) == "1":
                            testResult(self, "passed",
                                       "Newly created geofence should be listed & fetched successfully",
                                       f"Geofence with geoId '{geoId}' is successfully created and fetched with status {device_status}.")
                        else:
                            testResult(self, "failed",
                                       "Newly created geofence should be listed & fetched successfully",
                                       f"Geofence with geoId '{geoId}' has unexpected status {device_status}.")
                    elif "geofenceStatus" in geofence:
                        device_status = geofence["geofenceStatus"]
                        if device_status == "SAVED_IN_DEVICE":
                            testResult(self, "passed",
                                       "Newly created geofence should be listed & fetched successfully",
                                       f"Geofence with geoId '{geoId}' is successfully created and fetched with status {device_status}.")
                        else:
                            testResult(self, "failed",
                                       "Newly created geofence should be listed & fetched successfully",
                                       f"Geofence with geoId '{geoId}' has unexpected status {device_status}.")
                    else:
                        testResult(self, "failed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' has no recognizable status field.")
                    break

            if not found:
                testResult(self, "failed",
                           "Newly created geofence should be listed & fetched successfully",
                           f"No matching geofence found for geoId: {geoId}. Refer to device/cloud logs or API response.")
        else:
            print(f"Unexpected response message: {response_body['message']}")
            testResult(self, "failed",
                       "Newly created geofence should be listed & fetched successfully",
                       f"Unexpected response message: {response_body['message']}. Refer to device & cloud logs for more details.")

        print("----------------------------------------------------------")

    def test_polygon_geofence_IN_alert(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_entry')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_in_alert_text, geo_polygon_in_alert_text)

            if geo_in_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle entered the polygon geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_in_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle entered the polygon geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle enters the polygon geofence",
                       "Aert is triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle entered the polygon geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle enters the polygon geofence",
                       "Aert is not triggered/generated when a vehicle entered the polygon geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v2(self, systemId, geofence_entry_categoryName, geofence_entry_notification_name,
                                       notification_type, dt, dt1)

        print("----------------------------------------------------------")

    def test_polygon_geofence_OUT_alert(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        # categoryId = 3
        # status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'geofence_polygon_alert_exit')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, geo_polygon_out_alert_text, geo_polygon_out_alert_text)

            if geo_polygon_out_alert_text in str(ls[0]):
                print(f" => Aert is triggered/generated when a vehicle exit the polygon geofence")
                print("c2c logs line data : => ", ls[0])
                break
            else:
                time.sleep(5)

        print("----------------------------------------------------------")

        if geo_polygon_out_alert_text in str(ls[0]):
            print(f" => Aert is triggered/generated when a vehicle exited the polygon geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle exits the polygon geofence",
                       "Aert is triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle exited the polygon geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle exits the polygon geofence",
                       "Aert is not triggered/generated when a vehicle exited the polygon geofence, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        # Call verification module to validate alert details
        verify_notification_details_v2(self, systemId, geofence_exit_categoryName, geofence_exit_notification_name,
                                       notification_type, dt, dt1)

        print("----------------------------------------------------------")

    def test_polygon_geofence_delete(self):
        print("----------------------------------------------------------")
        print("Fetch newly created geofence details")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        offset = "1"
        limit = "10"
        isActive = "true"

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["geofences"])
            for i in range(data_len):
                isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                actual_Id = response_body["responseData"]["geofences"][i]["id"]
                actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                if isEdgeEnabled == 1 or isEdgeEnabled == "1":
                    actual_Id = response_body["responseData"]["geofences"][i]["id"]
                    actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                    break

            # Call api reusable module to delete geofence
            response = geofence_deleteGeofence_by_vehicleMappingId(self, actual_Id, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)
            if response.status_code != 200:
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Geofence deletion Initiated in the device":
                # vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
                message = response_body["message"]
                print("----------------------------------------------------------")
                # print('Vehicle Mapping Id : ', vehicleMappingId)
                print('Message : ', message)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully",
                           "Geofence deletion is initiated in the device and unmapped from Vehicle successfully ")
                #self.result.set_result(TestResults.passed)
            elif response_body["message"] != "Geofence deletion intiated in the device":
                # print(response_body["responseData"]["message"])
                testResult(self, "failed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                           "Failed to initiate geofence deletion in the device or failed to delete geofence in the device or failed to unmap Geofence from Vehicle " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                #self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong")
                #self.result.set_result(TestResults.failed)

            print("----------------------------------------------------------")
            print("Validation of Geofence Deletion at Device:")
            print("----------------------------------------------------------")
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the geofence Deletion message is received from cloud
            conf_msg = 'configuration data ='
            msgType_16650 = '"message_type": 16650'
            msg_266 = 'Message type: 266 : Encoding type : 2'
            flush_msg = "Flush geofence table success"
            msg_268 = 'Message type: 268 : Encoding type : 2'
            msg_267 = 'Message type: 267 : Encoding type : 1'
            delete_action = '"action": "delete"'
            success_status = '"status": 0'

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, conf_msg,
                                       conf_msg)

            if conf_msg in str(ls[0]):
                print(
                    f" => Device received required geofence details such as geoId from cloud for circular geofence "
                    f"deletion successfully ")
                testResult(self, "passed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device received required geofence details such as geoId from cloud for circular geofence deletion successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive required geofence details such as geoId from cloud for circular geofenc deletion.")
                testResult(self, "verificationFailed",
                           "Validate that device should receive required geofence details such as geoId from cloud for circular geofence deletion",
                           "Device failed to receive required geofence details such as geoId from cloud for circular geofence deletion , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, delete_action,
                                       success_status)
            if delete_action in str(ls[0]):
                print(f" => GeoId is deleted successfully on device")
                testResult(self, "passed",
                           "Validate that geofence is deleted successfully on device",
                           "geofence is deleted successfully on device, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(f" => Failed to delete geofence on device")
                testResult(self, "verificationFailed",
                           "Validate that geofence is deleted successfully on device",
                           "Failed to delete geofence on device or logs are not updated with required text , pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msgType_16650,
                                       msgType_16650)
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_266,
                                       msg_266)

            if msg_266 in str(ls[0]):
                print(
                    f" => Device received Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "passed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device received Geofence deletion request message from cloud post mapping to vehicle using POST API successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API")
                testResult(self, "verificationFailed",
                           "Validate that Device should receive Geofence deletion request message from cloud post mapping to vehicle using POST API",
                           "Device failed to receive Geofence deletion request message from cloud post mapping to vehicle using POST API, or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_267,
                                       msg_267)

            if msg_267 in str(ls[0]):
                print(
                    f" => Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device responded back/sends acknowledgement message to cloud post receiving Geofence deletion request message successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence deletion request message",
                           "Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, flush_msg,
                                       flush_msg)
            if msg_268 in str(ls[0]):
                print(f" => Device failed to flush/update geofence table successfully")
                testResult(self, "passed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device flushed/updated geofence table successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should flush/update geofence table successfully",
                           "Device failed to flush/update geofence table or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")

            print("----------------------------------------------------------")

            ls = verify_message_in_log(self, msg_268,
                                       msg_268)

            if msg_268 in str(ls[0]):
                print(f" => Device responded back/sends response message to cloud successfully")
                testResult(self, "passed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device responded back/sends response message to cloud successfully, pls refer device logs for "
                           "detailed info")
                print("c2c logs line data : => ", ls[0])

            if str(ls[0]) == "Error":
                print(
                    f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence deletion request message")
                testResult(self, "verificationFailed",
                           "Validate that Device should respond back/send response message to cloud successfully",
                           "Device failed to respond back/send response message to cloud or device log is not updated with required msg. pls refer device logs for "
                           "detailed info")
            print("----------------------------------------------------------")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                       "Failed to fetch geofence details for deletion " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            #self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
        print("Validation of Geofence Deletion at Cloud:")
        print("----------------------------------------------------------")

        # Call api reusable module
        response = geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, "valid")

        # Validate response status code
        # assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code == 200:
            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                geofences = response_body["responseData"]["geofences"]
                found = False

                for geofence in geofences:
                    actual_Id_del = geofence["id"]

                    # Check for matching ID and validate device status
                    if actual_Id == actual_Id_del:
                        found = True
                        if "deviceStatus" in geofence:
                            device_status = geofence["deviceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == 9:  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                        elif "geofenceStatus" in geofence:
                            device_status = geofence["geofenceStatus"]
                            print(f"Device Status for Geofence ID '{actual_Id}': {device_status}")
                            # Validate the device status ( DELETED status = 9)
                            if device_status == "DELETED":  # 9 means "DELETED"
                                testResult(self, "passed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' is successfully deleted with device status {device_status}.")
                            else:
                                testResult(self, "failed",
                                           "Validate Geofence deletion from Cloud DB",
                                           f"Geofence ID '{actual_Id}' has unexpected device status {device_status}.")
                            break
                if not found:
                    print(f"Error: Geofence ID '{actual_Id}' not found in response data.")
                    testResult(self, "passed",
                               "Validate Geofence deletion from Cloud DB",
                               f"Geofence ID '{actual_Id}' is not present in the Cloud DB.")
            else:
                print(f"Unexpected response message: {response_body['message']}")
                testResult(self, "failed",
                           "Validate Geofence deletion from Cloud DB",
                           f"Unexpected response message: {response_body['message']}")
        elif response.status_code == 204:
            testResult(self, "passed",
                       "Validate Geofence deletion from Cloud DB",
                       "No geofence data returned")
        else:
            print(f"Error: Unable to process the request. Status Code: {response.status_code}")
            testResult(self, "failed",
                       "Validate Geofence deletion from Cloud DB",
                       f"Unexpected status code: {response.status_code}")
        print("----------------------------------------------------------")