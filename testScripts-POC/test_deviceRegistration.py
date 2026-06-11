import json
import random

import pytest

from C2CModules.deviceRegistration_modules import registration_DeviceReg, \
    registration_getCount, registration_getDetails, deviceRegistration_post, deviceRegistration_getCount, \
    deviceRegistration_getDetails
from C2CModules.e2e_testData import deviceType_IVI
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


class Test_Registration:

    # Registration-DeviceReg
    @pytest.mark.Smoke
    def test1_positive_Registration_DeviceReg(self):
        registration_DeviceReg(self, deviceType_IVI)

    # Registration_getCount
    @pytest.mark.Smoke
    def test2_positive_Registration_getCount(self):
        registration_getCount(self)

    # Registration_getDetails
    @pytest.mark.Smoke
    def test3_positive_Registration_getDetails(self):
        registration_getDetails(self)


class Test_RegistrationNegative:

    @pytest.mark.Smoke
    def test1_negative_Registration_DeviceReg_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_Registration_DeviceReg_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "empty_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_Registration_DeviceReg_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "no_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_Registration_DeviceReg_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_negative_Registration_DeviceReg_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "no_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response"),
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6_negative_Registration_DeviceReg_invalid_deviceType(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_deviceType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "T%$"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "Invalid system name found":
                print("Device is not registered and displaying proper error message for invalid device type")
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7_negative_Registration_DeviceReg_empty_deviceType(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "Invalid system name found":
                print("Device is not registered and displaying proper error message for empty device type")
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8_negative_Registration_DeviceReg_no_deviceType(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "no_deviceType")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "13007" or response_body[
            "responseMessage"] == "required key [device_type] not found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    @pytest.mark.Smoke
    def test9_negative_Registration_DeviceReg_invalid_deviceIdLessThen3Chars(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_deviceIdLessThen3Chars")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)])
            device_id = "D" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "[device_id] length violation":
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10_negative_Registration_DeviceReg_invalid_deviceIdGreaterThen19Chars(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_deviceIdGreaterThen19Chars")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(9) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "[device_id] should be maximum 19 characters,[device_id] length violation":
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test11_negative_Registration_DeviceReg_invalid_deviceId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_deviceIdGreaterThen19Chars")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA %$ TCU " + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "[device_id] cannot contain invalid characters,[device_id] length violation":
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12_negative_Registration_DeviceReg_empty_deviceId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_deviceIdGreaterThen19Chars")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            # random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = ""
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "REGISTERED":
                print("Device is registered with new Device Id :", response_body["responseData"][0]["device_id"])
                testResult(self, "passed", "Device should be registered with auto generated device id",
                           "Device is registered successfully with auto generated device id. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'REGISTERED' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test13_negative_Registration_DeviceReg_no_deviceId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            # random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = ""
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "no_deviceId")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "13007" or response_body[
            "responseMessage"] == "required key [device_id] not found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test14_negative_Registration_DeviceReg_invalid_attestationMechanism(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_DeviceReg_invalid_attestationMechanism")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.50"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "Invalid attestation mechanism found":
                print("Device is not registered and displaying proper error message for invalid attestation mechanism")
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test15_negative_Registration_DeviceReg_empty_attestationMechanism(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = ""

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "Invalid attestation mechanism found":
                print(
                    "Device is not registered and displaying proper error message for empty attestation mechanism")
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test16_negative_Registration_DeviceReg_no_attestationMechanism(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        print("Device Id :", device_id)
        print("Device Type :", device_type)
        print("Attestation Mechanism :", attestationMechanism)

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism,
                                           "no_attestationMechanism")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "13007" and response_body[
            "responseMessage"] == "required key [attestationMechanism] not found":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test17_negative_Registration_getCount_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test18_negative_Registration_getCount_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "empty_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test19_negative_Registration_getCount_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "no_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test20_negative_Registration_getCount_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test21_negative_Registration_getCount_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "no_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test22_negative_Registration_getCount_invalid_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount_invalid_reqId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "invalid_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "responseCode"] == "13003" and "Invalid Request Id found" in response_body["responseMessage"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test23_negative_Registration_getCount_incorrect_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        try:
            # Read reqId from Registration_DeviceReg api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            requestId = json_object["responseData"]["requestId"]
        except:
            requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "incorrect_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "responseCode"] == "2002" and "does not exist" in response_body["responseMessage"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test24_negative_Registration_getCount_empty_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getCount")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            requestId = ""

        print("Request Id :", requestId)

        response = deviceRegistration_getCount(self, requestId, "no_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404 and response_body["error"] == "Not Found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test25_negative_Registration_getDetails_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test26_negative_Registration_getDetails_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "empty_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching..please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test27_negative_Registration_getDetails_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "no_apiKey")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test28_negative_Registration_getDetails_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test29_negative_Registration_getDetails_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "no_x-requestor")

        # Validate response status code
        if response.status_code == 202:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test30_negative_Registration_getDetails_invalid_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails_invalid_reqId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            try:
                # Read reqId from Registration_DeviceReg api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                requestId = json_object["responseData"]["requestId"]
            except:
                requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "invalid_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "responseCode"] == "13003" and "Invalid Request Id found" in response_body["responseMessage"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test31_negative_Registration_getDetails_incorrect_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # requestId = str(dict1["requestId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        try:
            # Read reqId from Registration_DeviceReg api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            requestId = json_object["responseData"]["requestId"]
        except:
            requestId = "63969765-356b-4ae2-9e65-151f4666eabe"

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "incorrect_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "responseCode"] == "2002" and "No devices found" in response_body["responseMessage"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test32_negative_Registration_getDetails_empty_requestId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration_getDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            requestId = ""

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "no_requestId")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404 and response_body["error"] == "Not Found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test33_negative_Registration_DeviceReg_duplicate_deviceId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DeviceRegistration",
                                         "Registration-DeviceReg")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            device_type = str(dict1["device_type"])
            device_id = str(dict1["device_id"])
            attestationMechanism = str(dict1["attestationMechanism"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            device_type = "TCU"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])
            device_id = "QA_TEST_TCU_" + random_id
            attestationMechanism = "X.509"

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "valid")

        response = deviceRegistration_post(self, device_type, device_id, attestationMechanism, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "SUCCESS":
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Read reqId from Registration_DeviceReg api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        requestId = json_object["responseData"]["requestId"]

        print("Request Id :", requestId)

        response = deviceRegistration_getDetails(self, requestId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["responseMessage"] == "Success":
            if response_body["responseData"][0]["status"] == "FAIL" and response_body["responseData"][0][
                "errorMessage"] == "Device is already registered":
                print(
                    "Device is not registered and displaying proper error message for duplicate device Id")
                testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print("Status is not 'FAIL' ")
                print("Response/Error message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")