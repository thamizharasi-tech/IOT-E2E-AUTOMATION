import glob
import os
import time
from datetime import datetime, timedelta, timezone

from C2CModules.fota_api_modules import FOTA_GetAllFirmware, FOTA_GetAllScriptDetails, FOTA_createPresigneUrl, \
    FOTA_uploadFile, FOTA_createSchedule, FOTA_GetAllScheduleDetails, FOTA_GetScheduleStatus
from C2CModules.sota_api_modules import SOTA_uploadFile, SOTA_ListPackages, SOTA_ListScripts, SOTA_CreateSchedule, \
    SOTA_ListSchedules, \
    SOTA_ListScheduleVin, SOTA_createPresignUrl
from C2CModules.c2c_modules import saveAPIrespIntoFile, testResult
from C2CModules.e2e_testData import C2CtestReport_otaPath, testData, deviceType_IVI
from C2CModules.primary_IVI_device_modules import getModel, getVIN
from C2CModules.resuse_modules import verify_message_in_ota_logs


def fileVer(self, file, option, FirmwareVerFlag_fota, FirmwareVersion_fota):
    global fileVer
    print("\n")

    if option == "baseFirmware":
        if FirmwareVerFlag_fota == "Yes":
            fileVer = FirmwareVersion_fota
        else:
            fileVer = file.split('_')
            fileVer = fileVer[1].replace('.zip', '')
            fileVer = fileVer.replace('v', '')

    elif option == "updateFirmware":
        if FirmwareVerFlag_fota == "Yes":
            fileVer = FirmwareVersion_fota
        else:
            fileVer = file.split('_')
            fileVer = fileVer[1].replace('.zip', '')
            fileVer = fileVer.replace('v', '')
    else:
        print("Incorrect Input")
    return fileVer


def sotaFileVer(self, packageNameFlag_sota, packageName_sota, packageVersionFlag_sota, packageVersion_sota,
                filename_sota):
    if packageNameFlag_sota == "Yes":
        appName = packageName_sota
    else:
        filenameS = filename_sota.split('_')
        appName = filenameS[0]

    if packageVersionFlag_sota == "Yes":
        targetVersion = packageVersion_sota
    else:
        filenameS = filename_sota.split('_')
        filenameV = filenameS[1].replace('.update', '')
        targetVersion = filenameV.replace('.zip', '')
        targetVersion = targetVersion.replace('v', '')
    return appName, targetVersion


def listFirmware(self, firmwareId, onboarding_Type, chipset_Type):
    time.sleep(30)
    s = 0

    # Get/Read Model
    model = getModel(self, onboarding_Type, chipset_Type)

    # fetch firmware details
    response = FOTA_GetAllFirmware(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listFirmware_" + model, str(response_body), "OTA")
    # print(response)

    if response_body['responseCode'] == '14000' or response_body['responseData']['message'] == str(14000):
        data_len = len(response_body["responseData"]["data"])
        # print(data_len)
        if data_len == 1:
            modelName = response_body["responseData"]["data"][0]['model']
            firmId = response_body["responseData"]["data"][0]['id']
            s = int(0)
        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["data"][i]['model']
                firmId = response_body["responseData"]["data"][i]['id']
                if modelName == model and str(firmwareId) == str(firmId):
                    s = int(i)
        firmId = response_body["responseData"]["data"][int(s)]['id']
        modelName = response_body["responseData"]["data"][int(s)]['model']
        status = response_body["responseData"]["data"][int(s)]['status']
        description = response_body["responseData"]["data"][int(s)]['description']
        system = response_body["responseData"]["data"][int(s)]['system']
        firmwareVersion = response_body["responseData"]["data"][int(s)]['firmwareVersion']
        fileName = response_body["responseData"]["data"][int(s)]['fileName']
        isDiffImage = response_body["responseData"]["data"][int(s)]['isDiffImage']
        isBase = response_body["responseData"]["data"][int(s)]['isBase']
        downloadConsent = response_body["responseData"]["data"][int(s)]['downloadConsent']
        installConsent = response_body["responseData"]["data"][int(s)]['installConsent']
        rebootConsent = response_body["responseData"]["data"][int(s)]['rebootConsent']

        if str(firmwareId) == str(firmId):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "Firmware package should listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files page",
                           "Firmware package is listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files page")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "Firmware package should listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files page",
                           "Firmware package is listed with FAILURE status on SMP UI-> Configuration -> OTA -> OTA Files page")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "Firmware package should listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files page",
                           "Firmware package is listed with ARCHIVE status on SMP UI-> Configuration -> OTA -> OTA Files page")

        elif str(firmwareId) != str(firmId):
            if firmwareId == 1:
                print("\n")
            else:
                testResult(self, "failed",
                           "Firmware package should be listed on first row on SMP UI-> Configuration -> OTA -> OTA Files page",
                           "Firmware package is not listed on first row or on SMP UI-> Configuration -> OTA -> OTA Files page")

    elif response_body["message"] != "SUCCESS":
        testResult(self, "failed",
                   "Firmware package should be listed on first row on SMP UI-> Configuration -> OTA -> OTA Files page",
                   "Firmware package list is not displayed on SMP UI-> Configuration -> OTA -> OTA Files page")

    else:
        print("Something went wrong")
    return model


def listFirmwareScript(self, scriptId, onboarding_Type, chipset_Type):
    time.sleep(30)
    refId = ''
    s = 0

    # Read model
    model = getModel(self, onboarding_Type, chipset_Type)

    # Get all script details
    response = FOTA_GetAllScriptDetails(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listFirmwareScript_" + model, str(response_body), "OTA")
    # print(response_body)

    if response_body["responseCode"] == "14000" or response_body["responseCode"] == 14000:
        data_len = len(response_body["responseData"]["data"])
        if data_len == 1:
            modelName = response_body["responseData"]["data"][0]['model']
            refId = response_body["responseData"]["data"][0]['refId']
            s = int(0)
        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["data"][i]['model']
                refId = response_body["responseData"]["data"][i]['refId']
                if modelName == model and scriptId == str(refId):
                    s = int(i)
        refId = response_body["responseData"]["data"][int(s)]['refId']
        name = response_body["responseData"]["data"][int(s)]['name']
        modelName = response_body["responseData"]["data"][int(s)]['model']
        status = response_body["responseData"]["data"][int(s)]['status']
        releaseNote = response_body["responseData"]["data"][int(s)]['releaseNote']
        sourceVersion = response_body["responseData"]["data"][int(s)]['steps'][0]['sourceVersion']
        targetVersion = response_body["responseData"]["data"][int(s)]['steps'][0]['targetVersion']
        if modelName == model and scriptId == str(refId):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "Firmware script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page",
                           name +
                           " - Firmware script is listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "Firmware script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page",
                           name +
                           " - Firmware script is listed with FAILURE status on SMP UI-> Configuration -> OTA -> Scripts page")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "Firmware script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page",
                           name +
                           " - Firmware script is listed with ARCHIVE status on SMP UI-> Configuration -> OTA -> Scripts page")

        elif modelName != model or scriptId != refId:
            testResult(self, "failed",
                       "Firmware script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page",
                       "Firmware script is not listed on first row or on SMP UI-> Configuration -> OTA -> Scripts page")

    elif response_body["responseCode"] != "14000":
        testResult(self, "failed",
                   "Firmware1 script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts page",
                   "Firmware1 script list is not displayed on SMP UI-> Configuration -> OTA -> Scripts page")

    else:
        print("Something went wrong")

    text_file = open(C2CtestReport_otaPath + r'beforeOTA\refId_fota.txt', "w")
    text_file.write(refId)
    text_file.close()
    return refId


def presignedUrl(self, model, filename, option, device_type):
    response_body = ""
    if option == "fota":
        if device_type == "IVI":
            response_body = FOTA_createPresigneUrl(self, filename, "IVI", model, "valid")
        if device_type == "TCU":
            response_body = FOTA_createPresigneUrl(self, filename, "Telematics", model, "valid")

    if option == "sota":
        if device_type == "IVI":
            response_body = SOTA_createPresignUrl(self, filename, "IVI", model, "valid")
        if device_type == "TCU":
            response_body = SOTA_createPresignUrl(self, filename, "Telematics", model, "valid")

    # Validate & parse api response in to json
    try:
        response_body = response_body.json()
    except:
        response_body = response_body

    saveAPIrespIntoFile("presignedUrl_" + model, response_body, "OTA")

    print(response_body["responseData"]["message"])
    upload_url = response_body["responseData"]["message"]
    saveAPIrespIntoFile("uploadUrl_" + model, "OTA", option)

    return response_body["responseData"]["message"]


def uploadFile_fota(self, model, upload_url, filepath, filename):
    # print("Final file path : => ", filepath)
    try:
        if upload_url != 'duplicated Firmware Version':
            files = {'file': open(filepath, 'rb')}
            # print(filepath)

            response_body = FOTA_uploadFile(self, upload_url, filepath, "valid")

            saveAPIrespIntoFile("uploadFile_" + filename + '_' + model, str(response_body), "OTA")
        else:
            print('duplicated Firmware Version, hence skipping upload file step')

    except:
        print("Something went wrong while uploading file")


def uploadFile(self, model, upload_url, filepath):
    try:
        print(upload_url)
        print(filepath)

        if upload_url != 'File already exists':

            print("Final file path : => ", filepath)

            files = {'file': open(filepath, 'rb')}
            # print(files)
            data = open(filepath, 'rb').read()

            response_body = SOTA_uploadFile(self, upload_url, data, "valid")
            print(response_body)

            saveAPIrespIntoFile("uploadFile_" + "IVI" + '_' + model, str(response_body), "OTA")
        else:
            print('Files already exists, hence skipping upload file step')

    except:
        print("Something went wrong while uploading file")


def triggerFirmwareUpdate(self, onboarding_Type, chipset_Type):
    scheduleId = ""
    model = getModel(self, onboarding_Type, chipset_Type)
    startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    print("Start Date : ", startDate)
    endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
    print("End Date : ", endDate)

    scriptId = read_refID(self, "fota")
    print(scriptId)

    vin = getVIN(self, onboarding_Type, chipset_Type)
    print("VIN No. : => ", vin)

    response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("triggerFirmwareUpdate_" + model, str(response_body), "OTA")
    # print(response_body)

    if response_body["responseCode"] == str(14000):
        if response_body["responseData"]["message"] == "success" or response_body["responseData"][
            "message"] == "Success":
            scheduleId = str(response_body["responseData"]["scheduleId"])
            testResult(self, "passed", "Firmware should be scheduled successfully and campaign should started ",
                       "Firmware scheduled successfully OR Campaign is started ")

    elif response_body["responseCode"] != str(14000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "Firmware should be scheduled successfully and campaign should started ",
                   "Firmware is not scheduled successfully OR Campaign is not started  " + " Reason for failure is : " +
                   response_body["responseData"]["message"])

    else:
        print("Something went wrong")
    text_file = open(C2CtestReport_otaPath + r'beforeOTA\scheduleId_fota.txt', "w")
    text_file.write(scheduleId)
    text_file.close()
    return scheduleId


def listFirmwareSchedules(self, scheduleId, onboarding_Type, chipset_Type):
    status = offered = accepted = complete = ""
    time.sleep(30)
    refId = ''
    s = 0

    model = getModel(self, onboarding_Type, chipset_Type)

    response = FOTA_GetAllScheduleDetails(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listFirmwareSchedules_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == 14000 or response_body["responseCode"] == "14000":
        data_len = len(response_body["responseData"]["data"])

        if data_len == 1:
            modelName = response_body["responseData"]["data"][0]['model']
            refId = response_body["responseData"]["data"][0]['refId']
            s = int(0)

        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["data"][i]['model']
                refId = response_body["responseData"]["data"][i]['refId']
                if modelName == model and scheduleId == str(refId):
                    s = int(i)

        modelName = response_body["responseData"]["data"][int(s)]['model']
        status = response_body["responseData"]["data"][int(s)]['status']
        offered = response_body["responseData"]["data"][int(s)]['offered']
        accepted = response_body["responseData"]["data"][int(s)]['accepted']
        complete = response_body["responseData"]["data"][int(s)]['complete']
        scriptId = response_body["responseData"]["data"][int(s)]['script']['id']
        scriptName = response_body["responseData"]["data"][int(s)]['script']['name']
        refId = response_body["responseData"]["data"][int(s)]['refId']

        if modelName == model and scheduleId == str(refId):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "Firmware schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates",
                           scriptName +
                           " - Firmware schedule/campaign is listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "Firmware schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates",
                           scriptName +
                           " - Firmware schedule/campaign is listed with FAILURE status on SMP UI-> Updates -> OTA -> OTA Updates")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "Firmware schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates",
                           scriptName +
                           " - Firmware schedule/campaign is listed with ARCHIVE status on SMP UI-> Updates -> OTA -> OTA Updates")

        elif modelName != model or scriptId != refId:
            testResult(self, "failed",
                       "Firmware schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates",
                       "Firmware schedule/campaign is not listed on first row or on SMP UI-> Updates -> OTA -> OTA Updates")

    elif response_body["responseCode"] != "14000":
        testResult(self, "failed",
                   "Firmware schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates",
                   "Firmware schedule/campaign list is not displayed on SMP UI-> Updates -> OTA -> OTA Updates")

    else:
        print("Something went wrong")

    return status, offered, accepted, complete


def listFirmwareScheduleStatus(self, onboarding_Type, chipset_Type):
    time.sleep(30)
    refId = status = ''

    model = getModel(self, onboarding_Type, chipset_Type)
    vin = getVIN(self, onboarding_Type, chipset_Type)
    scheduleId = read_scheduleId(self, "fota")

    response = FOTA_GetScheduleStatus(self, scheduleId, vin, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listFirmwareScheduleStatus_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(14000):

        vinNo = response_body["responseData"]["data"][0]['vin']
        status = response_body["responseData"]["data"][0]['status']

        # print(vin, vinNo)

        if vin == vinNo:
            print("Firmware schedule-status is listed with " + status + " status on SMP UI")

    return status


def listPackages(self, packageId, onboarding_Type, chipset_Type):
    time.sleep(30)
    s = 0
    model = getModel(self, onboarding_Type, chipset_Type)

    response = SOTA_ListPackages(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listPackages_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(15000):
        data_len = len(response_body["responseData"]["dataList"])
        if data_len == 1:
            modelName = response_body["responseData"]["dataList"][0]['model']
            packId = response_body["responseData"]["dataList"][0]['packageId']
            s = int(0)
        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["dataList"][i]['model']
                packId = response_body["responseData"]["dataList"][i]['packageId']
                if modelName == model and packageId == packId:
                    s = int(i)
        packId = response_body["responseData"]["dataList"][int(s)]['packageId']
        modelName = response_body["responseData"]["dataList"][int(s)]['model']
        status = response_body["responseData"]["dataList"][int(s)]['status']
        description = response_body["responseData"]["dataList"][int(s)]['description']
        system = response_body["responseData"]["dataList"][int(s)]['system']
        fileName = response_body["responseData"]["dataList"][int(s)]['filename']
        isDiffImage = response_body["responseData"]["dataList"][int(s)]['isDiffImage']
        downloadConsent = response_body["responseData"]["dataList"][int(s)]['downloadConsent']
        installConsent = response_body["responseData"]["dataList"][int(s)]['installConsent']
        rebootConsent = response_body["responseData"]["dataList"][int(s)]['rebootConsent']
        if modelName == model and packageId == packId:
            if status == "SUCCESS":
                testResult(self, "passed",
                           "Update package should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page",
                           "Update package is listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "Update package should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page",
                           "Update package is listed with FAILURE status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "Firmware package should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page",
                           "Firmware package is listed with ARCHIVE status on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page")

        elif modelName != model or packageId != packId:
            if packageId == 0:
                print("\n")
            else:
                testResult(self, "failed",
                           "SOTA Update package should be listed with SUCCESS message on first row on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page",
                           "SOTA Update package is not listed on first row on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page")

    elif response_body["message"] != "SUCCESS":
        testResult(self, "failed",
                   "SOTA Update package should be listed with SUCCESS message on first row on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page",
                   "SOTA Update package list is not displayed on SMP UI-> Configuration -> OTA -> OTA Files -> SOTA page")

    else:
        print("Something went wrong")

    return model


def listSOTAScript(self, scriptId, command, onboarding_Type, chipset_Type):
    time.sleep(30)
    refId = ''
    s = 0
    model = getModel(self, onboarding_Type, chipset_Type)

    response = SOTA_ListScripts(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listSOTAScript_" + model + "_" + command, str(response_body), "OTA")

    if response_body["responseCode"] == str(15000):
        try:
            data_len = len(response_body["responseData"]["dataList"])
            # print(data_len)
            if data_len == 1:
                modelName = response_body["responseData"]["dataList"][0]['model']
                refId = response_body["responseData"]["dataList"][0]['scriptId']
                s = int(0)
            else:
                for i in range(data_len):
                    modelName = response_body["responseData"]["dataList"][i]['model']
                    refId = response_body["responseData"]["dataList"][i]['scriptId']
                    if modelName == model and scriptId == str(refId):
                        s = int(i)
        except:
            modelName = response_body["responseData"]["dataList"]['model']
            refId = response_body["responseData"]["dataList"]['scriptId']

        scriptName = response_body["responseData"]["dataList"][int(s)]['scriptName']
        applicationName = response_body["responseData"]["dataList"][int(s)]['applicationName']
        command = response_body["responseData"]["dataList"][int(s)]['command']
        status = response_body["responseData"]["dataList"][int(s)]['status']
        refId = response_body["responseData"]["dataList"][int(s)]['scriptId']
        modelName = response_body["responseData"]["dataList"][int(s)]['model']
        targetVersion = response_body["responseData"]["dataList"][int(s)]['targetVersion']
        # print(modelName, model, scriptId, refId)
        if modelName == model and scriptId == str(refId):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "SOTA script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page",
                           scriptName +
                           " - SOTA script is listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "SOTA script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page",
                           scriptName +
                           " - SOTA script is listed with FAILURE status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "SOTA script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page",
                           scriptName +
                           " - SOTA script is listed with ARCHIVE status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page")

        elif modelName != model or scriptId != refId:
            testResult(self, "failed",
                       "SOTA script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page",
                       "SOTA script is not listed on first row or on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page")

    elif response_body["responseCode"] != str(15000):
        testResult(self, "failed",
                   "SOTA script should be listed with SUCCESS status on SMP UI-> Configuration -> OTA -> Scripts -> SOTA page",
                   "SOTA script list is not fetched")

    else:
        print("Something went wrong")

    text_file = open(C2CtestReport_otaPath + r'beforeOTA\refId_sota.txt', "w")
    text_file.write(refId)
    text_file.close()
    return refId


def triggerSOTAUpdate(self, scriptId, command, onboarding_Type, chipset_Type):
    model = getModel(self, onboarding_Type, chipset_Type)
    scheduleId = ''
    startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    print("Start Date : ", startDate)
    endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
    print("End Date: ", endDate)

    vin = getVIN(self, onboarding_Type, chipset_Type)
    print("VIN No. : => ", vin)

    # Act: convert dict to json by json.dumps() for body data and send POST request.

    response = SOTA_CreateSchedule(self, vin, scriptId, startDate, endDate, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("triggerSotaUpdate_" + model + "_" + command, str(response_body), "OTA")
    # print(response_body)

    if response_body["responseCode"] == str(15000):
        if response_body["responseData"]["message"] == "success" or response_body["responseData"][
            "message"] == "Success":
            scheduleId = str(response_body["responseData"]["scheduleId"])
            testResult(self, "passed",
                       "SOTA update should be scheduled successfully and campaign should be started ",
                       "SOTA update scheduled successfully and campaign is started ")

    elif response_body["responseCode"] != str(15000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "SOTA update should be scheduled successfully and campaign should be started ",
                   "SOTA update is not scheduled successfully OR Campaign is not started. " + " Reason for failure is : " +
                   response_body["responseData"]["message"])

    else:
        print("Something went wrong")
    text_file = open(C2CtestReport_otaPath + r'beforeOTA\scheduleId_sota.txt', "w")
    text_file.write(scheduleId)
    text_file.close()
    return scheduleId


def listSOTAupdateSchedules(self, scheduleId, command, onboarding_Type, chipset_Type):
    time.sleep(30)
    refId = ''
    s = 0
    model = getModel(self, onboarding_Type, chipset_Type)

    response = SOTA_ListSchedules(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listSOTAschedules_" + model + "_" + command, str(response_body), "OTA")

    if response_body["responseCode"] == "Success" or response_body["responseCode"] == str(15000):
        data_len = len(response_body["responseData"]["dataList"])
        print(data_len)
        if data_len == 1:
            modelName = response_body["responseData"]["dataList"][0]['model']
            refId = response_body["responseData"]["dataList"][0]['scheduleId']
            s = int(0)
        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["dataList"][i]['model']
                refId = response_body["responseData"]["dataList"][i]['scheduleId']
                if modelName == model and scheduleId == str(refId):
                    s = int(i)

        modelName = response_body["responseData"]["dataList"][int(s)]['model']
        status = response_body["responseData"]["dataList"][int(s)]['status']
        offered = response_body["responseData"]["dataList"][int(s)]['offered']
        accepted = response_body["responseData"]["dataList"][int(s)]['accepted']
        complete = response_body["responseData"]["dataList"][int(s)]['complete']
        scriptId = response_body["responseData"]["dataList"][int(s)]['scriptId']
        scriptName = response_body["responseData"]["dataList"][int(s)]['scriptName']
        command = response_body["responseData"]["dataList"][int(s)]['command']
        refId = response_body["responseData"]["dataList"][int(s)]['scheduleId']
        # print(modelName, model, scheduleId, refId)
        if modelName == model and scheduleId == str(refId):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "SOTA update schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                           scriptName +
                           " - SOTA update schedule/campaign is listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "SOTA update /schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                           scriptName +
                           " - SOTA update schedule/campaign is listed with FAILURE status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "SOTA update /schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                           scriptName +
                           " - SOTA update schedule/campaign is listed with ARCHIVE status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

        elif modelName != model or scriptId != refId:
            testResult(self, "failed",
                       "SOTA update /schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "SOTA update schedule/campaign is not listed on first row or on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

    elif response_body["message"] != "Success" or response_body["responseCode"] != str(15000):
        testResult(self, "failed",
                   "SOTA update /schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                   "SOTA update schedule/campaign list is not displayed on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

    else:
        print("Something went wrong")

    return refId


def replaceLineWithText(self, filename, linenumb, replacedtext):
    with open(filename, 'r') as givenfilecontent:
        filelines = givenfilecontent.readlines()
        filelines[linenumb - 1] = replacedtext
    with open(filename, 'w') as givenfilecontent:
        givenfilecontent.writelines(filelines)
    print('The given linenumber = ', linenumb, ' is replaced with {', replacedtext, '}')


def read_refID(self, option):
    filename = ""
    if option == "fota":
        filename = 'refId_fota.txt'
    elif option == "sota":
        filename = 'refId_sota.txt'
    text_file = C2CtestReport_otaPath + 'beforeOTA' + '\\' + filename
    # text_file = folderPath + r'C2CtestData\usr\local\json\refId.txt'
    files = glob.glob(text_file)
    max_file = max(files, key=os.path.getctime)
    with open(max_file) as f:
        refID = f.read()
    return refID


def read_scheduleId(self, option):
    filename = ""
    if option == "fota":
        filename = 'scheduleId_fota.txt'
    elif option == "sota":
        filename = 'scheduleId_sota.txt'
    text_file = C2CtestReport_otaPath + 'beforeOTA' + '\\' + filename
    files = glob.glob(text_file)
    max_file = max(files, key=os.path.getctime)
    with open(max_file) as f:
        scheduleId = f.read()
    return scheduleId


def stabilityCheck_triggerFirmwareUpdate(self, vin, model, scriptId):
    scheduleId = ""
    now = datetime.now()
    format = "%Y-%m-%d %I:%M:%S"
    # format datetime using strftime()
    startDate = now.strftime(format)
    dt = datetime.now() + timedelta(days=1)
    endDate = dt.strftime(format)
    print("Model No. : => ", model)
    print("VIN No. : => ", vin)

    # Act: convert dict to json by json.dumps() for body data and send POST request.

    response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("triggerFirmwareUpdate_" + model, str(response_body), "OTA")
    # print(response_body)

    if response_body["responseCode"] == str(14000):
        if response_body["responseData"]["message"] == "success" or response_body["responseData"][
            "message"] == "Success":
            scheduleId = str(response_body["responseData"]["scheduleId"])
            testResult(self, "passed", "Firmware should be scheduled successfully and campaign should be started ",
                       "Firmware scheduled successfully OR Campaign is started ")

    elif response_body["responseCode"] != str(14000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "Firmware should be scheduled successfully and campaign should be started ",
                   "Firmware is not scheduled successfully OR Campaign is not started. " + " Reason for failure is " +
                   response_body["responseData"]["message"])

    else:
        print("Something went wrong")
    return scheduleId


def listPackageSchedules(self, scheduleId, onboarding_Type, chipset_Type):
    status = offered = accepted = complete = ""
    time.sleep(30)
    refId = ''
    s = 0
    model = getModel(self, onboarding_Type, chipset_Type)

    response = SOTA_ListSchedules(self, str(1), str(10), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listPackageSchedules_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == "Success" or response_body["responseCode"] == str(15000):
        data_len = len(response_body["responseData"]["dataList"])
        if data_len == 1:
            modelName = response_body["responseData"]["dataList"][0]['model']
            scheduleId1 = response_body["responseData"]["dataList"][0]['scheduleId']
            s = int(0)
        else:
            for i in range(data_len):
                modelName = response_body["responseData"]["dataList"][i]['model']
                scheduleId1 = response_body["responseData"]["dataList"][i]['scheduleId']
                if modelName == model and scheduleId == str(scheduleId1):
                    s = int(i)

        modelName = response_body["responseData"]["dataList"][int(s)]['model']
        status = response_body["responseData"]["dataList"][int(s)]['status']
        offered = response_body["responseData"]["dataList"][int(s)]['offered']
        accepted = response_body["responseData"]["dataList"][int(s)]['accepted']
        complete = response_body["responseData"]["dataList"][int(s)]['complete']
        scriptName = response_body["responseData"]["dataList"][int(s)]['scriptName']
        scheduleId1 = response_body["responseData"]["dataList"][int(s)]['scheduleId']

        if modelName == model and scheduleId == str(scheduleId1):
            if status == "SUCCESS":
                testResult(self, "passed",
                           "Package schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates",
                           scriptName +
                           " - Package schedule/campaign is listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates")

            elif status == "FAILURE":
                testResult(self, "failed",
                           "Package schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates",
                           scriptName +
                           " - Package schedule/campaign is listed with FAILURE status on SMP UI-> Updates -> OTA -> SOTA Updates")

            elif status == "ARCHIVE":
                testResult(self, "failed",
                           "Package schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates",
                           scriptName +
                           " - Package schedule/campaign is listed with ARCHIVE status on SMP UI-> Updates -> OTA -> SOTA Updates")

        elif modelName != model and scheduleId != str(scheduleId1):
            testResult(self, "failed",
                       "Package schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates",
                       "Package schedule/campaign is not listed on first row or on SMP UI-> Updates -> OTA -> SOTA Updates")

    elif response_body["responseCode"] != "Success" or response_body["responseCode"] != str(15000):
        testResult(self, "failed",
                   "Package schedule/campaign should be listed with SUCCESS status on SMP UI-> Updates -> OTA -> SOTA Updates",
                   "Package schedule/campaign list is not displayed on SMP UI-> Updates -> OTA -> SOTA Updates")

    else:
        print("Something went wrong")

    return status, offered, accepted, complete


def listPackageScheduleStatus(self, onboarding_Type, chipset_Type):
    status = appName = ""
    time.sleep(30)
    refId = ''
    model = getModel(self, onboarding_Type, chipset_Type)
    vin = getVIN(self, onboarding_Type, chipset_Type)
    scheduleId = read_scheduleId(self, "sota")

    response = SOTA_ListScheduleVin(self, scheduleId, vin, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("listPackageScheduleStatus_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(15000):

        vinNo = response_body["responseData"]["dataList"][0]['vin']
        status = response_body["responseData"]["dataList"][0]['status']
        appName = response_body["responseData"]["dataList"][0]['appName']

        # print(vin, vinNo)

        if vin == vinNo:
            # print('\n')
            print("Package update schedule-status is listed with " + status + " status on SMP UI")

    return status, appName


def appCheck(self, file_name, appname):
    # entering try block
    appName = ""
    try:
        appName = ''
        # opening and reading the file
        file_read = open(file_name, "r")

        # reading file content line by line.
        lines = file_read.readlines()

        new_list = []
        idx = 0

        # looping through each line in the file
        for line in lines:

            # if line have the input string, get the index
            # of that line and put the
            # line into newly created list
            if appname in line:
                new_list.insert(idx, line)
                idx += 1

        # closing file after reading
        file_read.close()

        # if length of new list is 0 that means
        # the input string doesn't
        # found in the text file
        if len(new_list) == 0:
            # print("\n\"" + appname + "\" is not found in \"" + file_name + "\"!")
            appName = ''
        else:

            # displaying the lines
            # containing given string
            lineLen = len(new_list)
            # print("\n**** Lines containing \"" + appname + "\" ****\n")
            for i in range(lineLen):
                if appname in new_list[i]:
                    appName = new_list[i]
                    break
                else:
                    appName = ''
    # entering except block
    # if input file doesn't exist
    except FileNotFoundError:
        print("\nThe file doesn't exist!")
    except:
        print("Something went wrong!")
    return appName


def replaceLineWithText(self, filename, linenumb, replacedtext):
    with open(filename, 'r') as givenfilecontent:
        filelines = givenfilecontent.readlines()
        filelines[linenumb - 1] = replacedtext
    with open(filename, 'w') as givenfilecontent:
        givenfilecontent.writelines(filelines)
    print('The given linenumber = ', linenumb, ' is replaced with {', replacedtext, '}')


def stabilityCheck_SOTA_IVI(self):
    vin = testData("StabilityCheck", 3, 2)
    model = testData("StabilityCheck", 4, 2)
    scriptId = testData("StabilityCheck", 5, 2)
    command1 = "INSTALL"
    startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    print("\nStart Date : ", startDate)
    endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
    print("End Date: ", endDate)

    response = SOTA_CreateSchedule(self, vin, scriptId, startDate, endDate, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("stability_triggerSotaUpdate_" + model + "_" + command1, str(response_body), "OTA")
    # print(response_body)

    if response_body["responseCode"] == str(15000):
        if response_body["responseData"]["message"] == "success" or response_body["responseData"][
            "message"] == "Success":
            scheduleId = str(response_body["responseData"]["scheduleId"])
            testResult(self, "passed",
                       "SOTA update should be scheduled successfully and campaign should be started ",
                       "SOTA update scheduled successfully and campaign is started ")

    elif response_body["responseCode"] != str(15000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "SOTA update should be scheduled successfully and campaign should be started ",
                   "SOTA update is not scheduled successfully OR Campaign is not started. " + " Reason for failure is : " +
                   response_body["responseData"]["message"])

    else:
        print("Something went wrong")


def stabilityCheck_FOTA_IVI(self):
    vin = testData("StabilityCheck", 3, 3)
    model = testData("StabilityCheck", 4, 3)
    scriptId = testData("StabilityCheck", 5, 3)

    startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    print("\nStart Date : ", startDate)
    endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
    print("End Date: ", endDate)

    response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("stability_triggerFirmwareUpdate_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(14000):
        if response_body["responseData"]["message"] == "success" or response_body["responseData"][
            "message"] == "Success":
            scheduleId = str(response_body["responseData"]["scheduleId"])
            testResult(self, "passed", "Firmware should be scheduled successfully and campaign should started ",
                       "Firmware scheduled successfully OR Campaign is started ")

    elif response_body["responseCode"] != str(14000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "Firmware should be scheduled successfully and campaign should started ",
                   "Firmware is not scheduled successfully OR Campaign is not started  " + " Reason for failure is : " +
                   response_body["responseData"]["message"])
    else:
        print("Something went wrong")


# Verify PKI signature
def verify_PKIsignature(self, deviceType, chispetType):
    if deviceType == deviceType_IVI:
        # ===========================================================================================
        # Verify PKI signature in logs
        # ===========================================================================================

        try:
            ls1 = verify_message_in_ota_logs(self, 'SignatureHelper', "verifying file Signature")
            ls2 = verify_message_in_ota_logs(self, 'SignatureHelper', "Signature result is  Signature Verified")
            ls3 = verify_message_in_ota_logs(self, 'Signature', "Signature Verified")
            ls4 = verify_message_in_ota_logs(self, 'Signature', "Signature Verified, proceeding for installation")
            ls5 = verify_message_in_ota_logs(self, 'RockAgent', "PEM file copy removed")
            ls6 = verify_message_in_ota_logs(self, 'RockAgent', "Sota Install started")

            print("--------------------------------------------------------------------")
            print('\n', ls1, '\n', ls2, '\n', ls3, '\n', ls4, '\n', ls5, '\n', ls6, '\n')
            print("--------------------------------------------------------------------")

            if 'Signature Verified, proceeding for installation' in str(ls4).replace('\n', ''):
                testResult(self, "passed",
                           "PKI signature should be verified on device before installing application(apk) ",
                           "PKI signature is verified on device before installing application(apk) ")
            else:
                testResult(self, "failed",
                           "PKI signature should be verified on device before installing application(apk) ",
                           "PKI signature is not verified on device before installing application(apk) ")

        except:
            testResult(self, "failed", "PKI signature should be verified on device before installing application(apk) ",
                       "PKI signature is not verified on device before installing application(apk) ")
