import ast
import json
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# vehicleServices_CreateVehicleServiceEntry
def vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag, serviceDate,
                                              serviceDueDate, serviceOdo, serviceDueOdo, dateReminder, odoReminder,
                                              notes, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicleServices_createVehicleServiceEntry")
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
    print("Header : ",header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["vin"] = vin
    json_object["status"] = status
    json_object["deviceMaintenanceFlag"] = deviceMaintenanceFlag
    json_object["serviceDate"] = serviceDate
    json_object["serviceDueDate"] = serviceDueDate
    json_object["serviceOdo"] = serviceOdo
    json_object["serviceDueOdo"] = serviceDueOdo
    json_object["dateReminder"] = dateReminder
    json_object["odoReminder"] = odoReminder
    json_object["notes"] = notes
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('vehicleServices_createVehicleServiceEntry', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicleServices_createVehicleServiceEntry", response.text)

    return response


# vehicleServices_updateVehicleServiceEntry
def vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag, serviceDate,
                                              serviceDueDate, serviceOdo, serviceDueOdo, dateReminder, odoReminder,
                                              notes, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicleServices_updateVehicleServiceEntry")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ",header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["vin"] = vin
    json_object["status"] = status
    json_object["deviceMaintenanceFlag"] = deviceMaintenanceFlag
    json_object["serviceDate"] = serviceDate
    json_object["serviceDueDate"] = serviceDueDate
    json_object["serviceOdo"] = serviceOdo
    json_object["serviceDueOdo"] = serviceDueOdo
    json_object["dateReminder"] = dateReminder
    json_object["odoReminder"] = odoReminder
    json_object["notes"] = notes
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('vehicleServices_updateVehicleServiceEntry', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicleServices_updateVehicleServiceEntry", response.text)

    return response


# vehicleServices_getVehicleServiceHistoryList
def vehicleServices_getVehicleServiceHistoryList(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicleServices_getVehicleServiceHistoryList")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ",header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('vehicleServices_getVehicleServiceHistoryList', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicleServices_getVehicleServiceHistoryList", response.text)

    return response


# vehicleServices_getVehicleServiceDetails
def vehicleServices_getVehicleServiceDetails(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicleServices_getVehicleServiceDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ",header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('vehicleServices_getVehicleServiceDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicleServices_getVehicleServiceDetails", response.text)

    return response


# vehicleServices_deleteVehicleServiceEntry
def vehicleServices_deleteVehicleServiceEntry(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "vehicleServices_deleteVehicleServiceEntry")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ",header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('vehicleServices_deleteVehicleServiceEntry', response.text)
    save_api_resp_in_excel(self, "API_Data", "vehicleServices_deleteVehicleServiceEntry", response.text)

    return response
