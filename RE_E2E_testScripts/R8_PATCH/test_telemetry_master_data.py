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


class Test_Master_data:

    def test1_positive_telemetry_master_data_add_new_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Adding for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute (not validated in this test)
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Adding second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        response = Telemetry_master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_single_attribute"
        )

        if response.status_code == 200:
            response_body = response.json()
            if response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed",
                           "Telemetry Master Data - New event should saved successfully",
                           "Telemetry Master Data - New event is saved successfully")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - New event should saved successfully",
                           "Telemetry Master Data - New event is not saved successfully")
                assert False
        elif response.status_code == 400:
            response_body = response.json()
            if (response_body["errors"][0]["errorCode"] == "15565" and
                    response_body["errors"][0]["message"] == "Data Already exist with given Event Type"):
                testResult(self, "passed",
                           "Telemetry Master Data - Already event exist",
                           "Telemetry Master Data - Already event exist")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - Already event exist",
                           "Telemetry Master Data - event doesn't exist")
                assert False

        # Fetch event details
        response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
        assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

        response_body = response.json()
        if response_body["message"] == "Data Fetched Successfully":
            telemetry_list = response_body.get("telemetryData", [])
            assert telemetry_list, "No telemetry data returned for the eventType"

            event = telemetry_list[0]
            eventType_actual = event.get("eventType")
            eventName_actual = event.get("eventName")
            eventCategory_actual = event.get("eventCategory")
            modelCode_actual = event.get("modelCode")
            actual_params = event.get("attributeList", [])

            # Validate event details
            if (str(eventType_actual) == str(eventType) and
                    str(eventName_actual) == str(eventName) and
                    str(eventCategory_actual) == str(eventCategory) and
                    str(modelCode_actual) == str(modelCode)):

                # Check only attributeList1
                expected = attributeList1
                found = any(
                    str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                    str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                    str(actual.get("elementId")) == str(expected.get("elementId")) and
                    str(actual.get("idName")) == str(expected.get("idName")) and
                    str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                    str(actual.get("description")) == str(expected.get("description")) and
                    str(actual.get("areaList", [{}])[0].get("areaId")) == str(
                        expected.get("areaList", [{}])[0].get("areaId")) and
                    str(actual.get("areaList", [{}])[0].get("areaName")) == str(
                        expected.get("areaList", [{}])[0].get("areaName"))
                    for actual in actual_params
                )

                if found:
                    testResult(self, "passed",
                               "Expected telemetry attribute found in API response",
                               "Validation successful")
                    assert True
                else:
                    testResult(self, "failed",
                               "Expected telemetry attribute missing in API response",
                               f"Missing attribute: {expected.get('attributeName')}")
                    assert False, f"Missing attribute: {expected.get('attributeName')}"
            else:
                testResult(self, "failed",
                           "Event header details should match expected values",
                           f"Mismatch in event details: "
                           f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                           f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
                assert False, (
                    f"Header mismatch: Expected "
                    f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                    f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
                )

    def test2_positive_telemetry_master_data_add_new_event_with_multiple_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1006"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Adding for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Adding second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        response = Telemetry_master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_multiple_attribute"
        )

        if response.status_code == 200:
            response_body = response.json()
            if response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed",
                           "Telemetry Master Data - New event should saved successfully",
                           "Telemetry Master Data - New event is saved successfully")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - New event should saved successfully",
                           "Telemetry Master Data - New event is not saved successfully")
                assert False
        elif response.status_code == 400:
            response_body = response.json()
            if (response_body["errors"][0]["errorCode"] == "15565" and
                    response_body["errors"][0]["message"] == "Data Already exist with given Event Type"):
                testResult(self, "passed",
                           "Telemetry Master Data - Already event exist",
                           "Telemetry Master Data - Already event exist")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - Already event exist",
                           "Telemetry Master Data - event doesn't exist")
                assert False

        # Fetch event details
        response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
        assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

        response_body = response.json()
        if response_body["message"] == "Data Fetched Successfully":
            telemetry_list = response_body.get("telemetryData", [])
            assert telemetry_list, "No telemetry data returned for the eventType"

            event = telemetry_list[0]
            eventType_actual = event.get("eventType")
            eventName_actual = event.get("eventName")
            eventCategory_actual = event.get("eventCategory")
            modelCode_actual = event.get("modelCode")
            actual_params = event.get("attributeList", [])

            # Validate event details
            if (str(eventType_actual) == str(eventType) and
                    str(eventName_actual) == str(eventName) and
                    str(eventCategory_actual) == str(eventCategory) and
                    str(modelCode_actual) == str(modelCode)):

                # Validate both attributes
                expected_attributes = [attributeList1, attributeList2]
                missing = []

                for expected in expected_attributes:
                    found = any(
                        str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                        str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                        str(actual.get("elementId")) == str(expected.get("elementId")) and
                        str(actual.get("idName")) == str(expected.get("idName")) and
                        str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                        str(actual.get("description")) == str(expected.get("description")) and
                        str(actual.get("areaList", [{}])[0].get("areaId")) == str(
                            expected.get("areaList", [{}])[0].get("areaId")) and
                        str(actual.get("areaList", [{}])[0].get("areaName")) == str(
                            expected.get("areaList", [{}])[0].get("areaName"))
                        for actual in actual_params
                    )
                    if not found:
                        missing.append(expected.get("attributeName"))

                if not missing:
                    testResult(self, "passed",
                               "Both expected telemetry attributes found in API response",
                               "Validation successful")
                    assert True
                else:
                    testResult(self, "failed",
                               "Some expected telemetry attributes missing in API response",
                               f"Missing attributes: {', '.join(missing)}")
                    assert False, f"Missing attributes: {', '.join(missing)}"
            else:
                testResult(self, "failed",
                           "Event header details should match expected values",
                           f"Mismatch in event details: "
                           f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                           f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
                assert False, (
                    f"Header mismatch: Expected "
                    f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                    f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
                )

    def test3_positive_telemetry_master_data_update_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Updating for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Updating second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        response = Telemetry_master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_single_attribute"
        )

        if response.status_code == 200:
            response_body = response.json()
            if response_body["message"] == "Data Updated Successfully":
                testResult(self, "passed",
                           "Telemetry Master Data - Event details should updated successfully",
                           "Telemetry Master Data - Event detail is updated successfully")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - Event detail should updated successfully",
                           "Telemetry Master Data - Event detail is not updated successfully")
                assert False
        else:
            print("Response status code is not 200. Rather then found: ", response.status_code)
            assert False

        # Fetch event details
        response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
        assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

        response_body = response.json()
        if response_body["message"] == "Data Fetched Successfully":
            telemetry_list = response_body.get("telemetryData", [])
            assert telemetry_list, "No telemetry data returned for the eventType"

            event = telemetry_list[0]
            eventType_actual = event.get("eventType")
            eventName_actual = event.get("eventName")
            eventCategory_actual = event.get("eventCategory")
            modelCode_actual = event.get("modelCode")
            actual_params = event.get("attributeList", [])

            # Validate event details
            if (str(eventType_actual) == str(eventType) and
                    str(eventName_actual) == str(eventName) and
                    str(eventCategory_actual) == str(eventCategory) and
                    str(modelCode_actual) == str(modelCode)):

                # Check only attributeList1
                expected = attributeList1
                found = any(
                    str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                    str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                    str(actual.get("elementId")) == str(expected.get("elementId")) and
                    str(actual.get("idName")) == str(expected.get("idName")) and
                    str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                    str(actual.get("description")) == str(expected.get("description")) and
                    str(actual.get("areaList", [{}])[0].get("areaId")) == str(
                        expected.get("areaList", [{}])[0].get("areaId")) and
                    str(actual.get("areaList", [{}])[0].get("areaName")) == str(
                        expected.get("areaList", [{}])[0].get("areaName"))
                    for actual in actual_params
                )

                if found:
                    testResult(self, "passed",
                               "Expected telemetry attribute found in API response",
                               "Validation successful")
                    assert True
                else:
                    testResult(self, "failed",
                               "Expected telemetry attribute missing in API response",
                               f"Missing attribute: {expected.get('attributeName')}")
                    assert False, f"Missing attribute: {expected.get('attributeName')}"
            else:
                testResult(self, "failed",
                           "Event header details should match expected values",
                           f"Mismatch in event details: "
                           f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                           f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
                assert False, (
                    f"Header mismatch: Expected "
                    f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                    f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
                )

    def test4_positive_telemetry_master_data_update_event_with_multiple_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1006"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Updating for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Updating second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        response = Telemetry_master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_multiple_attribute"
        )

        if response.status_code == 200:
            response_body = response.json()
            if response_body["message"] == "Data Updated Successfully":
                testResult(self, "passed",
                           "Telemetry Master Data - Event detail should updated successfully",
                           "Telemetry Master Data - Event detail is updated successfully")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - Event detail should updated successfully",
                           "Telemetry Master Data - Event is not updated successfully")
                assert False
        else:
            print("Response status code is not 200. Rather then found: ", response.status_code)
            assert False

        # Fetch event details
        response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
        assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

        response_body = response.json()
        if response_body["message"] == "Data Fetched Successfully":
            telemetry_list = response_body.get("telemetryData", [])
            assert telemetry_list, "No telemetry data returned for the eventType"

            event = telemetry_list[0]
            eventType_actual = event.get("eventType")
            eventName_actual = event.get("eventName")
            eventCategory_actual = event.get("eventCategory")
            modelCode_actual = event.get("modelCode")
            actual_params = event.get("attributeList", [])

            # Validate event details
            if (str(eventType_actual) == str(eventType) and
                    str(eventName_actual) == str(eventName) and
                    str(eventCategory_actual) == str(eventCategory) and
                    str(modelCode_actual) == str(modelCode)):

                # Validate both attributes
                expected_attributes = [attributeList1, attributeList2]
                missing = []

                for expected in expected_attributes:
                    found = any(
                        str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                        str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                        str(actual.get("elementId")) == str(expected.get("elementId")) and
                        str(actual.get("idName")) == str(expected.get("idName")) and
                        str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                        str(actual.get("description")) == str(expected.get("description")) and
                        str(actual.get("areaList", [{}])[0].get("areaId")) == str(
                            expected.get("areaList", [{}])[0].get("areaId")) and
                        str(actual.get("areaList", [{}])[0].get("areaName")) == str(
                            expected.get("areaList", [{}])[0].get("areaName"))
                        for actual in actual_params
                    )
                    if not found:
                        missing.append(expected.get("attributeName"))

                if not missing:
                    testResult(self, "passed",
                               "Both expected telemetry attributes found in API response",
                               "Validation successful")
                    assert True
                else:
                    testResult(self, "failed",
                               "Some expected telemetry attributes missing in API response",
                               f"Missing attributes: {', '.join(missing)}")
                    assert False, f"Missing attributes: {', '.join(missing)}"
            else:
                testResult(self, "failed",
                           "Event header details should match expected values",
                           f"Mismatch in event details: "
                           f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                           f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
                assert False, (
                    f"Header mismatch: Expected "
                    f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                    f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
                )

    def test5_positive_telemetry_master_data_delete_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        modelCode = "1234"

        print("Event Type:", eventType)
        print("Model Code:", modelCode)

        # Call API to delete event
        response = Telemetry_master_data_delete_event(self, eventType, modelCode, "valid")

        #delete 1006- adding multiple attributes
        # Call API to add event
        response1 = Telemetry_master_data_delete_event(self, "1006", modelCode, "valid")

        if response.status_code == 200:
            response_body = response.json()
            if response_body["message"] == "Data Deleted Successfully.":
                testResult(self, "passed",
                           "Telemetry Master Data - Event should deleted successfully",
                           "Telemetry Master Data - Event is deleted successfully")
                assert True
            else:
                testResult(self, "failed",
                           "Telemetry Master Data - Event should deleted successfully",
                           "Telemetry Master Data - Event is not deleted successfully")
                assert False
        else:
            print("Response status code is not 200. Rather then found: ", response.status_code)
            assert False

        # Fetch event details
        response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")

        if response.status_code == 204:
            testResult(self, "passed",
                               "After deletion there should not be any data for the event",
                               "After deletion there is no data for the event")
            assert True
        else:
            testResult(self, "failed",
                               "After deletion there should not be any data for the event",
                               "After deletion still data exist for the event in cloud")
            assert False

class Test_Master_data_api_new:

    def test1_positive_telemetry_master_data_add_new_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Adding for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute (not validated in this test)
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Adding second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_single_attribute"
        )

    def test2_positive_telemetry_master_data_add_new_event_with_multiple_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1006"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Adding for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Adding second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_multiple_attribute"
        )

    def test3_positive_telemetry_master_data_update_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Updating for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Updating second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_single_attribute"
        )

    def test4_positive_telemetry_master_data_update_event_with_multiple_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1006"
        eventName = "Test_Event"
        eventCategory = "COMPLEX"
        modelCode = "1234"
        attributeList1 = {
            "elementId": 559940097,
            "attributeName": "LATITUDE",
            "idName": "AL_LATITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Updating for one attribute testing purpose",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "areaName": "GLOBAL", "modelCode": "1234", "dataType": "FLOAT"}
            ]
        }

        # Second attribute
        attributeList2 = {
            "elementId": 559940098,
            "attributeName": "LONGITUDE",
            "idName": "AL_LONGITUDE",
            "changeMode": "CONTINUOUS",
            "description": "Testing-Updating second attribute",
            "modelCode": "1234",
            "areaList": [
                {"areaId": 0, "modelCode": "1234", "areaName": "GLOBAL", "dataType": "FLOAT"}
            ]
        }

        print("Event Type:", eventType)
        print("Event Name:", eventName)
        print("Event Category:", eventCategory)
        print("Model Code:", modelCode)
        print("Attribute 1:", attributeList1)
        print("Attribute 2:", attributeList2)

        # Call API to add event
        master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_multiple_attribute"
        )

    def test5_positive_telemetry_master_data_delete_event_with_single_attribute(self):

        print("----------------------------------------------------------")

        # Testdata
        eventType = "1005"
        modelCode = "1234"

        print("Event Type:", eventType)
        print("Model Code:", modelCode)

        # Call API to delete event
        master_data_delete_event(self, eventType, modelCode, "valid")
