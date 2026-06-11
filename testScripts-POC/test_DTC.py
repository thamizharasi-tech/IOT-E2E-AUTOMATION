import pytest

from C2CModules.DTC import DTC_diagnosticErrorCodes, DTC_diagnosticErrorCodes_dtcCode
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_DTC:

    # DTC_diagnosticErrorCodes
    @pytest.mark.Smoke
    def test1_positive_DTC_diagnosticErrorCodes(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = "1"
            pageSize = "10"

        # Call DTC reusable module
        response_body = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])
                testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                           "Successfully fetched the current values/data for desired System Id ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                           "End point is working fine, but there is no data in DB for this System Id, thus marking "
                           "test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes
    @pytest.mark.Smoke
    def test2_positive_DTC_diagnosticErrorCodes_dtcCode(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = "1"
            pageSize = "10"

        # Call DTC reusable module
        response_body = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])
                if dtcCode_actual == dtcCode:
                    testResult(self, "passed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Successfully fetched the current values/data for desired System Id & dtc code")
                else:
                    testResult(self, "failed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Dtc Code does not match ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

        # DTC_diagnosticErrorCodes

    @pytest.mark.Smoke
    def test3_positive_DTC_diagnosticErrorCodes_details_true(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_details_parameter_true")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "true"
            pageNo = "1"
            pageSize = "10"

        # Call DTC reusable module
        response_body = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

                testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                           "Successfully fetched the current values/data for desired System Id ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                           "End point is working fine, but there is no data in DB for this System Id, thus marking "
                           "test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes
    @pytest.mark.Smoke
    def test4_positive_DTC_diagnosticErrorCodes_dtcCode_details_true(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_details_parameter_true")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "true"
            pageNo = "1"
            pageSize = "10"

        # Call DTC reusable module
        response_body = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])
                if dtcCode_actual == dtcCode:
                    testResult(self, "passed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Successfully fetched the current values/data for desired System Id & dtc code")
                else:
                    testResult(self, "failed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Dtc Code does not match ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False


    # DTC_diagnosticErrorCodes
    @pytest.mark.Smoke
    def test4_positive_DTC_diagnosticErrorCodes_dtcCode_details_false(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_details_parameter_true")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = "false"
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = "1"
            pageSize = "10"

        # Call DTC reusable module
        response_body = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])
                if dtcCode_actual == dtcCode:
                    testResult(self, "passed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Successfully fetched the current values/data for desired System Id & dtc code")
                else:
                    testResult(self, "failed",
                               "Should fetch the current data/values for System Id & dtc code successfully",
                               "Dtc Code does not match ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False



    # ------------------------
    # Negative Tcs
    # ------------------------

    # DTC_diagnosticErrorCodes_invalid_systemID
    @pytest.mark.Smoke
    def test1_negative_DTC_diagnosticErrorCodes_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = 'sys56'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Invalid SystemId or Dtc-Code Provided as Input" or response_body[
            "message"] == "No data records found for the given SystemId"

    # DTC_diagnosticErrorCodes_dtcCode_invalid_systemID
    @pytest.mark.Smoke
    def test2_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = 'sys56'
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Invalid SystemId or Dtc-Code Provided as Input"

        # DTC_diagnosticErrorCodes_invalidsystemID

    @pytest.mark.Smoke
    def test3_negative_DTC_diagnosticErrorCodes_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_empty_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ''
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_dtcCode_epmty_systemID
    @pytest.mark.Smoke
    def test4_negative_DTC_diagnosticErrorCodes_dtcCode_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_empty_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ''
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_incorrect_systemID
    @pytest.mark.Smoke
    def test5_negative_DTC_diagnosticErrorCodes_incorrect_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "No":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = 'sysc943bdfe252d11eeaed1'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "No data records found for the given SystemId"

    # DTC_diagnosticErrorCodes_dtcCode_incorrect_systemID
    @pytest.mark.Smoke
    def test6_negative_DTC_diagnosticErrorCodes_dtcCode_incorrect_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "No":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = 'sysc943bdfe252d11eeaed12'
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Invalid SystemId or Dtc-Code Provided as Input"

    # DTC_diagnosticErrorCodes_dtcCode_invalid_dtcCode
    @pytest.mark.Smoke
    def test7_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_dtcCode(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_invalid_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001&^%'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Invalid SystemId or Dtc-Code Provided as Input"

        # DTC_diagnosticErrorCodes_invalidsystemID

        # DTC_diagnosticErrorCodes_dtcCode_empty_dtcCode

    @pytest.mark.Smoke
    def test8_negative_DTC_diagnosticErrorCodes_dtcCode_empty_dtcCode(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_empty_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            if dtcCode == "None":
                dtcCode = ""
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = ''
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                # dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes_deatils_parameter_empty
    @pytest.mark.Smoke
    def test9_negative_DTC_diagnosticErrorCodes_details_parameter_empty(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_details_parameter_empty")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            if details == "None":
                details = ""
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = " "
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                # dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes_details_parameter_empty
    @pytest.mark.Smoke
    def test10_negative_DTC_diagnosticErrorCodes_dtcCode_details_parameter_empty(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_details_parameter_empty")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            if details == "None":
                details = ""
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = "P0001"
            details = " "
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                # dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

            else:
                print(" => datalist is empty")
                testResult(self, "passed",
                           "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed",
                       "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes_invalid_details_parameter
    @pytest.mark.Smoke
    def test11_negative_DTC_diagnosticErrorCodes_invalid_details_parameter(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_invalid_details_parameter")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "123 "
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                # dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed", "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes_dtcCode_invalid_details_parameter
    @pytest.mark.Smoke
    def test12_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_details_parameter(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_invalid_details_parameter")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = "P0001"
            details = "%^$"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Successfully fetched the current values'):

            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Device Id : ", response_body["responseData"]["dataList"][0]["deviceId"])
                # dtcCode_actual = response_body["responseData"]["dataList"][0]["dtcCode"]
                print("DTC Code : ", response_body["responseData"]["dataList"][0]["dtcCode"])
                print("DTC Sensor Value : ", response_body["responseData"]["dataList"][0]["dtcSensorValue"])
                print("DTC Description : ", response_body["responseData"]["dataList"][0]["dtcDescription"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Created By : ", response_body["responseData"]["dataList"][0]["createdBy"])
                print("Updated Time : ", response_body["responseData"]["dataList"][0]["updatedTime"])
                print("Updated By : ", response_body["responseData"]["dataList"][0]["updatedBy"])

            else:
                print(" => datalist is empty")
                testResult(self, "passed",
                           "Should fetch the current data/values for System Id & dtc code successfully",
                           "End point is working fine, but there is no data in DB for this System Id & dtc code, "
                           "thus marking test case as pass")

        elif response_body["message"] != str('Successfully fetched the current values'):

            testResult(self, "failed",
                       "Should fetch the current data/values for System id & dtc code successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    # DTC_diagnosticErrorCodes_pageNo_lessThanOne
    @pytest.mark.Smoke
    def test13_negative_DTC_diagnosticErrorCodes_pageNo_lessThanOne(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_pageNo_lessThanOne")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '0'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page index must not be less than zero!"

    # DTC_diagnosticErrorCodes_dtcCode_pageNo_lessThanOne
    @pytest.mark.Smoke
    def test14_negative_DTC_diagnosticErrorCodes_dtcCode_pageNo_lessThanOne(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_pageNo_lessThanOne")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '0'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page index must not be less than zero!"

    # DTC_diagnosticErrorCodes_empty_pageNo
    @pytest.mark.Smoke
    def test15_negative_DTC_diagnosticErrorCodes_empty_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_empty_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            if pageNo == "None":
                pageNo = ""
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = ''
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_dtcCode_empty_pageNo
    @pytest.mark.Smoke
    def test16_negative_DTC_diagnosticErrorCodes_dtcCode_empty_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_empty_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            if pageNo == "None":
                pageNo = ""
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = ''
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_negative_pageNo
    @pytest.mark.Smoke
    def test17_negative_DTC_diagnosticErrorCodes_negative_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_negative_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '-1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page index must not be less than zero!"

    # DTC_diagnosticErrorCodes_dtcCode_negative_pageNo
    @pytest.mark.Smoke
    def test18_negative_DTC_diagnosticErrorCodes_dtcCode_negative_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_negative_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '-1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page index must not be less than zero!"

    # DTC_diagnosticErrorCodes_invalid_pageNo
    @pytest.mark.Smoke
    def test19_negative_DTC_diagnosticErrorCodes_invalid_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = 'set%$'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_dtcCode_invalid_pageNo
    @pytest.mark.Smoke
    def test20_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_pageNo(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '%$%6'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_pageSize_lessThanOne
    @pytest.mark.Smoke
    def test21_negative_DTC_diagnosticErrorCodes_pageSize_lessThanOne(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_pageSize_lessThanOne")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '0'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page size must not be less than one!"

    # DTC_diagnosticErrorCodes_dtcCode_pageSize_lessThanOne
    @pytest.mark.Smoke
    def test22_negative_DTC_diagnosticErrorCodes_dtcCode_pageSize_lessThanOne(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_pageSize_lessThanOne")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '0'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page size must not be less than one!"

    # DTC_diagnosticErrorCodes_empty_pageSize
    @pytest.mark.Smoke
    def test23_negative_DTC_diagnosticErrorCodes_empty_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_empty_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            if pageSize == "None":
                pageSize = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = ''

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_dtcCode_empty_pageSize
    @pytest.mark.Smoke
    def test24_negative_DTC_diagnosticErrorCodes_dtcCode_empty_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_empty_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            if pageSize == "None":
                pageSize = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = ''

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_negative_pageSize
    @pytest.mark.Smoke
    def test25_negative_DTC_diagnosticErrorCodes_negative_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_negative_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '-1'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page size must not be less than one!"

    # DTC_diagnosticErrorCodes_dtcCode_negative_pageSize
    @pytest.mark.Smoke
    def test26_negative_DTC_diagnosticErrorCodes_dtcCode_negative_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_negative_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '-1'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validation of response body
        assert response_body["responseCode"] == "17003"
        assert response_body["responseData"]["message"] == "Page size must not be less than one!"

    # DTC_diagnosticErrorCodes_invalid_pageSize
    @pytest.mark.Smoke
    def test27_negative_DTC_diagnosticErrorCodes_invalid_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = 'set%$'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_dtcCode_invalid_pageSize
    @pytest.mark.Smoke
    def test28_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = 'set%$'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

    # DTC_diagnosticErrorCodes_pageNo_greaterThan_pageSize
    @pytest.mark.Smoke
    def test29_negative_DTC_diagnosticErrorCodes_pageNo_greaterThan_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_pageNo_greaterThan_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '11'
            pageSize = '1'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        response_body = response.json()
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_dtcCode_pageNo_greaterThan_pageSize
    @pytest.mark.Smoke
    def test30_negative_DTC_diagnosticErrorCodes_dtcCode_pageNo_greaterThan_pageSize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode_pageNo_greaterThan_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '11'
            pageSize = '1'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize, "invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        response_body = response.json()
        assert response_body["message"] == "Successfully fetched the current values"

    # DTC_diagnosticErrorCodes_invalid_apiKey
    @pytest.mark.Smoke
    def test31_negative_DTC_diagnosticErrorCodes_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

    # DTC_diagnosticErrorCodes_dtcCode_invalid_apiKey
    @pytest.mark.Smoke
    def test32_negative_DTC_diagnosticErrorCodes_dtcCode_invalid_apikey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize,
                                                    "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

    # DTC_diagnosticErrorCodes_empty_apiKey
    @pytest.mark.Smoke
    def test33_negative_DTC_diagnosticErrorCodes_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

    # DTC_diagnosticErrorCodes_dtcCode_empty_apiKey
    @pytest.mark.Smoke
    def test34_negative_DTC_diagnosticErrorCodes_dtcCode_empty_apikey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize,
                                                    "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

    # DTC_diagnosticErrorCodes_no_apiKey
    @pytest.mark.Smoke
    def test35_negative_DTC_diagnosticErrorCodes_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

    # DTC_diagnosticErrorCodes_dtcCode_no_apiKey
    @pytest.mark.Smoke
    def test36_negative_DTC_diagnosticErrorCodes_dtcCode_no_apikey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize,
                                                    "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

    # DTC_diagnosticErrorCodes_empty_x-requestor
    @pytest.mark.Smoke
    def test37_negative_DTC_diagnosticErrorCodes_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "x-requestor header cannot be blank"

    # DTC_diagnosticErrorCodes_dtcCode_empty_x-requestor
    @pytest.mark.Smoke
    def test38_negative_DTC_diagnosticErrorCodes_dtcCode_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize,
                                                    "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "x-requestor header cannot be blank"

    # DTC_diagnosticErrorCodes_no_x-requestor
    @pytest.mark.Smoke
    def test39_negative_DTC_diagnosticErrorCodes_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes(self, systemId, details, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

    # DTC_diagnosticErrorCodes_dtcCode_no_x-requestor
    @pytest.mark.Smoke
    def test40_negative_DTC_diagnosticErrorCodes_dtcCode_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC", "DTC_diagnosticErrorCodes_dtcCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            dtcCode = str(dict1["dtcCode"])
            details = str(dict1["details"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            dtcCode = 'P0001'
            details = "false"
            pageNo = '1'
            pageSize = '10'

        # Call DTC reusable module
        response = DTC_diagnosticErrorCodes_dtcCode(self, systemId, dtcCode, details, pageNo, pageSize,
                                                    "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["responseData"]["message"] == "Required authentication headers are missing"
