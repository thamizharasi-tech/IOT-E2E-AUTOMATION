import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.telemetry_persistance import get_telemetry_history_details
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import *


# API Operation to create master configuration for model
def vehicleConfigurations_createMasterConfigurationForModel(self, model, version, RegionalAPNEndpoints, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["configuration"]["Communication"]["NetworkAPNConfig"]["RegionalAPNEndpoints"] = RegionalAPNEndpoints
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createMasterConfig", response.text)

    return response


# API Operation to update master configuration for model
def vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["configuration"]["Communication"]["NetworkAPNConfig"]["RegionalAPNEndpoints"] = RegionalAPNEndpoints
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateMasterConfig", response.text)

    return response


# API Operation to fetch master configuration for model
def vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).split('?')[0]
    if "version" in tc:
        complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getMasterConfig", response.text)

    return response


# API Operation to delete master configuration for model
def vehicleConfigurations_deleteMasterConfigurationForModel(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_deleteMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_deleteMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_deleteMasterConfig", response.text)

    return response


# API Operation to create Factory configuration for model
def vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["configuration"]["Communication"]["NetworkAPNConfig"]["RegionalAPNEndpoints"] = RegionalAPNEndpoints
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createFactoryConfig", response.text)

    return response


# API Operation to update master configuration for model
def vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["configuration"]["Communication"]["NetworkAPNConfig"]["RegionalAPNEndpoints"] = RegionalAPNEndpoints
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateFactoryConfig", response.text)

    return response


# API Operation to fetch factory configuration for model
def vehicleConfigurations_fetchFactoryConfigurationForModel(self, model, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).split('?')[0]
    if "version" in tc:
        complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getFactoryConfig", response.text)

    return response


# API Operation to delete factory configuration for model
def vehicleConfigurations_deleteFactoryConfigurationForModel(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_deleteFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_deleteFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_deleteFactoryConfig", response.text)

    return response


# API Operation to create initial config
def vehicleConfigurations_createInitialConfig(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createInitialConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    # json_object = json.loads(payload)
    # payload = json_object
    # print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createInitialConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createInitialConfig", response.text)

    return response


# API Operation to get initial config
def vehicleConfigurations_getConfig(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    # json_object = json.loads(payload)
    # payload = json_object
    # print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getConfig", response.text)

    return response


# API Operation to update configuration
def vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, updateScope, modelCode, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    if tc == "ADD":
        payload = {
  "updates": [{
			"action": action,
            "path": path,
             "attribute": attribute,
			"value": value
		}],
  "systemIds":[systemId]
}
    elif tc == "EDIT":
        payload = {
            "updates": [{
                "action": action,
                "path": path,
                "value": value
            }],
            "systemIds": [systemId]
        }
    elif tc == "DELETE":
        payload = {
            "updates": [{
                "action": action,
                "path": path
            }],
            "systemIds": [systemId]
        }
    elif tc == "model_based_configuration":
        payload = {
    "updates": [
        {
            "action": action,
            "path": path,
            "value": value
        }
    ],
    "updateScope" : updateScope,
    "modelCode" : modelCode,
    "country" : country
}
    elif tc == "model_based_configuration_add_action":
        payload = {
            "updates": [
                {
                    "action": action,
                    "path": path,
                    "attribute": attribute,
                    "value": value
                }
            ],
            "updateScope": updateScope,
            "modelCode": modelCode,
            "country": country
        }
    elif tc == "model_based_configuration_delete_action":
        payload = {
            "updates": [
                {
                    "action": action,
                    "path": path
                }
            ],
            "updateScope": updateScope,
            "modelCode": modelCode,
            "country": country
        }
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateConfiguration', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration", response.text)

    return response


# API Operation to track the configuration
def vehicleConfigurations_configurationUpdateTracking(self, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_configurationUpdateTracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    # json_object = json.loads(payload)
    # payload = json_object
    # print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_configurationUpdateTracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_configurationUpdateTracking", response.text)

    return response


def vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled, start_time,
                                                                       end_time, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration_vacation_new")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["updates"][0]["action"] = action
    json_object["updates"][0]["path"] = path
    json_object["updates"][0]["value"]["enabled"] = enabled
    json_object["updates"][0]["value"]["start_time"] = start_time
    json_object["updates"][0]["value"]["end_time"] = end_time
    json_object["systemIds"][0] = systemId
    if tc == "without_end_time":
        del json_object["updates"][0]["value"]["end_time"]
    elif tc == "without_start_time":
        del json_object["updates"][0]["value"]["start_time"]
    elif tc == "without_start_end_time":
        del json_object["updates"][0]["value"]["start_time"]
        del json_object["updates"][0]["value"]["end_time"]
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateConfiguration_vacation_new', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration_vacation_new", response.text)

    return response


# ----------------------------------------------------------------------------------------------------------

# new module as per latest

# ---------------------------------------------------------------------------------------------------------

# API Operation to create factory configuration for model
def vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=dtc_configurations"
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}', version)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r', encoding='utf-8') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createFactoryConfig", response.text)

    return response


# API Operation to update factory configuration for model
def vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r', encoding='utf-8') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateFactoryConfig", response.text)

    return response


# API Operation to create master configuration for model
def vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url, header, and payload) for POST request

    # Url:
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4","GCP-QA2","GCP-QA5","GCP-QA8","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}', version)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model).replace('{version}',
                                                                                      version) + "?configType=dtc_configurations"
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}', version)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
                '{version}',
                version) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createMasterConfig", response.text)

    return response


# API Operation to update master configuration for model
def vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_updateMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_updateMasterConfig", response.text)

    return response


def vehicleConfigurations_createInitialConfig_new(self, systemId, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_createInitialConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId) + "&model={model}".replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_createInitialConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_createInitialConfig", response.text)

    return response


# API Operation to fetch factory configuration for model
def vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
        elif "version" in tc:
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?version={version}".replace(
                '{version}',
                version)
        else:
            complete_url = str(base_url + endpoint).replace('{model}', model)
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
        elif "version" in tc:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?version={version}".replace(
                '{version}',
                version)
        else:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getFactoryConfig", response.text)

    return response


# API Operation to delete factory configuration for model
def vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_deleteFactoryConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
        else:
            complete_url = str(base_url + endpoint).replace('{model}', model)
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
        else:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_deleteFactoryConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_deleteFactoryConfig", response.text)

    return response


# API Operation to fetch master configuration for model
def vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
        elif "version" in tc:
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?version={version}".replace(
                '{version}',
                version)
        else:
            complete_url = str(base_url + endpoint).replace('{model}', model)
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
        elif "version" in tc:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?version={version}".replace(
                '{version}',
                version)
        else:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getMasterConfig", response.text)

    return response


# API Operation to delete master configuration for model
def vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_deleteMasterConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4","GCP-QA5","GCP-QA8","GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{model}', model) + "?configType=dtc_configurations"
        else:
            complete_url = str(base_url + endpoint).replace('{model}', model)
    else:
        if tc == "vehicle_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
        elif tc == "telemetry_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=telemetry"
        elif tc == "command_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=remote_operations"
        elif tc == "alert_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=alert_configurations"
        elif tc == "dtc_conf":
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}',
                                                                                          country) + "?configType=dtc_configurations"
        else:
            complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_deleteMasterConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_deleteMasterConfig", response.text)

    return response


# API Operation to get initial config
def vehicleConfigurations_getConfig_new(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_getConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :

    if tc == "vehicle_conf":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    elif tc == "telemetry_conf":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId) + "?configType=telemetry"
    elif tc == "command_conf":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId) + "?configType=remote_operations"
    elif tc == "alert_conf":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId) + "?configType=alert_configurations"
    elif tc == "dtc_conf":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    # json_object = json.loads(payload)
    # payload = json_object
    # print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    #print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_getConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_getConfig", response.text)

    return response


def vehicleConfigurations_factoryReset(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_factoryReset")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_factoryReset', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_factoryReset", response.text)

    return response


def vehicleConfigurations_decision_table_for_rules(self, configType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_decisionTable_for_rules")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{configType}', configType)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_decisionTable_for_rules', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_decisionTable_for_rules", response.text)

    return response


def vehicleConfigurations_createGlobalConfiguration(self, version, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_global_create_configuration")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if tc == "vehicle_conf":
        complete_url = str(base_url + endpoint).replace('{version}', version)
    elif tc == "telemetry_conf":
        complete_url = str(base_url + endpoint).replace('{version}', version) + "?configType=telemetry"
    elif tc == "command_conf":
        complete_url = str(base_url + endpoint).replace('{version}', version) + "?configType=remote_operations"
    elif tc == "alert_conf":
        complete_url = str(base_url + endpoint).replace('{version}', version) + "?configType=alert_configurations"
    elif tc == "dtc_conf":
        complete_url = str(base_url + endpoint).replace('{version}', version) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_global_create_configuration', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_global_create_configuration", response.text)

    return response


# API Operation to update master configuration for model
def vehicleConfigurations_updateGlobalConfiguration(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_global_update_configuration")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    if tc == "vehicle_conf":
        complete_url = str(base_url + endpoint)
    elif tc == "telemetry_conf":
        complete_url = str(base_url + endpoint) + "?configType=telemetry"
    elif tc == "command_conf":
        complete_url = str(base_url + endpoint) + "?configType=remote_operations"
    elif tc == "alert_conf":
        complete_url = str(base_url + endpoint) + "?configType=alert_configurations"
    elif tc == "dtc_conf":
        complete_url = str(base_url + endpoint) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload:
    if "vehicle_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"
    elif "telemetry_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"
    elif "command_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"
    elif "alert_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"
    elif "dtc_conf" in tc:
        payload_file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\dtc_conf.json"
    else:
        raise ValueError("Invalid configuration type in tc")

    with open(payload_file, 'r') as file:
        json_object = json.load(file)

    payload = {"configuration": json_object}
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_global_update_configuration', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_global_update_configuration", response.text)

    return response


# API Operation to fetch factory configuration for model
def vehicleConfigurations_getGlobalConfiguration(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_global_get_configuration")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    if tc == "vehicle_conf":
        complete_url = str(base_url + endpoint)
    elif tc == "telemetry_conf":
        complete_url = str(base_url + endpoint) + "?configType=telemetry"
    elif tc == "command_conf":
        complete_url = str(base_url + endpoint) + "?configType=remote_operations"
    elif tc == "alert_conf":
        complete_url = str(base_url + endpoint) + "?configType=alert_configurations"
    elif tc == "dtc_conf":
        complete_url = str(base_url + endpoint) + "?configType=dtc_configurations"
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_global_get_configuration', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_global_get_configuration", response.text)

    return response


# API Operation to delete factory configuration for model
def vehicleConfigurations_deleteGlobalConfiguration(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_global_delete_configuration")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    if tc == "vehicle_conf":
        complete_url = str(base_url + endpoint)
    elif tc == "telemetry_conf":
        complete_url = str(base_url + endpoint) + "?configType=telemetry"
    elif tc == "command_conf":
        complete_url = str(base_url + endpoint) + "?configType=remote_operations"
    elif tc == "alert_conf":
        complete_url = str(base_url + endpoint) + "?configType=alert_configurations"
    elif tc == "dtc_conf":
        complete_url = str(base_url + endpoint) + "?configType=dtc_configurations"

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_global_delete_configuration', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_global_delete_configuration", response.text)

    return response


# vehicle mode precondition
def vehicleConfigurations_save_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1,
                                            statePreconditions2,
                                            tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_save_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
        json_object["model"] = model
        json_object["action"] = action
        json_object["subAction"] = subAction
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
    else:
        json_object["modelCode"] = model
        json_object["country"] = country
        json_object["action"] = action
        json_object["subAction"] = subAction
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_save_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_save_precondition", response.text)

    return response


def vehicleConfigurations_update_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1,
                                              statePreconditions2,
                                              tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_update_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
        json_object["model"] = model
        json_object["action"] = action
        json_object["subAction"] = subAction
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
    else:
        json_object["modelCode"] = model
        json_object["country"] = country
        json_object["action"] = action
        json_object["subAction"] = subAction
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_update_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_update_precondition", response.text)

    return response


def vehicleConfigurations_get_precondition(self, cloudEnv, model, country, action, subAction, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_get_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
        complete_url = str(base_url + endpoint).replace('{model}', model).replace('{action}',
                                                                                  action) + "&subAction={subAction}".replace(
            '{subAction}', subAction)
    else:
        complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country).replace(
            '{action}',
            action) + "&subAction={subAction}".replace(
            '{subAction}', subAction)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_get_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_get_precondition", response.text)

    return response


# --------------------------------------------------------------------------------------
# Vehicle configuration Reusable modules
# --------------------------------------------------------------------------------------


def factoryConfiguration(self, model, version):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Save Factory Configuration via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    print("==============1.Vehicle Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Vehicle configuration should be saved successfully for the given model.",
                       "Factory Conf - Vehicle configuration is saved successfully for this model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Vehicle configuration should be saved successfully for this model.",
                       "Factory Conf - Vehicle configuration already exists for this model.")
            assert True

            # Update vehicle configuration with the latest configuration
            print("Updating vehicle configuration with the latest configuration...")
            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                               "Factory Conf - Vehicle configuration is updated successfully for this model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                      "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save vehicle configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============2.Telemetry Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "telemetry_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Telemetry configuration should be saved successfully for the given model.",
                       "Factory Conf - Telemetry configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
            "message"] == "Mode Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Telemetry configuration should be saved successfully for the given model.",
                       "Factory Conf - Telemetry configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest telemetry configuration
            print("Updating vehicle configuration with the latest telemetry configuration...")
            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "telemetry_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Telemetry configuration should be updated successfully for the given model.",
                               "Factory Conf - Telemetry configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print(
                    "Error: Unable to update telemetry configuration. Please check the API response for more details.",
                    "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save factory telemetry configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============3.Command Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "command_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Command configuration should be saved successfully for the given model.",
                       "Factory Conf - Command configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
            "message"] == "Mode Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Command configuration should be saved successfully for the given model.",
                       "Factory Conf - Command configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest telemetry configuration
            print("Updating vehicle configuration with the latest command configuration...")
            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "command_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Command configuration should be updated successfully for the given model.",
                               "Factory Conf - Command configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print(
                    "Error: Unable to update command configuration. Please check the API response for more details.",
                    "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save factory command configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============4.Alert Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "alert_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Alert configuration should be saved successfully for the given model.",
                       "Factory Conf - Alert configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
            "message"] == "Mode Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Alert configuration should be saved successfully for the given model.",
                       "Factory Conf - Alert configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest telemetry configuration
            print("Updating vehicle configuration with the latest alert configuration...")
            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "alert_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Alert configuration should be updated successfully for the given model.",
                               "Factory Conf - Alert configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print(
                    "Error: Unable to update alert configuration. Please check the API response for more details.",
                    "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save factory alert configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")


def masterConfiguration(self, model, version):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Save Master Configuration via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    print("==============1.Vehicle Conf==============")
    response = vehicleConfigurations_createMasterConfigurationForModel_new(self, model, version, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Master Conf - Vehicle configuration should be saved successfully for the given model.",
                       "Master Conf - Vehicle configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16000" and response_body["errors"][0][
            "message"] == "Master Config version already exist for this model":
            testResult(self, "passed",
                       "Master Conf - Vehicle configuration should be saved successfully for the given model.",
                       "Master Conf - Vehicle configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest configuration
            print("Updating vehicle configuration with the latest configuration...")
            response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "vehicle_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Master Conf - Vehicle configuration should be updated successfully for the given model.",
                               "Master Conf - Vehicle configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                      "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save master configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============2.Telemetry Conf==============")
    response = vehicleConfigurations_createMasterConfigurationForModel_new(self, model, version, "telemetry_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Master Conf - Telemetry configuration should be saved successfully for the given model.",
                       "Master Conf - Telemetry configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Master Config version already exist for this model":
            testResult(self, "passed",
                       "Master Conf - Telemetry configuration should be saved successfully for the given model.",
                       "Master Conf - Telemetry configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest configuration
            print("Updating telemetry configuration with the latest configuration...")
            response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "telemetry_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Master Conf - Telemetry configuration should be updated successfully for the given model.",
                               "Master Conf - Telemetry configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print(
                    "Error: Unable to update telemetry configuration. Please check the API response for more details.",
                    "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save master configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============3.Command Conf==============")
    response = vehicleConfigurations_createMasterConfigurationForModel_new(self, model, version, "command_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Master Conf - Command configuration should be saved successfully for the given model.",
                       "Master Conf - Command configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Master Config version already exist for this model":
            testResult(self, "passed",
                       "Master Conf - Command configuration should be saved successfully for the given model.",
                       "Master Conf - Command configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest configuration
            print("Updating command configuration with the latest configuration...")
            response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "command_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Master Conf - Command configuration should be updated successfully for the given model.",
                               "Master Conf - Command configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print("Error: Unable to update command configuration. Please check the API response for more details.",
                      "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save master configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============4.Alert Conf==============")
    response = vehicleConfigurations_createMasterConfigurationForModel_new(self, model, version, "alert_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Master Conf - Alert configuration should be saved successfully for the given model.",
                       "Master Conf - Alert configuration is saved successfully for the given model.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Master Config version already exist for this model":
            testResult(self, "passed",
                       "Master Conf - Alert configuration should be saved successfully for the given model.",
                       "Master Conf - Alert configuration already exists for the given model.")
            assert True

            # Update vehicle configuration with the latest configuration
            print("Updating alert configuration with the latest configuration...")
            response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "alert_conf")

            # Parse the API response into JSON format
            response_body = response.json()

            # Validate the response status code and message
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Master Conf - Alert configuration should be updated successfully for the given model.",
                               "Master Conf - Alert configuration is updated successfully for the given model.")
                    assert True
                else:
                    print("Unexpected response message during update:", response_body["message"])
                    assert False
            else:
                print("Error: Unable to update alert configuration. Please check the API response for more details.",
                      "Status Code:", response.status_code, "Response Body:", response_body)
                assert False
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to save master configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")


def initializeConfiguration(self, systemId, model):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Initialize Configuration On the vehicle via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "valid")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Vehicle configuration, Telemetry configuration, Command configuration, and Alert configuration should be initialized successfully on the vehicle.",
                       "Vehicle configuration, Telemetry configuration, Command configuration, and Alert configuration are initialized successfully on the vehicle.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16004" and response_body["errors"][0][
            "message"] == "Initial config already exist for this system id":
            testResult(self, "passed",
                       "Vehicle configuration, Telemetry configuration, Command configuration, and Alert configuration should be initialized successfully on the vehicle.",
                       "Vehicle configuration, Telemetry configuration, Command configuration, and Alert configuration are already initialized on the vehicle.")
            assert True
        else:
            print("Unexpected error code or message:", response_body["errors"][0]["errorCode"],
                  response_body["errors"][0]["message"])
            assert False
    else:
        print("Error: Unable to fetch configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")


def getConfiguration(self, systemId):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the vehicle via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    print("============1.GET - VEHICLE CONF===========")
    response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Vehicle configuration fetched successfully for the given vehicle.",
                       "The vehicle configuration has been successfully retrieved for the specified vehicle.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    else:
        print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("============2.GET - TELEMETRY CONF===========")
    response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Telemetry configuration fetched successfully for the given vehicle.",
                       "The telemetry configuration has been successfully retrieved for the specified vehicle.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    else:
        print("Error: Unable to fetch telemetry configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("============3.GET - COMMAND CONF===========")
    response = vehicleConfigurations_getConfig_new(self, systemId, "command_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Command configuration fetched successfully for the given vehicle.",
                       "The command configuration has been successfully retrieved for the specified vehicle.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    else:
        print("Error: Unable to fetch command configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("============4.GET - ALERT CONF===========")
    response = vehicleConfigurations_getConfig_new(self, systemId, "alert_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Alert configuration fetched successfully for the given vehicle.",
                       "The alert configuration has been successfully retrieved for the specified vehicle.")
            assert True
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
    else:
        print("Error: Unable to fetch alert configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False

    print("----------------------------------------------------------")


def vehicle_conf_factory_reset(self, systemId):
    # systemId = read_vehicleJsonFile(self, "system_id")
    # systemId = "7238"

    response = vehicleConfigurations_factoryReset(self, systemId, "valid")

    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        assert True
        # self.result.set_result(TestResults.passed)
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "verificationPassed",
                       "Factory Reset - Configuration reset should be triggered successfully",
                       "Factory Reset - Configuration reset is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed", "Factory Reset - Configuration reset should be triggered successfully",
                   "Factory Reset - Configuration reset is not triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    for i in range(5):
        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        print(response.status_code)

        print("----------------------------------------------------------")

        # Validate response status code
        if response.status_code == 200 or response.status_code == 207:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["results"][0]["status"] == "PROGRESSING":
            testResult(self, "verificationPassed", "Factory Reset - Configuration reset should  be 'PROGRESSING'",
                       "Factory Reset - Configuration reset is PROGRESSING")
        # Validate response body
        elif response_body["results"][0]["status"] == "COMPLETED":
            break

        time.sleep(10)

    # Validate response body
    if response_body["results"][0]["status"] == "COMPLETED":
        testResult(self, "passed", "Factory Reset - Configuration reset should success/completed",
                   "Factory Reset - Configuration reset is success/completed")
        assert True
        # self.result.set_result(TestResults.passed)
    elif response_body["results"][0]["status"] == "FAILED":
        testResult(self, "failed", "Factory Reset - Configuration reset should success/completed",
                   "Factory Reset - Configuration reset is not success/completed")
        # self.result.set_result(TestResults.passed)
        assert False
    else:
        print("Something went wrong, Please check API Response for more details")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")


def vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1,
                             statePreconditions2, tc):
    # Call API reusable module
    if tc == "save_precondition":
        response = vehicleConfigurations_save_precondition(self, cloudEnv, model, country, action, subAction,
                                                           statePreconditions1,
                                                           statePreconditions2, "valid")
    if tc == "update_precondition":
        response = vehicleConfigurations_update_precondition(self, cloudEnv, model, country, action, subAction,
                                                             statePreconditions1,
                                                             statePreconditions2, "valid")
    # Validate response status code
    if response.status_code == 200:
        response_body = response.json()

        if response_body.get("status") == "COMPLETED":
            print("Vehicle Mode precondition data saved successfully.")
            assert True
        else:
            print("Failed to save vehicle mode precondition.")
            assert False
    elif response.status_code == 400:
        response_body = response.json()
        if response_body["errors"][0]["errorCode"] == "16072" and (response_body["errors"][0][
                                                                       "message"] == "Precondition already exist for the model and action." or
                                                                   response_body["errors"][0][
                                                                       "message"] == "Precondition already exist for the modelCode, country and action."):
            assert True
        else:
            assert False
    else:
        print("Response status code is not 200. Rather than found: ", response.status_code)
        assert False

    # Fetch vehicle mode precondition
    response = vehicleConfigurations_get_precondition(self, cloudEnv, model, country, action, subAction, "valid")

    # Ensure valid response
    if response.status_code == 200:
        assert True
    else:
        print(f"API request failed with status {response.status_code}")
        assert False

    response_body = response.json()

    if response_body.get("model") == model and response_body.get("action") == action:
        print("----------------------------------------------------------")
        print(f"Status: {response_body.get('status')}")
        print("----------------------------------------------------------")

        if "result" in response_body:
            try:
                response_body["result"] = json.loads(response_body["result"])
            except json.JSONDecodeError:
                print("Invalid JSON format in 'result'")

            precondition = response_body["result"]["statePreconditions"]
            print(f"Fetched Precondition: {precondition}")
            assert True
        else:
            print("Precondition is not fetched or saved")
            assert False


# R8S4- Create bundle API

def vehicleConfigurations_create_bundle(self, cloudEnv, model, country, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_create_bundle")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
        complete_url = str(base_url + endpoint).replace('{model}', model)
    else:
        complete_url = str(base_url + endpoint).replace('{modelCode}', model).replace('{country}', country)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleConfiguration_create_bundle', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleConfiguration_create_bundle", response.text)

    return response


def getset_config(self, onboardingType, chipsetType, option, path):
    print("===========================================")
    print("GET AND SET CONFIGURATION ON THE DEVICE SIDE")
    print("===========================================")
    systemId = read_vehicleJsonFile(self, "system_id")

    if "master_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "master_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        # Generate and compare checksums
        cloud_checksum = generate_cloud_checksum(self, "master_conf")
        device_checksum = generate_device_checksum(self, "master_conf")

        print(f"Generated cloud checksum from the file saved in {save_path}:", cloud_checksum)
        print("Generated device checksum from the pulled file from /mnt/vendor/persist/data/c2c:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)

    elif "telemetry_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "telemetry_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "telemetry_conf")
        device_checksum = generate_device_checksum(self, "telemetry_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)
    elif "command_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "command_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "command_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "command_conf")
        device_checksum = generate_device_checksum(self, "command_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)
    elif "alert_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "alert_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "alert_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "alert_conf")
        device_checksum = generate_device_checksum(self, "alert_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)

def getset_config_v2(self, onboardingType, chipsetType, option, path):
    print("===========================================")
    print("GET AND SET CONFIGURATION ON THE DEVICE SIDE")
    print("===========================================")
    systemId = read_vehicleJsonFile(self, "system_id")

    if "master_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "master_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # Generate and compare checksums
        cloud_checksum = generate_cloud_checksum(self, "master_conf")
        device_checksum = generate_device_checksum(self, "master_conf")

        print(f"Generated cloud checksum from the file saved in {save_path}:", cloud_checksum)
        print("Generated device checksum from device conf file:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)

    elif "telemetry_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\telemetry_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "telemetry_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "telemetry_conf")
        device_checksum = generate_device_checksum(self, "telemetry_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)
    elif "command_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "command_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\command_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "command_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "command_conf")
        device_checksum = generate_device_checksum(self, "command_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)
    elif "alert_conf" in option:
        response = vehicleConfigurations_getConfig_new(self, systemId, "alert_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\alert_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f, separators=(',', ':'))

        print(f"Configuration updated successfully and saved to {save_path}.")

        # step 6:
        push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "alert_conf", path)

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "alert_conf")
        device_checksum = generate_device_checksum(self, "alert_conf")

        print("Generated cloud checksum:", cloud_checksum)
        print("Generated device checksum:", device_checksum)

        if cloud_checksum is None or device_checksum is None:
            print("Error: One of the checksums is None. Please check the file paths and ensure the files exist.")
        elif cloud_checksum == device_checksum:
            print(f"The file at {save_path} on the device matches the cloud file.")
            testResult(self, "passed", "Checksum validation", "The file on the device matches the cloud file.")
        else:
            print("The file on the device does not match the cloud file.")
            testResult(self, "failed", "Checksum validation", "The file on the device does not match the cloud file.")
            status = "FAIL"
            print("Status", status)
def vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time, end_time,
                               vehicleMode):
    # ===========================================================================================
    # Trigger Vacation Mode
    # ===========================================================================================

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print(f"Trigger {vehicleMode} Mode via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # call update vehicle configuration api module
    response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                  start_time, end_time, systemId,
                                                                                  "valid")

    print("----------------------------------------------------------")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        assert True
        # self.result.set_result(TestResults.passed)
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "verificationPassed",
                       f"{vehicleMode} Mode - Configuration update should be triggered successfully",
                       f"{vehicleMode} Mode - Configuration update is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed", f"{vehicleMode} Mode - Configuration update should be triggered successfully",
                   f"{vehicleMode} Mode - Configuration update is not triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    #pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    #time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validation via Tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    for i in range(5):
        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        print(response.status_code)

        print("----------------------------------------------------------")

        # Validate response status code
        if response.status_code == 200 or response.status_code == 207:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["results"][0]["status"] == "PROGRESSING":
            testResult(self, "verificationPassed",
                       f"{vehicleMode} Mode - Configuration update should  be 'PROGRESSING'",
                       f"{vehicleMode} Mode - Configuration update is PROGRESSING")
        # Validate response body
        elif response_body["results"][0]["status"] == "COMPLETED":
            break

        time.sleep(10)

    # Validate response body
    if response_body["results"][0]["status"] == "COMPLETED":
        testResult(self, "passed", f"{vehicleMode} Mode - Configuration update should success/completed",
                   f"{vehicleMode} Mode - Configuration update is success/completed")
        assert True
        # self.result.set_result(TestResults.passed)
    elif response_body["results"][0]["status"] == "FAILED":
        testResult(self, "failed", f"{vehicleMode} Mode - Configuration update should success/completed",
                   f"{vehicleMode} Mode - Configuration update is not success/completed")
        # self.result.set_result(TestResults.passed)
        assert False
    else:
        print("Something went wrong, Please check API Response for more details")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print(f"Validate {vehicleMode} mode is enabled in master_conf.json : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    if vehicleMode == "Vacation":
        # Read master_conf.json file
        vacationMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        vacationMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_StartTime", "vacationMode")
        vacationMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_EndTime", "vacationMode")

        print(" Vacation Mode - Enabled :", vacationMode_Enabled)
        print(" Vacation Mode - Start Time :", vacationMode_StartTime)
        print(" Vacation Mode - End Time :", vacationMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(vacationMode_Enabled) == enabled or bool(vacationMode_Enabled) == enabled:
            testResult(self, "passed", "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if vacationMode_StartTime == start_time:
            testResult(self, "passed", "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if vacationMode_EndTime == end_time:
            testResult(self, "passed", "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    elif vehicleMode == "Incognito":
        # Read master_conf.json file
        incognitoMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled", "incognitoMode")
        incognitoMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_StartTime", "incognitoMode")
        incognitoMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_EndTime", "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Enabled)
        print(" Incognito Mode - Start Time :", incognitoMode_StartTime)
        print(" Incognito Mode - End Time :", incognitoMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(incognitoMode_Enabled) == enabled or bool(incognitoMode_Enabled) == enabled:
            testResult(self, "passed",
                       "Incognito Mode Flag should be set to True in master_conf.json file on device",
                       "Incognito Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode Flag should be set to True in master_conf.json file on device",
                       "Incognito Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if incognitoMode_StartTime == start_time:
            testResult(self, "passed",
                       "Incognito Mode Start time should be updated in master_conf.json file on device",
                       "Incognito Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode Start time should be updated in master_conf.json file on device",
                       "Incognito Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if incognitoMode_EndTime == end_time:
            testResult(self, "passed",
                       "Incognito Mode End time should be updated in master_conf.json file on device",
                       "Incognito Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode End time should be updated in master_conf.json file on device",
                       "Incognito Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    elif vehicleMode == "RemoteDiagnostic":
        # Read master_conf.json file
        remoteDiagnosticMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_Enabled", "remoteDiagnosticMode")
        remoteDiagnosticMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_StartTime", "remoteDiagnosticMode")
        remoteDiagnosticMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_EndTime", "remoteDiagnosticMode")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Enabled)
        print(" Remote Diagnostic Mode - Start Time :", remoteDiagnosticMode_StartTime)
        print(" Remote Diagnostic Mode - End Time :", remoteDiagnosticMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(remoteDiagnosticMode_Enabled) == enabled or bool(remoteDiagnosticMode_Enabled) == enabled:
            testResult(self, "passed", "Remote Diagnostic Mode Flag should be set to True in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Remote Diagnostic Mode Flag should be set to True in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if remoteDiagnosticMode_StartTime == start_time:
            testResult(self, "passed", "Remote Diagnostic Mode Start time should be updated in master_conf.json file on device",
                       "Remote Diagnostic Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Remote Diagnostic Mode Start time should be updated in master_conf.json file on device",
                       "Remote Diagnostic Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if remoteDiagnosticMode_EndTime == end_time:
            testResult(self, "passed", "Remote Diagnostic Mode End time should be updated in master_conf.json file on device",
                       "Remote Diagnostic Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Remote Diagnostic Mode End time should be updated in master_conf.json file on device",
                       "Remote Diagnostic Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    elif vehicleMode == "Service":
        # Read master_conf.json file
        serviceMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "ServiceMode_Enabled", "serviceMode")
        serviceMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "ServiceMode_StartTime", "serviceMode")
        serviceMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "ServiceMode_EndTime", "serviceMode")

        print(" Service Mode - Enabled :", serviceMode_Enabled)
        print(" Service Mode - Start Time :", serviceMode_StartTime)
        print(" Service Mode - End Time :", serviceMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(serviceMode_Enabled) == enabled or bool(serviceMode_Enabled) == enabled:
            testResult(self, "passed", "Service Mode Flag should be set to True in master_conf.json file on device",
                       "Service Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Service Mode Flag should be set to True in master_conf.json file on device",
                       "Service Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if serviceMode_StartTime == start_time:
            testResult(self, "passed", "Service Mode Start time should be updated in master_conf.json file on device",
                       "Service Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Service Mode Start time should be updated in master_conf.json file on device",
                       "Service Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if serviceMode_EndTime == end_time:
            testResult(self, "passed", "Service Mode End time should be updated in master_conf.json file on device",
                       "Service Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Service Mode End time should be updated in master_conf.json file on device",
                       "Service Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    elif vehicleMode == "Privacy":
        # Read master_conf.json file
        privacyMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")
        privacyMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_StartTime", "privacyMode")
        privacyMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_EndTime", "privacyMode")

        print(" Privacy Mode - Enabled :", privacyMode_Enabled)
        print(" Privacy Mode - Start Time :", privacyMode_StartTime)
        print(" Privacy Mode - End Time :", privacyMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(privacyMode_Enabled) == enabled or bool(privacyMode_Enabled) == enabled:
            testResult(self, "passed", "Privacy Mode Flag should be set to True in master_conf.json file on device",
                       "Privacy Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode Flag should be set to True in master_conf.json file on device",
                       "Privacy Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if privacyMode_StartTime == start_time:
            testResult(self, "passed", "Privacy Mode Start time should be updated in master_conf.json file on device",
                       "Privacy Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode Start time should be updated in master_conf.json file on device",
                       "Privacy Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if privacyMode_EndTime == end_time:
            testResult(self, "passed", "Privacy Mode End time should be updated in master_conf.json file on device",
                       "Privacy Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode End time should be updated in master_conf.json file on device",
                       "Privacy Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    elif vehicleMode == "Normal":
        # Read master_conf.json file
        normalMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "NormalMode_Enabled", "normalMode")
        normalMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "NormalMode_StartTime", "normalMode")
        normalMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "NormalMode_EndTime", "normalMode")

        print(" Normal Mode - Enabled :", normalMode_Enabled)
        print(" Normal Mode - Start Time :", normalMode_StartTime)
        print(" Normal Mode - End Time :", normalMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(normalMode_Enabled) == enabled or bool(normalMode_Enabled) == enabled:
            testResult(self, "passed", "Normal Mode Flag should be set to True in master_conf.json file on device",
                       "Normal Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Normal Mode Flag should be set to True in master_conf.json file on device",
                       "Normal Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if normalMode_StartTime == start_time:
            testResult(self, "passed", "Normal Mode Start time should be updated in master_conf.json file on device",
                       "Normal Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Normal Mode Start time should be updated in master_conf.json file on device",
                       "Normal Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if normalMode_EndTime == end_time:
            testResult(self, "passed", "Normal Mode End time should be updated in master_conf.json file on device",
                       "Normal Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Normal Mode End time should be updated in master_conf.json file on device",
                       "Normal Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    else:
        print("Invalid Mode")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Fetch configuration from the vehicle configuration API
    response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body.get("message") == "Success":
            # Extract vehicle mode configuration
            if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD","GCP-QA8","GCP-QA2","RE-UAT","GCP-PERF2","GCP-QA2-EU"]:
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
            else:
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")

            # Handle each mode
            if vehicleMode == "Vacation" and "vacation_mode" in vehicle_mode:
                mode_config = vehicle_mode["vacation_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                               "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Vacation Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            elif vehicleMode == "Privacy" and "privacy_mode" in vehicle_mode:
                mode_config = vehicle_mode["privacy_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config[
                    "enabled"] == 1) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Privacy Mode Flag should be set to True in master_conf.json file on cloud",
                               "Privacy Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Privacy Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            elif vehicleMode == "Incognito" and "incognito_mode" in vehicle_mode:
                mode_config = vehicle_mode["incognito_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config[
                    "enabled"] == 1) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Incognito Mode Flag should be set to True in master_conf.json file on cloud",
                               "Incognito Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Incognito Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            elif vehicleMode == "RemoteDiagnostic" and "remote_diagnostic_mode" in vehicle_mode:
                mode_config = vehicle_mode["remote_diagnostic_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config[
                    "enabled"] == 1) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Remote Diagnostic Mode Flag should be set to True in master_conf.json file on cloud",
                               "Remote Diagnostic Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Remote Diagnostic Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            elif vehicleMode == "Service" and "service_mode" in vehicle_mode:
                mode_config = vehicle_mode["service_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config[
                    "enabled"] == 1) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Service Mode Flag should be set to True in master_conf.json file on cloud",
                               "Service Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Service Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            elif vehicleMode == "Normal" and "normal_mode" in vehicle_mode:
                mode_config = vehicle_mode["normal_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config[
                    "enabled"] == 1) and mode_config[
                    "start_time"] == start_time and mode_config[
                    "end_time"] == end_time:
                    testResult(self, "passed",
                               "Normal Mode Flag should be set to True in master_conf.json file on cloud",
                               "Normal Mode Flag is set to True in master_conf.json file on cloud")
                    assert True
                else:
                    print("Normal Mode validation failed")
                    print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=True")
                    print(f"Start time mismatch: actual={mode_config['start_time']}, expected={start_time}")
                    print(f"End time mismatch: actual={mode_config['end_time']}, expected={end_time}")
                    assert False

            else:
                print("Invalid or unsupported vehicle mode.")
                assert False
        else:
            print("Response message is not expected.Rather than found: ", response_body["message"])
            assert False
    else:
        print("Response status code is not 200, Rather than found: ", response.status_code)
        assert False
def vehicle_conf_telemetry_push_frequency_update(self, onboardingType, chipsetType, tc):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("UPDATE TELEMETRY PUSH FREQUENCY via VEHICLE CONFIGURATION API: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Test Data*

    systemId = read_vehicleJsonFile(self, "system_id")
    action = "EDIT"
    attribute = push_freq = path = value = value_dict = ""
    updateScope = "MODEL"

    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])

    # Original JSON
    if tc == "normal_mode":
        if cloudEnv in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA8", "GCP-QA5", "RE-UAT", "GCP-PERF2"]:
            path = "vehicle_settings.telemetry.normal_mode.events.3101.push_freq"
            value = updated_value = push_freq = 15000
        elif cloudEnv in ["GCP-QA2"]:
            path = "vehicle_settings.telemetry.events.3101.push_freq.normal_mode"
            value = updated_value = push_freq = 15000
        else:
            path = "vehicle_settings.telemetry.normal_mode.events.3101"
            value = "{\"batch_frequency\":0,\"batch_size\":0,\"acc_size\":0,\"acc_enable\":false,\"enable_flag\":true,\"ena_dis_op_suportd\":true,\"priority_index\":0,\"filter_plugin\":[],\"block_id\":3101,\"reason_code\":0,\"push_freq\":10000,\"ddl_budget\":0,\"ddl_timeout\":0,\"ddl_flag\":0,\"sms_flag\":false,\"qos\":1,\"msg_type\":304,\"notif_type\":-1,\"attributes\":[2404924404334067712,2404924408629035008,2404924412924002304,2404924417218969600,2404933217606959104,2405133367377920000,2405133371672887296,2405133375967854592,2405133380262821888,2405133406032625664,2405133410327592960,2405133414622560256,2405133418917527552,2405133384557789184,2405133388852756480]}"
            value_dict = json.loads(value)
            value_dict["push_freq"] = push_freq = 15000
            # Serialize back into a JSON string
            updated_value = json.dumps(value_dict)

        print("Inside normal_mode_3101")
    elif tc == "vacation_mode":
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA8", "GCP-QA5", "GCP-QA2", "RE-UAT",
                            "GCP-PERF2"]:
            path = "vehicle_settings.telemetry.vacation_mode.events.3101"
            value = "{\"batch_frequency\":1,\"batch_size\":3,\"acc_size\":0,\"acc_enable\":false,\"enable_flag\":true,\"ena_dis_op_suportd\":true,\"priority_index\":0,\"filter_plugin\":[],\"block_id\":3101,\"reason_code\":0,\"push_freq\":21600000,\"ddl_budget\":0,\"ddl_timeout\":0,\"ddl_flag\":0,\"sms_flag\":false,\"qos\":1,\"msg_type\":304,\"notif_type\":-1,\"attributes\":[2404924404334067712,2404924408629035008,2404924412924002304,2404924417218969600,2404933217606959104,2405133367377920000,2405133371672887296,2405133375967854592,2405133380262821888,2405133406032625664,2405133410327592960,2405133414622560256,2405133418917527552,2405133384557789184,2405133388852756480]}"
            value_dict = json.loads(value)
            value_dict["push_freq"] = push_freq = 20000
            # Serialize back into a JSON string
            updated_value = json.dumps(value_dict)
        elif cloudEnv in ["GCP-QA2"]:
            path = "vehicle_settings.telemetry.events.3101.push_freq.vacation_mode"
            value = updated_value = push_freq = 20000
        else:
            path = "vehicle_settings.telemetry.vacation_mode.events.3101.push_freq"
            value = updated_value = push_freq = 20000
    elif tc == "privacy_mode":
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA8", "GCP-QA5", "GCP-QA2", "RE-UAT",
                            "GCP-PERF2"]:
            path = "vehicle_settings.telemetry.privacy_mode.events.1001"
            value = "{\"batch_frequency\":0,\"batch_size\":0,\"acc_size\":0,\"acc_enable\":false,\"enable_flag\":true,\"ena_dis_op_suportd\":true,\"priority_index\":0,\"filter_plugin\":[],\"block_id\":1001,\"ddl_budget\":0,\"ddl_timeout\":0,\"ddl_flag\":0,\"sms_flag\":false,\"reason_code\":0,\"push_freq\":15000,\"qos\":1,\"msg_type\":304,\"notif_type\":-1,\"attributes\":[2396056671257362432,2405064304303800320,1252004033598586880,2405064364433342464,2405064368728309760,2405064373023277056,2405064377318244352,2405064381613211648,2405064385908178944,2405063866217136128,2405064239879290880]}"
            value_dict = json.loads(value)
            value_dict["push_freq"] = push_freq = 11000
            # Serialize back into a JSON string
            updated_value = json.dumps(value_dict)
        elif cloudEnv in ["GCP-QA2"]:
            path = "vehicle_settings.telemetry.events.6500.push_freq.privacy_mode"
            value = updated_value = push_freq = 11000
        else:
            path = "vehicle_settings.telemetry.privacy_mode.events.6500.push_freq"
            value = updated_value = push_freq = 11000
    # Parse the string into a Python dictionary

    # Dynamically update fields
    # value_dict["batch_frequency"] = batch_frequency = 5000  # Updating batch frequency

    # to 5000
    # value_dict["push_freq"] = push_freq = 15000  # Updating push frequency
    # value_dict["enable_flag"] = enable_flag = True  # Enabling acceleration flag

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", updated_value)
    print("----------------------------------------------------------")

    # call update vehicle configuration api module
    if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA8", "GCP-QA5", "GCP-QA2", "RE-UAT",
                        "GCP-PERF2"]:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")
    else:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "model_based_configuration")

    print("----------------------------------------------------------")

    # Validate response status code
    if response.status_code == 200 or response.status_code == 207:
        assert True
        # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        # Parse API response into JSON
        response_body = response.json()
        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
            print(f"Already Telemetry Conf is having the push fre value as {push_freq}")
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Parse API response into JSON
    response_body = response.json()
    # Validate response body
    trackingId = ""
    if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Telemetry Configuration - Push frequency update request should be triggered successfully",
                       "Telemetry Configuration - Push frequency update request is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed",
                   "Telemetry Configuration - Push frequency update request should be triggered successfully",
                   "Telemetry Configuration - Push frequency update request is triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    time.sleep(10)
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    # time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validations via tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                if status == "PROGRESSING":
                    testResult(self, "verificationPassed",
                               "EDIT Feature - Configuration update should be 'PROGRESSING'",
                               "EDIT Feature - Configuration update is PROGRESSING")
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)

    # Final status check
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False
    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    status = Telemetry_pushFrequency = ""

    if tc == "normal_mode":
        # Read master_conf.json file
        Telemetry_pushFrequency = read_telemetryConfJsonFile(self, cloudEnv, "pushFrequencyUpdate_3101", "normalMode")
    elif tc == "vacation_mode":
        Telemetry_pushFrequency = read_telemetryConfJsonFile(self, cloudEnv,"pushFrequencyUpdate_3101", "vacationMode")
    elif tc == "privacy_mode":
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "RE-DEV", "RE-DM1", "GCP-QA8", "GCP-QA2", "RE-UAT",
                            "GCP-PERF2"]:
            Telemetry_pushFrequency = read_telemetryConfJsonFile(self, cloudEnv, "pushFrequencyUpdate_1001", "privacyMode")
        else:
            Telemetry_pushFrequency = read_telemetryConfJsonFile(self, cloudEnv, "pushFrequencyUpdate_6500", "privacyMode")
    print("Push Frequency for Event:", Telemetry_pushFrequency)

    print("----------------------------------------------------------")

    if Telemetry_pushFrequency == push_freq:
        testResult(self, "passed",
                   "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
                   "Push frequency is updated in telemetry_conf.json file on device for event 3101")
    else:
        testResult(self, "verificationFailed",
                   "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
                   "Push frequency is not updated in telemetry_conf.json file on device for event 3101")
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")

    # Parse API response into JSON
    #response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        # Parse response body
        response_body = response.json()

        # Validate response message
        if response_body["message"] == "Success":

            # FIX: normalize tc value
            tc = tc.strip().lower().replace(" ", "_")

            vehicle_features = None

            if cloudEnv not in r8_patch4_sp17_envs:
                telemetry = response_body["configurations"]["vehicle_settings"]["telemetry"]

                if tc == "normal_mode":
                    vehicle_features = telemetry["events"]["3101"]["push_freq"]["normal_mode"]

                elif tc == "vacation_mode":
                    vehicle_features = telemetry["events"]["3101"]["push_freq"]["vacation_mode"]

                elif tc == "privacy_mode":
                    vehicle_features = telemetry["events"]["3101"]["push_freq"]["privacy_mode"]

                else:
                    testResult(
                        self, "failed",
                        "Invalid mode",
                        f"Unsupported tc value: {tc}"
                    )
                    assert False

                # ---- Validation ----
                if vehicle_features == push_freq:
                    testResult(
                        self, "passed",
                        "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
                        "Push frequency is updated in telemetry_conf.json file on device for event 3101."
                    )
                    assert True
                else:
                    testResult(
                        self, "failed",
                        "Push frequency should match the expected value",
                        f"Push frequency mismatch: Expected {push_freq}, Found {vehicle_features}"
                    )
                    assert False

            else:
                telemetry = response_body["configurations"]["vehicle_settings"]["telemetry"]

                if tc == "normal_mode":
                    vehicle_features = telemetry["events"]["3101"]["push_freq"]["normal_mode"]

                elif tc == "vacation_mode":
                    vehicle_features = telemetry["vacation_mode"]["events"]["3101"]["push_freq"]

                elif tc == "privacy_mode":
                    if any(cloudEnv in lst for lst in
                           (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
                        vehicle_features = telemetry["events"]["6500"]["push_freq"]["privacy_mode"]
                    else:
                        vehicle_features = telemetry["privacy_mode"]["events"]["6500"]["push_freq"]

                else:
                    testResult(
                        self, "failed",
                        "Invalid mode",
                        f"Unsupported tc value: {tc}"
                    )
                    assert False

                # ---- Validation ----
                if vehicle_features == push_freq:
                    testResult(
                        self, "passed",
                        "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
                        "Push frequency is updated in telemetry_conf.json file on device for event 3101."
                    )
                    assert True
                else:
                    testResult(
                        self, "failed",
                        "Push frequency should match the expected value",
                        f"Push frequency mismatch: Expected {push_freq}, Found {vehicle_features}"
                    )
                    assert False

        else:
            testResult(
                self, "failed",
                "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
                f"Unexpected response message: {response_body.get('message', 'No message available')}."
            )
            assert False

    else:
        testResult(
            self, "failed",
            "Push frequency should be updated in telemetry_conf.json file on device for event 3101",
            f"API call failed with status code {response.status_code}."
        )
        assert False

def vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                  start_time,
                                  end_time,
                                  vehicleMode):
    # ===========================================================================================
    # Trigger Vacation Mode
    # ===========================================================================================

    print("*" * 50)
    print(f"Trigger {vehicleMode} Mode via Vehicle configuration API:")
    print("*" * 50)

    # Define mode mappings
    mode_mapping = {
        "vacationMode": "valid",
        "privacyMode": "valid",
        "incognitoMode": "valid",
        "remoteDiagnosticMode": "valid",
        "serviceMode": "valid",
        "normalMode": "valid",
        "vacationMode_without_startEndTime": "without_start_end_time",
        "privacyMode_without_startEndTime": "without_start_end_time",
        "incognitoMode_without_startEndTime": "without_start_end_time",
        "remoteDiagnosticMode_without_startEndTime": "without_start_end_time",
        "serviceMode_without_startEndTime": "without_start_end_time",
        "normalMode_without_startEndTime": "without_start_end_time",
        "vacationMode_without_startTime": "without_start_time",
        "privacyMode_without_startTime": "without_start_time",
        "incognitoMode_without_startTime": "without_start_time",
        "remoteDiagnosticMode_without_startTime": "without_start_time",
        "serviceMode_without_startTime": "without_start_time",
        "normalMode_without_startTime": "without_start_time",
        "vacationMode_without_endTime": "without_end_time",
        "privacyMode_without_endTime": "without_end_time",
        "incognitoMode_without_endTime": "without_end_time",
        "remoteDiagnosticMode_without_endTime": "without_end_time",
        "serviceMode_without_endTime": "without_end_time",
        "normalMode_without_endTime": "without_end_time"
    }

    # Call the relevant API based on mode
    response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(
        self, action, path, enabled, start_time, end_time, systemId, mode_mapping.get(vehicleMode, "unknown_mode")
    )

    print("----------------------------------------------------------")

    # Parse and validate API response
    response_body = response.json()

    if response.status_code == 200 and (
            response_body.get("status") == "Progressing" or response_body.get("status") == "PROGRESSING"):
        trackingId = response_body.get("trackingId", "")
        print(f"trackingId: {trackingId}")
        testResult(self, "verificationPassed",
                   f"{vehicleMode} Mode - Configuration update triggered successfully",
                   f"{vehicleMode} Mode - Configuration update is triggered successfully")
        assert True
    else:
        testResult(self, "failed",
                   f"{vehicleMode} Mode - Configuration update should be triggered successfully",
                   f"{vehicleMode} Mode - Configuration update is not triggered successfully")
        print("Response status or body validation failed.")
        assert False

    print("----------------------------------------------------------")

    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    checksums = {
        "device_checksum": "successfully got checksum of the file",
        "cloud_checksum": "successfully got cloud checksum",
        "checksum_validation_status": "checksum validation"
    }

    for key, message in checksums.items():
        print(f"Validating {key}:")
        ls = verify_message_in_log(self, message, message)
        if message in str(ls[0]):
            print(f" => {key.capitalize()} successfully validated.")
            testResult(self, "verificationPassed",
                       f"Validate that {key} is successfully received and validated",
                       f"{key.capitalize()} is successfully validated. Refer to device logs for details.")
            print("c2c logs line data: =>", ls[0])
        elif str(ls[0]) == "Error":
            print(f" => Failed to validate {key}.")
            testResult(self, "verificationFailed",
                       f"Validate that {key} is successfully received and validated",
                       f"Failed to validate {key}. Log file might not be updated. Refer to device logs for details.")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validation via Tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    for i in range(5):
        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        print(response.status_code)

        print("----------------------------------------------------------")

        # Validate response status code
        if response.status_code == 200 or response.status_code == 207:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["results"][0]["status"] == "PROGRESSING":
            testResult(self, "verificationPassed",
                       f"{vehicleMode} Mode - Configuration update should  be 'PROGRESSING'",
                       f"{vehicleMode} Mode - Configuration update is PROGRESSING")
        # Validate response body
        elif response_body["results"][0]["status"] == "COMPLETED":
            break

        time.sleep(10)

    # Validate response body
    if response_body["results"][0]["status"] == "COMPLETED":
        testResult(self, "passed", f"{vehicleMode} Mode - Configuration update should success/completed",
                   f"{vehicleMode} Mode - Configuration update is success/completed")
        assert True
        # self.result.set_result(TestResults.passed)
    elif response_body["results"][0]["status"] == "FAILED":
        testResult(self, "failed", f"{vehicleMode} Mode - Configuration update should success/completed",
                   f"{vehicleMode} Mode - Configuration update is not success/completed")
        # self.result.set_result(TestResults.passed)
        assert False
    else:
        print("Something went wrong, Please check API Response for more details")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print(f"Validate {vehicleMode} mode is enabled in master_conf.json:")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    # Define mapping for keys and attributes
    vehicle_mode_mapping = {
        "vacationMode": {
            "Enabled": "VacationMode_Enabled",
            "StartTime": "VacationMode_StartTime",
            "EndTime": "VacationMode_EndTime",
            "mode_key": "vacationMode"
        },
        "vacationMode_without_startEndTime": {
            "Enabled": "VacationMode_Enabled",
            "mode_key": "vacationMode_without_startEndTime"
        },
        "vacationMode_without_startTime": {
            "Enabled": "VacationMode_Enabled",
            "StartTime": "VacationMode_EndTime",
            "mode_key": "vacationMode_without_startTime"
        },
        "vacationMode_without_endTime": {
            "Enabled": "VacationMode_Enabled",
            "EndTime": "VacationMode_StartTime",
            "mode_key": "vacationMode_without_endTime"
        },
        "incognitoMode": {
            "Enabled": "IncognitoMode_Enabled",
            "StartTime": "IncognitoMode_StartTime",
            "EndTime": "IncognitoMode_EndTime",
            "mode_key": "incognitoMode"
        },
        "incognitoMode_without_startEndTime": {
            "Enabled": "IncognitoMode_Enabled",
            "mode_key": "incognitoMode_without_startEndTime"
        },
        "incognitoMode_without_startTime": {
            "Enabled": "IncognitoMode_Enabled",
            "StartTime": "IncognitoMode_EndTime",
            "mode_key": "incognitoMode_without_startTime"
        },
        "incognitoMode_without_endTime": {
            "Enabled": "IncognitoMode_Enabled",
            "EndTime": "IncognitoMode_StartTime",
            "mode_key": "incognitoMode_without_endTime"
        },
        "privacyMode": {
            "Enabled": "PrivacyMode_Enabled",
            "StartTime": "PrivacyMode_StartTime",
            "EndTime": "PrivacyMode_EndTime",
            "mode_key": "privacyMode"
        },
        "privacyMode_without_startEndTime": {
            "Enabled": "PrivacyMode_Enabled",
            "mode_key": "privacyMode_without_startEndTime"
        },
        "privacyMode_without_startTime": {
            "Enabled": "PrivacyMode_Enabled",
            "StartTime": "PrivacyMode_EndTime",
            "mode_key": "privacyMode_without_startTime"
        },
        "privacyMode_without_endTime": {
            "Enabled": "PrivacyMode_Enabled",
            "EndTime": "PrivacyMode_StartTime",
            "mode_key": "privacyMode_without_endTime"
        },
        "remoteDiagnosticMode": {
            "Enabled": "RemoteDiagnosticMode_Enabled",
            "StartTime": "RemoteDiagnosticMode_StartTime",
            "EndTime": "RemoteDiagnosticMode_EndTime",
            "mode_key": "remoteDiagnosticMode"
        },
        "remoteDiagnosticMode_without_startEndTime": {
            "Enabled": "RemoteDiagnosticMode_Enabled",
            "mode_key": "remoteDiagnosticMode_without_startEndTime"
        },
        "remoteDiagnosticMode_without_startTime": {
            "Enabled": "RemoteDiagnosticMode_Enabled",
            "StartTime": "RemoteDiagnosticMode_EndTime",
            "mode_key": "remoteDiagnosticMode_without_startTime"
        },
        "remoteDiagnosticMode_without_endTime": {
            "Enabled": "RemoteDiagnosticMode_Enabled",
            "EndTime": "RemoteDiagnosticMode_StartTime",
            "mode_key": "remoteDiagnosticMode_without_endTime"
        },
        "serviceMode": {
            "Enabled": "ServiceMode_Enabled",
            "StartTime": "ServiceMode_StartTime",
            "EndTime": "ServiceMode_EndTime",
            "mode_key": "serviceMode"
        },
        "serviceMode_without_startEndTime": {
            "Enabled": "ServiceMode_Enabled",
            "mode_key": "serviceMode_without_startEndTime"
        },
        "serviceMode_without_startTime": {
            "Enabled": "ServiceMode_Enabled",
            "StartTime": "ServiceMode_EndTime",
            "mode_key": "serviceMode_without_startTime"
        },
        "serviceMode_without_endTime": {
            "Enabled": "ServiceMode_Enabled",
            "EndTime": "ServiceMode_StartTime",
            "mode_key": "serviceMode_without_endTime"
        },
        "normalMode": {
            "Enabled": "NormalMode_Enabled",
            "StartTime": "NormalMode_StartTime",
            "EndTime": "NormalMode_EndTime",
            "mode_key": "normalMode"
        },
        "normalMode_without_startEndTime": {
            "Enabled": "NormalMode_Enabled",
            "mode_key": "normalMode_without_startEndTime"
        },
        "normalMode_without_startTime": {
            "Enabled": "NormalMode_Enabled",
            "StartTime": "NormalMode_EndTime",
            "mode_key": "normalMode_without_startTime"
        },
        "normalMode_without_endTime": {
            "Enabled": "NormalMode_Enabled",
            "EndTime": "NormalMode_StartTime",
            "mode_key": "normalMode_without_endTime"
        }
    }

    if vehicleMode in vehicle_mode_mapping:
        mode_config = vehicle_mode_mapping[vehicleMode]
        status = "PASS"

        # Validate 'Enabled' flag
        if "Enabled" in mode_config and start_time is not None:
            if cloudEnv not in ["GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT", "GCP-PERF2"]:
                enabled_value = read_masterConfJsonFile_v2(self, cloudEnv, mode_config["Enabled"],
                                                           mode_config["mode_key"])
                print(f"{vehicleMode} Mode - Enabled: {enabled_value}")
                if enabled is not None and (str(enabled_value) == enabled or bool(enabled_value) == enabled):
                    testResult(self, "passed",
                               f"{vehicleMode} Mode Flag should be set to {enabled} in master_conf.json file on device",
                               f"{vehicleMode} Mode Flag is set to {enabled} in master_conf.json file on device")
                    status = "PASS"

        # Validate 'StartTime' if applicable
        if "StartTime" in mode_config and start_time is not None:
            start_time_value = read_masterConfJsonFile_v2(self, cloudEnv, mode_config["StartTime"],
                                                          mode_config["mode_key"])
            print(f"{vehicleMode} Mode - Start Time: {start_time_value}")
            if start_time_value == start_time:
                testResult(self, "passed",
                           f"{vehicleMode} Mode Start time should be updated in master_conf.json file on device",
                           f"{vehicleMode} Mode Start time is updated in master_conf.json file on device")
                status = "PASS"

        # Validate 'EndTime' if applicable
        if "EndTime" in mode_config and end_time is not None:
            end_time_value = read_masterConfJsonFile_v2(self, cloudEnv, mode_config["EndTime"], mode_config["mode_key"])
            print(f"{vehicleMode} Mode - End Time: {end_time_value}")
            if end_time_value != end_time:
                testResult(self, "verificationFailed",
                           f"{vehicleMode} Mode End time should be updated in master_conf.json file on device",
                           f"{vehicleMode} Mode End time is not updated in master_conf.json file on device")
                status = "FAIL"

        print("----------------------------------------------------------")
        if status == "PASS":
            testResult(self, "passed", f"{vehicleMode} Mode validation passed in master_conf.json",
                       f"{vehicleMode} Mode configuration is correctly updated in master_conf.json.")
            assert True
        else:
            assert False
    else:
        print(f"[ERROR] Unsupported vehicle mode: {vehicleMode}")
        assert False

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the Cloud via Vehicle Configuration API:")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Fetch configuration from the vehicle configuration API
    response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    # Validate response status code
    if response.status_code == 200 and response_body.get("message") == "Success":
        # Define mapping for vehicle modes and their respective keys
        vehicle_modes = {
            "vacationMode": ["vacation_mode", ["enabled", "start_time", "end_time"]],
            "vacationMode_without_startEndTime": ["vacation_mode", ["enabled"]],
            "vacationMode_without_startTime": ["vacation_mode", ["enabled", "end_time"]],
            "vacationMode_without_endTime": ["vacation_mode", ["enabled", "start_time"]],
            "privacyMode": ["privacy_mode", ["enabled", "start_time", "end_time"]],
            "privacyMode_without_startEndTime": ["privacy_mode", ["enabled"]],
            "privacyMode_without_startTime": ["privacy_mode", ["enabled", "end_time"]],
            "privacyMode_without_endTime": ["privacy_mode", ["enabled", "start_time"]],
            "incognitoMode": ["incognito_mode", ["enabled", "start_time", "end_time"]],
            "incognitoMode_without_startEndTime": ["incognito_mode", ["enabled"]],
            "incognitoMode_without_startTime": ["incognito_mode", ["enabled", "end_time"]],
            "incognitoMode_without_endTime": ["incognito_mode", ["enabled", "start_time"]],
            "remoteDiagnosticMode": ["remote_diagnostic_mode", ["enabled", "start_time", "end_time"]],
            "remoteDiagnosticMode_without_startEndTime": ["remote_diagnostic_mode", ["enabled"]],
            "remoteDiagnosticMode_without_startTime": ["remote_diagnostic_mode", ["enabled", "end_time"]],
            "remoteDiagnosticMode_without_endTime": ["remote_diagnostic_mode", ["enabled", "start_time"]],
            "serviceMode": ["service_mode", ["enabled", "start_time", "end_time"]],
            "serviceMode_without_startEndTime": ["service_mode", ["enabled"]],
            "serviceMode_without_startTime": ["service_mode", ["enabled", "end_time"]],
            "serviceMode_without_endTime": ["service_mode", ["enabled", "start_time"]],
            "normalMode": ["normal_mode", ["enabled", "start_time", "end_time"]],
            "normalMode_without_startEndTime": ["normal_mode", ["enabled"]],
            "normalMode_without_startTime": ["normal_mode", ["enabled", "end_time"]],
            "normalMode_without_endTime": ["normal_mode", ["enabled", "start_time"]]
        }

        # Fetch mode-specific key and attributes to validate
        vehicle_mode_data = vehicle_modes.get(vehicleMode, None)
        if vehicle_mode_data:
            vehicle_mode_key, attributes_to_validate = vehicle_mode_data

            # Check if the mode exists in the cloud response
            if cloudEnv not in ["GCP-QA4", 'GCP-QA5', "GCP-QA8", "GCP-QA2", "RE-UAT", "GCP-PERF2"]:
                if vehicle_mode_key in response_body["configurations"]["vehicle_settings"]["vehicle_mode"]:
                    mode_config = response_body["configurations"]["vehicle_settings"]["vehicle_mode"][vehicle_mode_key]

                    # Generalized validation for attributes
                    status = "PASS"
                    for attribute in attributes_to_validate:
                        expected_value = locals().get(
                            attribute)  # Fetch expected value dynamically (e.g., enabled, start_time)
                        actual_value = mode_config.get(attribute, None)

                        if actual_value is not None:  # Only validate if the attribute exists in the cloud configuration
                            if str(actual_value).lower() != str(expected_value).lower():
                                print(
                                    f"[ERROR] Mismatch for {attribute}: Expected({expected_value}) vs Actual({actual_value})")
                                testResult(self, "failed",
                                           f"{vehicleMode} Mode - {attribute} validation failed",
                                           f"Mismatch found: Expected({expected_value}) vs Actual({actual_value})")
                                status = "FAIL"
                            else:
                                print(
                                    f"[DEBUG] Match for {attribute}: Expected({expected_value}) == Actual({actual_value})")
                        else:
                            print(f"[WARNING] {attribute} not found in the configuration, skipping validation.")

                    if status == "PASS":
                        testResult(self, "passed",
                                   f"{vehicleMode} Mode validation passed in master_conf.json file on cloud",
                                   f"{vehicleMode} Mode configuration is consistent with expectations in cloud")
                        assert True
                    else:
                        assert False
                else:
                    print(f"[ERROR] Vehicle mode key '{vehicle_mode_key}' is not found in the cloud configuration.")
                    assert False
            else:
                if vehicle_mode_key in response_body["configurations"]["vehicle_settings"]["user_settings"][
                    "vehicle_mode"]:
                    mode_config = response_body["configurations"]["vehicle_settings"]["user_settings"]["vehicle_mode"][
                        vehicle_mode_key]

                    # Generalized validation for attributes
                    status = "PASS"
                    for attribute in attributes_to_validate:
                        expected_value = locals().get(
                            attribute)  # Fetch expected value dynamically (e.g., enabled, start_time)
                        actual_value = mode_config.get(attribute, None)

                        if actual_value is not None:  # Only validate if the attribute exists in the cloud configuration
                            if str(actual_value).lower() != str(expected_value).lower():
                                print(
                                    f"[ERROR] Mismatch for {attribute}: Expected({expected_value}) vs Actual({actual_value})")
                                testResult(self, "failed",
                                           f"{vehicleMode} Mode - {attribute} validation failed",
                                           f"Mismatch found: Expected({expected_value}) vs Actual({actual_value})")
                                status = "FAIL"
                            else:
                                print(
                                    f"[DEBUG] Match for {attribute}: Expected({expected_value}) == Actual({actual_value})")
                        else:
                            print(f"[WARNING] {attribute} not found in the configuration, skipping validation.")

                    if status == "PASS":
                        testResult(self, "passed",
                                   f"{vehicleMode} Mode validation passed in master_conf.json file on cloud",
                                   f"{vehicleMode} Mode configuration is consistent with expectations in cloud")
                        assert True
                    else:
                        assert False
                else:
                    print(f"[ERROR] Vehicle mode key '{vehicle_mode_key}' is not found in the cloud configuration.")
                    assert False
        else:
            print(f"[ERROR] Unsupported or invalid vehicle mode: {vehicleMode}")
            assert False
    else:
        print("[ERROR] Failed to fetch configuration or unexpected response message.")
        assert False

def validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq):
    print("*" * 50)
    print("Validation telemetry push frequency on the device:")
    print("*" * 50)

    timestamps = []

    # Extract timestamps for all matching log entries
    for telemetry_msg in telemetry_msgs:
        try:
            with open(C2CtestReport_c2cLogsPath + 'c2clogs.txt', 'r') as logfile:
                log_entries = []
                for line in logfile:
                    if telemetry_msg in line:
                        log_entries.append(line)  # Collect all matching lines

                if not log_entries:
                    print(f"No matching log entries found for '{telemetry_msg}'.")
                    continue

                print(f"Found {len(log_entries)} occurrences of '{telemetry_msg}'.")

                # Process each log entry
                for log_entry in log_entries:
                    try:
                        # Extract and parse the timestamp
                        timestamp_str = log_entry.split()[0] + " " + log_entry.split()[
                            1]  # Example: "03-28 05:58:30.827"
                        timestamp = datetime.strptime(timestamp_str, "%m-%d %H:%M:%S.%f")
                        timestamps.append(timestamp)
                        print(f"Extracted Timestamp: {timestamp}")
                    except ValueError as e:
                        print(f"Timestamp Parsing Failed for '{log_entry}': {str(e)}")

        except Exception as e:
            print(f"Exception while processing telemetry message '{telemetry_msg}': {str(e)}")

    # Validate timestamps
    if len(timestamps) < 2:
        print("Not enough timestamps were extracted. Validation failed.")
        return

    time_differences = []
    timestamps.sort()  # Ensure timestamps are sorted before calculating differences

    for i in range(1, len(timestamps)):
        time_diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
        time_differences.append(time_diff)
        print(f"Time Difference Between Event {i} and Event {i + 1}: {time_diff} seconds")

        # Validate against the expected frequency of 15 seconds
        if abs(time_diff - (push_freq / 1000)) <= 0.01:  # Allow tolerance of ±0.01 seconds
            testResult(self, "verificationPassed",
                       f"Validate telemetry message frequency for event '{event_id}'",
                       f"Telemetry message frequency is valid: {time_diff} seconds.")
        else:
            testResult(self, "verificationFailed",
                       f"Validate telemetry message frequency for event '{event_id}'",
                       f"Telemetry message frequency mismatch: Expected {push_freq / 1000} seconds, Found {time_diff} seconds.")
            print(f"Telemetry message frequency mismatch: Expected {push_freq / 1000} seconds, Found {time_diff}.")

    # Summary Output
    print("\n[SUMMARY OF TIME DIFFERENCES]")
    if time_differences:
        for i, diff in enumerate(time_differences, start=1):
            print(f"Event {i} to Event {i + 1}: {diff} seconds.")
    else:
        print("No time differences were calculated. Ensure multiple log entries exist.")

def validate_device_telemetry_message_v2(self, systemId, eventType, start, stop, offset, limit, push_freq):
    # Call reusable module
    response = get_telemetry_history_details(self, systemId, eventType, start, stop, offset, limit, "valid")

    response_body = response.json()

    print("*" * 50)
    print("Validation telemetry push frequency using API response:")
    print("*" * 50)

    timestamps = []

    # Extract timestamps
    for entry in response_body.get("telemetryHistoryDataList", []):
        time_val = entry.get("time")

        if time_val:
            try:
                timestamp = datetime.fromtimestamp(time_val / 1000)
                timestamps.append(timestamp)
                print(f"Extracted Time: {timestamp}")
            except Exception as e:
                print(f"Time conversion error: {time_val} | Error: {e}")

    # Validate count
    if len(timestamps) < 2:
        msg = "Not enough timestamps to validate frequency."
        print(msg)
        testResult(
            self,
            "failed",
            f"Telemetry frequency validation - {eventType}",
            msg
        )
        return

    # Sort timestamps
    timestamps.sort()

    expected_interval = push_freq / 1000
    tolerance = 1  # seconds

    time_differences = []
    failure_count = 0

    # Calculate differences with detailed debug
    for i in range(1, len(timestamps)):
        prev_ts = timestamps[i - 1]
        curr_ts = timestamps[i]

        diff = (curr_ts - prev_ts).total_seconds()
        time_differences.append(diff)

        deviation = diff - expected_interval

        print(f"Event {i} → {i + 1}: {diff:.3f} sec")

        #  Build detailed debug message
        debug_message = (
            f"\nEvent Index        : {i} -> {i+1}"
            f"\nPrevious Timestamp : {prev_ts}"
            f"\nCurrent Timestamp  : {curr_ts}"
            f"\nExpected Interval  : {expected_interval:.3f} sec"
            f"\nActual Interval    : {diff:.3f} sec"
            f"\nDeviation          : {deviation:.3f} sec"
            f"\nTolerance Allowed  : ±{tolerance} sec"
        )

        if abs(diff - expected_interval) <= tolerance:
            testResult(
                self,
                "passed",
                f"Telemetry frequency validation - {eventType}",
                "PASS" + debug_message
            )
        else:
            failure_count += 1
            testResult(
                self,
                "failed",
                f"Telemetry frequency validation - {eventType}",
                "FAIL " + debug_message
            )

    # Summary (very helpful for debugging)
    print("\n[SUMMARY]")
    print(f"Total Events Checked : {len(time_differences)}")
    print(f"Failures             : {failure_count}")

    for i, diff in enumerate(time_differences, 1):
        print(f"{i}: {diff:.3f} sec")

    # Final overall result (optional but very useful)
    if failure_count == 0:
        testResult(
            self,
            "passed",
            f"Telemetry frequency validation summary - {eventType}",
            f"All {len(time_differences)} intervals are within tolerance."
        )
    else:
        testResult(
            self,
            "failed",
            f"Telemetry frequency validation summary - {eventType}",
            f"{failure_count} out of {len(time_differences)} intervals failed."
        )

def vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, tc):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("UPDATE PRECONDITION FOR COMMAND via VEHICLE CONFIGURATION API: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Test Data*

    systemId = read_vehicleJsonFile(self, "system_id")
    action = "EDIT"
    attribute = d_device = path = value = value_dict = ""

    updateScope = "MODEL"
    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])
    # Original JSON
    if cloudEnv not in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "RE-DEV", "RE-DM1", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT",
                        "GCP-PERF2"]:
        if tc == "normal_mode":
            path = "vehicle_settings.remote_operations.normal_mode.condition.0"
            value = "{\"d_device\":10.0,\"area_device\":0,\"oper_req\":0,\"dtype_dev\":2,\"datatype\":1,\"area_req\":0,\"cond_idx\":0,\"cond_desc\":\"SPEED\",\"oper_device\":0,\"area_id\":0,\"d_req\":1,\"property_id\":291504647}"
            value_dict = json.loads(value)
            value_dict["d_device"] = d_device = 10.0
        elif tc == "vacation_mode":
            path = "vehicle_settings.remote_operations.vacation_mode.condition.0"
            value = "{\"d_device\":50.0,\"area_device\":0,\"oper_req\":0,\"dtype_dev\":2,\"datatype\":1,\"area_req\":0,\"cond_idx\":0,\"cond_desc\":\"SPEED\",\"oper_device\":0,\"area_id\":0,\"d_req\":1,\"property_id\":291504647}"
            value_dict = json.loads(value)
            value_dict["d_device"] = d_device = 10.0
        elif tc == "privacy_mode":
            path = "vehicle_settings.remote_operations.privacy_mode.condition.0"
            value = "{\"d_device\":50.0,\"area_device\":0,\"oper_req\":0,\"dtype_dev\":2,\"datatype\":1,\"area_req\":0,\"cond_idx\":0,\"cond_desc\":\"SPEED\",\"oper_device\":0,\"area_id\":0,\"d_req\":1,\"property_id\":291504647}"
            value_dict = json.loads(value)
            value_dict["d_device"] = d_device = 10.0
        elif tc == "incognito_mode":
            path = "vehicle_settings.remote_operations.incognito_mode.condition.0"
            value = "{\"d_device\":50.0,\"area_device\":0,\"oper_req\":0,\"dtype_dev\":2,\"datatype\":1,\"area_req\":0,\"cond_idx\":0,\"cond_desc\":\"SPEED\",\"oper_device\":0,\"area_id\":0,\"d_req\":1,\"property_id\":291504647}"
            value_dict = json.loads(value)
            value_dict["d_device"] = d_device = 10.0
    else:
        if tc == "normal_mode":
            path = "vehicle_settings.remote_operations.normal_mode.condition.0.d_device"
            value = d_device = "10.0"
        elif tc == "vacation_mode":
            path = "vehicle_settings.remote_operations.vacation_mode.condition.0.d_device"
            value = "10.0"
            d_device = 10.0
        elif tc == "privacy_mode":
            path = "vehicle_settings.remote_operations.privacy_mode.condition.0.d_device"
            value = "10.0"
            d_device = 10.0
        elif tc == "incognito_mode":
            path = "vehicle_settings.remote_operations.incognito_mode.condition.0.d_device"
            value = "10.0"
            d_device = 10.0

    # Serialize back into a JSON string
    updated_value = json.dumps(value_dict)

    # Print the updated JSON string
    print(f"Updated Value: {updated_value}")

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", updated_value)
    print("----------------------------------------------------------")

    # call update vehicle configuration api module
    if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT",
                        "GCP-PERF2"]:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")
    else:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "model_based_configuration")

    print("----------------------------------------------------------")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200 or response.status_code == 207:
        assert True
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Command Configuration - Precondition update request should be triggered successfully",
                       "Command Configuration - Precondition update request is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed",
                   "Command Configuration - Precondition update update request should be triggered successfully",
                   "Command Configuration - Precondition update update request is triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    time.sleep(30)
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validations via tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                if status == "PROGRESSING":
                    testResult(self, "verificationPassed",
                               "EDIT Feature - Configuration update should be 'PROGRESSING'",
                               "EDIT Feature - Configuration update is PROGRESSING")
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)

    # Final status check
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False
    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    status = Command_preconditionForSpeed = ""

    if tc == "normal_mode":
        # Read master_conf.json file
        Command_preconditionForSpeed = read_commandConfJsonFile(self, "d_device_update_speed", "normalMode")
    elif tc == "vacation_mode":
        Command_preconditionForSpeed = read_commandConfJsonFile(self, "d_device_update_speed", "vacationMode")
    elif tc == "privacy_mode":
        Command_preconditionForSpeed = read_commandConfJsonFile(self, "d_device_update_speed", "privacyMode")
    elif tc == "incognito_mode":
        Command_preconditionForSpeed = read_commandConfJsonFile(self, "d_device_update_speed", "incognitoMode")
    print("Command Precondition For Speed [ d-device ]:", Command_preconditionForSpeed)

    print("----------------------------------------------------------")

    if Command_preconditionForSpeed == d_device:
        testResult(self, "passed",
                   "Command Precondition For Speed should be updated in command_conf.json file on device",
                   "Command Precondition For Speed is updated in command_conf.json file on device for event 3101")
    else:
        testResult(self, "verificationFailed",
                   "Command Precondition For Speed should be updated in command_conf.json file on device",
                   "Command Precondition For Speed is not updated in command_conf.json file on device")
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_getConfig_new(self, systemId, "command_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        # Parse response body
        response_body = response.json()

        # Validate response message
        if response_body["message"] == "Success":
            conditions = ""
            if tc == "normal_mode":
                conditions = \
                    response_body["configurations"]["vehicle_settings"]["remote_operations"]["normal_mode"]["condition"]
            elif tc == "vacation_mode":
                conditions = \
                    response_body["configurations"]["vehicle_settings"]["remote_operations"]["vacation_mode"][
                        "condition"]
            elif tc == "privacy_mode":
                conditions = \
                    response_body["configurations"]["vehicle_settings"]["remote_operations"]["privacy_mode"][
                        "condition"]
            elif tc == "incognito_mode":
                conditions = \
                    response_body["configurations"]["vehicle_settings"]["remote_operations"]["incognito_mode"][
                        "condition"]
            # Check if 'push_freq' key exists
            if "0" in conditions:
                try:
                    # Retrieve "d_device" using key "0"
                    d_device_actual = conditions["0"]["d_device"]
                    if d_device_actual == d_device:
                        testResult(self, "passed",
                                   "Command Precondition for speed should be updated in command_conf.json file on device",
                                   "Command Precondition for speed is updated in command_conf.json file on device.")
                        assert True
                    else:
                        testResult(self, "failed",
                                   "Command Precondition for speed should match the expected value",
                                   f"Command Precondition for speed value mismatch: Expected {d_device}, Found {d_device_actual}.")
                        assert False, f"Command Precondition for speed mismatch: Expected {d_device}, Found {d_device_actual}."
                except KeyError as e:
                    print(f"Error accessing 'd_device': {e}")
                    testResult(self, "failed",
                               "Command Precondition for speed should be updated in command_conf.json file on device",
                               f"'d_device' key is missing in condition '0': {e}")
                    assert False, f"'d_device' key is missing in condition '0': {e}"
            else:
                print("'condition' does not contain key '0' for 'normal_mode'.")
                testResult(self, "failed",
                           "Command Precondition for speed should be updated in command_conf.json file on device",
                           "'condition' does not contain key '0' for 'normal_mode'.")
                assert False, "'condition' does not contain key '0' for 'normal_mode'."

        else:
            # Fail the test for unexpected response message
            testResult(self, "failed",
                       "Command Precondition for speed should be updated in command_conf.json file on device",
                       f"Unexpected response message: {response_body.get('message', 'No message available')}.")
            # self.result.set_result(TestResults.failed)
            assert False, f"Unexpected response message: {response_body.get('message', 'No message available')}."
    else:
        # Fail the test for invalid status code
        testResult(self, "failed",
                   "Command Precondition for speed should be updated in command_conf.json file on device",
                   f"API call failed with status code {response.status_code}.")
        # self.result.set_result(TestResults.failed)
        assert False, f"API call failed with status code {response.status_code}."

def vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, tc):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("UPDATE THRESHOLD LIMIT FOR OVER SPEED via VEHICLE CONFIGURATION API: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Test Data*

    systemId = read_vehicleJsonFile(self, "system_id")
    action = "EDIT"
    path = value = attribute = ""
    lower_limit = 90.0
    updateScope = "MODEL"

    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])

    if tc == "normal_mode" or tc == "vacation_mode" or tc == "privacy_mode" or tc == "incognito_mode":
        path = "vehicle_settings.alert_configurations.alerts.4.alert_logic.alert_reg"
        value = {
            "flags": "0x17",
            "data_id": "1252002925497024512",
            "threshold": [
                {
                    "action": "0x04",
                    "type": "0x08",
                    "one_shot_flag": "0x40",
                    "upper_limit_data": 0,
                    "lower_limit_data": lower_limit,
                    "reason_code": [103],
                    "block_id": [4445],
                    "index": 0
                }
            ]
        }
    # Update the lower_limit_data
    # value['threshold'][0]['lower_limit_data'] = lower_limit

    # Serialize back into a JSON string
    # updated_value = json.dumps(value, separators=(',', ':'))
    # Print the updated JSON string
    # print(f"Updated Value: {value}")

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", value)
    print("----------------------------------------------------------")

    # call update vehicle configuration api module
    if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT",
                        "GCP-PERF2"]:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")
    else:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "model_based_configuration")

    print("----------------------------------------------------------")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200 or response.status_code == 207:
        assert True
        # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
            print(f"Already Alert Conf is having the priority value as {lower_limit}")
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Alert Configuration - Over speed limit update request should be triggered successfully",
                       "Alert Configuration - Over speed limit update request is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed",
                   "Alert Configuration - Over speed limit update request should be triggered successfully",
                   "Alert Configuration - Over speed limit update request is triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validations via tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                if status == "PROGRESSING":
                    testResult(self, "verificationPassed",
                               "EDIT Feature - Configuration update should be 'PROGRESSING'",
                               "EDIT Feature - Configuration update is PROGRESSING")
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)

    # Final status check
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False
    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    status = Alert_overSpeedThreshold = ""

    if tc == "normal_mode" or tc == "vacation_mode" or tc == "privacy_mode" or tc == "incognito_mode":
        # Read master_conf.json file
        Alert_overSpeedThreshold = read_alertConfJsonFile(self, "over_speed_limit", "normalMode")
    print("Over Speed Limit:", Alert_overSpeedThreshold)

    print("----------------------------------------------------------")

    if Alert_overSpeedThreshold == lower_limit:
        testResult(self, "passed",
                   "Over Speed lower limit should be updated in alert_conf.json file on device",
                   "Over Speed lower limit is updated in alert_conf.json file on device")
    else:
        testResult(self, "verificationFailed",
                   "Over Speed lower limit should be updated in alert_conf.json file on device",
                   "Over Speed lower limit is not updated in alert_conf.json file on device")
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_getConfig_new(self, systemId, "alert_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        # Parse response body
        response_body = response.json()

        # Validate response message
        if response_body["message"] == "Success":
            vehicle_features = ""
            if tc == "normal_mode" or tc == "vacation_mode" or tc == "privacy_mode" or tc == "incognito_mode":
                vehicle_features = \
                    response_body["configurations"]["vehicle_settings"]["alert_configurations"]["alerts"]["4"][
                        "alert_logic"]["alert_reg"]["threshold"][0]

            # Check if 'push_freq' key exists
            if "lower_limit_data" in vehicle_features:
                if vehicle_features['lower_limit_data'] == lower_limit:
                    testResult(self, "passed",
                               "Over speed limit should be updated in alert_conf.json file on device",
                               "Over speed limit is updated in alert_conf.json file on device")
                    assert True
                else:
                    # Fail the test if 'push_freq' value does not match
                    testResult(self, "failed",
                               "Over speed limit should match the expected value",
                               f"Over speed limit value mismatch: Expected {lower_limit}, Found {vehicle_features['lower_limit_data']}.")
                    # self.result.set_result(TestResults.failed)
                    assert False, f"Over speed limit mismatch: Expected {lower_limit}, Found {vehicle_features['lower_limit_data']}."
            else:
                # Fail the test if 'push_freq' key is missing
                testResult(self, "failed",
                           "Over speed limit should be updated in alert_conf.json file on device",
                           "Over speed limit key is missing in alert_conf.json file.")
                # self.result.set_result(TestResults.failed)
                assert False, "'lower_limit_data' key is missing in alert_conf.json."
        else:
            # Fail the test for unexpected response message
            testResult(self, "failed",
                       "Over speed limit should be updated in alert_conf.json file on device",
                       f"Unexpected response message: {response_body.get('message', 'No message available')}.")
            # self.result.set_result(TestResults.failed)
            assert False, f"Unexpected response message: {response_body.get('message', 'No message available')}."
    else:
        # Fail the test for invalid status code
        testResult(self, "failed",
                   "Over speed limit should be updated in alert_conf.json file on device",
                   f"API call failed with status code {response.status_code}.")
        # self.result.set_result(TestResults.failed)
        assert False, f"API call failed with status code {response.status_code}."

def vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, tc, option):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("ADD/REMOVE NEW TELEMETRY BLOCK via VEHICLE CONFIGURATION API: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Test Data*

    systemId = read_vehicleJsonFile(self, "system_id")

    # path = "vehicle_settings.telemetry.vacation_mode.events"
    attribute = "126"
    path = value = ""
    updateScope = "MODEL"

    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])

    # Original JSON
    if tc == "normal_mode":
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            action = "ADD"
            if cloudEnv in r8_patch4_sp17_envs:
                path = "vehicle_settings.telemetry.events"
                value = {"batch_frequency":0,"batch_size":0,"acc_size":0,"acc_enable":False,"enable_flag":{"normal_mode":1,"vacation_mode":1,"privacy_mode":0,"incognito_mode":0,"remote_diagnostic_mode":1,"service_mode":1},"ena_dis_op_suportd":True,"priority_index":0,"filter_plugin":[],"block_id":3101,"reason_code":0,"push_freq":{"normal_mode":5000,"vacation_mode":10000,"privacy_mode":10000,"incognito_mode":10000,"remote_diagnostic_mode":10000,"service_mode":10000},"ddl_budget":0,"ddl_timeout":0,"ddl_flag":0,"sms_flag":0,"hmi_flag":0,"msg_type":304,"tele_flag":0,"notif_type":0,"attributes":[2396058015582126080,2404924404334067712,2404924408629035008,2404924412924002304,2404924417218969600,2404933217606959104,2382615369241067520,2382615373536034816,2382615377831002112,2396073365795241984,2400629780635451392,2405133406032625664,2405133410327592960,2405133414622560256,2405133418917527552,2382615386420936704,2382615390715904000,2382615395010871296,2382615399305838592,2382615403600805888,2382615407895773184,2382615412190740480,2382615416485707776,2382615420780675072,2382615425075642368,2382615446550478848,2382615450845446144,2382615455140413440,2382615459435380736]}
            else:
                path = "vehicle_settings.telemetry.normal_mode.events"
                value = {"batch_frequency": 1, "acc_size": 0, "acc_enable": False, "enable_flag": True,
                         "ena_dis_op_suportd": True, "priority_index": 0, "filter_plugin": [], "block_id": 1001,
                         "ddl_budget": 0, "ddl_timeout": 0, "ddl_flag": 0, "sms_flag": False, "reason_code": 0,
                         "push_freq": 20000, "qos": 1, "msg_type": 304, "notif_type": -1,
                         "attributes": [1252004033598587000, 2404938959978234000, 2404939801791824000, 2404939797496856600,
                                        2404939810381758500, 2404939814676726000, 2404924404334067700, 2404924408629035000,
                                        2404924412924002300, 2404924417218969600, 2404933217606959000, 2405133367377920000,
                                        2405133371672887300, 2405133375967854600, 2405133380262822000, 2405133406032625700,
                                        2405133410327593000, 2405133414622560000, 2405133418917527600, 2405133384557789000,
                                        2405133388852756500]}
        elif option == "REMOVE_TELEMETRY_BLOCK":
            action = "DELETE"
            if cloudEnv in r8_patch4_sp17_envs:
                path = "vehicle_settings.telemetry.events.126"
            else:
                path = "vehicle_settings.telemetry.normal_mode.events.126"
        else:
            print("Invalid Option")
    elif tc == "vacation_mode":
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            action = "ADD"
            path = "vehicle_settings.telemetry.vacation_mode.events"
            value = {"batch_frequency": 1, "acc_size": 0, "acc_enable": False, "enable_flag": True,
                     "ena_dis_op_suportd": True, "priority_index": 0, "filter_plugin": [], "block_id": 1001,
                     "ddl_budget": 0, "ddl_timeout": 0, "ddl_flag": 0, "sms_flag": False, "reason_code": 0,
                     "push_freq": 20000, "qos": 1, "msg_type": 304, "notif_type": -1,
                     "attributes": [1252004033598587000, 2404938959978234000, 2404939801791824000, 2404939797496856600,
                                    2404939810381758500, 2404939814676726000, 2404924404334067700, 2404924408629035000,
                                    2404924412924002300, 2404924417218969600, 2404933217606959000, 2405133367377920000,
                                    2405133371672887300, 2405133375967854600, 2405133380262822000, 2405133406032625700,
                                    2405133410327593000, 2405133414622560000, 2405133418917527600, 2405133384557789000,
                                    2405133388852756500]}
        elif option == "REMOVE_TELEMETRY_BLOCK":
            action = "DELETE"
            path = "vehicle_settings.telemetry.vacation_mode.events.126"
        else:
            print("Invalid Option")
    elif tc == "privacy_mode":
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            action = "ADD"
            path = "vehicle_settings.telemetry.privacy_mode.events"
            value = {"batch_frequency": 1, "acc_size": 0, "acc_enable": False, "enable_flag": True,
                     "ena_dis_op_suportd": True, "priority_index": 0, "filter_plugin": [], "block_id": 1001,
                     "ddl_budget": 0, "ddl_timeout": 0, "ddl_flag": 0, "sms_flag": False, "reason_code": 0,
                     "push_freq": 20000, "qos": 1, "msg_type": 304, "notif_type": -1,
                     "attributes": [1252004033598587000, 2404938959978234000, 2404939801791824000, 2404939797496856600,
                                    2404939810381758500, 2404939814676726000, 2404924404334067700, 2404924408629035000,
                                    2404924412924002300, 2404924417218969600, 2404933217606959000, 2405133367377920000,
                                    2405133371672887300, 2405133375967854600, 2405133380262822000, 2405133406032625700,
                                    2405133410327593000, 2405133414622560000, 2405133418917527600, 2405133384557789000,
                                    2405133388852756500]}
        elif option == "REMOVE_TELEMETRY_BLOCK":
            action = "DELETE"
            path = "vehicle_settings.telemetry.privacy_mode.events.126"
        else:
            print("Invalid Option")
    elif tc == "incognito_mode":
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            action = "ADD"
            path = "vehicle_settings.telemetry.incognito_mode.events"
            value = {"batch_frequency": 1, "acc_size": 0, "acc_enable": False, "enable_flag": True,
                     "ena_dis_op_suportd": True, "priority_index": 0, "filter_plugin": [], "block_id": 1001,
                     "ddl_budget": 0, "ddl_timeout": 0, "ddl_flag": 0, "sms_flag": False, "reason_code": 0,
                     "push_freq": 20000, "qos": 1, "msg_type": 304, "notif_type": -1,
                     "attributes": [1252004033598587000, 2404938959978234000, 2404939801791824000, 2404939797496856600,
                                    2404939810381758500, 2404939814676726000, 2404924404334067700, 2404924408629035000,
                                    2404924412924002300, 2404924417218969600, 2404933217606959000, 2405133367377920000,
                                    2405133371672887300, 2405133375967854600, 2405133380262822000, 2405133406032625700,
                                    2405133410327593000, 2405133414622560000, 2405133418917527600, 2405133384557789000,
                                    2405133388852756500]}
        elif option == "REMOVE_TELEMETRY_BLOCK":
            action = "DELETE"
            path = "vehicle_settings.telemetry.incognito_mode.events.126"
        else:
            print("Invalid Option")

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", value)
    print("----------------------------------------------------------")

    # call update vehicle configuration api module
    if cloudEnv not in ["GCP-QA3", "GCP-QA4", "RE-DEV", "RE-DM1", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT",
                        "GCP-PERF2"]:
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                        updateScope, modelCode, country,
                                                                        "ADD")
        elif option == "REMOVE_TELEMETRY_BLOCK":
            response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                        updateScope, modelCode, country,
                                                                        "DELETE")
    else:
        if option == "ADD_NEW_TELEMETRY_BLOCK":
            response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                        updateScope, modelCode, country,
                                                                        "model_based_configuration_add_action")
        elif option == "REMOVE_TELEMETRY_BLOCK":
            response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                        updateScope, modelCode, country,
                                                                        "model_based_configuration_delete_action")

    print("----------------------------------------------------------")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        assert True
        # self.result.set_result(TestResults.passed)
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "passed",
                       "Telemetry Configuration - New block should be added successfully",
                       "Telemetry Configuration - New block is added successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed",
                   "Telemetry Configuration - New block should be added successfully",
                   "Telemetry Configuration - New block is not added successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    time.sleep(10)
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    # time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validations via tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                if status == "PROGRESSING":
                    testResult(self, "verificationPassed",
                               "EDIT Feature - Configuration update should be 'PROGRESSING'",
                               "EDIT Feature - Configuration update is PROGRESSING")
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)

    # Final status check
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    status = Telemetry_addNewBlock = ""

    if option == "ADD_NEW_TELEMETRY_BLOCK":
        if tc == "normal_mode":
            # Read master_conf.json file
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "add_new_block", "normalMode")
        elif tc == "vacation_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "add_new_block", "vacationMode")
        elif tc == "privacy_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "add_new_block", "privacyMode")
        elif tc == "incognito_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "add_new_block", "incognitoMode")
        print("Telemetry New Block:", Telemetry_addNewBlock)

        print("----------------------------------------------------------")

        if attribute in Telemetry_addNewBlock:
            testResult(self, "passed",
                       "Telemetry Block Add - New Telemetry block should be added in telemetry_conf.json file on device",
                       "Telemetry Block Add - New Telemetry block is added in telemetry_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Telemetry Block Add - New Telemetry block should be added in telemetry_conf.json file on device",
                       "Telemetry Block Add - New Telemetry block is not added in telemetry_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")
    elif option == "REMOVE_TELEMETRY_BLOCK":
        if tc == "normal_mode":
            # Read master_conf.json file
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "remove_new_block", "normalMode")
        elif tc == "vacation_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "remove_new_block", "vacationMode")
        elif tc == "privacy_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "remove_new_block", "privacyMode")
        elif tc == "incognito_mode":
            Telemetry_addNewBlock = read_telemetryConfJsonFile(self, "remove_new_block", "incognitoMode")
        print("Telemetry New Block:", Telemetry_addNewBlock)

        print("----------------------------------------------------------")

        if attribute not in Telemetry_addNewBlock:
            testResult(self, "passed",
                       "Telemetry Block Add - New Telemetry block should be deleted in telemetry_conf.json file on device",
                       "Telemetry Block Add - New Telemetry block is deleted in telemetry_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Telemetry Block Add - New Telemetry block should be deleted in telemetry_conf.json file on device",
                       "Telemetry Block Add - New Telemetry block is not deleted in telemetry_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        # Parse response body
        response_body = response.json()

        # Validate response message
        if response_body["message"] == "Success":
            vehicle_features = ""
            if cloudEnv in r8_patch4_sp17_envs:
                if tc == "normal_mode":
                    vehicle_features = \
                        response_body["configurations"]["vehicle_settings"]["telemetry"]["normal_mode"]["events"]
                elif tc == "vacation_mode":
                    vehicle_features = \
                        response_body["configurations"]["vehicle_settings"]["telemetry"]["vacation_mode"]["events"]
                elif tc == "privacy_mode":
                    vehicle_features = \
                        response_body["configurations"]["vehicle_settings"]["telemetry"]["privacy_mode"]["events"]
                elif tc == "incognito_mode":
                    vehicle_features = \
                        response_body["configurations"]["vehicle_settings"]["telemetry"]["incognito_mode"]["events"]
            else:
                if tc in ["normal_mode", "vacation_mode", "privacy_mode", "incognito_mode"]:
                    vehicle_features = \
                        response_body["configurations"]["vehicle_settings"]["telemetry"]["events"]
            # Check if 'push_freq' key exists
            if option == "ADD_NEW_TELEMETRY_BLOCK":
                if attribute in vehicle_features:
                    testResult(self, "passed",
                               "Telemetry Block Add - New Telemetry block should be added in telemetry_conf.json file on cloud",
                               "Telemetry Block Add - New Telemetry block is added in telemetry_conf.json file on cloud")
                    assert True
                else:
                    # Fail the test if 'push_freq' key is missing
                    testResult(self, "failed",
                               "Telemetry Block Add - New Telemetry block should be added in telemetry_conf.json file on cloud",
                               "Telemetry Block Add - New Telemetry block is not added in telemetry_conf.json file on cloud")
                    # self.result.set_result(TestResults.failed)
                    assert False
            if option == "REMOVE_TELEMETRY_BLOCK":
                if attribute not in vehicle_features:
                    testResult(self, "passed",
                               "Telemetry Block Add - New Telemetry block should be deleted in telemetry_conf.json file on cloud",
                               "Telemetry Block Add - New Telemetry block is deleted in telemetry_conf.json file on cloud")
                    assert True
                else:
                    # Fail the test if 'push_freq' key is missing
                    testResult(self, "failed",
                               "Telemetry Block Add - New Telemetry block should be deleted in telemetry_conf.json file on cloud",
                               "Telemetry Block Add - New Telemetry block is not deleted in telemetry_conf.json file on cloud")
                    # self.result.set_result(TestResults.failed)
                    assert False
        else:
            # Fail the test for unexpected response message
            testResult(self, "failed",
                       "Telemetry Block Add - New Telemetry block should be added/removed in telemetry_conf.json file on cloud",
                       f"Unexpected response message: {response_body.get('message', 'No message available')}.")
            # self.result.set_result(TestResults.failed)
            assert False, f"Unexpected response message: {response_body.get('message', 'No message available')}."
    else:
        # Fail the test for invalid status code
        testResult(self, "failed",
                   "Telemetry Block Add - New Telemetry block should be added/removed in telemetry_conf.json file on cloud",
                   f"API call failed with status code {response.status_code}.")
        # self.result.set_result(TestResults.failed)
        assert False, f"API call failed with status code {response.status_code}."

def update_priority_in_dtcConf(self, cloudEnv, onboardingType, chipsetType, priority_value):
    getset_config_v2(self, onboardingType, chipsetType, "dtc_conf", "path2")
    time.sleep(20)

    systemId = read_vehicleJsonFile(self, "system_id")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Trigger EDIT Priority Request Via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Test Data*

    action = "EDIT"
    path = "vehicle_settings.dtc_configurations.dtc_1.priority"
    attribute = "priority"
    value = priority_value
    updateScope = "MODEL"

    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", value)
    print("Model Code: ", modelCode)
    print("Country: ", country)
    print("----------------------------------------------------------")

    # call update vehicle configuration api module
    if cloudEnv not in ["GCp-QA4", "GCP-QA5", "RE-DEV", "GCP-QA8", "GCP-QA2", "GCP-PERF2"]:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")
    else:
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "model_based_configuration")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200 or response.status_code == 207:
        assert True
        # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
            print(f"Already DTC Conf is having the priority value as {priority_value}")
    else:
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # Validate response body
    trackingId = ""
    if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(self, "verificationPassed",
                       "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is triggered successfully")
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                   "EDIT Feature - Configuration update is not triggered successfully")
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, device_checksum,
                               device_checksum)

    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   " Device got the checksum of the file successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the checksum of the file successfully",
                   "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, cloud_checksum,
                               cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(self, "verificationPassed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Device got the cloud checksum successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    ls = verify_message_in_log(self, checksum_validation_status,
                               checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(self, "verificationPassed",
                   "Validate the device & cloud checksum successfully",
                   "Checksum is validated successfully, pls refer device logs for "
                   "detailed info")
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(self, "verificationFailed",
                   "Validate that device should receive/get the cloud checksum successfully",
                   "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                   "detailed info")

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validation - Configuration status by trackingId: ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                if status == "PROGRESSING":
                    testResult(self, "verificationPassed",
                               "EDIT Feature - Configuration update should be 'PROGRESSING'",
                               "EDIT Feature - Configuration update is PROGRESSING")
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)

    # Final status check
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False

    print("----------------------------------------------------------")

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    print("VALIDATE UPDATED CONFIGURATION IN DTC_CONF.JSON")

    # Read master_conf.json file
    dtc_1_P1001_priority_value = read_dtcConfJsonFile(self, "dtc_P1001_update_priority")

    status = ""

    if dtc_1_P1001_priority_value == value:
        testResult(self, "passed", "Priority value should be updated in dtc_conf.json file on device",
                   "Priority value is updated in dtc_conf.json file on device")
    else:
        testResult(self, "verificationFailed",
                   "Priority value should be updated in dtc_conf.json file on device",
                   "Priority value is not updated in dtc_conf.json file on device")
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    response = vehicleConfigurations_getConfig_new(self, systemId, "dtc_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            vehicle_features = response_body["configurations"]["vehicle_settings"]["dtc_configurations"]["dtc_1"]

            # Check for 'tyre_pressure' feature
            if "priority" in vehicle_features:
                if vehicle_features["priority"] == value:
                    testResult(self, "passed",
                               "Priority and value should be present in the DTC configuration",
                               "Priority and value is present in the DTC configuration.")
                    assert True
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Priority value does not match the expected value.")
                    assert False
                    # self.result.set_result(TestResults.failed)
            else:
                # Log an error if 'tyre_pressure' feature is missing
                print("Priority is not found in vehicle features.")
                testResult(self, "failed",
                           "Priority should be present in the DTC configuration",
                           "'Priority' feature is missing in the DTC configuration.")
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Unexpected response message:", response_body["message"])
            assert False
            # self.result.set_result(TestResults.failed)
    else:
        print("Unable to fetch DTC configuration. Please check the API response for more details.",
              "Status Code:", response.status_code, "Response Body:", response_body)
        assert False
        # self.result.set_result(TestResults.failed)

def vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                  vehicleMode):
    # ===========================================================================================
    # Trigger Vacation Mode
    # ===========================================================================================

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print(f"Trigger {vehicleMode} Mode via Cluster: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # =======================================================================================================
    # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
    # =======================================================================================================
    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print(f"Validate {vehicleMode} mode is enabled in master_conf.json : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    if vehicleMode == "Vacation":
        # Read master_conf.json file
        vacationMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        print(" Vacation Mode - Enabled :", vacationMode_Enabled)

        print("----------------------------------------------------------")
        status = ""

        if str(vacationMode_Enabled) == enabled or bool(vacationMode_Enabled) == enabled:
            testResult(self, "passed",
                       f"Vacation Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Vacation Mode Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Vacation Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Vacation Mode Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    elif vehicleMode == "Incognito":
        # Read master_conf.json file
        incognitoMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled", "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Enabled)

        print("----------------------------------------------------------")
        status = ""

        if str(incognitoMode_Enabled) == enabled or bool(incognitoMode_Enabled) == enabled:
            testResult(self, "passed",
                       f"Incognito Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Incognito Mode Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Incognito Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Incognito Mode Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    elif vehicleMode == "RemoteDiagnostic":
        # Read master_conf.json file
        remoteDiagnosticMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_Enabled",
                                                                  "remoteDiagnosticMode")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Enabled)

        print("----------------------------------------------------------")
        status = ""

        if str(remoteDiagnosticMode_Enabled) == enabled or bool(remoteDiagnosticMode_Enabled) == enabled:
            testResult(self, "passed",
                       f"Remote Diagnostic Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Remote Diagnostic Mode Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Remote Diagnostic Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Remote Diagnostic Mode Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    elif vehicleMode == "Service":
        # Read master_conf.json file
        serviceMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "ServiceMode_Enabled", "serviceMode")

        print(" Service Mode - Enabled :", serviceMode_Enabled)

        print("----------------------------------------------------------")
        status = ""

        if str(serviceMode_Enabled) == enabled or bool(serviceMode_Enabled) == enabled:
            testResult(self, "passed",
                       f"Service Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Service Mode Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Service Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Service Mode Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    elif vehicleMode == "Privacy":
        # Read master_conf.json file
        privacyMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")

        print(" Privacy Mode - Enabled :", privacyMode_Enabled)

        print("----------------------------------------------------------")
        status = ""

        if str(privacyMode_Enabled) == enabled or bool(privacyMode_Enabled) == enabled:
            testResult(self, "passed",
                       f"Privacy Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Privacy Mode Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Privacy Mode Flag should be set to {enabled} in master_conf.json file on device",
                       f"Privacy Mode Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    elif vehicleMode == "Service_rdm":
        # Read master_conf.json file
        service_rdm = read_masterConfJsonFile_v2(self, cloudEnv, "service_rdm", "service_rdm")

        print(" Service rdm - Enabled :", service_rdm)

        print("----------------------------------------------------------")
        status = ""

        if str(service_rdm) == enabled or bool(service_rdm) == enabled:
            testResult(self, "passed",
                       f"Service rdm Flag should be set to {enabled} in master_conf.json file on device",
                       f"Service rdm Flag is set to {enabled} in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       f"Service rdm Flag should be set to {enabled} in master_conf.json file on device",
                       f"Service rdm Flag is not set to {enabled} in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
    else:
        print("Invalid Mode")

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Fetch configuration from the vehicle configuration API
    response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body.get("message") == "Success":
            # Extract vehicle mode configuration
            if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2", "RE-UAT", "GCP-PERF2"]:
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
            else:
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")
                service_rdm_path = response_body["configurations"]["vehicle_settings"]["vehicle_function"]

            if vehicle_mode is None:
                print("vehicle_mode block not found in response.")
                testResult(self, "failed",
                           "vehicle_mode should be present in master_conf.json file on cloud",
                           "vehicle_mode block not found in API response")
                assert False

            # ----------------service rdm---------------
            if cloudEnv in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2", "GCP-PERF2"]:
                if "service_rdm" in service_rdm_path:
                    if vehicleMode == "Service_rdm":
                        mode_config = service_rdm_path["service_rdm"]
                        eff = mode_config["enabled"] if type(mode_config) is dict else mode_config
                        if (eff == str(enabled) or eff == bool(enabled) or eff == enabled):
                            testResult(self, "passed",
                                       f"Service rdm Flag should be set to {enabled} in master_conf.json file on cloud",
                                       f"Service rdm Flag is set to {enabled} in master_conf.json file on cloud")
                            assert True
                            return
                        else:
                            testResult(self, "failed",
                                       f"Service rdm Flag should be set to {enabled} in master_conf.json file on cloud",
                                       f"Service rdm Flag is not set to {enabled} in master_conf.json file on cloud")
                            assert False
                            return
                else:
                    print("service_rdm block not found in vehicle_function.")
                    testResult(self, "failed",
                               "service_rdm should be present in master_conf.json file on cloud",
                               "service_rdm block not found in API response under vehicle_function")
                    assert False
                    return

            # Handle each mode
            if vehicleMode == "Vacation" and "vacation_mode" in vehicle_mode:
                mode_config = vehicle_mode["vacation_mode"]
                if (mode_config["enabled"] == str(enabled) or mode_config["enabled"] == bool(enabled) or mode_config[
                    "enabled"] == enabled):
                    testResult(self, "passed",
                               f"Vacation Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Vacation Mode Flag is set to {enabled} in master_conf.json file on cloud")
                    assert True
                else:
                    testResult(self, "failed",
                               f"Vacation Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Vacation Mode Flag is not set to {enabled} in master_conf.json file on cloud")
                    assert False

            elif vehicleMode == "Privacy" and "privacy_mode" in vehicle_mode:
                mode_config = vehicle_mode["privacy_mode"]
                if (mode_config["enabled"] == str(enabled) or mode_config["enabled"] == bool(enabled) or mode_config[
                    "enabled"] == enabled):
                    testResult(self, "passed",
                               f"Privacy Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Privacy Mode Flag is set to {enabled} in master_conf.json file on cloud")  # *** kept same message format, fixed to f-string if you want
                    assert True
                else:
                    testResult(self, "failed",
                               f"Privacy Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Privacy Mode Flag is not set to {enabled} in master_conf.json file on cloud")
                    assert False

            elif vehicleMode == "Incognito" and "incognito_mode" in vehicle_mode:
                mode_config = vehicle_mode["incognito_mode"]
                if (mode_config["enabled"] == str(enabled) or mode_config["enabled"] == bool(enabled) or mode_config[
                    "enabled"] == enabled):
                    testResult(self, "passed",
                               f"Incognito Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Incognito Mode Flag is set to {enabled} in master_conf.json file on cloud")
                    assert True
                else:
                    testResult(self, "failed",
                               f"Incognito Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Incognito Mode Flag is not set to {enabled} in master_conf.json file on cloud")
                    assert False

            elif vehicleMode == "RemoteDiagnostic" and "remote_diagnostic_mode" in vehicle_mode:
                mode_config = vehicle_mode["remote_diagnostic_mode"]
                if (mode_config["enabled"] == str(enabled) or mode_config["enabled"] == bool(enabled) or mode_config[
                    "enabled"] == enabled):
                    testResult(self, "passed",
                               f"Remote Diagnostic Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Remote Diagnostic Mode Flag is set to {enabled} in master_conf.json file on cloud")
                    assert True
                else:
                    testResult(self, "failed",
                               f"Remote Diagnostic Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Remote Diagnostic Mode Flag is not set to {enabled} in master_conf.json file on cloud")
                    assert False

            elif vehicleMode == "Service" and "service_mode" in vehicle_mode:
                mode_config = vehicle_mode["service_mode"]
                if (mode_config["enabled"] == "true" or mode_config["enabled"] == True or mode_config["enabled"] == 1):
                    testResult(self, "passed",
                               f"Service Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Service Mode Flag is set to {enabled} in master_conf.json file on cloud")
                    assert True
                else:
                    testResult(self, "failed",
                               f"Service Mode Flag should be set to {enabled} in master_conf.json file on cloud",
                               f"Service Mode Flag is not set to {enabled} in master_conf.json file on cloud")
                    assert False

            else:
                print("Invalid or unsupported vehicle mode.")
                assert False

        else:
            # *** added else for message != Success ***
            testResult(self, "failed",
                       "Vehicle configuration API should return message 'Success'",
                       f"API returned message: {response_body.get('message')}")
            assert False
    else:
        # *** added else for HTTP != 200 ***
        testResult(self, "failed",
                   "Vehicle configuration API should return HTTP 200",
                   f"Received HTTP {response.status_code}")
        assert False

def ert_sms_alert(self, onboardingType, chipsetType, categoryId, mobileNo, tc):
    # -------------------- High-level banner for readability in logs --------------------
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("UPDATE SMS NUMBER AND TEMPLATE via VEHICLE CONFIGURATION API: ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # -------------------- Test Data / Constants --------------------
    # Read the systemId from vehicle JSON
    systemId = read_vehicleJsonFile(self, "system_id")

    # Action type for Vehicle Configuration API (ADD/EDIT/DELETE). Here: EDIT
    action = "EDIT"

    # Initialize request fields
    path = value = attribute = ""

    # ERT SMS data used for update (mobile number + template)
    intro = "Emergency SMS with Unique ID $uniqueid for VIN $vin"
    fields = [
        "AL_LATITUDE", "AL_LONGITUDE", "AL_ALTITUDE", "AL_BEARING", "AL_VELOCITY",
        "AL_GPS_STATUS", "AL_GPS_SIGNAL_STRENGTH", "AL_NETWORK_OP_NAME", "AL_TIMESTAMP",
        "AL_DELTA_DIST_COVERED", "AL_PDOP", "AL_HDOP", "AL_GPS_FIX", "AL_LAT_DIR", "AL_LONG_DIR"
    ]
    delimit_text = "with"

    cloudEnv = read_cloud_env(self)
    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    modelCode = str(dict1["modelCode"])
    country = str(dict1["country"])
    updateScope = "MODEL"  # Scope of update (MODEL/SYSTEM/etc.)

    # -------------------- Build request payload based on environment & test case --------------------
    if cloudEnv in ["GCP-QA2"]:
        if tc == "crash_sms":
            path = "vehicle_settings.vehicle_function.communication.sms.crash_sms"
        elif tc == "sos_sms":
            path = "vehicle_settings.vehicle_function.communication.sms.sos_sms"
        elif tc == "towaway_sms":
            path = "vehicle_settings.vehicle_function.communication.sms.towaway_sms"
        elif tc == "heartbeat_sms":
            path = "vehicle_settings.vehicle_function.communication.sms.heartbeat_sms"
        value = {
            "sms_number": mobileNo,
            "category_id": categoryId,
            "sms_template": {
                "intro": intro,
                "delimit_text": delimit_text,
                "fields": fields
            }
        }
    else:
        if tc == "crash_sms":
            path = "sms.crash_sms"
        elif tc == "sos_sms":
            path = "sms.sos_sms"
        elif tc == "towaway_sms":
            path = "sms.towaway_sms"
        elif tc == "heartbeat_sms":
            path = "sms.heartbeat_sms"
        value = {
            "sms_number": mobileNo,
            "category_id": categoryId,
            "sms_template": {
                "intro": intro,
                "delimit_text_2": delimit_text,
                "fields": fields
            }
        }

    print("----------------------------------------------------------")
    print("System Id :", systemId)
    print("Action :", action)
    print("Path :", path)
    print("Value :", value)
    print("----------------------------------------------------------")

    # -------------------- Call Update Vehicle Configuration API --------------------

    response = vehicleConfigurations_updateVehicleConfiguration(
        self, action, path, attribute, value, systemId,
        updateScope, modelCode, country, "EDIT"
    )

    print("----------------------------------------------------------")

    # -------------------- Parse API response --------------------
    response_body = response.json()

    # -------------------- Validate HTTP status --------------------
    if response.status_code == 200 or response.status_code == 207:
        assert True
        # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
    else:
        # Unexpected status — fail early
        print("Response status is not as expected OR something went wrong, please check API response")
        assert False
        # self.result.set_result(TestResults.failed)

    # -------------------- Validate response body (tracking) --------------------
    trackingId = ""
    if response_body["status"] == "PROGRESSING":
        if response_body["trackingId"]:
            print("----------------------------------------------------------")
            trackingId = response_body["trackingId"]
            print("trackingId: ", response_body["trackingId"])
            print("----------------------------------------------------------")
            testResult(
                self, "passed",
                "ERT - Mobile number and sms template update request should be triggered successfully",
                "ERT - Mobile number and sms template update request is triggered successfully"
            )
            assert True
            # self.result.set_result(TestResults.passed)
    else:
        # If not PROGRESSING, mark as failed
        testResult(
            self, "failed",
            "ERT - Mobile number and sms template update request should be triggered successfully",
            "ERT - Mobile number and sms template update request is triggered successfully"
        )
        # self.result.set_result(TestResults.failed)
        assert False

    print("----------------------------------------------------------")

    # =======================================================================================================
    # Pull/Fetch required files (conf/license/logs) from device for post-event validations
    # =======================================================================================================

    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    # Strings used to search in device logs
    device_checksum = "successfully got checksum of the file"
    cloud_checksum = "successfully got cloud checksum"
    checksum_validation_status = "checksum validation"

    print("----------------------------------------------------------")

    # -------------------- Validate: device checksum logged --------------------
    ls = verify_message_in_log(self, device_checksum, device_checksum)
    if device_checksum in str(ls[0]):
        print(f" => Device got the checksum of the file successfully")
        testResult(
            self, "verificationPassed",
            "Validate that device should receive/get the checksum of the file successfully",
            " Device got the checksum of the file successfully, pls refer device logs for detailed info"
        )
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the checksum of the file.")
        testResult(
            self, "verificationFailed",
            "Validate that device should receive/get the checksum of the file successfully",
            "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for detailed info"
        )

    print("----------------------------------------------------------")

    # -------------------- Validate: cloud checksum logged --------------------
    ls = verify_message_in_log(self, cloud_checksum, cloud_checksum)
    if cloud_checksum in str(ls[0]):
        print(f" => Device got the cloud checksum successfully")
        testResult(
            self, "verificationPassed",
            "Validate that device should receive/get the cloud checksum successfully",
            "Device got the cloud checksum successfully, pls refer device logs for detailed info"
        )
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to get the cloud checksum")
        testResult(
            self, "verificationFailed",
            "Validate that device should receive/get the cloud checksum successfully",
            "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for detailed info"
        )

    print("----------------------------------------------------------")

    # -------------------- Validate: checksum comparison status logged --------------------
    ls = verify_message_in_log(self, checksum_validation_status, checksum_validation_status)
    if checksum_validation_status in str(ls[0]):
        print(f" => Checksum should be validated successfully")
        testResult(
            self, "verificationPassed",
            "Validate the device & cloud checksum successfully",
            "Checksum is validated successfully, pls refer device logs for detailed info"
        )
        print("c2c logs line data : => ", ls[0])

    if str(ls[0]) == "Error":
        print(f" => Failed to validate the checksum")
        testResult(
            self, "verificationFailed",
            "Validate that device should receive/get the cloud checksum successfully",
            "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for detailed info"
        )

    print("----------------------------------------------------------")

    # -------------------- Tracking API polling & final cloud-side status --------------------
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Cloud Side Validations via tracking API : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    final_status = None
    for attempt in range(5):
        # Query tracking API for current status of configuration update
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        # Basic HTTP status validation
        if response.status_code not in [200, 207]:
            print("Unexpected response status")
            assert False

        response_body = response.json()
        results = response_body.get("results", [])
        results_len = len(results)

        found = False
        for i in range(results_len):
            result = results[i]
            if result.get("systemId") == systemId:
                found = True
                status = result.get("status")

                # Live progress marker for audit
                if status == "PROGRESSING":
                    testResult(
                        self, "verificationPassed",
                        "EDIT Feature - Configuration update should be 'PROGRESSING'",
                        "EDIT Feature - Configuration update is PROGRESSING"
                    )
                elif status == "COMPLETED":
                    final_status = "COMPLETED"
                    break
                elif status == "FAILED":
                    final_status = "FAILED"
                    break

        # Break/Retry logic based on whether we found the system or reached final state
        if found and final_status in ["COMPLETED", "FAILED"]:
            break
        elif not found:
            print(f"SystemId {systemId} not found in response. Retrying...")

        time.sleep(10)  # Wait between polling attempts

    # -------------------- Final decision based on cloud update status --------------------
    if final_status == "COMPLETED":
        testResult(self, "passed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update is successful")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed", "EDIT Feature - Configuration update should succeed",
                   "EDIT Feature - Configuration update failed")
        assert False
    else:
        print("Configuration update did not complete within expected attempts.")
        assert False
    print("----------------------------------------------------------")

    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)  # Give device time to write logs/updated conf

    # -------------------- Device-side validation: master_conf.json --------------------
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("Device Side Validations : ")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")

    # Read/compare SMS template fields from device conf (only for non-GCP-QA5 crash_sms)
    status = sms_number = sms_template_category_id = sms_template_intro = sms_template_delimit_text = sms_template_fields = ""

    if cloudEnv in ["GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT", "GCP-PERF2"]:
        if tc == "crash_sms":
            sms_number = read_masterConfJsonFile_v2(self, cloudEnv, "sms_number", "crash_sms")
            sms_template_category_id = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_category_id",
                                                                  "crash_sms")
            sms_template_intro = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_intro", "crash_sms")
            sms_template_delimit_text = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_delimit_text",
                                                                   "crash_sms")
            sms_template_fields = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_fields", "crash_sms")
        elif tc == "sos_sms":
            sms_number = read_masterConfJsonFile_v2(self, cloudEnv, "sms_number", "sos_sms")
            sms_template_category_id = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_category_id",
                                                                  "sos_sms")
            sms_template_intro = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_intro", "sos_sms")
            sms_template_delimit_text = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_delimit_text",
                                                                   "sos_sms")
            sms_template_fields = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_fields", "sos_sms")
        elif tc == "towaway_sms":
            sms_number = read_masterConfJsonFile_v2(self, cloudEnv, "sms_number", "towaway_sms")
            sms_template_category_id = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_category_id",
                                                                  "towaway_sms")
            sms_template_intro = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_intro", "towaway_sms")
            sms_template_delimit_text = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_delimit_text",
                                                                   "towaway_sms")
            sms_template_fields = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_fields", "towaway_sms")
        elif tc == "heartbeat_sms":
            sms_number = read_masterConfJsonFile_v2(self, cloudEnv, "sms_number", "heartbeat_sms")
            sms_template_category_id = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_category_id",
                                                                  "heartbeat_sms")
            sms_template_intro = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_intro", "heartbeat_sms")
            sms_template_delimit_text = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_delimit_text",
                                                                   "heartbeat_sms")
            sms_template_fields = read_masterConfJsonFile_v2(self, cloudEnv, "sms_template_fields", "heartbeat_sms")
        else:
            print("Invalid Testcase")

        print("SMS Number:", sms_number)
        print("Intro:", sms_template_intro)
        print("Category Id:", sms_template_category_id)
        print("Delimit Text:", sms_template_delimit_text)
        print("Fields:", sms_template_fields)

    print("----------------------------------------------------------")

    # Device-side assertion: all expected values must match
    if sms_number == mobileNo and sms_template_category_id == categoryId and sms_template_intro == intro and sms_template_delimit_text == delimit_text and sms_template_fields == fields:
        testResult(
            self, "passed",
            "SMS number and template should be updated in master_conf.json file on device",
            "SMS number and template is updated in master_conf.json file on device"
        )
    else:
        testResult(
            self, "verificationFailed",
            "SMS number and template should be updated in master_conf.json file on device",
            "SMS number and template is not updated in master_conf.json file on device"
        )
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    # Final assert based on device validation status
    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

    print("===============================================")
    print("----Check mobile number updated in apkconfig.txt----")
    print("==============================================")

    if tc == "crash_sms":
        sms_number = read_apkconf(cloudEnv, "crash_sms","sms_number")
        sms_template_category_id = read_apkconf(cloudEnv, "crash_sms", "sms_template_category_id")
        sms_template_intro = read_apkconf(cloudEnv, "crash_sms", "sms_template_intro")
        sms_template_delimit_text = read_apkconf(cloudEnv, "crash_sms", "sms_template_delimit_text")
        sms_template_fields = read_apkconf(cloudEnv, "crash_sms", "sms_template_fields")
    elif tc == "sos_sms":
        sms_number = read_apkconf(cloudEnv, "sos_sms", "sms_number")
        sms_template_category_id = read_apkconf(cloudEnv, "sos_sms", "sms_template_category_id")
        sms_template_intro = read_apkconf(cloudEnv, "sos_sms", "sms_template_intro")
        sms_template_delimit_text = read_apkconf(cloudEnv, "sos_sms", "sms_template_delimit_text")
        sms_template_fields = read_apkconf(cloudEnv, "sos_sms", "sms_template_fields")
    elif tc == "towaway_sms":
        sms_number = read_apkconf(cloudEnv, "towaway_sms", "sms_number")
        sms_template_category_id = read_apkconf(cloudEnv, "towaway_sms", "sms_template_category_id")
        sms_template_intro = read_apkconf(cloudEnv, "towaway_sms", "sms_template_intro")
        sms_template_delimit_text = read_apkconf(cloudEnv, "towaway_sms", "sms_template_delimit_text")
        sms_template_fields = read_apkconf(cloudEnv, "towaway_sms", "sms_template_fields")
    elif tc == "heartbeat_sms":
        sms_number = read_apkconf(cloudEnv, "heartbeat_sms", "sms_number")
        sms_template_category_id = read_apkconf(cloudEnv, "heartbeat_sms", "sms_template_category_id")
        sms_template_intro = read_apkconf(cloudEnv, "heartbeat_sms", "sms_template_intro")
        sms_template_delimit_text = read_apkconf(cloudEnv, "heartbeat_sms", "sms_template_delimit_text")
        sms_template_fields = read_apkconf(cloudEnv, "heartbeat_sms", "sms_template_fields")
    else:
        print("Invalid Testcase")

    print("SMS Number:", sms_number)
    print("Intro:", sms_template_intro)
    print("Category Id:", sms_template_category_id)
    print("Delimit Text:", sms_template_delimit_text)
    print("Fields:", sms_template_fields)

    print("----------------------------------------------------------")

    # Device-side assertion: all expected values must match
    if sms_number == mobileNo and sms_template_category_id == categoryId and sms_template_intro == intro and sms_template_delimit_text == delimit_text and sms_template_fields == fields:
        testResult(
            self, "passed",
            "SMS number and template should be updated in apkconfig.txt file on device",
            "SMS number and template is updated in apkconfig.txt file on device"
        )
    else:
        testResult(
            self, "verificationFailed",
            "SMS number and template should be updated in apkconfig.txt file on device",
            "SMS number and template is not updated in apkconfig.txt file on device"
        )
        status = "FAIL"
        print("Status", status)
    print("----------------------------------------------------------")

    # Final assert based on device validation status
    if status != "FAIL":
        # self.result.set_result(TestResults.passed)
        assert True
    else:
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")


    # -------------------- Cloud-side GET validation: master_conf --------------------
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Get Configuration On the cloud via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    sms_number_cloud = sms_template_category_id_cloud = sms_template_intro_cloud = sms_template_delimit_text_cloud = sms_template_fields_cloud = ""

    # Fetch the alert_conf from cloud to validate SMS template persisted correctly
    response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

    # Validate HTTP status & response content
    if response.status_code == 200:
        response_body = response.json()

        if response_body["message"] == "Success":
            vehicle_features = ""
            if cloudEnv in ["GCP-QA2"]:
                if tc == "crash_sms":
                    sms_number_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"]["crash_sms"]["sms_number"]
                    sms_template_category_id_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"]["crash_sms"]["category_id"]
                    sms_template_intro_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"]["crash_sms"]["sms_template"]["intro"]
                    sms_template_delimit_text_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"]["crash_sms"]["sms_template"][
                        "delimit_text"]
                    sms_template_fields_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"]["crash_sms"]["sms_template"][
                        "fields"]
                elif tc == "sos_sms":
                    sms_number_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                        "sos_sms"]["sms_number"]
                    sms_template_category_id_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                        "sos_sms"]["sms_template"][
                        "category_id"]
                    sms_template_intro_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["sos_sms"][
                        "sms_template"]["intro"]
                    sms_template_delimit_text_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["sos_sms"][
                        "sms_template"][
                        "delimit_text"]
                    sms_template_fields_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["sos_sms"][
                        "sms_template"][
                        "fields"]
                elif tc == "towaway_sms":
                    sms_number_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                        "towaway_sms"]["sms_number"]
                    sms_template_category_id_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                        "towaway_sms"]["sms_template"][
                        "category_id"]
                    sms_template_intro_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["towaway_sms"][
                        "sms_template"]["intro"]
                    sms_template_delimit_text_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["towaway_sms"][
                        "sms_template"][
                        "delimit_text"]
                    sms_template_fields_cloud = \
                    response_body["configurations"]["vehicle_function"]["communication"]["sms"]["towaway_sms"][
                        "sms_template"][
                        "fields"]
                elif tc == "heartbeat_sms":
                    sms_number_cloud = \
                        response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                            "heartbeat_sms"]["sms_number"]
                    sms_template_category_id_cloud = \
                        response_body["configurations"]["vehicle_settings"]["vehicle_function"]["communication"]["sms"][
                            "heartbeat_sms"]["sms_template"][
                            "category_id"]
                    sms_template_intro_cloud = \
                        response_body["configurations"]["vehicle_function"]["communication"]["sms"]["heartbeat_sms"][
                            "sms_template"]["intro"]
                    sms_template_delimit_text_cloud = \
                        response_body["configurations"]["vehicle_function"]["communication"]["sms"]["heartbeat_sms"][
                            "sms_template"][
                            "delimit_text"]
                    sms_template_fields_cloud = \
                        response_body["configurations"]["vehicle_function"]["communication"]["sms"]["heartbeat_sms"][
                            "sms_template"][
                            "fields"]
                else:
                    print("Invalid Testcase")
            else:
                if tc == "crash_sms":
                    sms_number_cloud = response_body["configurations"]["sms"]["crash_sms"]["ert_number"]
                    sms_template_category_id_cloud = response_body["configurations"]["sms"]["crash_sms"][
                        "category_id"]
                    sms_template_intro_cloud = response_body["configurations"]["sms"]["crash_sms"]["sms_template"]["intro"]
                    sms_template_delimit_text_cloud = response_body["configurations"]["sms"]["crash_sms"]["sms_template"][
                        "delimit_text_2"]
                    sms_template_fields_cloud = response_body["configurations"]["sms"]["crash_sms"]["sms_template"][
                        "fields"]
                elif tc == "sos_sms":
                    sms_number_cloud = response_body["configurations"]["sms"]["sos_sms"]["ert_number"]
                    sms_template_category_id_cloud = response_body["configurations"]["sms"]["sos_sms"][
                        "category_id"]
                    sms_template_intro_cloud = response_body["configurations"]["sms"]["sos_sms"]["sms_template"]["intro"]
                    sms_template_delimit_text_cloud = response_body["configurations"]["sms"]["sos_sms"]["sms_template"][
                        "delimit_text_2"]
                    sms_template_fields_cloud = response_body["configurations"]["sms"]["sos_sms"]["sms_template"][
                        "fields"]
                elif tc == "towaway_sms":
                    sms_number_cloud = response_body["configurations"]["sms"]["towaway_sms"]["ert_number"]
                    sms_template_category_id_cloud = response_body["configurations"]["sms"]["towaway_sms"][
                        "category_id"]
                    sms_template_intro_cloud = response_body["configurations"]["sms"]["towaway_sms"]["sms_template"][
                        "intro"]
                    sms_template_delimit_text_cloud = response_body["configurations"]["sms"]["towaway_sms"]["sms_template"][
                        "delimit_text_2"]
                    sms_template_fields_cloud = response_body["configurations"]["sms"]["towaway_sms"]["sms_template"][
                        "fields"]
                elif tc == "heartbeat_sms":
                    sms_number_cloud = response_body["configurations"]["sms"]["heartbeat_sms"]["ert_number"]
                    sms_template_category_id_cloud = response_body["configurations"]["sms"]["heartbeat_sms"][
                        "category_id"]
                    sms_template_intro_cloud = response_body["configurations"]["sms"]["heartbeat_sms"]["sms_template"][
                        "intro"]
                    sms_template_delimit_text_cloud = \
                    response_body["configurations"]["sms"]["heartbeat_sms"]["sms_template"][
                        "delimit_text_2"]
                    sms_template_fields_cloud = response_body["configurations"]["sms"]["heartbeat_sms"]["sms_template"][
                        "fields"]
                else:
                    print("Invalid Testcase")

            # Final cloud-side assertion
            if sms_number_cloud == mobileNo and sms_template_category_id_cloud == categoryId and sms_template_intro_cloud == intro and sms_template_delimit_text_cloud == delimit_text and sms_template_fields_cloud == fields:
                testResult(
                    self, "passed",
                    "SMS number and template should be updated in master_conf.json file on device",
                    "SMS number and template is updated in alert_conf.json file on device"
                )
                assert True
            else:
                testResult(
                    self, "failed",
                    "SMS number and template should be updated in master_conf.json file on device",
                    "SMS number and template key is missing in master_conf.json file."
                )
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            # Response message not Success — fail with context
            testResult(
                self, "failed",
                "SMS number and template should be updated in master_conf.json file on device",
                f"Unexpected response message: {response_body.get('message', 'No message available')}."
            )
            # self.result.set_result(TestResults.failed)
            assert False, f"Unexpected response message: {response_body.get('message', 'No message available')}."
    else:
        testResult(
            self, "failed",
            "SMS number and template should be updated in master_conf.json file on device",
            f"API call failed with status code {response.status_code}."
        )
        # self.result.set_result(TestResults.failed)
        assert False, f"API call failed with status code {response.status_code}."