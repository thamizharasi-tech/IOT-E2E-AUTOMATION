import ast
import json

import requests

from C2CModules.api_modules import header_update
from C2CModules.e2e_testData import *
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ------------------------------------------
# Vehicle State Reusable Modules
# ------------------------------------------

def get_vehicle_state_details_global(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleStateOperation_get_vehicle_state_global")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object[0] = systemId
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleStateOperation_get_vehicle_state_global', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleStateOperation_get_vehicle_state_global", response.text)

    return response


def get_vehicle_state_details_regional(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleStateOperation_get_vehicle_state_regional")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object[0] = systemId
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleStateOperation_get_vehicle_state_regional', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleStateOperation_get_vehicle_state_regional", response.text)

    return response


def vehicle_state_update_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, Parameter1, Parameter2,
                                              Parameter3, Parameter4, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicle_state_update_telemetry_parameters")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode)
    if tc == "vehicle_type":
        complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode) + "/{vehicle_type}".replace(
            '{vehicle_type}', vehicle_type)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    if cloudEnv in r5_envs:
        json_object[0] = Parameter1
        json_object[1] = Parameter2
        json_object[2] = Parameter3
    else:
        json_object[0] = Parameter1
        json_object[1] = Parameter2
        json_object[2] = Parameter3
        json_object[3] = Parameter4

    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('vehicle_state_update_telemetry_parameters', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicle_state_update_telemetry_parameters", response.text)

    return response


def vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicle_state_get_telemetry_parameters")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode)
    if tc == "vehicle_type":
        complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode) + "/{vehicle_type}".replace(
            '{vehicle_type}', vehicle_type)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.get(complete_url, headers=header_x)
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('vehicle_state_get_telemetry_parameters', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicle_state_get_telemetry_parameters", response.text)

    return response


def vehicle_state_info(self, cloudEnv, systemId, tc):
    if tc == "global":
        response = get_vehicle_state_details_global(self, systemId, tc)
    elif tc == "regional":
        response = get_vehicle_state_details_regional(self, systemId, tc)

    print("----------------------------------------------------------")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_body = response.json()
    result_data = response_body.get("result", [])

    if len(result_data) >= 1:
        for vehicle_data in result_data:
            systemId_actual = vehicle_data["systemId"]
            if any(cloudEnv in lst for lst in
                   (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
                status = vehicle_data["message"]
            else:
                status = vehicle_data["status"]
            response_data = vehicle_data["responseData"]
            vehicle_state_data = response_data["vehicleStateData"]

            lastHeartBeatTime = response_data.get("lastHeartBeatTime", "")
            currentState = vehicle_state_data.get("currentState", "")
            if any(cloudEnv in lst for lst in
                   (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
                connectionState = vehicle_state_data.get("connectionState", "")
            else:
                connectionState = None
            ignition = vehicle_state_data.get("ignition", "")
            speed = vehicle_state_data.get("speed", "")
            ota = vehicle_state_data.get("ota", "")
            command = vehicle_state_data.get("command", "")
            gpsFix = vehicle_state_data.get("gpsFix", "")
            primaryBatteryStatus = vehicle_state_data.get("primaryBatteryStatus", "")
            vehicleMode = vehicle_state_data.get("vehicleMode", "")

            # Determine mode based on cloudEnv
            if any(cloudEnv in lst for lst in
                   (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
                rideMode = vehicle_state_data.get("rideMode", "")
                parkMode = None
            else:
                parkMode = vehicle_state_data.get("parkMode", "")
                rideMode = None

            if any(cloudEnv in lst for lst in
                   (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
                deviceActivationState = vehicle_state_data.get("deviceActivationState", "")
            else:
                deviceActivationState = None

            if cloudEnv in r8_patch4_sp17_envs:
                rideState = vehicle_state_data.get("rideState", "")
            else:
                rideState = None

            if systemId == systemId_actual and status == "Success":
                print("Vehicle state details retrieved successfully.")
                assert True
                break
        else:
            testResult(self, "failed",
                       "Vehicle state details should be retrieved for the desired systemId.",
                       "Vehicle state details retrieval failed.")
            assert False
    else:
        print("No vehicle state records exist in the cloud database.")
        assert False

    print("----------------------------------------------------------")
    print(f"System ID: {systemId_actual}")
    print(f"Current State: {currentState}")
    print(f"Connection State: {connectionState}")
    print(f"Park Mode: {parkMode}")
    print(f"Ride Mode: {rideMode}")
    print(f"Ignition: {ignition}")
    print(f"Speed: {speed}")
    print(f"OTA: {ota}")
    print(f"Command: {command}")
    print(f"GPS Fix: {gpsFix}")
    print(f"Primary Battery Status: {primaryBatteryStatus}")
    print(f"Vehicle Mode: {vehicleMode}")
    print(f"Last Heart Beat Time: {lastHeartBeatTime}")
    print(f"Device Activation State: {deviceActivationState}")
    print(f"Ride State: {rideState}")
    print("----------------------------------------------------------")

    # testResult(self, "passed",
    # "Vehicle metadata details should be retrieved successfully for the desired systemId.",
    # "Vehicle metadata details retrieved successfully.")

    return currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState


def vehicle_state_save_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, Parameter1, Parameter2, Parameter3,
                                            Parameter4, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicle_state_save_telemetry_parameters")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode)
    if tc == "vehicle_type":
        complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode) + "/{vehicle_type}".replace(
            '{vehicle_type}', vehicle_type)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    if cloudEnv in r5_envs:
        json_object[0] = Parameter1
        json_object[1] = Parameter2
        json_object[2] = Parameter3
    else:
        json_object[0] = Parameter1
        json_object[1] = Parameter2
        json_object[2] = Parameter3
        json_object[3] = Parameter4

    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('vehicle_state_save_telemetry_parameters', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicle_state_save_telemetry_parameters", response.text)

    return response


def vehicle_state_delete_telemetry_parameters(self, cloudEnv, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicle_state_delete_telemetry_parameters")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.delete(complete_url, headers=header_x)
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('vehicle_state_delete_telemetry_parameters', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicle_state_delete_telemetry_parameters", response.text)

    return response
