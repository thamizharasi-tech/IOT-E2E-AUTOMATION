import ast
import json
import requests

from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# FileUpload
def notification_message(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FileUpload")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    #  vin = getVIN(self, "tel", deviceType_IVI)
    #  systemId = get_SystemId(self, deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FileUpload', response.text)
    save_api_resp_in_excel(self, "API_Data", "FileUpload", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert (response_body["responseData"]["message"] == "Vehicle data updated successfully")
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body
