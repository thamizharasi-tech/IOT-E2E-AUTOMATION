import ast
import json
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# DTC
def DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_diagnosticErrorCodes")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DTC_diagnosticErrorCodes', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_diagnosticErrorCodes", response.text)

    return response


# DTC
def DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DTC_diagnosticErrorCodes_dtcCode")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{dtcCode}',dtcCode).replace('{pageNo}',pageNo).replace('{pageSize}',pageSize)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DTC_diagnosticErrorCodes_dtcCode', response.text)
    save_api_resp_in_excel(self, "API_Data", "DTC_diagnosticErrorCodes_dtcCode", response.text)

    return response


