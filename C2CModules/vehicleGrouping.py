import ast
import json
import time
import requests
import os

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult

folder_path = "C:\Car2Cloud_E2ETesting"

# ------------------------------------------
# Vehicle Grouping Reusable Modules
# ------------------------------------------

# API operation to create a vehicle group
def vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                           criteria2_operator, criteria2_value, criteria2_key, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleGrouping_create_vehicle_group")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    #url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    #payload
    json_object = json.loads(payload)
    json_object["name"] = groupName
    json_object["description"] = desc
    json_object["criteria"][0]["operator"] = criteria1_operator
    json_object["criteria"][0]["value"][0] = criteria1_value
    json_object["criteria"][0]["key"] = criteria1_key
    json_object["criteria"][1]["operator"] = criteria2_operator
    json_object["criteria"][1]["value"][0] = criteria2_value
    json_object["criteria"][1]["key"] = criteria2_key
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleGrouping_create_vehicle_group', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleGrouping_create_vehicle_group", response.text)

    return response


# API operation to update/edit vehicle group details
def edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                       criteria2_operator, criteria2_value, criteria2_key, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleGrouping_update_vehicle_group")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    #url
    complete_url = str(base_url + endpoint).replace('{groupName}', groupName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    #payload
    json_object = json.loads(payload)
    json_object["name"] = groupName
    json_object["description"] = desc
    json_object["criteria"][0]["operator"] = criteria1_operator
    json_object["criteria"][0]["value"][0] = criteria1_value
    json_object["criteria"][0]["key"] = criteria1_key
    json_object["criteria"][1]["operator"] = criteria2_operator
    json_object["criteria"][1]["value"][0] = criteria2_value
    json_object["criteria"][1]["key"] = criteria2_key
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleGrouping_update_vehicle_group', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleGrouping_update_vehicle_group", response.text)

    return response

# API operation to fetch vehicle group details with pagination
def fetch_vehicle_group_details_with_pagination(self, groupName, offset, limit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleGrouping_get_vehicle_group_based_on_pagination")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{groupName}', groupName).replace('{offset}', offset).replace('{limit}', limit)
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
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleGrouping_get_vehicle_group_based_on_pagination', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleGrouping_get_vehicle_group_based_on_pagination", response.text)

    return response


# API operation to fetch vehicle group details based on criteria
def fetch_vehicle_group_details_based_on_criteria(self, key, operator, value, offset, limit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleGrouping_get_vehicle_group_based_on_criteria")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace(
        '{limit}', limit)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["criteria"][0]["key"] = key
    json_object["criteria"][0]["operator"] = operator
    json_object["criteria"][0]["value"][0] = value
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleGrouping_get_vehicle_group_based_on_criteria', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleGrouping_get_vehicle_group_based_on_criteria", response.text)

    return response


# API operation to delete a vehicle group
def vehicle_group_deletion(self, groupName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "VehicleGrouping_delete_vehicle_group")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{groupName}', groupName)
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
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('VehicleGrouping_delete_vehicle_group', response.text)
    save_api_resp_in_excel(self, "API_Data", "VehicleGrouping_delete_vehicle_group", response.text)

    return response


def vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                  criteria2_operator, criteria2_value, criteria2_key, option, tc):
    # print(option, tc)
    if tc == "create_vehicle_group":
        # Call vehicle group creation reusable module
        response = vehicle_group_creation(self, groupName, desc, criteria1_operator, criteria1_value, criteria1_key,
                                          criteria2_operator, criteria2_value, criteria2_key, option)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        message = response_body["message"]

        if message == "Data Saved Successfully":
            testResult(self, "passed",
                   "The vehicle group should be created successfully",
                   "The vehicle group is created successfully")
        else:
            testResult(self, "failed",
                   "The vehicle group should be created successfully",
                   "Failed to create vehicle group. Refer api response for failure details")

        groupName_file = os.path.join(folder_path, 'groupName.txt')
        print("Vehicle Group Name File : ", groupName_file)

        text_file = open(groupName_file, "w+")
        text_file.write(str(groupName))
        text_file.close()

    elif tc == "update_vehicle_group":
        groupName_file = os.path.join(folder_path, 'groupName.txt')
        print("Vehicle Group Name File : ", groupName_file)

        text_file = open(groupName_file, "r")
        groupName = text_file.read()
        text_file.close()

        # Call vehicle group update reusable module
        response = edit_vehicle_group(self, groupName, desc, criteria1_operator, criteria1_value,
                                      criteria1_key,
                                      criteria2_operator, criteria2_value, criteria2_key, option)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        message = response_body["message"]

        if message == "Data Updated Successfully":
            testResult(self, "passed",
                   "The vehicle group should be updated successfully",
                   "The vehicle group is created successfully")
        else:
            testResult(self, "failed",
                   "The vehicle group should be updated successfully",
                   "Failed to update vehicle group. Refer api response for failure details")
    else:
        print("Incorrect test case/option")

    print("----------------------------------------------------------")

    # Fetch vehicle group details and Verify
    response = fetch_vehicle_group_details_based_on_criteria(self, criteria1_key, criteria1_operator,
                                                             criteria1_value, '0', '100', "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    status = ''
    if response_body["message"] == "Data fetched Successfully":
        data_len = len(response_body["vehicleGroup"])
        if data_len >= 1:
            for i in range(data_len):
                name = response_body["vehicleGroup"][i]["name"]
                if groupName == name:
                    status = "pass"
                    testResult(self, "passed",
                           "The vehicle group should be fetched successfully based on criteria",
                           "The vehicle group is fetched successfully based on criteria")
                    break

        if status != "pass":
            testResult(self, "failed",
                   "The vehicle group should be fetched successfully based on criteria",
                   "Failed to fetch vehicle group based on criteria. Refer api response for failure details")

    print("----------------------------------------------------------")

    # Fetch vehicle group details and Verify
    response = fetch_vehicle_group_details_with_pagination(self, groupName, '0', '100', "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    status = ''
    if response_body["message"] == "Data Fetched Successfully":
        name = response_body["vehicleGroup"]["name"]

        if groupName == name:
            testResult(self, "passed",
                   "The vehicle group should be fetched successfully",
                   "The vehicle group is fetched successfully")
        else:
            testResult(self, "failed",
                   "The vehicle group should be fetched successfully",
                   "Failed to fetch vehicle group. Refer api response for failure details")

    print("----------------------------------------------------------")


def delete_vehicle_group(self):
    groupName_file = os.path.join(folder_path, 'groupName.txt')
    print("Vehicle Group Name File : ", groupName_file)

    text_file = open(groupName_file, "r")
    groupName_for_delete = text_file.read()
    text_file.close()

    # Call vehicle group deletion reusable module
    response = vehicle_group_deletion(self, groupName_for_delete, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response body
    message = response_body["message"]

    if message == "Data Deleted Successfully":
        testResult(self, "passed",
               "The vehicle group should be deleted successfully",
               "The vehicle group is deleted successfully")
    else:
        testResult(self, "failed",
               "The vehicle group should be deleted successfully",
               "Failed to delete vehicle group. Refer api response for failure details")

    print("----------------------------------------------------------")
