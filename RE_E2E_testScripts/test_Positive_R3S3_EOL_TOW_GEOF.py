import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile
from C2CModules.notifications import notification_verify_update_status, notification_verify_notify_status, \
    notification_verify_event_details, notification_verify_alert_details, \
    notificationServiceController_details_by_systemId_Category
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.e2e_testData import *
from C2CModules.geofence import Geofence_createGeofence, geofence_getGeofence_by_systemId, \
    geofence_map_geofence_to_vehicle, geofence_getGeofence_by_vehicleMappingId, \
    geofence_deleteGeofence_by_vehicleMappingId, geofence_precondition
from C2CModules.notifications import notification_event_details_by_systemId_Category

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

class Test_EOL_Onboarding:

    def test_positive_eol_onboarding(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, "global")

        vehicle_connection_state(self, "global")

    @pytest.mark.smoke
    def test_positive_device_rehoming_v2(self):

        print("----------------------------------------------------------")
        print("Rehome the vehicle with predefined input/data")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)
        action = "rehome"

        # Call api reusable module
        response = deviceRehoming(self, systemId, action, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "IN_PROGRESS":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                trackingId = response_body["trackingId"]
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "IN_PROGRESS":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # verify rehoming status on the cloud side
        response = deviceRehoming_status(self, trackingId, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "SUCCESS":
            trackingId_actual = response_body["trackingId"]
            if trackingId == trackingId_actual:
                testResult(self, "passed", "Device rehoming should be success",
                           "Device rehoming is success")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "SUCCESS":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming should be success",
                       "Device rehoming failed" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE" or system_state == "REHOMED":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, "regional")

        vehicle_connection_state(self, "regional")


class Test_RE_SP2_ToAwayAlert:

    @pytest.mark.regression
    # Validate tow away alert functionality.
    # Verify whether the alert is sent from device when tow away event occurs
    # Validate that the tow way alert is not sent from device when IMU value is 0 and location is triggered
    def test1_positive_bikeSecuritySafety_towAway_alert1(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Start c2c services
        # ===========================================================================================
        print("----------------------------------------------------------")
        # run_c2cServices_on_primary_IVI(self, onboardingType, chipsetType)
        time.sleep(5)

        # ===========================================================================================
        # Run tub on device for TOW AWAY ALERTadb shell

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TOW AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "towAway_alert1")


        print("TOW AWAY ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        towAway_enable_msg = "tamper_alert:1"
        ls = verify_message_in_log(self, towAway_enable_msg, towAway_enable_msg)
        print(ls)

        towAway_alert_notification_string = "constr_and_send_proto_msg success for 1 : 0"
        ls = verify_message_in_log(self, towAway_alert_notification_string, towAway_alert_notification_string)
        print(ls)

        towAway_disable_msg = "tamper_alert:0"
        ls = verify_message_in_log(self, towAway_disable_msg , towAway_disable_msg)
        print(ls)

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
        notification_verify_alert_details(self, systemId, towAway_categoryName_v2, towAway_notification_name_v2,notification_type, dt, dt1)


class Test_RE_R3_SP3_Geofence:

    def test_create_circle_geofence(self):
        print("----------------------------------------------------------")
        print("Create new geofence with predefined input/data")
        print("----------------------------------------------------------")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
        name = 'Geofence' + str(msg_id)
        geometryType = "circle"
        radius = str(150)
        lat = str(28.61370736476138)
        long = str(77.22751858264235)
        isActive = 'true'
        tolerance = str(0)
        type1 = 'PERSONAL'
        poiFlag = 'False'
        tag = 'office'

        offset = "1"
        limit = "100"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Saved Successfully":
            geoId = response_body["responseData"]["geoId"]
            # message = response_body["responseData"]["message"]
            print("----------------------------------------------------------")
            print('Geofence Id : ', geoId)
            print("----------------------------------------------------------")
            # print('Message : ', message)
            testResult(self, "passed", "New geofence should be created successfully",
                       "New geofence is created successfully ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Data Saved Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "New geofence should be created successfully ",
                       "New geofence is not created " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")
        print("Map Geofence with Vehicle:")
        print("----------------------------------------------------------")

        # Call api reusable module

        response = geofence_map_geofence_to_vehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                    ruleExpression, systemId, "valid")

        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Geofence creation Initiated in the device":
            vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
            message = response_body["message"]
            print("----------------------------------------------------------")
            print('Vehicle Mapping Id : ', vehicleMappingId)
            print('Message : ', message)
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                       "Geofence creation is initiated in the device and mapped to Vehicle successfully ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Geofence creation Initiated in the device":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully ",
                       "Failed to initiate geofence creation in the device or failed to create geofence in the device or failed to map Geofence to Vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
        print("Validation of Geofence Creation at Device:")
        print("----------------------------------------------------------")
        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the geofence creation message is received from cloud
        conf_msg = 'configuration data ='
        msgType_16650 = '"message_type": 16650'
        msg_266 = 'Message type: 266 : Encoding type : 1'
        flush_msg = "Flush geofence table success"
        msg_268 = 'Message type: 268 : Encoding type : 1'
        msg_267 = 'Message type: 267 : Encoding type : 1'

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, conf_msg,
                                   conf_msg)

        if conf_msg in str(ls[0]):
            print(f" => Device received required geofence details such as geoId from cloud for circular geofence "
                  f"creation successfully ")
            testResult(self, "passed",
                       "Validate that device should receive required geofence details such as geoId from cloud for circular geofence creation",
                       "Device received required geofence details such as geoId from cloud for circular geofence creation successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to receive required geofence details such as geoId from cloud for circular geofenc creation.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive required geofence details such as geoId from cloud for circular geofence creation",
                       "Device failed to receive required geofence details such as geoId from cloud for circular geofence creation , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, geoId,
                                   geoId)
        if geoId in str(ls[0]):
            print(f" => GeoId is present and same as that of created using POST API")
            testResult(self, "passed",
                       "Validate that GeoId should be present and same as that of created using POST API",
                       "GeoId is present and same as that of created using POST API successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => GeoId is missing or not same as that of created using POST API")
            testResult(self, "verificationFailed",
                       "Validate that GeoId should be present and same as that of created using POST API",
                       "GeoId is missing or not same as that of created using POST API , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msgType_16650,
                                   msgType_16650)
        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msg_266,
                                   msg_266)

        if msg_266 in str(ls[0]):
            print(
                f" => Device received Geofence creation request message from cloud post mapping to vehicle using POST API")
            testResult(self, "passed",
                       "Validate that Device should receive Geofence creation request message from cloud post mapping to vehicle using POST API",
                       "Device received Geofence creation request message from cloud post mapping to vehicle using POST API successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to receive Geofence creation request message from cloud post mapping to vehicle using POST API")
            testResult(self, "verificationFailed",
                       "Validate that Device should receive Geofence creation request message from cloud post mapping to vehicle using POST API",
                       "Device failed to receive Geofence creation request message from cloud post mapping to vehicle using POST API, or device log is not updated with required msg. pls refer device logs for "
                       "detailed info")
        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msg_267,
                                   msg_267)

        if msg_267 in str(ls[0]):
            print(
                f" => Device responded back/sends acknowledgement message to cloud post receiving Geofence creation request message successfully")
            testResult(self, "passed",
                       "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence creation request message",
                       "Device responded back/sends acknowledgement message to cloud post receiving Geofence creation request message successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
            testResult(self, "verificationFailed",
                       "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence creation request message",
                       "Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message or device log is not updated with required msg. pls refer device logs for "
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
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
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
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
            testResult(self, "verificationFailed",
                       "Validate that Device should respond back/send response message to cloud successfully",
                       "Device failed to respond back/send response message to cloud or device log is not updated with required msg. pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")
        print("Cloud Side Validations : ")
        print("----------------------------------------------------------")

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
                # actual_Id = response_body["responseData"]["geofences"][i]["id"]
                actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                if actual_geoId == geoId and isEdgeEnabled == 1 or isEdgeEnabled == "1":
                    actual_Id = response_body["responseData"]["geofences"][i]["id"]
                    actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                    status = "PASS"
                    testResult(self, "Passed",
                               "Validate that newly created geofence should be listed & fetched successfully",
                               "Newly created geofence is listed & fetched successfully, pls refer device & cloud logs or api response for "
                               "detailed info")
                    # self.result.set_result(TestResults.passed)
                    break
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Validate that newly created geofence should be listed & fetched successfully",
                       "Failed to fetch newly created geofence successfully, pls refer device & cloud logs or api response for "
                       "detailed info")
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong, pls refer device & cloud logs or api response for detailed info")
            # self.result.set_result(TestResults.failed)

    def test_circle_geofence_IN_OUT_alert(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
        geo_out_alert_text = "Vehicle has exited geofence"
        categoryId = 3
        status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'geofence_alert1')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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

        ls1 = verify_message_in_log(self, geo_out_alert_text,
                                    geo_out_alert_text)

        if geo_out_alert_text in str(ls1[0]):
            print(f" => Aert is triggered/generated when a vehicle leaves the circular geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle leaves/exited the circular geofence",
                       "Aert is triggered/generated when a vehicle leaves/exited the circular geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls1[0])

        if str(ls1[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle leaves/exited the circular geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle leaves/exited the circular geofence",
                       "Aert is not triggered/generated when a vehicle leaves/exited the circular geofence, pls refer device logs for "
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
        #notification_verify_alert_details(self, systemId, geofence_categoryName_v2,geofence_notification_name_v2,notification_type, dt, dt1)

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
                # self.result.set_result(TestResults.failed)
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
                # self.result.set_result(TestResults.passed)
            elif response_body["message"] != "Geofence deletion intiated in the device":
                # print(response_body["responseData"]["message"])
                testResult(self, "failed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                           "Failed to initiate geofence deletion in the device or failed to delete geofence in the device or failed to unmap Geofence from Vehicle " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong")
                # self.result.set_result(TestResults.failed)

            print("----------------------------------------------------------")
            print("Validation of Geofence Deletion at Device:")
            print("----------------------------------------------------------")
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the geofence Deletion message is received from cloud
            conf_msg = 'configuration data ='
            msgType_16650 = '"message_type": 16650'
            msg_266 = 'Message type: 266 : Encoding type : 1'
            flush_msg = "Flush geofence table success"
            msg_268 = 'Message type: 268 : Encoding type : 1'
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
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)

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
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":
                data_len = len(response_body["responseData"]["geofences"])
                print("Deleted Id :  ", actual_Id)
                for i in range(data_len):
                    # isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                    actual_Id_del = response_body["responseData"]["geofences"][i]["id"]
                    if actual_Id == actual_Id_del:
                        testResult(self, "failed",
                                   "Validate that Geofence should be deleted from Cloud DB successfully",
                                   "Geofence is not deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                                   "detailed info")
                        break
                else:
                    testResult(self, "passed",
                               "Validate that Geofence should be deleted from Cloud DB successfully",
                               "Geofence is deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                               "detailed info")
            elif response_body["message"] != "Data Fetched Successfully":
                # print(response_body["responseData"]["message"])
                testResult(self, "passed",
                           "Validate that Geofence should be deleted from Cloud DB successfully",
                           "Geofence is deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                           "detailed info")
                # self.result.set_result(TestResults.failed)
            else:
                print("No geofence")
                # self.result.set_result(TestResults.failed)
        elif response.status_code == 204:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False


class Test_RE_R3_SP3_Geofence_polygon:

    def test_create_polygon_geofence(self):
        print("----------------------------------------------------------")
        print("Create new geofence with predefined input/data")
        print("----------------------------------------------------------")
        msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
        name = 'Geofence' + str(msg_id)
        geometryType = "polygon"
        radius = str(0)
        lat = str(28.61370736476138)
        long = str(77.22751858264235)
        isActive = 'true'
        tolerance = str(0)
        type1 = 'PERSONAL'
        poiFlag = 'False'
        tag = 'office'

        offset = "1"
        limit = "100"

        notification = 3
        isEdgeEnabled = 1
        ruleId = 0
        ruleExpression = "speed>50"

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "polygon_geofence")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Saved Successfully":
            geoId = response_body["responseData"]["geoId"]
            # message = response_body["responseData"]["message"]
            print("----------------------------------------------------------")
            print('Geofence Id : ', geoId)
            print("----------------------------------------------------------")
            # print('Message : ', message)
            testResult(self, "passed", "New geofence should be created successfully",
                       "New geofence is created successfully ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Data Saved Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "New geofence should be created successfully ",
                       "New geofence is not created " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")
        print("Map Geofence with Vehicle:")
        print("----------------------------------------------------------")

        # Call api reusable module

        response = geofence_map_geofence_to_vehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                    ruleExpression, systemId, "valid")

        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Geofence creation Initiated in the device":
            vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
            message = response_body["message"]
            print("----------------------------------------------------------")
            print('Vehicle Mapping Id : ', vehicleMappingId)
            print('Message : ', message)
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                       "Geofence creation is initiated in the device and mapped to Vehicle successfully ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Geofence creation Initiated in the device":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Geofence creation should be initiated in device and mapped to Vehicle successfully ",
                       "Failed to initiate geofence creation in the device or failed to create geofence in the device or failed to map Geofence to Vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
        print("Validation of Geofence Creation at Device:")
        print("----------------------------------------------------------")
        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the geofence creation message is received from cloud
        conf_msg = 'configuration data ='
        msgType_16650 = '"message_type": 16650'
        msg_266 = 'Message type: 266 : Encoding type : 1'
        flush_msg = "Flush geofence table success"
        msg_268 = 'Message type: 268 : Encoding type : 1'
        msg_267 = 'Message type: 267 : Encoding type : 1'

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, conf_msg,
                                   conf_msg)

        if conf_msg in str(ls[0]):
            print(f" => Device received required geofence details such as geoId from cloud for circular geofence "
                  f"creation successfully ")
            testResult(self, "passed",
                       "Validate that device should receive required geofence details such as geoId from cloud for circular geofence creation",
                       "Device received required geofence details such as geoId from cloud for circular geofence creation successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to receive required geofence details such as geoId from cloud for circular geofenc creation.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive required geofence details such as geoId from cloud for circular geofence creation",
                       "Device failed to receive required geofence details such as geoId from cloud for circular geofence creation , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, geoId,
                                   geoId)
        if geoId in str(ls[0]):
            print(f" => GeoId is present and same as that of created using POST API")
            testResult(self, "passed",
                       "Validate that GeoId should be present and same as that of created using POST API",
                       "GeoId is present and same as that of created using POST API successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => GeoId is missing or not same as that of created using POST API")
            testResult(self, "verificationFailed",
                       "Validate that GeoId should be present and same as that of created using POST API",
                       "GeoId is missing or not same as that of created using POST API , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msgType_16650,
                                   msgType_16650)
        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msg_266,
                                   msg_266)

        if msg_266 in str(ls[0]):
            print(
                f" => Device received Geofence creation request message from cloud post mapping to vehicle using POST API")
            testResult(self, "passed",
                       "Validate that Device should receive Geofence creation request message from cloud post mapping to vehicle using POST API",
                       "Device received Geofence creation request message from cloud post mapping to vehicle using POST API successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to receive Geofence creation request message from cloud post mapping to vehicle using POST API")
            testResult(self, "verificationFailed",
                       "Validate that Device should receive Geofence creation request message from cloud post mapping to vehicle using POST API",
                       "Device failed to receive Geofence creation request message from cloud post mapping to vehicle using POST API, or device log is not updated with required msg. pls refer device logs for "
                       "detailed info")
        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, msg_267,
                                   msg_267)

        if msg_267 in str(ls[0]):
            print(
                f" => Device responded back/sends acknowledgement message to cloud post receiving Geofence creation request message successfully")
            testResult(self, "passed",
                       "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence creation request message",
                       "Device responded back/sends acknowledgement message to cloud post receiving Geofence creation request message successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
            testResult(self, "verificationFailed",
                       "Validate that Device should respond back/send acknowledgement message to cloud post receiving Geofence creation request message",
                       "Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message or device log is not updated with required msg. pls refer device logs for "
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
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
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
                f" => Device failed to respond back/send acknowledgement message to cloud post receiving Geofence creation request message")
            testResult(self, "verificationFailed",
                       "Validate that Device should respond back/send response message to cloud successfully",
                       "Device failed to respond back/send response message to cloud or device log is not updated with required msg. pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")
        print("Cloud Side Validations : ")
        print("----------------------------------------------------------")

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
        status = ""
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["geofences"])
            print("Number of geofences:", data_len)
            for i in range(data_len):
                isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                actual_geoId = response_body["responseData"]["geofences"][i]["geofence"]["geoId"]
                # Ensure the logical condition is correctly grouped
                if actual_geoId == geoId and (isEdgeEnabled == 1 or isEdgeEnabled == "1"):
                    status = "PASS"
                    print("Geofence found with matching geoId and isEdgeEnabled")
                    testResult(self, "passed",
                               "Validate that newly created geofence should be listed & fetched successfully",
                               "Newly created geofence is listed & fetched successfully, pls refer device & cloud logs or API response for detailed info")
                    # Uncomment this line if you want to set the result status here
                    # self.result.set_result(TestResults.passed)
                    break
            else:
                # If no matching geofence is found
                status = "FAIL"
                print("No matching geofence found")
                testResult(self, "failed",
                           "Validate that newly created geofence should be listed & fetched successfully",
                           "Failed to fetch newly created geofence successfully, pls refer device & cloud logs or API response for detailed info")
                # Uncomment this line if you want to set the result status here
                # self.result.set_result(TestResults.failed)
        elif response_body["message"] != "Data Fetched Successfully":
            status = "FAIL"
            print("Message not 'Data Fetched Successfully'")
            testResult(self, "failed",
                       "Validate that newly created geofence should be listed & fetched successfully",
                       "Failed to fetch newly created geofence successfully, pls refer device & cloud logs or API response for detailed info")
            # Uncomment this line if you want to set the result status here
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong, pls refer device & cloud logs or API response for detailed info")
            # Uncomment this line if you want to set the result status here
            # self.result.set_result(TestResults.failed)

        # Print the final status for debugging
        print("Final status:", status)

    def test_circle_geofence_IN_OUT_alert(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        geo_in_alert_text = "Polygon geofence:Vehicle has entered geofence"  # "Vehicle has entered geofence"
        geo_out_alert_text = "Polygon geofence:Vehicle has exited geofence"
        categoryId = 3
        status = "NOTIFIED"

        ls = ""
        for i in range(2):
            # ===========================================================================================
            # Run telemetry stub on device for trip waypoint
            # ===========================================================================================
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run location stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'geofence_alert_polygon')

            print("Location stub start/run process is completed, verify logs for trip & telemetry details : ")

            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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

        ls1 = verify_message_in_log(self, geo_out_alert_text,
                                    geo_out_alert_text)

        if geo_out_alert_text in str(ls1[0]):
            print(f" => Aert is triggered/generated when a vehicle leaves the circular geofence")
            testResult(self, "passed",
                       "Validate if an alert is triggered/generated when a vehicle leaves/exited the circular geofence",
                       "Aert is triggered/generated when a vehicle leaves/exited the circular geofence, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls1[0])

        if str(ls1[0]) == "Error":
            print(
                f" => Failed to trigger Alert when a vehicle leaves/exited the circular geofence. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Validate if an alert is generated when a vehicle leaves/exited the circular geofence",
                       "Aert is not triggered/generated when a vehicle leaves/exited the circular geofence, pls refer device logs for "
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
        #notification_verify_alert_details(self, systemId, geofence_categoryName_v2,geofence_notification_name_v2,notification_type, dt, dt1)

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
                # self.result.set_result(TestResults.failed)
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
                # self.result.set_result(TestResults.passed)
            elif response_body["message"] != "Geofence deletion intiated in the device":
                # print(response_body["responseData"]["message"])
                testResult(self, "failed",
                           "Geofence deletion should be initiated in device and unmapped from Vehicle successfully ",
                           "Failed to initiate geofence deletion in the device or failed to delete geofence in the device or failed to unmap Geofence from Vehicle " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong")
                # self.result.set_result(TestResults.failed)

            print("----------------------------------------------------------")
            print("Validation of Geofence Deletion at Device:")
            print("----------------------------------------------------------")
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the geofence Deletion message is received from cloud
            conf_msg = 'configuration data ='
            msgType_16650 = '"message_type": 16650'
            msg_266 = 'Message type: 266 : Encoding type : 1'
            flush_msg = "Flush geofence table success"
            msg_268 = 'Message type: 268 : Encoding type : 1'
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
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)

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
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":
                data_len = len(response_body["responseData"]["geofences"])
                print("Deleted Id :  ", actual_Id)
                for i in range(data_len):
                    # isEdgeEnabled = response_body["responseData"]["geofences"][i]["isEdgeEnabled"]
                    actual_Id_del = response_body["responseData"]["geofences"][i]["id"]
                    if actual_Id == actual_Id_del:
                        testResult(self, "failed",
                                   "Validate that Geofence should be deleted from Cloud DB successfully",
                                   "Geofence is not deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                                   "detailed info")
                        break
                else:
                    testResult(self, "passed",
                               "Validate that Geofence should be deleted from Cloud DB successfully",
                               "Geofence is deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                               "detailed info")
            elif response_body["message"] != "Data Fetched Successfully":
                # print(response_body["responseData"]["message"])
                testResult(self, "passed",
                           "Validate that Geofence should be deleted from Cloud DB successfully",
                           "Geofence is deleted from Cloud DB successfully, pls refer device & cloud logs or api response for "
                           "detailed info")
                # self.result.set_result(TestResults.failed)
            else:
                print("No geofence")
                # self.result.set_result(TestResults.failed)
        elif response.status_code == 204:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

class Test_geofence_precondition1:

    def test_pos_save_geofence_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "geofence_config_update"
        statePreconditions1 = {
            "value": [
                "ON"
            ],
            "operator": "eq",
            "attribute": "ignition"
        }

        statePreconditions2 = {
            "value": [
                "privacy_mode",
                "incognito_mode",
                "remote_diagnostic",
                "NORMAL_MODE"
            ],
            "operator": "in",
            "attribute": "vehicleMode"
        }

        statePreconditions3 = {
            "value": [
                "OFF"
            ],
            "operator": "eq",
            "attribute": "parkMode"
        }
        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("----------------------------------------------------------")

        geofence_precondition(self, model, action, statePreconditions1, statePreconditions2, statePreconditions3, "save_precondition")

    def test_pos_update_geofence_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "geofence_config_update"
        statePreconditions1 = {
            "value": [
                "ON"
            ],
            "operator": "eq",
            "attribute": "ignition"
        }

        statePreconditions2 = {
            "value": [
                "privacy_mode",
                "incognito_mode",
                "remote_diagnostic",
                "NORMAL_MODE"
            ],
            "operator": "in",
            "attribute": "vehicleMode"
        }

        statePreconditions3 = {
            "value": [
                "OFF"
            ],
            "operator": "eq",
            "attribute": "parkMode"
        }
        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("----------------------------------------------------------")

        geofence_precondition(self, model, action, statePreconditions1, statePreconditions2, statePreconditions3,
                              "update_precondition")