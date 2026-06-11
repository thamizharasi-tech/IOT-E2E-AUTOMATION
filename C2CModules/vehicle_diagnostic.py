import ast
import json
import requests
import time
from datetime import datetime, timedelta, timezone

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel
from C2CModules.testResults import testResult
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.notifications import *


def DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_fetchDTCCodes")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{startDate}',startDate).replace('{endDate}', endDate).replace('{offset}', offset).replace('{limit}', limit).replace('{details}', details)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x)
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DTC_fetchDTCCodes",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DTC_fetchDTCCodes', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_fetchDTCCodes", response.text)

    return response

def DTC_clearDTC(self, systemId, action, timestamp, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_clearDTC")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}',action)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["timeStamp"] = timestamp
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DTC_clearDTC",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DTC_clearDTC', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_clearDTC", response.text)

    return response

def DTC_clearDTC_status(self, trackingId, systemId, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_clearDTC_status")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId).replace('{systemId}', systemId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DTC_clearDTC_status",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DTC_clearDTC_status', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_clearDTC_status", response.text)

    return response
    
def VehicleHealthReport_insertModel(self, modelId, attributeId, attributeName, areaId, thresholdHigh, thresholdLow, attributeId1, attributeName1, areaId1, thresholdHigh1, thresholdLow1, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_insertModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    if tc == "valid":
        json_object = json.loads(payload)
        json_object["modelId"] = modelId
        json_object["telemetryAttributes"][0]["attributeId"] = attributeId
        json_object["telemetryAttributes"][0]["attributeName"] = attributeName
        json_object["telemetryAttributes"][0]["areaId"] = areaId
        json_object["telemetryAttributes"][0]["thresholdHigh"] = thresholdHigh
        json_object["telemetryAttributes"][0]["thresholdLow"] = thresholdLow
        json_object["telemetryAttributes"][1]["attributeId"] = attributeId1
        json_object["telemetryAttributes"][1]["attributeName"] = attributeName1
        json_object["telemetryAttributes"][1]["areaId"] = areaId1
        json_object["telemetryAttributes"][1]["thresholdHigh"] = thresholdHigh1
        json_object["telemetryAttributes"][1]["thresholdLow"] = thresholdLow1
        payload = json_object
        print("Payload: ", payload)

    # Send POST request
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_insertModel",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_insertModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_insertModel", response.text)

    return response

def VehicleHealthReport_updateModel(self, modelId, attributeId, attributeName, areaId, thresholdHigh, thresholdLow, attributeId1, attributeName1, areaId1, thresholdHigh1, thresholdLow1, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_updateModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{model}', modelId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object[0]["attributeId"] = attributeId
    json_object[0]["attributeName"] = attributeName
    json_object[0]["areaId"] = areaId
    json_object[0]["thresholdHigh"] = thresholdHigh
    json_object[0]["thresholdLow"] = thresholdLow
    json_object[1]["attributeId"] = attributeId1
    json_object[1]["attributeName"] = attributeName1
    json_object[1]["areaId"] = areaId1
    json_object[1]["thresholdHigh"] = thresholdHigh1
    json_object[1]["thresholdLow"] = thresholdLow1
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_updateModel",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_updateModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_updateModel", response.text)

    return response

def VehicleHealthReport_generate_vehicleHealthReport(self, systemId, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_generate_vehicleHealthReport")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_generate_vehicleHealthReport",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_generate_vehicleHealthReport', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_generate_vehicleHealthReport", response.text)

    return response

def VehicleHealthReport_updateModel_new(self, modelId, attributeId, attributeName, areaId, thresholdHigh, thresholdLow, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_updateModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{model}', modelId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object[0]["attributeId"] = attributeId
    json_object[0]["attributeName"] = attributeName
    json_object[0]["areaId"] = areaId
    json_object[0]["thresholdHigh"] = thresholdHigh
    json_object[0]["thresholdLow"] = thresholdLow
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_updateModel",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_updateModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_updateModel", response.text)

    return response
    

def DTC_get_dtc_details(self, model, make, dtcCode, priority, offset, limit, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_get_dtc_details")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint)
    if "based_on_model" in tc:
       complete_url = str(base_url + endpoint) + "?model={model}".replace('{model}', model)
    elif "model_make_dtcCode_priority" in tc:
       complete_url = str(base_url + endpoint) + "?model={model}&make={make}&dtcCode={dtcCode}&priority={priority}".replace('{model}', model).replace('{make}', make).replace('{dtcCode}', dtcCode).replace('{priority}', priority)
    elif "pagination" in tc:
       complete_url = str(base_url + endpoint) + "?offset={offset}&limit={limit}".replace('{offset}', offset).replace('{limit}', limit)

    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "DTC-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DTC_get_dtc_details",
                                                "DTC-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DTC_get_dtc_details', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_get_dtc_details", response.text)

    return response

def DTC_dtcOccurence(self, offset, limit, startTime, endTime, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_Occurrence")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace('{limit}',limit)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["startTime"] = startTime
    json_object["endTime"] = endTime
    json_object["status"] = status
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DTC_Occurrence', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_Occurrence", response.text)

    return response

#-------------------------------------------------------
#Reusable Modules
#-------------------------------------------------------
def new_model_config_for_vehicle_health_report(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1):
    print("----------------------------------------------------------")
    print("Insert model for vehicle health report config")
    print("----------------------------------------------------------")

    # Call api reusable module
    response = VehicleHealthReport_insertModel(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1, "valid")

    # Parse API response into JSON
    response_body = response.json()

    if response.status_code == 200 or response.status_code == str(200):
        if response_body["message"] == "Vehicle Health Report Saved Successfully":
            testResult(self, "passed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Vehicle modelId is configured on the db to generate vehicle health report")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Vehicle Health Report Saved Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Failed to configure modelId on the db to generate vehicle health report" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
    elif response.status_code == 400 or response.status_code == str(400):
        if response_body["errors"][0]["errorCode"] == "17008" and response_body["errors"][0][
            "message"] == "model id already exist":
            testResult(self, "passed",
                       "Vehicle model should exist on db for the given model",
                       "Vehicle Model is exist on db for given model")
            # self.result.set_result(TestResults.passed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False


def update_model_config_for_vehicle_health_report(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1):
    # Call api reusable module
    response = VehicleHealthReport_updateModel(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    if response_body["message"] == "Vehicle Health Report Updated Successfully":
        testResult(self, "passed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Vehicle model configuration is updated successfully on db to generate vehicle health report")
        # self.result.set_result(TestResults.passed)
    elif response_body["message"] != "Vehicle Health Report Updated Successfully":
        # print(response_body["responseData"]["message"])
        testResult(self, "failed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Failed to update configuration on the db to generate vehicle health report" + " Reason for failure is : " +
                   response_body["responseData"]["message"])
        # self.result.set_result(TestResults.failed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False

def update_model_config_for_vehicle_health_report_new(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow):
    print("----------------------------------------------------------")
    print("Update model for vehicle health report config")
    print("----------------------------------------------------------")

    # Call api reusable module
    response = VehicleHealthReport_updateModel_new(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    if response_body["message"] == "Vehicle Health Report Updated Successfully":
        testResult(self, "passed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Vehicle model configuration is updated successfully on db to generate vehicle health report")
        # self.result.set_result(TestResults.passed)
    elif response_body["message"] != "Vehicle Health Report Updated Successfully":
        # print(response_body["responseData"]["message"])
        testResult(self, "failed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Failed to update configuration on the db to generate vehicle health report" + " Reason for failure is : " +
                   response_body["responseData"]["message"])
        # self.result.set_result(TestResults.failed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False

def generate_vehicle_health_report(self, systemId, attributeName, thresholdLow, thresholdHigh, value):
    print("----------------------------------------------------------")
    print("Generate Vehicle Health Report")
    print("----------------------------------------------------------")

    response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")

    # Validate response status code
    assert response.status_code == 200, "Status code is not 200. Rather found: " + str(response.status_code)
    if response.status_code != 200:
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    try:
        if response_body["message"] == "Vehicle Health Report Generated Successfully":
            model = response_body["responseData"]["model"]
            dateOfInspection = response_body["responseData"]["dateOfInspection"]
            kilometers = response_body["responseData"]["kilometers"]
            systemId = response_body["responseData"]["systemId"]
            reportId = response_body["responseData"]["reportId"]

            print("Model: ", model)
            print("DateOfInspection: ", dateOfInspection)
            print("Kilometers: ", kilometers)
            print("SystemId: ", systemId)
            print("Report Id: ", reportId)

            dataList_len = len(response_body["responseData"]["engineManagementSystem"])

            result = autualReading = ""

            for j in range(dataList_len):
                parameter = response_body["responseData"]["engineManagementSystem"][j]["parameter"]
                unit = response_body["responseData"]["engineManagementSystem"][j]["unit"]
                actualReading = float(response_body["responseData"]["engineManagementSystem"][j]["actualReading"])
                result = response_body["responseData"]["engineManagementSystem"][j]["result"]

                if parameter == attributeName:
                    print(f"------------------Vehicle Health Report: {attributeName}------------------")
                    print("Parameter: ", parameter)
                    print("Unit: ", unit)
                    print(f"Threshold Low: {thresholdLow}")
                    print(f"Threshold High: {thresholdHigh}")
                    print("Actual Reading: ", actualReading)
                    print("Result: ", result)
                    print("-------------------------------------------------------------")

                    try:
                        # print(f"Threshold Low: {thresholdLow} (Type: {type(thresholdLow)}, Threshold High: {thresholdHigh} (Type: {type(thresholdHigh)}, Actual Reading: {actualReading} (Type: {type(actualReading)}")
                        actualReading = float(actualReading)
                        if thresholdLow <= actualReading <= thresholdHigh:
                            if actualReading == float(value):
                                result = 'pass'
                                testResult(self, "passed",
                                           "Battery SOH level should be within the configured threshold limit",
                                           "Battery SOH level is within the configured threshold limit and matches the expected value")
                            else:
                                result = 'fail'
                                testResult(self, "failed",
                                           "Battery SOH level should be within the configured threshold limit",
                                           "Battery SOH level is within the configured range but does not match the expected value")

                        else:
                            result = 'fail'
                            testResult(self, "verificationFailed",
                                       "Battery SOH level should be within the configured threshold limit",
                                       "Battery SOH level is outside the configured threshold range")
                    except ValueError:
                        print(f"Invalid actualReading: {actualReading}")
                        result = 'fail'
                        testResult(self, "failed",
                                   "Battery SOH validation failed",
                                   "Actual reading is invalid or non-numeric")

        else:
            testResult(self, "failed",
                       "Vehicle health report should be generated successfully",
                       "Failed to generate vehicle health report. Reason for failure is: " +
                       response_body["responseData"]["message"])

    except KeyError as e:
        print(f"KeyError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

def dtc_occurrence(self, offset, limit, startTime, endTime, status, tc):

    # Call DTC reusable module
    response = DTC_dtcOccurence(self, offset, limit, startTime, endTime, status, "valid")

    # Validate response status code
    assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

    if response.status_code != 200:
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Max records will be 2 only, 1: vehicle with lower DTC occurrence, 2: vehicle with highest DTC Occurrence
    if response_body["message"] == "Data Fetched Successfully":
        dtc_len = len(response_body["dtcSystemDetails"])
        offset = response_body["offset"]
        limit = response_body["limit"]
        totalRecords = response_body["totalRecords"]
        print("Offset: ", offset)
        print("Limit: ", limit)
        print("Total Records: ", totalRecords)
        if dtc_len == 1:
            systemId = response_body["dtcSystemDetails"][0]["systemId"]
            dtc = response_body["dtcSystemDetails"][0]["dtc"]
            count = response_body["dtcSystemDetails"][0]["count"]
            definition = response_body["dtcSystemDetails"][0]["definition"]
            status_actual = response_body["dtcSystemDetails"][0]["status"]
            if status == "Unresolved" and status_actual == "Unresolved":
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            elif status == "RESOLVED" and status_actual == "RESOLVED":
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            elif status == "All" and (status_actual == "RESOLVED" or status_actual == "Unresolved" or status_actual == "unresolved"):
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            else:
                testResult(self, "failed", "DTC Occurrence details should be saved & fetched successfully",
                           "DTC Occurrence details are fetched with invalid status")
            print("----------------------------------------")
            print("SystemId: ", systemId)
            print("DTC Code: ", dtc)
            print("Count: ", count)
            print("Definition: ", definition)
            print("Status: ", status)
            print("----------------------------------------")
        elif dtc_len == 2:
            systemId1 = response_body["dtcSystemDetails"][0]["systemId"]
            dtc1 = response_body["dtcSystemDetails"][0]["dtc"]
            lowest_count = response_body["dtcSystemDetails"][0]["count"]
            definition1 = response_body["dtcSystemDetails"][0]["definition"]
            status1_actual = response_body["dtcSystemDetails"][0]["status"]
            systemId2 = response_body["dtcSystemDetails"][1]["systemId"]
            dtc2 = response_body["dtcSystemDetails"][1]["dtc"]
            highest_count = response_body["dtcSystemDetails"][1]["count"]
            definition2 = response_body["dtcSystemDetails"][1]["definition"]
            status2_actual = response_body["dtcSystemDetails"][1]["status"]
            if status == "Unresolved" and status1_actual == "Unresolved" and status2_actual == "Unresolved":
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            elif status == "RESOLVED" and status1_actual == "RESOLVED" and status2_actual == "RESOLVED":
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            elif status == "All" and ((status1_actual == "RESOLVED" and status2_actual == "RESOLVED") or (status1_actual == "Unresolved" and status1_actual == "Unresolved") or (status1_actual == "unresolved" and status1_actual == "unresolved")):
                testResult(self, "passed", f"DTC Occurrence details should be saved & fetched successfully with the status as {status}",
                           f"DTC Occurrence details are saved & fetched successfully with the status as {status}")
            else:
                testResult(self, "failed", "DTC Occurrence details should be saved & fetched successfully",
                           "DTC Occurrence details are fetched with invalid status")
            print("----------------------------------------")
            print("SystemId-1: ", systemId1)
            print("DTC Code-1: ", dtc1)
            print("Lowest Count: ", lowest_count)
            print("Definition-1: ", definition1)
            print("Status-1: ", status1_actual)
            print("SystemId-2: ", systemId2)
            print("DTC Code-2: ", dtc2)
            print("Highest Count: ", highest_count)
            print("Definition-2: ", definition2)
            print("Status-2: ", status2_actual)
            print("----------------------------------------")
        else:
            print("No DTC record exists in cloud DB")
            assert False
            # self.result.set_result(TestResults.passed)

    elif response_body["message"] != "Data Fetched Successfully":
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "DTC Occurrence details should be saved & fetched successfully",
                   "Failed to save/fetch the dtc details " + " Reason for failure is : " +
                   response_body)
        assert False
        # self.result.set_result(TestResults.failed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False
    print("\n------------------------------END------------------------------\n")

def VehicleHealthReport_insertModel_v2(self, modelId, attributeId, eventType, attributeName, areaId, thresholdHigh, thresholdLow, attributeId1, eventType1, attributeName1, areaId1, thresholdHigh1, thresholdLow1, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_insertModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    if tc == "valid":
        json_object = json.loads(payload)
        json_object["modelId"] = modelId
        json_object["telemetryAttributes"][0]["attributeId"] = attributeId
        json_object["telemetryAttributes"][0]["eventType"] = eventType
        json_object["telemetryAttributes"][0]["attributeName"] = attributeName
        json_object["telemetryAttributes"][0]["areaId"] = areaId
        json_object["telemetryAttributes"][0]["thresholdHigh"] = thresholdHigh
        json_object["telemetryAttributes"][0]["thresholdLow"] = thresholdLow
        json_object["telemetryAttributes"][1]["attributeId"] = attributeId1
        json_object["telemetryAttributes"][1]["eventType"] = eventType1
        json_object["telemetryAttributes"][1]["attributeName"] = attributeName1
        json_object["telemetryAttributes"][1]["areaId"] = areaId1
        json_object["telemetryAttributes"][1]["thresholdHigh"] = thresholdHigh1
        json_object["telemetryAttributes"][1]["thresholdLow"] = thresholdLow1
        payload = json_object
        print("Payload: ", payload)

    # Send POST request
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_insertModel",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_insertModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_insertModel", response.text)

    return response

def VehicleHealthReport_updateModel_v2(self, modelId, attributeId, eventType, attributeName, areaId, thresholdHigh, thresholdLow, attributeId1, eventType1, attributeName1, areaId1, thresholdHigh1, thresholdLow1, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleHealthReport_updateModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{model}', modelId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object[0]["attributeId"] = attributeId
    json_object[0]["eventType"] = eventType
    json_object[0]["attributeName"] = attributeName
    json_object[0]["areaId"] = areaId
    json_object[0]["thresholdHigh"] = thresholdHigh
    json_object[0]["thresholdLow"] = thresholdLow
    json_object[1]["attributeId"] = attributeId1
    json_object[1]["eventType"] = eventType1
    json_object[1]["attributeName"] = attributeName1
    json_object[1]["areaId"] = areaId1
    json_object[1]["thresholdHigh"] = thresholdHigh1
    json_object[1]["thresholdLow"] = thresholdLow1
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "VehicleHealthReport_updateModel",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('VehicleHealthReport_updateModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleHealthReport_updateModel", response.text)

    return response


#vehicle health report new module
def new_model_config_for_vehicle_health_report(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1):
    print("----------------------------------------------------------")
    print("Insert model for vehicle health report config")
    print("----------------------------------------------------------")

    # Call api reusable module
    response = VehicleHealthReport_insertModel(self, modelId, attributeId,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1, "valid")

    # Parse API response into JSON
    response_body = response.json()

    if response.status_code == 200 or response.status_code == str(200):
        if response_body["message"] == "Vehicle Health Report Saved Successfully":
            testResult(self, "passed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Vehicle modelId is configured on the db to generate vehicle health report")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Vehicle Health Report Saved Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Failed to configure modelId on the db to generate vehicle health report" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
    elif response.status_code == 400 or response.status_code == str(400):
        if response_body["errors"][0]["errorCode"] == "17008" and response_body["errors"][0][
            "message"] == "model id already exist":
            testResult(self, "passed",
                       "Vehicle model should exist on db for the given model",
                       "Vehicle Model is exist on db for given model")
            # self.result.set_result(TestResults.passed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False

def generate_vehicle_health_report_v2(self, systemId, attributeName, thresholdLow, thresholdHigh, value):
    print("----------------------------------------------------------")
    print("Generate Vehicle Health Report")
    print("----------------------------------------------------------")

    response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")

    # Validate response status code
    assert response.status_code == 200, "Status code is not 200. Rather found: " + str(response.status_code)
    if response.status_code != 200:
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    try:
        if response_body["message"] == "Vehicle Health Report Generated Successfully":
            model = response_body["vehicleHealthReport"]["model"]
            dateOfInspection = response_body["vehicleHealthReport"]["dateOfInspection"]
            kilometers = response_body["vehicleHealthReport"]["kilometers"]
            systemId = response_body["vehicleHealthReport"]["systemId"]
            reportId = response_body["vehicleHealthReport"]["reportId"]

            print("Model: ", model)
            print("DateOfInspection: ", dateOfInspection)
            print("Kilometers: ", kilometers)
            print("SystemId: ", systemId)
            print("Report Id: ", reportId)

            dataList_len = len(response_body["vehicleHealthReport"]["vehicleHealthStatus"])

            result = autualReading = ""

            for j in range(dataList_len):
                parameter = response_body["vehicleHealthReport"]["vehicleHealthStatus"][j]["parameter"]
                unit = response_body["vehicleHealthReport"]["vehicleHealthStatus"][j]["unit"]
                actualReading = float(response_body["vehicleHealthReport"]["vehicleHealthStatus"][j]["actualReading"])
                result = response_body["vehicleHealthReport"]["vehicleHealthStatus"][j]["result"]

                if parameter == attributeName:
                    print(f"------------------Vehicle Health Report: {attributeName}------------------")
                    print("Parameter: ", parameter)
                    print("Unit: ", unit)
                    print(f"Threshold Low: {thresholdLow}")
                    print(f"Threshold High: {thresholdHigh}")
                    print("Actual Reading: ", actualReading)
                    print("Result: ", result)
                    print("-------------------------------------------------------------")

                    try:
                        # print(f"Threshold Low: {thresholdLow} (Type: {type(thresholdLow)}, Threshold High: {thresholdHigh} (Type: {type(thresholdHigh)}, Actual Reading: {actualReading} (Type: {type(actualReading)}")
                        actualReading = float(actualReading)
                        if thresholdLow <= actualReading <= thresholdHigh:
                            if actualReading == float(value):
                                result = 'pass'
                                testResult(self, "passed",
                                           "Battery SOH level should be within the configured threshold limit",
                                           "Battery SOH level is within the configured threshold limit and matches the expected value")
                            else:
                                result = 'fail'
                                testResult(self, "failed",
                                           "Battery SOH level should be within the configured threshold limit",
                                           "Battery SOH level is within the configured range but does not match the expected value")

                        else:
                            result = 'fail'
                            testResult(self, "verificationFailed",
                                       "Battery SOH level should be within the configured threshold limit",
                                       "Battery SOH level is outside the configured threshold range")
                    except ValueError:
                        print(f"Invalid actualReading: {actualReading}")
                        result = 'fail'
                        testResult(self, "failed",
                                   "Battery SOH validation failed",
                                   "Actual reading is invalid or non-numeric")

        else:
            testResult(self, "failed",
                       "Vehicle health report should be generated successfully",
                       "Failed to generate vehicle health report. Reason for failure is: " +
                       response_body["responseData"]["message"])

    except KeyError as e:
        print(f"KeyError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

def new_model_config_for_vehicle_health_report_v2(self, modelId, attributeId,eventType,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1,eventType1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1):
    print("----------------------------------------------------------")
    print("Insert model for vehicle health report config")
    print("----------------------------------------------------------")

    # Call api reusable module
    response = VehicleHealthReport_insertModel_v2(self, modelId, attributeId, eventType,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1, eventType1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1, "valid")

    # Parse API response into JSON
    response_body = response.json()

    if response.status_code == 200 or response.status_code == str(200):
        if response_body["message"] == "Vehicle Health Report Saved Successfully":
            testResult(self, "passed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Vehicle modelId is configured on the db to generate vehicle health report")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Vehicle Health Report Saved Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed",
                       "Vehicle modelId should configured on the db to generate vehicle health report",
                       "Failed to configure modelId on the db to generate vehicle health report" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
    elif response.status_code == 400 or response.status_code == str(400):
        if response_body["errors"][0]["errorCode"] == "17008" and response_body["errors"][0][
            "message"] == "model id already exist":
            testResult(self, "passed",
                       "Vehicle model should exist on db for the given model",
                       "Vehicle Model is exist on db for given model")
            # self.result.set_result(TestResults.passed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False

def update_model_config_for_vehicle_health_report_v2(self, modelId, attributeId, eventType,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1, eventType1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1):
    # Call api reusable module
    response = VehicleHealthReport_updateModel_v2(self, modelId, attributeId, eventType,
                                               attributeName, areaId, thresholdHigh,
                                               thresholdLow, attributeId1, eventType1,
                                               attributeName1, areaId1, thresholdHigh1,
                                               thresholdLow1, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    if response_body["message"] == "Vehicle Health Report Updated Successfully":
        testResult(self, "passed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Vehicle model configuration is updated successfully on db to generate vehicle health report")
        # self.result.set_result(TestResults.passed)
    elif response_body["message"] != "Vehicle Health Report Updated Successfully":
        # print(response_body["responseData"]["message"])
        testResult(self, "failed",
                   "Vehicle model configuration should be updated successfully on db to generate vehicle health report",
                   "Failed to update configuration on the db to generate vehicle health report" + " Reason for failure is : " +
                   response_body["responseData"]["message"])
        # self.result.set_result(TestResults.failed)
    else:
        print("Something went wrong")
        # self.result.set_result(TestResults.failed)
        assert False


def generate_vehicle_health_report_v3(self, systemId, attributeName,
                                      thresholdLow, thresholdHigh, value,
                                      ignitionLowThreshold, ignitionHighThreshold, ignition_value):
    print("----------------------------------------------------------")
    print("Generate Vehicle Health Report")
    print("----------------------------------------------------------")

    response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
    assert response.status_code == 200, "Status code is not 200. Found: " + str(response.status_code)

    response_body = response.json()

    try:
        if response_body["message"] == "Vehicle Health Report Generated Successfully":
            report = response_body["vehicleHealthReport"]
            model = report["model"]
            dateOfInspection = report["dateOfInspection"]
            kilometers = report["kilometers"]
            systemId = report["systemId"]
            reportId = report["reportId"]
            ignitionStatus = report["ignitionStatus"]
            activeDTCs = report["activeDTCs"]
            vehicleStatus = report["vehicleStatus"]
            healthStatusList = report["vehicleHealthStatus"]

            print("Report Details:")
            print(f"-> Model               : {model}")
            print(f"-> Date of Inspection  : {dateOfInspection}")
            print(f"-> Kilometers          : {kilometers}")
            print(f"-> System ID           : {systemId}")
            print(f"-> Report ID           : {reportId}")
            print(f"-> Ignition Status     : {ignitionStatus}")
            print(f"-> Active DTCs         : {activeDTCs}")
            print(f"-> Vehicle Status      : {vehicleStatus}")
            print("----------------------------------------------------------")

            telemetry_results = []
            for item in healthStatusList:
                if item["parameter"] != attributeName:
                    continue

                parameter = item["parameter"]
                unit = item["unit"]
                actualReading = item["actualReading"]
                result = item["result"]
                eventType = item["eventType"]

                telemetry_results.append(result)

                print(f"\nValidating: {attributeName}")
                print("-------------------------------------------------------------")
                print(f"-> Parameter        : {parameter}")
                print(f"-> Unit             : {unit}")
                print(f"-> Threshold Low    : {thresholdLow}")
                print(f"-> Threshold High   : {thresholdHigh}")
                print(f"-> Actual Reading   : {actualReading}")
                print(f"-> Telemetry Result : {result}")
                print(f"-> Event Type             : {eventType}")
                print("-------------------------------------------------------------")

                # Validate DTC Status
                print("\nDTC Status Validation")
                startDate = datetime.now() - timedelta(days=1)
                endDate = datetime.now() + timedelta(days=1)

                startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
                endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")
                offset = "0"
                limit = "10"
                details = "true"
                # Read systemId
                systemId = read_vehicleJsonFile(self, "system_id")

                print("startDate: ", startDate)
                print("endDate: ", endDate)
                print("offset: ", offset)
                print("limit: ", limit)
                print("details: ", details)
                print("systemId: ", systemId)

                # Call DTC reusable module

                response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

                # Validate response status code

                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                if response.status_code != 200:
                    # self.result.set_result(TestResults.failed)

                    assert False

                # Parse API response into JSON
                response_body = response.json()

                # Validate response body
                if response_body["message"] == "Data Saved Successfully":
                    dtc_list = response_body["responseData"]["DTCs"]
                    dtc_len = len(dtc_list)

                    if dtc_len >= 1:
                        for dtc in dtc_list:
                            status = dtc["status"]
                            expected_active = status == "RESOLVED"

                            if not activeDTCs == expected_active:
                                testResult(self, "passed",
                                           "DTC status matches telemetry result",
                                           f"Status: {status}, activeDTCs: {activeDTCs}")
                                assert True
                            else:
                                testResult(self, "failed",
                                           "DTC status mismatch with telemetry result",
                                           f"Status: {status}, activeDTCs: {activeDTCs}")
                                assert False
                    else:
                        print("No DTC record exists in cloud DB")
                        assert False

                    print("----------------------------------------------------------")

                # Validate Ignition Status
                print("\nIgnition Status Validation")
                expected_ignition_status = "Off" if ignitionLowThreshold <= int(ignition_value) <= ignitionHighThreshold else "On"
                print(f"-> Ignition Value        : {ignition_value}")
                print(f"-> Expected Ignition     : {expected_ignition_status}")
                print(f"-> Actual Ignition Status: {ignitionStatus}")
                if expected_ignition_status == ignitionStatus:
                    testResult(self, "passed",
                               "Ignition status should be match expected",
                               "Ignition status is matching with expected")
                    assert True
                else:
                    testResult(self, "verificationFailed", "Ignition status should be match expected", "Ignition status is not matching with expected")
                    assert False

                # Compute Expected Vehicle Status
                if activeDTCs:
                    expected_vehicle_status = "BAD"
                elif any(res == "fail" for res in telemetry_results):
                    expected_vehicle_status = "BAD"
                elif all(res == "pass" for res in telemetry_results) and not activeDTCs:
                    expected_vehicle_status = "GOOD"
                else:
                    expected_vehicle_status = "UNKNOWN"

                actual_vehicle_status = vehicleStatus.upper()

                # Validate Overall Vehicle Status
                print("\n Vehicle Status Evaluation")
                print(f"-> Expected Status : {expected_vehicle_status}")
                print(f"-> Reported Status : {actual_vehicle_status}")
                if expected_vehicle_status == actual_vehicle_status:
                    testResult(self, "passed",
                               "Overall status should correctly reflects vehicle health status",
                               "Overall status is correctly reflects vehicle health status")
                    assert True
                else:
                    testResult(self, "failed",
                               "Overall status should correctly reflects vehicle health status",
                               "Overall status is not correctly reflects vehicle health status")
                    #assert False

                # Validate Reading Value Against Thresholds
                print(f"\nTelemetry {attributeName} Value Validation")
                try:
                    print(f"actualReading: {actualReading}")
                    print(f"thresholdLow: {thresholdLow}")
                    print(f"thresholdHigh: {thresholdHigh}")
                    print(f"expected_value: {value}")


                    actualReading = float(actualReading)

                    # Main validation logic
                    if thresholdLow <= actualReading <= thresholdHigh:
                        if actualReading == float(value):
                            testResult(self, "passed",
                                       f"{attributeName} Reading should be within threshold and matches expected value.",
                                       f"{attributeName} Reading is within threshold and matches expected value.")
                            assert True
                        else:
                            testResult(self, "failed",
                                       f"{attributeName} Reading should be within threshold and matches expected value.",
                                       f"{attributeName} Reading is in threshold range but does not match expected value.")
                            assert False
                    else:
                        testResult(self, "passed",
                                   f"{attributeName} Reading should be within threshold and matches expected value.",
                                   f"{attributeName} Reading is outside acceptable threshold range.")
                        assert True

                except (ValueError, AttributeError, TypeError) as e:
                    testResult(self, "failed",
                               f"{attributeName} Reading should be within threshold and matches expected value.",
                               f"{attributeName} Actual reading is not a valid numeric value. Error: {e}")
                    assert False

                print("\nCompleted Validation for:", attributeName)
                print("=============================================================")

        else:
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))

    except KeyError as e:
        print(f"KeyError: Missing expected field — {e}")
    except ValueError as e:
        print(f"ValueError: Invalid data type — {e}")

def generate_vehicle_health_report_v4(self, systemId, attributeName,
                                      thresholdLow, thresholdHigh, value,
                                      ignitionLowThreshold, ignitionHighThreshold, ignition_value):
    print("----------------------------------------------------------")
    print("Generate Vehicle Health Report")
    print("----------------------------------------------------------")

    response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
    assert response.status_code == 200, "Status code is not 200. Found: " + str(response.status_code)

    response_body = response.json()

    try:
        if response_body["message"] == "Vehicle Health Report Generated Successfully":
            report = response_body["vehicleHealthReport"]
            model = report["model"]
            dateOfInspection = report["dateOfInspection"]
            kilometers = report["kilometers"]
            systemId = report["systemId"]
            reportId = report["reportId"]
            ignitionStatus = report["ignitionStatus"]
            activeDTCs = report["activeDTCs"]
            vehicleStatus = report["vehicleStatus"]
            healthStatusList = report["vehicleHealthStatus"]

            print("Report Details:")
            print(f"-> Model               : {model}")
            print(f"-> Date of Inspection  : {dateOfInspection}")
            print(f"-> Kilometers          : {kilometers}")
            print(f"-> System ID           : {systemId}")
            print(f"-> Report ID           : {reportId}")
            print(f"-> Ignition Status     : {ignitionStatus}")
            print(f"-> Active DTCs         : {activeDTCs}")
            print(f"-> Vehicle Status      : {vehicleStatus}")
            print("----------------------------------------------------------")

            telemetry_results = []
            for item in healthStatusList:
                if item["parameter"] != attributeName:
                    continue

                parameter = item["parameter"]
                unit = item["unit"]
                actualReading = item["actualReading"]
                result = item["result"]
                eventType = item["eventType"]

                telemetry_results.append(result)

                print(f"\nValidating: {attributeName}")
                print("-------------------------------------------------------------")
                print(f"-> Parameter        : {parameter}")
                print(f"-> Unit             : {unit}")
                print(f"-> Threshold Low    : {thresholdLow}")
                print(f"-> Threshold High   : {thresholdHigh}")
                print(f"-> Actual Reading   : {actualReading}")
                print(f"-> Telemetry Result : {result}")
                print(f"-> Event Type             : {eventType}")
                print("-------------------------------------------------------------")

                # Validate DTC Status
                print("\nDTC Status Validation")
                startDate = datetime.now() - timedelta(days=1)
                endDate = datetime.now() + timedelta(days=1)

                startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
                endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")
                offset = "0"
                limit = "10"
                details = "true"
                # Read systemId
                systemId = read_vehicleJsonFile(self, "system_id")

                print("startDate: ", startDate)
                print("endDate: ", endDate)
                print("offset: ", offset)
                print("limit: ", limit)
                print("details: ", details)
                print("systemId: ", systemId)

                # Call DTC reusable module

                response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

                # Validate response status code

                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                if response.status_code != 200:
                    # self.result.set_result(TestResults.failed)

                    assert False

                # Parse API response into JSON
                response_body = response.json()

                # Validate response body
                if response_body["message"] == "Data Saved Successfully":
                    dtc_list = response_body["responseData"]["DTCs"]
                    dtc_len = len(dtc_list)

                    if dtc_len >= 1:
                        for dtc in dtc_list:
                            status = dtc["status"]
                            expected_active = status == "RESOLVED"

                            if not activeDTCs == expected_active:
                                testResult(self, "passed",
                                           "DTC status matches telemetry result",
                                           f"Status: {status}, activeDTCs: {activeDTCs}")
                                assert True
                            else:
                                testResult(self, "failed",
                                           "DTC status mismatch with telemetry result",
                                           f"Status: {status}, activeDTCs: {activeDTCs}")
                                assert False
                    else:
                        print("No DTC record exists in cloud DB")
                        assert False

                    print("----------------------------------------------------------")

                # Validate Ignition Status
                print("\nIgnition Status Validation")
                expected_ignition_status = "Off" if ignitionLowThreshold <= int(ignition_value) <= ignitionHighThreshold else "On"
                print(f"-> Ignition Value        : {ignition_value}")
                print(f"-> Expected Ignition     : {expected_ignition_status}")
                print(f"-> Actual Ignition Status: {ignitionStatus}")
                if expected_ignition_status == ignitionStatus:
                    testResult(self, "passed",
                               "Ignition status should be match expected",
                               "Ignition status is matching with expected")
                    assert True
                else:
                    testResult(self, "verificationFailed", "Ignition status should be match expected", "Ignition status is not matching with expected")
                    assert False

                # Compute Expected Vehicle Status
                if activeDTCs:
                    expected_vehicle_status = "BAD"
                elif any(res == "fail" for res in telemetry_results):
                    expected_vehicle_status = "BAD"
                elif all(res == "pass" for res in telemetry_results) and not activeDTCs:
                    expected_vehicle_status = "GOOD"
                else:
                    expected_vehicle_status = "UNKNOWN"

                actual_vehicle_status = vehicleStatus.upper()

                # Validate Overall Vehicle Status
                print("\n Vehicle Status Evaluation")
                print(f"-> Expected Status : {expected_vehicle_status}")
                print(f"-> Reported Status : {actual_vehicle_status}")
                if expected_vehicle_status == actual_vehicle_status:
                    testResult(self, "passed",
                               "Overall status should correctly reflects vehicle health status",
                               "Overall status is correctly reflects vehicle health status")
                    assert True
                else:
                    testResult(self, "failed",
                               "Overall status should correctly reflects vehicle health status",
                               "Overall status is not correctly reflects vehicle health status")
                    #assert False

                # Validate Reading Value Against Thresholds
                print(f"\nTelemetry {attributeName} Value Validation")
                try:
                    print(f"actualReading: {actualReading}")
                    print(f"thresholdLow: {thresholdLow}")
                    print(f"thresholdHigh: {thresholdHigh}")
                    print(f"expected_value: {value}")


                    actualReading = float(actualReading)

                    # Main validation logic
                    if thresholdLow <= actualReading <= thresholdHigh:
                        if actualReading == float(value):
                            testResult(self, "passed",
                                       f"{attributeName} Reading should be within threshold and matches expected value.",
                                       f"{attributeName} Reading is within threshold and matches expected value.")
                            assert True
                        else:
                            testResult(self, "failed",
                                       f"{attributeName} Reading should be within threshold and matches expected value.",
                                       f"{attributeName} Reading is in threshold range but does not match expected value.")
                            assert False
                    else:
                        testResult(self, "passed",
                                   f"{attributeName} Reading should be within threshold and matches expected value.",
                                   f"{attributeName} Reading is outside acceptable threshold range.")
                        assert True

                except (ValueError, AttributeError, TypeError) as e:
                    testResult(self, "failed",
                               f"{attributeName} Reading should be within threshold and matches expected value.",
                               f"{attributeName} Actual reading is not a valid numeric value. Error: {e}")
                    assert False

                print("\nCompleted Validation for:", attributeName)
                print("=============================================================")

        else:
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))

    except KeyError as e:
        print(f"KeyError: Missing expected field — {e}")
    except ValueError as e:
        print(f"ValueError: Invalid data type — {e}")


def generate_vehicle_health_report_v5(
    self, systemId, attributeName,
    thresholdLow, thresholdHigh, value,
    ignitionLowThreshold, ignitionHighThreshold, ignition_value
):
    print("----------------------------------------------------------")
    print("Generate Vehicle Health Report")
    print("----------------------------------------------------------")

    # Fetch Vehicle Health Report
    response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
    assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

    response_body = response.json()

    if response_body.get("message") != "Vehicle Health Report Generated Successfully":
        print("Vehicle health report was not generated successfully.")
        print("Reason:", response_body.get("message", "Unknown error"))
        return

    try:
        report = response_body["vehicleHealthReport"]
        model = report.get("model")
        dateOfInspection = report.get("dateOfInspection")
        kilometers = report.get("kilometers")
        ignitionStatus = report.get("ignitionStatus")
        activeDTCs = report.get("activeDTCs")
        actual_vehicle_status = report.get("vehicleStatus")
        healthStatusList = report.get("vehicleHealthStatus", [])

        # Print Report Details
        print("Report Details:")
        print(f"-> Model              : {model}")
        print(f"-> Date of Inspection : {dateOfInspection}")
        print(f"-> Kilometers         : {kilometers}")
        print(f"-> System ID          : {systemId}")
        print(f"-> Report ID          : {report.get('reportId')}")
        print(f"-> Ignition Status    : {ignitionStatus}")
        print(f"-> Active DTCs        : {activeDTCs}")
        print(f"-> Vehicle Status     : {actual_vehicle_status}")
        print("----------------------------------------------------------")

        # Validate Telemetry Parameter
        for item in healthStatusList:
            if item.get("parameter") != attributeName:
                continue

            parameter = item.get("parameter")
            unit = item.get("unit")
            actualReading = item.get("actualReading")
            result = item.get("result")
            eventType = item.get("eventType")

            print(f"\nValidating: {attributeName}")
            print("-------------------------------------------------------------")
            print(f"-> Parameter        : {parameter}")
            print(f"-> Unit             : {unit}")
            print(f"-> Threshold Low    : {thresholdLow}")
            print(f"-> Threshold High   : {thresholdHigh}")
            print(f"-> Actual Reading   : {actualReading}")
            print(f"-> Telemetry Result : {result}")
            print(f"-> Event Type       : {eventType}")
            print("-------------------------------------------------------------")

            # 1. Ignition Status Validation
            expected_ignition_status = "Off" if ignitionLowThreshold <= int(ignition_value) <= ignitionHighThreshold else "On"
            print("\n1. Ignition Status Validation")
            print(f"-> Ignition Value        : {ignition_value}")
            print(f"-> Expected Ignition     : {expected_ignition_status}")
            print(f"-> Actual Ignition Status: {ignitionStatus}")

            if expected_ignition_status == ignitionStatus:
                testResult(self, "passed", "Ignition status should match expected", "Ignition status matches expected")
            else:
                testResult(self, "verificationFailed", "Ignition status should match expected", "Ignition status does not match expected")
                assert False

            # 2. Telemetry Value Validation
            print(f"\n2. Telemetry {attributeName} Value Validation")
            try:
                actualReading = float(actualReading)
                if thresholdLow <= actualReading <= thresholdHigh:
                    if actualReading == float(value):
                        testResult(self, "passed",
                                   f"{attributeName} Reading within threshold and matches expected value.",
                                   f"{attributeName} Reading is correct.")
                    else:
                        testResult(self, "failed",
                                   f"{attributeName} Reading should match expected value.",
                                   f"{attributeName} Reading is in range but does not match expected value.")
                        assert False
                else:
                    testResult(self, "passed",
                               f"{attributeName} Reading should be within threshold.",
                               f"{attributeName} Reading is outside acceptable range.")
                    assert True
            except (ValueError, TypeError) as e:
                testResult(self, "failed",
                           f"{attributeName} Reading should be numeric.",
                           f"Invalid reading. Error: {e}")
                assert False

            # Read systemId
            systemId = read_vehicleJsonFile(self, "system_id")

            startDate = datetime.now() - timedelta(days=1)
            endDate = datetime.now() + timedelta(days=1)

            startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
            endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

            offset = "0"
            limit = "10"
            details = "true"

            print("Start Date : ", startDate)
            print("End Date : ", endDate)
            print("----------------------------------------------------------")

            # Call DTC reusable module
            response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

            if response.status_code == 200:
                # Parse API response into JSON
                response_body = response.json()

                # Validate response body
                # issuedTime = ""
                dtc_priority = None

                if response_body["message"] == "Data Saved Successfully":
                    dtc_len = len(response_body["responseData"]["DTCs"])

                    if dtc_len >= 1:
                        for i in range(dtc_len):
                            status = response_body["responseData"]["DTCs"][i]["status"]
                            if status == 'Unresolved':
                                dtc_priority = response_body["responseData"]["DTCs"][i]["priority"]
                                # issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]
                                break

                        print('DTC Priority : ', dtc_priority)
                    print("----------------------------------------------------------")

                    testResult(self, "passed", "DTC Alert details should be saved & fetched successfully",
                               "DTC Alert details are saved & fetched successfully ")
                    # self.result.set_result(TestResults.passed)

                elif response_body["message"] != "Data Saved Successfully":
                    testResult(self, "failed", "DTC Alert details should be saved & fetched successfully",
                               "Failed to save/fetch the dtc details. Reason for failure: " + str(response_body))
                    assert False
                    # self.result.set_result(TestResults.failed)

                else:
                    print("Something went wrong")
                    # self.result.set_result(TestResults.failed)
                    assert False
            elif response.status_code == 204:
                assert True
                print("There is no DTC stored in db for the given systemId")
            else:
                # self.result.set_result(TestResults.failed)
                print("Response status code is not 200, 204. Rather than found: ", response.status_code)
                assert False

            print("----------------------------------------------------------")

        # Compute Expected Vehicle Status
        if activeDTCs == 0 or dtc_priority == 3:
            expected_vehicle_status = "Good"
        elif activeDTCs == 1 and dtc_priority in [1, 2]:
            expected_vehicle_status = "Warning"
        elif activeDTCs == 1 and dtc_priority == 0:
            expected_vehicle_status = "Critical"

        # Validate Overall Vehicle Status
        print("\nVehicle Status Evaluation")
        print(f"-> Expected Status : {expected_vehicle_status}")
        print(f"-> Reported Status : {actual_vehicle_status}")

        if expected_vehicle_status == actual_vehicle_status:
            testResult(self, "passed", "Overall status should reflect vehicle health", "Overall status matches expected")
        else:
            testResult(self, "failed", "Overall status should reflect vehicle health", "Overall status does not match expected")

        print("\nCompleted Validation for:", attributeName)
        print("=============================================================")

    except KeyError as e:
        print(f"KeyError: Missing expected field — {e}")
    except ValueError as e:
        print(f"ValueError: Invalid data type — {e}")


def dtc_clear(self, onboardingType, chipsetType):

    print("----------------------------------------------------------")

    utc_time = datetime.now()

    dt = utc_time.strftime("%Y-%m-%d_%H_%M")

    dt1 = utc_time.strftime("%Y-%m-%d_%H")

    print("Current date & time :", dt)

    # Read systemId
    systemId = read_vehicleJsonFile(self, "system_id")

    startDate = datetime.now() - timedelta(days=1)

    endDate = datetime.now() + timedelta(days=1)

    startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")

    endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

    offset = "0"
    limit = "10"
    details = "true"

    print("Start Date : ", startDate)

    print("End Date : ", endDate)

    print("----------------------------------------------------------")

    # Call DTC reusable module

    response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

    # Validate response status code

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    if response.status_code != 200:
        #self.result.set_result(TestResults.failed)

        assert False

    # Parse API response into JSON

    response_body = response.json()

    # Validate response body

    issuedTime = ""

    if response_body["message"] == "Data Saved Successfully":

        dtc_len = len(response_body["responseData"]["DTCs"])

        if dtc_len >= 1:

            for i in range(dtc_len):

                status = response_body["responseData"]["DTCs"][i]["status"]

                if status == 'Unresolved':
                    issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]

                    break

        print("----------------------------------------------------------")

        print('DTC Issued Time : ', issuedTime)

        print("----------------------------------------------------------")

        # print('Message : ', message)

        testResult(self, "passed", "DTC Alert details should be saved & fetched successfully",

                   "DTC Alert details are saved & fetched successfully ")

        #self.result.set_result(TestResults.passed)

    elif response_body["message"] != "Data Saved Successfully":

        # print(response_body["responseData"]["message"])

        testResult(self, "failed", "DTC Alert details should be saved & fetched successfully",

                   "Failed to save/fetch the dtc details " + " Reason for failure is : " +

                   response_body)

        assert False

        #self.result.set_result(TestResults.failed)

    else:

        print("Something went wrong")

        #self.result.set_result(TestResults.failed)

        assert False

    print("----------------------------------------------------------")

    # ===========================================================================================
    # Run tub on device for TOW AWAY ALERT
    # ===========================================================================================
    print("----------------------------------------------------------")
    print("Run stub on device : ")

    run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
    time.sleep(15)

    action = "CLEAR"

    # Call DTC clear reusable module

    response = DTC_clearDTC(self, systemId, action, issuedTime, "valid")

    # Validate response status code

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    if response.status_code != 200:
        #self.result.set_result(TestResults.failed)

        assert False

    # Parse API response into JSON

    response_body = response.json()

    # Validate response body

    if response_body["message"] == "DTC clear message sent successfully":

        tracking_id = response_body["responseData"]["tracking_id"]

        # message = response_body["responseData"]["message"]

        print("----------------------------------------------------------")

        print('DTC Clear - Tracking Id : ', tracking_id)

        print("----------------------------------------------------------")

        # print('Message : ', message)

        testResult(self, "passed", "DTC Clear message should be sent with tracking Id successfully ",

                   "DTC Clear message is sent with tracking Id successfully  ")

        #self.result.set_result(TestResults.passed)

    elif response_body["message"] != "DTC clear message sent successfully":

        # print(response_body["responseData"]["message"])

        testResult(self, "failed", "DTC Clear message should be sent with tracking Id successfully ",

                   "Failed to send DTC clear msg " + " Reason for failure is : " +

                   response_body)

        assert False

        #self.result.set_result(TestResults.failed)

    else:

        print("Something went wrong")

        #self.result.set_result(TestResults.failed)

        assert False

    print("-----------------------------")
    print("Device Side Validations : ")
    print("-----------------------------")

    # ===========================================================================================
    # Pull logs for validations
    # ===========================================================================================
    print("Pull/Fetch device logs for validation : ")

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    print("Logs are fetched from device to host machine @ desired location ")
    print("----------------------------------------------------------")

    # Verify whether the DTC Clear req is sent from cloud to device post triggering DTC Clear API
    # Verify DTC Clear msgs & type code in fetched device logs
    ls = verify_message_in_log(self, dtcClr_req_msg_type_code,
                               dtcClr_req_msg_type_code)
    print(ls)

    if dtcClr_req_msg_type_code in str(ls[0]):
        print(f"DTC Clear request sent from cloud' {dtcClr_req_msg_type_code} ' ")
        testResult(self, "verificationPassed", "DTC Clear request message should send to device from cloud",

                   "DTC Clear request has been received successfully from the cloud")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(
            "DTC Clear request is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
        testResult(self, "verificationFailed", "DTC Clear request message should send to device from cloud",

                   "DTC Clear request is not received from the cloud")

    print("----------------------------------------------------------")
    # time.sleep(90)

    # Verify whether the DTC Clear res is sent from device to cloud
    # Verify DTC Clear msgs & type code in fetched device logs
    ls = verify_message_in_log(self, dtcClr_res_msg_type_code,
                               dtcClr_res_msg_type_code)
    print(ls)

    if dtcClr_res_msg_type_code in str(ls[0]):
        print(f"DTC Clear response sent to cloud' {dtcClr_res_msg_type_code} ' ")
        testResult(self, "verificationPassed", "DTC Clear response message should send to cloud from device",

                   "DTC Clear response has been sent successfully to the cloud")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(
            "DTC Clear response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
        testResult(self, "verificationFailed", "DTC Clear response message should send to device from cloud",

                   "DTC Clear response is not received from the cloud")

    print("----------------------------------------------------------")

    print("----------------------------------------------------------")

    for i in range(5):

        # Call DTC clear reusable module

        response = DTC_clearDTC_status(self, tracking_id, systemId, "valid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        if response_body["message"] == "Data Fetched Successfully":

            status = response_body["dtcClearResponse"]["status"]

            if status == "RESOLVED":

                break

            else:

                time.sleep(15)

    if response_body["message"] == "Data Fetched Successfully":

        status = response_body["dtcClearResponse"]["status"]

        # message = response_body["responseData"]["message"]

        print("----------------------------------------------------------")

        print('DTC Clear - Status : ', status)

        print("----------------------------------------------------------")

        # print('Message : ', message)

        if status == "RESOLVED":

            testResult(self, "passed", "DTC Clear status should be set to 'RESOLVED' successfully ",

                       "DTC Clear status is set to 'RESOLVED' successfully  ")

            #self.result.set_result(TestResults.passed)

        else:

            # print(response_body["responseData"]["message"])

            testResult(self, "failed", "DTC Clear status should be set to 'RESOLVED' successfully ",

                       "DTC Clear status is not set to 'RESOLVED' " + " Reason for failure is : " +

                       response_body)

            assert False

            #self.result.set_result(TestResults.failed)

    else:

        print("Something went wrong")

        #self.result.set_result(TestResults.failed)

        assert False

    print("----------------------------------------------------------")

    print("\n------------------------------END------------------------------\n")


def test_fetch_active_clear_dtc_details(self, cloudEnv, tc):

    print("\n===================== TEST START =====================\n")

    # ==========================================================
    # Step 1: Prepare Date Range for API
    # ==========================================================
    startDate = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    endDate = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

    offset = "0"
    limit = "50"
    details = "true"

    # Fetch systemId from config
    systemId = read_vehicleJsonFile(self, "system_id")

    print("Input Parameters:")
    print(f"   System ID  : {systemId}")
    print(f"   Start Date : {startDate}")
    print(f"   End Date   : {endDate}")
    print(f"   Limit      : {limit}")
    print("------------------------------------------------------")

    # ==========================================================
    # Step 2: Call API
    # ==========================================================
    response = DTC_fetchDTCCodes(
        self, systemId, startDate, endDate, offset, limit, details, "valid"
    )

    # Validate HTTP response
    assert response.status_code == 200, \
        f"API Failed. Status Code: {response.status_code}"

    response_body = response.json()

    # Validate API response message
    assert response_body.get("message") == "Data Saved Successfully", \
        f"API Error: {response_body}"

    # Extract DTC list
    dtcs = response_body.get("responseData", {}).get("DTCs", [])
    assert len(dtcs) > 0, "No DTC records found in response"

    print(f"\nTotal DTC records fetched: {len(dtcs)}")

    # ==========================================================
    # CASE 1: FETCH ONLY ACTIVE / PENDING DTCs
    # ==========================================================
    if tc == "fetch_active_dtcs":

        print("\nFiltering ACTIVE / PENDING DTCs...\n")

        # Filter active/pending DTCs
        active_dtcs = [
            d for d in dtcs
            if d.get("status") in ["ACTIVE", "PENDING"]
        ]

        print(f"ACTIVE/PENDING DTC count: {len(active_dtcs)}")

        # Validation
        assert len(active_dtcs) > 0, "No ACTIVE/PENDING DTCs found"

        # Print details
        print("\nACTIVE / PENDING DTC Details:")
        print("------------------------------------------------------")

        for d in active_dtcs:
            print(
                f"Session: {d.get('sessionId')} | "
                f"DTC: {d.get('dtcCode')} | "
                f"Status: {d.get('status')}"
            )

        print("------------------------------------------------------")
        print("\nACTIVE DTC validation successful")

    # ==========================================================
    # CASE 2: FETCH CLEAR + SHOW ACTIVE + VALIDATE LIFECYCLE
    # ==========================================================
    elif tc == "fetch_clear_dtcs":

        print("\nSeparating CLEAR and ACTIVE/PENDING DTCs...\n")

        clear_dtcs = []
        active_dtcs = []

        # Separate DTCs by status
        for d in dtcs:
            if d.get("status") == "CLEAR":
                clear_dtcs.append(d)
            elif d.get("status") in ["ACTIVE", "PENDING"]:
                active_dtcs.append(d)

        # Print summary counts
        print(f"CLEAR DTC count          : {len(clear_dtcs)}")
        print(f"ACTIVE/PENDING DTC count: {len(active_dtcs)}")

        # ======================================================
        # Print CLEAR DTCs
        # ======================================================
        print("\n CLEAR DTC Details:")
        print("------------------------------------------------------")

        for d in clear_dtcs:
            print(
                f"Session: {d.get('sessionId')} | "
                f"DTC: {d.get('dtcCode')} | "
                f"Status: {d.get('status')}"
            )

        print("------------------------------------------------------")

        # ======================================================
        # Print ACTIVE/PENDING (If Still Present)
        # ======================================================
        if active_dtcs:
            print("\n ACTIVE/PENDING DTCs STILL PRESENT:")
            print("------------------------------------------------------")

            for d in active_dtcs:
                print(
                    f"Session: {d.get('sessionId')} | "
                    f"DTC: {d.get('dtcCode')} | "
                    f"Status: {d.get('status')}"
                )

            print("------------------------------------------------------")

        # ======================================================
        # Step 3: Lifecycle Validation (ACTIVE → CLEAR)
        # ======================================================
        print("\n Validating DTC Lifecycle (ACTIVE → CLEAR)...\n")

        # Capture all ACTIVE/PENDING keys (sessionId + dtcCode)
        active_keys = {
            (d.get("sessionId"), d.get("dtcCode"))
            for d in dtcs
            if d.get("status") in ["ACTIVE", "PENDING"]
        }

        not_cleared = []

        # Validate each ACTIVE/PENDING DTC has CLEAR
        for session_id, dtc_code in active_keys:

            # Collect all statuses for same DTC
            statuses = [
                x.get("status")
                for x in dtcs
                if x.get("sessionId") == session_id and
                   x.get("dtcCode") == dtc_code
            ]

            # Check if CLEAR state exists
            if "CLEAR" not in statuses:
                not_cleared.append({
                    "sessionId": session_id,
                    "dtcCode": dtc_code,
                    "statuses": statuses
                })

        # Print failures if any
        if not_cleared:
            print("\nDTCs NOT CLEARED:")
            print("------------------------------------------------------")

            for item in not_cleared:
                print(item)

            print("------------------------------------------------------")

        # Final assertion
        assert len(not_cleared) == 0, \
            f"Lifecycle validation failed: {not_cleared}"

        print("\nSUCCESS: All ACTIVE/PENDING DTCs transitioned to CLEAR")

    # ==========================================================
    # INVALID TEST CASE
    # ==========================================================
    else:
        assert False, f"Invalid test case value: {tc}"

    print("\n====================== TEST END ======================\n")
