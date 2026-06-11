import random

import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.commandControl_modules import (CommandControl_Request_addTemplate,
                                               CommandControl_Request_getTemplateInfo,
                                               CommandControl_Request_updateTemplate,
                                               CommandControl_Request_addModelTemplate,
                                               CommandControl_Request_getModelTemplate,
                                               CommandControl_Request_updateModelTemplate,
                                               CommandControl_Request_addOEM, CommandControl_Request_getOEM,
                                               CommandControl_Request_updateOEM)
from C2CModules.primary_IVI_device_modules import getModel
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_CommandAPI:

    # CommandControl_Request_addTemplate
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addTemplate(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_invalid_baseTemplateID
    def test1_positive_CommandControl_Request_invalid_baseTemplateID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate_invalid_baseTemplateID")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_without_name
    def test1_positive_CommandControl_Request_without_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "missing_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_without_name
    def test1_positive_command_control_request_without_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "missing_description")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_empty_name
    def test1_positive_commandcontrol_request_empty_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate_empty_name")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            if name == "None":
                name = ""
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_empty_description
    def test1_positive_CommandControl_Request_empty_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate_empty_description")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            if description == "None":
                description = ''
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")
        # CommandControl_Request_addTemplate_empty_description

    # CommandControl_Request_addTemplate_invalid_apikey
    def test1_positive_CommandControl_Request_invalid_apikey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_empty_apikey
    def test1_positive_CommandControl_Request_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_no_apiKey
    def test1_positive_CommandControl_Request_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_empty_x-requestor
    def test1_positive_CommandControl_Request_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate_no_x-requestor
    def test1_positive_CommandControl_Request_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getTemplateInfo(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_invalid_templateID
    def test1_negative_CommandControl_Request_getTemplateInfo_invalid_templateID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo_invalid_templateID")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_invalid_name
    def test1_negative_CommandControl_Request_getTemplateInfo_invalid_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo_invalid_name")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_invalid_baseTemplateID
    def test1_negative_CommandControl_Request_getTemplateInfo_invalid_baseTemplateID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo_invalid_baseTemplateID")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_invalid_apiKey
    def test1_negative_CommandControl_Request_getTemplateInfo_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_empty_apiKey
    def test1_negative_CommandControl_Request_getTemplateInfo_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_no_apiKey
    def test1_negative_CommandControl_Request_getTemplateInfo_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_empty_x-requestor
    def test1_negative_CommandControl_Request_getTemplateInfo_empty_x_requestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getTemplateInfo_no_x-requestor
    def test1_negative_CommandControl_Request_getTemplateInfo_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getTemplateInfo")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            # description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            # description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateTemplate
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateTemplate(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateTemplate_invalid_templateID
    def test1_negative_CommandControl_Request_updateTemplate_invalid_templateID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateTemplate_invalid_templateID")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # without_name
    def test1_negative_CommandControl_Request_updateTemplate_without_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "missing_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

        # without_description

    def test1_negative_CommandControl_Request_updateTemplate_without_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "missing_description")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateTemplate_invalid_basetemplateID
    def test1_negative_CommandControl_Request_updateTemplate_invalid_basetemplateID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateTemplate_invalid_basetemplateID")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateTemplate_empty_name
    def test1_negative_CommandControl_Request_updateTemplate_empty_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateTemplate_empty_name")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            if name == "None":
                name = ''
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateTemplate_empty_description
    def test1_negative_CommandControl_Request_updateTemplate_empty_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateTemplate_empty_description")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            if description == "None":
                description = ''
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_invalid_apiKey
    def test1_positive_CommandControl_Request_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_empty_apiKey
    def test1_negative_CommandControl_Request_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_no_apiKey
    def test1_negative_CommandControl_Request_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_empty_x-requestor
    def test1_negative_CommandControl_Request_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_no_x-requestor
    def test1_negative_CommandControl_Request_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            template_id = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"
            template_id = "31"

        response = CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,
                                                         "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addTemplate
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addTemplate(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            baseTemplateId = str(dict1["baseTemplateId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            baseTemplateId = 13
            name = 'bmw'
            description = "testingAPI"

        response = CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addModelTemplate
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addModelTemplate(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # invalid_apiKey
    def test1_negative_CommandControl_Request_addModelTemplate_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = "Bmw"
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_apiKey
    def test1_negative_CommandControl_Request_addModelTemplate_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = "Bmw"
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # no_apiKey
    def test1_negative_CommandControl_Request_addModelTemplate_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = "Bmw"
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_x-requestor
    def test1_negative_CommandControl_Request_addModelTemplate_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = "Bmw"
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # no_x-requestor
    def test1_negative_CommandControl_Request_addModelTemplate_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = "Bmw"
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # invalid_appId
    def test1_negative_CommandControl_Request_addModelTemplate_invalid_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_invalid_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_appId
    def test1_negative_CommandControl_Request_addModelTemplate_empty_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_empty_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # without_appId
    def test1_negative_CommandControl_Request_addModelTemplate_without_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "missing_appId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_appId
    def test1_negative_CommandControl_Request_addModelTemplate_empty_model(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_empty_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])

            model = str(dict1["model"])
            if model == "None":
                model = ''
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # without_model
    def test1_negative_CommandControl_Request_addModelTemplate_without_model(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "missing_model")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_class
    def test1_negative_CommandControl_Request_addModelTemplate_empty_class(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_empty_class")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            if class1 == "None":
                class1 = ''
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # without_class
    def test1_negative_CommandControl_Request_addModelTemplate_without_class(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "missing_class")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_style
    def test1_negative_CommandControl_Request_addModelTemplate_empty_style(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_empty_style")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            if style == "None":
                style = ''
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # without_style
    def test1_negative_CommandControl_Request_addModelTemplate_without_style(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "missing_style")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_template_Id
    def test1_negative_CommandControl_Request_addModelTemplate_empty_template_Id(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate_empty_templateId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])

            templateId = str(dict1["templateId"])
            if templateId == "None":
                templateId = ''
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # missing_templateId
    def test2_negative_CommandControl_Request_addModelTemplate_without_style(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_addModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'

        response = CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                           "missing_templateId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

        # CommandControl_Request_getModelTemplate

    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getModelTemplate(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No input required")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = getModel(self, "IVI", b2c_ivi_chipset)

        response = CommandControl_Request_getModelTemplate(self, model, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # invalid_apikey
    def test1_negative_CommandControl_Request_getModelTemplate_invalid_apikey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            model = str(dict1["model"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

        response = CommandControl_Request_getModelTemplate(self, model, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_apiKey
    def test1_negative_CommandControl_Request_getModelTemplate_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            model = str(dict1["model"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

        response = CommandControl_Request_getModelTemplate(self, model, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # no_apiKey
    def test1_negative_CommandControl_Request_getModelTemplate_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            model = str(dict1["model"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

        response = CommandControl_Request_getModelTemplate(self, model, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # empty_x-requestor
    def test1_negative_CommandControl_Request_getModelTemplate_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            model = str(dict1["model"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

        response = CommandControl_Request_getModelTemplate(self, model, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # no_x-requestor
    def test1_negative_CommandControl_Request_getModelTemplate_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_getModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            model = str(dict1["model"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            model = 'BMW_' + str(msg_id)

        response = CommandControl_Request_getModelTemplate(self, model, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate
    def test1_positive_CommandControl_Request_updateModelTemplate(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style, templateId,
                                                              baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_invalid_apiKey
    def test1_positive_CommandControl_Request_updateModelTemplate_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_apiKey
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_no_apiKey
    def test1_positive_CommandControl_Request_updateModelTemplate_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_x-requestor
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_no_x-requestor
    def test1_positive_CommandControl_Request_updateModelTemplate_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_invalid_appId
    def test1_positive_CommandControl_Request_updateModelTemplate_invalid_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_invalid_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_appId
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_without_appId
    def test1_positive_CommandControl_Request_updateModelTemplate_without_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_appId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_model
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_model(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_model")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            if model == "None":
                model = ''
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_without_model
    def test1_positive_CommandControl_Request_updateModelTemplate_without_model(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_model")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_modelYear
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_modelYear(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_modelYear")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            if modelYear == "None":
                modelYear = ''
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_without_modelYear
    def test1_positive_CommandControl_Request_updateModelTemplate_without_modelYear(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_ModelYear")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_class
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_class(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_class")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])

            class1 = str(dict1["class"])
            if class1 == "None":
                class1 = ''
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'

            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_without_class
    def test1_positive_CommandControl_Request_updateModelTemplate_without_class(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_class")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_style
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_style(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_style")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            if style == "None":
                style = ''
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            if class1 == "None":
                class1 = ''
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_without_style
    def test1_positive_CommandControl_Request_updateModelTemplate_without_style(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_style")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_invalid_template_id
    def test1_positive_CommandControl_Request_updateModelTemplate_invalid_template_id(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_invalid_template_id")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateModelTemplate_empty_template_id
    def test1_positive_CommandControl_Request_updateModelTemplate_empty_template_id(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate_empty_template_id")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])

            templateId = str(dict1["templateId"])
            if templateId == "None":
                templateId = ''
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            if class1 == "None":
                class1 = ''
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

        # CommandControl_Request_updateModelTemplate_without_templateId

    def test1_positive_CommandControl_Request_updateModelTemplate_without_templateId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl",
                                         "CommandControl_Request_updateModelTemplate")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            model = str(dict1["model"])
            modelYear = str(dict1["modelYear"])
            class1 = str(dict1["class"])
            style = str(dict1["style"])
            templateId = str(dict1["templateId"])
            baseTemplateId = str(dict1["baseTemplateId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            appId = 'c6078'
            model = 'BMW9'
            modelYear = '2021'
            class1 = 'F'
            style = 'Sedan'
            templateId = '1'
            baseTemplateId = '1'

        response = CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style,
                                                              templateId, baseTemplateId, "missing_templateId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addOEM
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            oemId = str(dict1["oemId"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("Validations : ")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            print("Response message : ", response_body['responseData']['message'])

            testResult(self, "passed",
                       "Should add to OEM successfully",
                       "Successfully added to OEM")
        elif response_body["responseCode"] != str(1200):
            print("response Code is not 1200. Rather found : " + str(response_body["message"]))
            testResult(self, "failed",
                       "Should add to OEM successfully",
                       "Failed to add to OEM")
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_empty_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_empty_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM_empty_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_without_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_without_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, "missing_appId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_invalid_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_invalid_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM_invalid_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, "missing_appId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_empty_name
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_empty_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM_empty_name")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            if name == "None":
                name = ''
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_without_name
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_without_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, "missing_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_empty_description
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_empty_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM_empty_description")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            if description == "None":
                description = ''
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_without_description
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_without_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "missing_description")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_without_defaultTemplateId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_without_defaultTemplateId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "missing_defaultTemplateId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_invalid_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_empty_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_no_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_empty_x-requestor
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_addOEM_no_x-requestor
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_addOEM_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_addOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            name = 'Maruti'
            description = "New OEM"
            defaultTemplateId = '1'

        response = CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId,
                                                 "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

    print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("Validations : ")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            print("Response message : ", response_body['responseData']['message'])

            testResult(self, "passed",
                       "Should update to OEM successfully",
                       "Successfully updated to OEM")
        elif response_body["responseCode"] != str(1200):
            print("response Code is not 1200. Rather found : " + str(response_body["message"]))
            testResult(self, "failed",
                       "Should update to OEM successfully",
                       "Failed to update to OEM")
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_invalid_oemId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_invalid_oemId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM_invalid_oemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        oemId = "32swefw#$$$$"
        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_empty_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_empty_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM_empty_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            if appId == "None":
                appId = ''
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_invalid_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_invalid_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM_invalid_appId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_without_appId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_without_appId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "missing_appId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_empty_name
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_empty_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM_empty_name")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            if name == "None":
                name = ''
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_without_name
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_without_name(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "missing_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_empty_description
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_empty_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM_empty_description")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            if description == "None":
                description = ''
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_without_description
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_without_description(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "missing_description")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_without_defaultTemplateId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_without_defaultTemplateId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "missing_defaultTemplateId")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_invalid_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_empty_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_no_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_empty_x-requestor
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_updateOEM_no_x-requestor
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_updateOEM_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_updateOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])
            appId = str(dict1["appid"])
            name = str(dict1["name"])
            description = str(dict1["description"])
            defaultTemplateId = str(dict1["defaultTemplateId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            print("Initiated message Id : ", msg_id)
            appId = "appId_" + str(msg_id)
            oemId = "32"
            name = "Tesla"
            description = "update_OEM"
            defaultTemplateId = "6"

        response = CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId,
                                                    "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("Validations : ")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            print("Response message : ", response_body['responseData']['message'])
            if response_body['responseData']['dataList'][0]['oemId'] == int(oemId):
                print("OEM Id : ", response_body['responseData']['dataList'][0]['oemId'])
                print("Name : ", response_body['responseData']['dataList'][0]['name'])
                print("Default Template Id : ", response_body['responseData']['dataList'][0]['defaultTemplateId'])
                print("description : ", response_body['responseData']['dataList'][0]['description'])

                testResult(self, "passed",
                           "Should fetch OEM details successfully",
                           "Successfully fetched OEM details")
            else:
                print("oemId mismatch or data list is empty")
                testResult(self, "failed",
                           "Should fetch OEM details successfully",
                           "oemId mismatch or data list is empty")
        elif response_body["responseCode"] != str(1200):
            print("response Code is not 1200. Rather found : " + str(response_body["message"]))
            testResult(self, "failed",
                       "Should fetch OEM details successfully",
                       "Failed to fetch OEM details")
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_invalid_oemId
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_invalid_oemId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM_invalid_oemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, testCaseName)

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_invalid_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_empty_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_no_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_no_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_empty_x-requestor
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")

    # CommandControl_Request_getOEM_invalid_apiKey
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_getOEM_no_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_getOEM")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            oemId = str(dict1["oemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            oemId = '3'

        response = CommandControl_Request_getOEM(self, oemId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        print("----------------------------------------------------------")
