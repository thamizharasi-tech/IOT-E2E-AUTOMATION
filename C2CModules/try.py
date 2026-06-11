import base64
import glob
import inspect
import json
import logging
import os
import os.path
import random
import subprocess
import sys
import time

import openpyxl
import requests

from API_Testing.testData.api_endpoints import api_endpoints

#from C2CModules.c2c_modules import *
from C2CModules.c2c_modules import apiHeader, testResult, replaceLineWithText, saveAPIrespIntoFile, \
    deleteFoldersForUpdate, checkChipsetAndSystemState
from C2CModules.e2e_testData import *
#from C2CModules.resuse_modules import *
from C2CModules.resuse_modules import device_reg_post_request, get_request_api, verify_message_in_log

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

sys.path.insert(1, r'C:\Car2Cloud_E2ETesting')

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

# ============================================================
# Pull/Fetch files from device for validations
# ============================================================

def pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, option):
    try:
        # print("Fetch/Pull files from device for validation & backup : ")
        # print("\n-------------------------------------------------------------")
        if onboarding_Type == deviceType_IVI:
            if chipset_type == drimaes_ivi_chipset:
                subprocess.call(
                    [drimaes_batchPath + 'C2C_pullFilesFromDevice.bat',
                     drimaes_ivi_adbSerialNo, option], timeout=60)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.call(
                    [b2c_batchPath + 'C2C_pullFilesFromDevice.bat',
                     b2c_ivi_adbSerialNo, option], timeout=60)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.call(
                    [c2c_ivi_batchPath + 'C2C_pullFilesFromDevice.bat',
                     b2c_ivi_adbSerialNo, option], timeout=60)
        time.sleep(10)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_pullFilesFromDevice.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while fetching/pulling files from device")


# ============================================================
# Stop services on device
# ============================================================

def stop_C2Cservices_on_primary_IVI(self, onboarding_Type, chipset_type, option):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            subprocess.call(
                [drimaes_batchPath + r'C2C_stopServicesOnDevices.bat',
                 drimaes_ivi_adbSerialNo, option])
        if onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            subprocess.call(
                [b2c_batchPath + r'C2C_stopServicesOnDevices.bat',
                 b2c_ivi_adbSerialNo, option])
        if onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_stopServicesOnDevices.bat',
                 c2c_ivi_adbSerialNo, option])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_stopServicesOnDevices.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while stopping c2c services")


# ============================================================
# reboot/remount device
# ============================================================

def reboot_primary_IVI(self, onboarding_Type, chipset_type, option):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            subprocess.call(
                [drimaes_batchPath + r'C2C_adbCommands.bat',
                 drimaes_ivi_chipset, option])
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            subprocess.call(
                [b2c_batchPath + r'C2C_adbCommands.bat',
                 b2c_ivi_adbSerialNo, option])
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_adbCommands.bat',
                 c2c_ivi_adbSerialNo, option])
        time.sleep(60)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while rebooting device")


# ============================================================
# Copy default files
# ============================================================

def copyDefaultFiles(self, onboarding_Type, chipset_type):
    try:
        if spvalidationFlag != "Yes":
            print(
                f"=> SP Validation flag is set  to {spvalidationFlag}, thus conf files are replaced with deafult confiles")
            if chipset_type == drimaes_ivi_chipset:
                subprocess.call(
                    [drimaes_batchPath + 'C2C_copydefaultFiles.bat'], timeout=5)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.call(
                    [b2c_batchPath + 'C2C_copydefaultFiles.bat'], timeout=5)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.call(
                    [c2c_ivi_batchPath + 'C2C_copydefaultFiles.bat'], timeout=5)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")
    try:
        if spvalidationFlag == "Yes":
            print(
                f"=> SP Validation flag is set  to {spvalidationFlag}, thus conf files are fetched/pulled from flashed metabuild on device")
            if chipset_type == drimaes_ivi_chipset:
                subprocess.call(
                    [drimaes_batchPath + r'C2C_copydefaultFiles_SPvalidation.bat',
                     onboarding_Type, drimaes_ivi_adbSerialNo], timeout=5)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.call(
                    [b2c_batchPath + r'C2C_copydefaultFiles_SPvalidation.bat',
                     onboarding_Type, b2c_ivi_adbSerialNo], timeout=5)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.call(
                    [c2c_ivi_batchPath + r'C2C_copydefaultFiles_SPvalidation.bat',
                     onboarding_Type, c2c_ivi_adbSerialNo], timeout=5)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles_SPvalidation.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")


# ============================================================
# Push files on device function
# ============================================================

def push_files_on_primary_IVI(self, onboarding_Type, chipset_type):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [drimaes_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 drimaes_ivi_adbSerialNo, drimaes_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [b2c_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 b2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 c2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
    except FileNotFoundError:
        print(f"Sorry, the push files on device (batch file) does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while pushing files on device")


# ============================================================
# Push files on device function
# ============================================================

def push_desired_file_on_primary_IVI(self, onboarding_Type, chipset_type, filename):
    try:
        if onboarding_Type == deviceType_IVI_nonPrimary and chipset_type == drimaes_ivi_chipset:
            rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
            rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "remount")
            time.sleep(15)
            subprocess.call(
                [drimaes_batchPath + r'C2C_pushDesiredFileOnIVIdevice.bat',
                 drimaes_ivi_adbSerialNo, filename, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [b2c_batchPath + r'C2C_pushDesiredFileOnIVIdevice.bat',
                 b2c_ivi_adbSerialNo, filename, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_pushDesiredFileOnIVIdevice.bat',
                 c2c_ivi_adbSerialNo, filename, DeviceCommandFiles_path])
    except FileNotFoundError:
        print(f"Sorry, the push files on device (batch file) does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while pushing files on device")


# ============================================================
# replace text in IVI conf files
# ============================================================

def replaceText_IVIconf(self, onboarding_Type, chipset_type, TC):
    try:
        folderPath_ivi = C2CtestData_c2c2Path
        files = glob.glob(data_file)
        max_file = max(files, key=os.path.getctime)
        wb_obj = openpyxl.load_workbook(max_file)
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            sheetName = "IVIConfFileDetails_Drimaes"
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            sheetName = "IVIConfFileDetails_B2C"
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            sheetName = "IVIConfFileDetails_Primary"
        sheet_obj = wb_obj[sheetName]
        for i in range(2, int(sheet_obj.max_row + 1)):
            fileName = str(testData(sheetName, int(i), 2))
            oldString = str(testData(sheetName, int(i), 3))
            newString = str(testData(sheetName, int(i), 4))
            if fileName != None and oldString != None and newString != None:
                finalPath = folderPath_ivi + fileName
                replaceLineWithText(self, finalPath, oldString, newString)
            else:
                break
                print('\n')
        if TC == "invalidPrgmSkuId":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_PrgmSkuId, defaultIVI_PrgmSkuId + invalidPrgmSkuId)
        elif TC == "invalidSkuId":
            replaceLineWithText(self, ivi_car2cloudFile, defaultIVI_SkuId, defaultIVI_SkuId + invalidSkuId)
        elif TC == "invalidPrgmId":
            replaceLineWithText(self, ivi_car2cloudFile, defaultIVI_PrgmId, defaultIVI_PrgmId + invalidPrgmId)
        elif TC == "invalidchipsetType":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetType,
                                defaultIVI_chipsetType + invalidchipsetType)
        elif TC == "invalidchipsetSp":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetSpVer,
                                defaultIVI_chipsetSpVer + invalidchipsetSp)
        elif TC == "invalidChipsetName":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetName,
                                defaultIVI_chipsetName + invalidChipsetName)
        elif TC == "emptyPrgmSkuId":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_PrgmSkuId, defaultIVI_PrgmSkuId + emptyPrgmSkuId)
        elif TC == "emptySkuId":
            replaceLineWithText(self, ivi_car2cloudFile, defaultIVI_SkuId, defaultIVI_SkuId + emptySkuId)
        elif TC == "emptyPrgmId":
            replaceLineWithText(self, ivi_car2cloudFile, defaultIVI_PrgmId, defaultIVI_PrgmId + emptyPrgmId)
        elif TC == "emptyChipsetType":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetType, defaultIVI_chipsetType + emptyChipsetType)
        elif TC == "emptychipsetSp":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetSpVer, defaultIVI_chipsetSpVer + emptychipsetSp)
        elif TC == "emptyChipsetName":
            replaceLineWithText(self, ivi_dmconfFile, defaultIVI_chipsetName, defaultIVI_chipsetName + emptyChipsetName)
    except FileNotFoundError:
        print("Sorry, the conf file does not exist or incorrect file path/name")
    except:
        print("Something went wrong while updating conf file")


# =======================================================================
# Device Registration To Cloud Connection Establishment with valid & invalid data
# =======================================================================


def standalone_IVI_device_reg_to_CldConnEstb(self, onboarding_Type, chipset_type, TC):
    print("------------------------------------------------------------")
    print("Device On-boarding/Provisioning details : ")
    print("Test Case details => ", TC)
    print(f"Environment selected for device onboarding => {onboardingEnv}")
    print(f"Cloud Base Url => {BaseUrl_gbl}")
    print("------------------------------------------------------------")
    print("IVI device chipset program details configured for onboarding : ")
    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        print(f"Sku Id =>  {drimaes_IVI_SkuId}")
        print(f"Program Id =>  {drimaes_IVI_PrgmId}")
        print(f"Program sku Id =>  {drimaes_IVI_PrgmSkuId}")
        print(f"Chipset Type =>  {drimaes_IVI_chipsetType}")
        print(f"Chipset SP version =>  {drimaes_IVI_chipsetSpVer}")
    elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
        print(f"Sku Id =>  {b2c_IVI_SkuId}")
        print(f"Program Id =>  {b2c_IVI_PrgmId}")
        print(f"Program sku Id =>  {b2c_IVI_PrgmSkuId}")
        print(f"Chipset Type =>  {b2c_IVI_chipsetType}")
        print(f"Chipset SP version =>  {b2c_IVI_chipsetSpVer}")
    elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        print(f"Sku Id =>  {C2C_IVI_SkuId}")
        print(f"Program Id =>  {C2C_IVI_PrgmId}")
        print(f"Program sku Id =>  {C2C_IVI_PrgmSkuId}")
        print(f"Chipset Type =>  {C2C_IVI_chipsetType}")
        print(f"Chipset SP version =>  {C2C_IVI_chipsetSpVer}")
    print("------------------------------------------------------------")

    random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])

    subSystemId = "sub" + random_id
    if vinNoFlag == "Yes":
        vinNo = reqVinNo
    else:
        if TC == "invalidVIN_lessCharLen":
            vinNo = invalidVIN_lessCharLen
        elif TC == "invalidVIN_grtrCharLen":
            vinNo = invalidVIN_grtrCharLen
        elif TC == "invalidVIN_withSpace":
            vinNo = invalidVIN_withSpace
        elif TC == "invalidVIN_withSplchar":
            vinNo = invalidVIN_withSplchar
        elif TC == "duplicateVIN":
            vinNo = duplicateVIN
        elif TC == "emptyVIN":
            vinNo = emptyVIN
        else:
            vinNo = "VIN" + "QCOMIVI" + random_id

    if reqModelNameFlag == "Yes":
        uniqueModel = reqModelName
    elif OTA_ModelFlag == "Yes":
        uniqueModel = "model" + random_id

    text_file = folderPath + r'C2CtestData\VinNo.txt'
    # print('VinNo')
    files = glob.glob(text_file)
    max_file = max(files, key=os.path.getctime)
    text_file = open(text_file, "w")
    n = text_file.write(vinNo)
    text_file.close()

    headers = apiHeader(self)

    print("Registration of IVI device : ")
    print("------------------------------------------------------------")

    response_body = device_reg_post_request(self, deviceType_IVI)

    request_id = response_body["responseData"]["requestId"]
    print("Request id fo IVI device = ", request_id)
    if response_body["responseData"]["status"] == "SUBMITTED":
        # print("Response Data Status is SUBMITTED")
        # assert True
        assert (response_body["responseData"]["status"] == "SUBMITTED")
        assert (response_body["responseData"]["message"] == "Request Submitted for registration!")

    getOverallCount_url = str(api_endpoints.getOverallCount_url) + str(request_id)
    print(getOverallCount_url)
    time.sleep(5)

    response_body = get_request_api(getOverallCount_url, headers, "\IVI_deviceCntDetails")

    request_id = response_body["responseData"]["requestId"]

    # Validate request id in response body content
    # assert request_id == request_id

    # Validate response data
    if response_body["responseData"]["successCount"] == 1:
        print("successCount is set to :=> ", response_body["responseData"]["successCount"])
        testResult(self, "passed", 'New IVI Device Registration', 'New IVI Device is registered successfully')
        print('\n')
        # assert True
    elif response_body["responseData"]["failCount"] == 1:
        print("failCount is set to :=> ", response_body["responseData"]["failCount"])
        testResult(self, "failed", 'New IVI Device Registration', 'New IVI Device is not registered successfully')

    assert (response_body["responseData"]["totalCount"] == 1)
    assert (response_body["responseData"]["status"] == "Completed")
    assert (response_body["responseData"]["successCount"] == 1)
    assert (response_body["responseData"]["failCount"] == 0)
    assert (response_body["responseData"]["message"] == "Successfully generated the registration data.")

    getDeviceDetails_url = api_endpoints.getDeviceDetails_url + request_id + "/devices"
    # print(getDeviceDetails_url)
    time.sleep(5)

    response_body = get_request_api(getDeviceDetails_url, headers, "\IVI_deviceDetails")

    if response_body["responseMessage"] == "SUCCESS" or response_body["responseMessage"] == "Success":
        # print(f"Response Message is SUCCESS")
        assert True
        assert (response_body["responseMessage"] == "Success")
    else:
        print(str(response_body["responseMessage"]))

    device_id = response_body["responseData"][0]["device_id"]
    status = response_body["responseData"][0]["status"]
    url = response_body["responseData"][0]["url"]
    systemId = response_body["responseData"][0]["system_id"]
    deviceType = response_body["responseData"][0]["device_type"]
    certificateDetails = response_body["responseData"][0]["certificateDetails"]["certificate"]
    PrivateKeyDetails = response_body["responseData"][0]["certificateDetails"]["privateKey"]

    decodedBytes = base64.b64decode(str(certificateDetails)).decode("utf-8")
    decodedStr = str(decodedBytes)
    time.sleep(5)
    print("------------------------------------------------------------")
    print("Update Certs and private key files : ")
    path = C2CtestData_certsPath + r'clientcert.pem.crt'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    text_file = open(path, "w")
    n = text_file.write(decodedBytes)
    text_file.close()

    decodedByteskey = base64.b64decode(str(PrivateKeyDetails)).decode("utf-8")
    decodedStrkey = str(decodedByteskey)
    time.sleep(5)

    path = C2CtestData_certsPath + r'private.pem.key'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    text_file = open(path, "w")
    n = text_file.write(decodedStrkey)
    text_file.close()

    path = C2CtestData_certsPath + r'private.pem.key'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    text_file = open(path, "w")
    n = text_file.write(decodedStrkey)
    text_file.close()
    print("=> Certs & private key files are updated with newly registered device data")

    if TC == "invalidDeviceId_lessCharLen":
        device_id = invalidDeviceId_lessCharLen
    elif TC == "invalidDeviceId_grtrCharLen":
        device_id = invalidDeviceId_grtrCharLen
    elif TC == "invalidDeviceId_withSpace":
        device_id = invalidDeviceId_withSpace
    elif TC == "invalidDeviceId_withSplchar":
        device_id = invalidDeviceId_withSplchar
    elif TC == "dupDeviceId":
        device_id = dupDeviceId
    elif TC == "emptyDeviceID":
        device_id = emptyDeviceID

    if TC == "invalid_systemId":
        systemId = invalid_systemId
    if TC == "emptySystemID":
        systemId = emptySystemID

    if TC == "invalidSubSysId_lessCharLen":
        subSystemId = invalidSubSysId_lessCharLen
    elif TC == "invalidSubSysId_grtrCharLen":
        subSystemId = invalidSubSysId_grtrCharLen
    elif TC == "invalidSubSysId_withSpace":
        subSystemId = invalidSubSysId_withSpace
    elif TC == "invalidSubSysId_withSplchar":
        subSystemId = invalidSubSysId_withSplchar
    elif TC == "emptySubSystemID":
        subSystemId = emptySubSystemID

    if TC == "invalidGlbUrl":
        url = invalidGlbUrl
    elif TC == "devOnbrdWithRegionalUrl":
        url = devOnbrdWithRegionalUrl
    elif TC == "emptyUrl":
        subSystemId = emptyUrl

    print("------------------------------------------------------------")
    print("Update desired conf files with newly registered IVI device data : ")

    replaceLineWithText(self, sideloadedFile, defaultSystemID, defaultSystemID + systemId)
    replaceLineWithText(self, sideloadedFile, defaultVIN, defaultVIN + vinNo)

    replaceLineWithText(self, car2cloudFile, defaultVIN, defaultVIN + vinNo)
    replaceLineWithText(self, car2cloudFile, defaultSubSystemId, defaultSubSystemId + subSystemId)
    replaceLineWithText(self, car2cloudFile, defaultDeviceId, defaultDeviceId + device_id)

    replaceLineWithText(self, dmconfFile, dm_defaultDeviceId, dm_defaultDeviceId + device_id)

    with open(c2cvehicleFile) as f:
        json_data = json.load(f)
        json_data["C2C_Vehicle"]["url_cloud"] = url
        # json_data["C2C_Vehicle"]["system_state"] = "REGISTERED_NOT_PROVISIONED"
        json_data["C2C_Vehicle"]["Subsystems"][0]["Subsystem-id"] = subSystemId
        json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["deviceId"] = device_id
        # json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["state"] = "UNREGISTERED"
        json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["device_info"]["ecu_type"] = deviceType_IVI
        # json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["device_info"]["primary"] = "true"
        if OTA_ModelFlag == "Yes" or reqModelNameFlag == "Yes":
            json_data["C2C_Vehicle"]["vehicle_info"]["model"] = uniqueModel

        json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["chipsets_count"] = 1

    with open(c2cvehicleFile, 'w') as f:
        f.write(json.dumps(json_data))

    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, drimaes_ivi_chipset, "valid")
        print("=> Conf file(s) are updated with newly registered device data")
        print("\n------------------------------------------------------------")
        print("Stop all c2c services on device(s) : ")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, drimaes_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("\n------------------------------------------------------------")
        print("Push updated files on device : ")
        push_files_on_primary_IVI(self, onboarding_Type, drimaes_ivi_chipset)
    elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, b2c_ivi_chipset, "valid")
        print("=> Conf file(s) are updated with newly registered device data")
        print("\n------------------------------------------------------------")
        print("Stop all c2c services on device(s) : ")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, b2c_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("\n------------------------------------------------------------")
        print("Push updated files on device : ")
        push_files_on_primary_IVI(self, onboarding_Type, b2c_ivi_chipset)
    elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, c2c_ivi_chipset, "valid")
        print("\n------------------------------------------------------------")
        print("=> Conf file(s) are updated with newly registered device data")
        print("Stop all c2c services on device(s) : ")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, c2c_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("\n------------------------------------------------------------")
        print("Push updated files on device : ")
        push_files_on_primary_IVI(self, onboarding_Type, c2c_ivi_chipset)
    else:
        print("Invalid chipset type")

    print("\n=>All required files have been pushed on device and ready for onboarding")


# ============================================================
# Run all c2c services on device
# ============================================================
def run_c2cServices_on_primary_IVI(self, onboarding_Type, chipset_type):
    # print("------------------------------------------------------------")
    print("\n============================================================")
    print("Run/Start c2c services on device(s) : ")
    print("============================================================")

    if onboarding_Type == deviceType_IVI:
        try:
            if chipset_type == drimaes_ivi_chipset:
                subprocess.run(
                    [drimaes_batchPath + 'C2C_startServicesOnDevices.bat',
                     drimaes_ivi_adbSerialNo, "C2CServices"], timeout=5)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.run(
                    [b2c_batchPath + 'C2C_startServicesOnDevices.bat',
                     b2c_ivi_adbSerialNo, "C2CServices"], timeout=5)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.run(
                    [c2c_ivi_batchPath + 'C2C_startServicesOnDevices.bat',
                     c2c_ivi_adbSerialNo, "C2CServices"], timeout=5)
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")


# ============================================================
# Run all ota services on device
# ============================================================
def run_otaServices_on_primary_IVI(self, onboarding_Type, chipset_type):
    # print("------------------------------------------------------------")
    print("\n============================================================")
    print("Run/Start c2c services on device(s) : ")
    print("============================================================")

    if onboarding_Type == deviceType_IVI:
        try:
            if chipset_type == drimaes_ivi_chipset:
                subprocess.run(
                    [drimaes_batchPath + 'C2C_startServicesOnDevices.bat',
                     drimaes_ivi_adbSerialNo, "OTAServices"], timeout=5)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.run(
                    [b2c_batchPath + 'C2C_startServicesOnDevices.bat',
                     b2c_ivi_adbSerialNo, "OTAServices"], timeout=5)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.run(
                    [c2c_ivi_batchPath + 'C2C_startServicesOnDevices.bat',
                     c2c_ivi_adbSerialNo, "OTAServices"], timeout=5)
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")


# ============================================================
# Run all ota services on device
# ============================================================
def run_desired_service_on_primary_IVI(self, onboarding_Type, chipset_type, serviceName):
    # print("------------------------------------------------------------")
    print("\n============================================================")
    print("Run/Start dm services on device(s) : ")
    print("============================================================")

    if onboarding_Type == deviceType_IVI:
        try:
            if chipset_type == drimaes_ivi_chipset:
                subprocess.run(
                    [drimaes_batchPath + 'C2C_startServicesOnDevices.bat',
                     drimaes_ivi_adbSerialNo, serviceName], timeout=5)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.run(
                    [b2c_batchPath + 'C2C_startServicesOnDevices.bat',
                     b2c_ivi_adbSerialNo, serviceName], timeout=5)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.run(
                    [c2c_ivi_batchPath + 'C2C_startServicesOnDevices.bat',
                     c2c_ivi_adbSerialNo, serviceName], timeout=5)
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")


def restart_c2cServices_on_primary_IVI(self, onboarding_Type, chipset_type):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            subprocess.run(
                [drimaes_batchPath + r'C2C_startServicesOnDevices.bat',
                 drimaes_ivi_adbSerialNo, "IVIrestart"], timeout=5)
        elif onboarding_Type == deviceType_VT and chipset_type == b2c_ivi_chipset:
            subprocess.run(
                [b2c_batchPath + r'C2C_startServicesOnDevices.bat',
                 b2c_ivi_adbSerialNo, "IVIrestart"], timeout=5)
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            subprocess.run(
                [c2c_ivi_batchPath + r'C2C_startServicesOnDevices.bat',
                 c2c_ivi_adbSerialNo, "IVIrestart"], timeout=5)
    except FileNotFoundError:
        print(
            f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
    except subprocess.TimeoutExpired:
        print(f'process ran too long')
    except:
        print(f"Something went wrong while re-starting c2c service on IVI device")


# ============================================================
# Run all c2c services on device
# ============================================================
def run_paho_command_on_primary_IVI(self, onboarding_Type, chipset_type, option):
    # print("------------------------------------------------------------")
    print("\n============================================================")
    print("Push required files & run/start stub on device : ")
    print("============================================================")

    if onboarding_Type == deviceType_IVI:
        try:
            if chipset_type == drimaes_ivi_chipset:

                subprocess.run(
                    [drimaes_batchPath + 'C2C_paho_commands.bat',
                     drimaes_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=15)

                subprocess.run(
                    [drimaes_batchPath + 'C2C_paho_commands.bat',
                     drimaes_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=15)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.run(
                    [b2c_batchPath + 'C2C_paho_commands.bat',
                     b2c_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=15)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.run(
                    [c2c_ivi_batchPath + 'C2C_paho_commands.bat',
                     c2c_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=15)
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_paho_commands.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")


# ============================================================
# Check chipset and system states in c2c_vehicle json file
# ============================================================

def verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type):
    if onboarding_Type == deviceType_IVI:
        c2cvehicleFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\c2c_vehicle.json'
        with open(c2cvehicleFile, 'r') as file:
            json_data = json.load(file)
            try:
                primaryDevice_chipset_count = json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets_count']
                primaryDevice_chipset1_state = json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][0][
                    "state"]
            except:
                primaryDevice_chipset1_state = "IVI chipset data is not fetched"
            print("\n")

        system_state = json_data['C2C_Vehicle']['system_state']
        print("\n")
        vin = json_data['C2C_Vehicle']['vin']
        model = json_data['C2C_Vehicle']['vehicle_info']['model']
        try:
            systemId = json_data['C2C_Vehicle']['system_id']
        except:
            systemId = ''

    return primaryDevice_chipset1_state, system_state, vin, primaryDevice_chipset_count, model, systemId


# ============================================================
# Save VIN no in file for SKU/Feature Update
# ============================================================
def saveVIN_primary_IVI(self, onboarding_Type):
    states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, c2c_ivi_chipset)
    path = folderPath + r'C2CtestData\VinNo.txt'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    # print(max_file)
    text_file = open(max_file, "w")
    text_file.write(states[2])
    text_file.close()


# ============================================================
# Get Onboarded VIN details from cloud via API
# ============================================================

def get_VIN_details_Primary_IVI(self, val, onboarding_Type, chipset_type):
    # Get VIN details
    headers = apiHeader(self)
    states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)
    payload = {"vin": [states[2]]}
    # getVINdetails_url = BaseUrl_reg + "/smp-server/vin/vehiclesearch"
    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(api_endpoints.getVINdetails_url, headers=headers, data=json.dumps(payload))
    # Parse HTTP response body to json format
    response_body = response.json()
    # print(response_body)

    # Save response full body as text in a file
    saveAPIrespIntoFile("FetchNewVINRegistration_details", response.text, val)

    try:
        # Assert: Validate response status code and body contents
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        lendevice = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"])
        if chipset_type == drimaes_ivi_chipset:
            for i in range(lendevice):
                if response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                    "chipsetType"] == drimaes_IVI_chipsetType or \
                        response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                            "chipsetType"] == "SA6155":
                    skuIdChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuId"]
                    skuNameChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuName"]
                    print("=============================================================")
                    print("Onboarded VIN/device chipset details fetched via Cloud API : ")
                    print("=============================================================")
                    print("IVI Device Sku Id =>  ", skuIdChk)
                    print("IVI Device Sku Name =>  ", skuNameChk)
        if chipset_type == b2c_ivi_chipset:
            for i in range(lendevice):
                if response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                    "chipsetType"] == b2c_IVI_chipsetType or \
                        response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                            "chipsetType"] == "SA2290":
                    skuIdChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuId"]
                    skuNameChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuName"]
                    print("=============================================================")
                    print("Onboarded VIN/device chipset details fetched via Cloud API : ")
                    print("=============================================================")
                    print("IVI Device Sku Id =>  ", skuIdChk)
                    print("IVI Device Sku Name =>  ", skuNameChk)
        if chipset_type == c2c_ivi_chipset:
            for i in range(lendevice):
                if response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                    "chipsetType"] == C2C_IVI_chipsetType or \
                        response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                            "chipsetType"] == "SA8295":
                    skuIdChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuId"]
                    skuNameChk = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "skuName"]
                    print("=============================================================")
                    print("Onboarded VIN/device chipset details fetched via Cloud API : ")
                    print("=============================================================")
                    print("IVI Device Sku Id =>  ", skuIdChk)
                    print("IVI Device Sku Name =>  ", skuNameChk)
    except:
        print("=> Refer FetchNewVINRegistration_details json response for detailed info")


# ===========================================================================================
# Validate chipset & system state
# ===========================================================================================
def validate_chipset_and_system_state_IVI(self, onboarding_Type, chipset_type, val):
    states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)

    print("=============================================================")
    print("Validate Chipset & System type post device onboarding/provisioning")
    print("=============================================================")

    if states[1] != 'ACTIVE':
        time.sleep(60)
        print('waiting for another 60 sec')

        pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "DeviceOnboarding")

        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)

    print("=> IVI Chipset Count is : ", states[3])
    print("=> IVI Chipset State is : ", states[0])
    print("-----------------------------------------")
    print("=> System State is : ", states[1])
    print('\n')
    print("-------------------------------------------------------------")

    if val == "ACTIVE":

        if states[0] == "ACTIVE":
            testResult(self, "passed", "IVI Chipset State should be set to ACTIVE",
                       "IVI Chipset State is set to ACTIVE")

        elif states[0] != "ACTIVE":
            testResult(self, "failed", "IVI Chipset State should be set to ACTIVE",
                       "IVI Chipset State is not set to ACTIVE")

        if states[1] == "ACTIVE":
            testResult(self, "passed", "System State should be set to ACTIVE", "System State is set to ACTIVE")

        elif states[1] != "ACTIVE":
            testResult(self, "failed", "System State should be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed")

    elif val == "NOT_ACTIVE":

        if states[0] != "ACTIVE":
            testResult(self, "passed", "IVI Chipset State should not be set to ACTIVE",
                       "IVI Chipset State is not set to ACTIVE")

        elif states[0] == "ACTIVE":
            testResult(self, "failed", "IVI Chipset State should not be set to ACTIVE",
                       "IVI Chipset State is set to ACTIVE")

        if states[1] != "ACTIVE":
            testResult(self, "passed", "System State should be set to ACTIVE", "System State is set to ACTIVE")

        elif states[1] == "ACTIVE":
            testResult(self, "failed", "System State should be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed")


def rem_files_from_IVI_device(fileName, chipset_type):
    if chipset_type == drimaes_ivi_chipset:
        subprocess.call(
            [drimaes_batchPath + r'C2C_remFilesfromDevice.bat',
             drimaes_ivi_adbSerialNo, fileName])
    elif chipset_type == b2c_ivi_chipset:
        subprocess.call(
            [b2c_batchPath + r'C2C_remFilesfromDevice.bat',
             b2c_ivi_adbSerialNo, fileName])
    elif chipset_type == c2c_ivi_chipset:
        subprocess.call(
            [c2c_ivi_batchPath + r'C2C_remFilesfromDevice.bat',
             c2c_ivi_adbSerialNo, fileName])


def device_onboarding_via_DepPack_IVI(self, onboarding_Type, chipset_type):
    if onboarding_Type == deviceType_IVI:
        if chipset_type == drimaes_ivi_chipset:
            deviceSerialNo = drimaes_ivi_adbSerialNo
        elif chipset_type == b2c_ivi_chipset:
            deviceSerialNo = b2c_ivi_adbSerialNo
        elif chipset_type == c2c_ivi_chipset:
            deviceSerialNo = c2c_ivi_adbSerialNo

        try:
            subprocess.call([drimaes_batchPath + r'deviceOnboarding_IVI.bat', deviceSerialNo, chipset_type, DeviceCommandFiles_path], timeout=10)
            time.sleep(15)
        except FileNotFoundError:
            print(f"Sorry, the file 'deviceOnboarding_IVI.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")

    time.sleep(15)


# ============================================================
# reboot/remount device
# ============================================================

def rebootOrRunAsRoot(self, deviceSerialNo, option):
    try:
        subprocess.call(
            [drimaes_batchPath + r'C2C_adbCommands.bat',
             deviceSerialNo, option])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while rebooting device")


def checkFirmwareVer(self, option):
    try:
        if option == deviceType_IVI:
            result1 = subprocess.call(
                [drimaes_batchPath + r'C2C_adbCommands.bat',
                 drimaes_ivi_adbSerialNo, "firmwareVer_ivi"])
            with open(C2CtestReport_DeviceOnbrdng_backupPath + ivi_files + r'\ver_info.txt',
                      "r") as file:
                json_data = json.load(file)
                Meta_Build_ID_ivi = json_data['Metabuild_Info']['Meta_Build_ID']
                Product_Flavor_ivi = json_data['Metabuild_Info']['Product_Flavor']
                Time_Stamp_ivi = json_data['Metabuild_Info']['Time_Stamp']
                Version_ivi = json_data['Version']

            print("IVI device - Metabuild_Info : ")
            # print(json_data)
            print("Meta_Build_ID : ", Meta_Build_ID_ivi)
            print("Product_Flavor : ", Product_Flavor_ivi)
            print("Time_Stamp : ", Time_Stamp_ivi)
    except:
        print("Something went wrong, pls check logs")


def deviceReplacement_IVI(self, onboarding_Type, chipset_type):
    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        subprocess.call(
            [drimaes_batchPath + r'C2C_deviceReplacement.bat',
             drimaes_ivi_adbSerialNo, deviceType_IVI, drimaes_ivi_chipset, DeviceCommandFiles_path])
        testResult(self, "passed",
                   "Device should be setup with c2c files",
                   "Device is setup with c2c files")
    elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
        subprocess.call(
            [b2c_batchPath + r'C2C_deviceReplacement.bat',
             b2c_ivi_adbSerialNo, deviceType_IVI, b2c_ivi_chipset, DeviceCommandFiles_path])
        testResult(self, "passed",
                   "Device should be setup with c2c files",
                   "Device is setup with c2c files")
    elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        subprocess.call(
            [c2c_ivi_batchPath + r'C2C_deviceReplacement.bat',
             c2c_ivi_adbSerialNo, deviceType_IVI, c2c_ivi_chipset, DeviceCommandFiles_path])
        testResult(self, "passed",
                   "Device should be setup with c2c files",
                   "Device is setup with c2c files")


# ============================================================
# copy default files for fresh IVI device onboarding
# ============================================================
# ============================================================
# Copy default files
# ============================================================

def copy_default_IVI_files(self, onboarding_Type, chipset_type):
    try:
        if chipset_type == drimaes_ivi_chipset:
            deviceSerailNo = drimaes_ivi_adbSerialNo
            batchFolder = drimaes_batchPath
        elif chipset_type == b2c_ivi_chipset:
            deviceSerailNo = b2c_ivi_adbSerialNo
            batchFolder = b2c_batchPath
        if chipset_type == c2c_ivi_chipset:
            deviceSerailNo = c2c_ivi_adbSerialNo
            batchFolder = c2c_ivi_batchPath
        if spvalidationFlag != "Yes":
            print(
                f" => SP Validation flag is set  to {spvalidationFlag}, thus conf files are replaced with deafult confiles")

            subprocess.call(
                [batchFolder + r'C2C_copydefaultFiles.bat',
                 onboarding_Type])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")
    try:
        if spvalidationFlag == "Yes":
            print(
                f"=> SP Validation flag is set  to {spvalidationFlag}, thus conf files are fetched/pulled from flashed metabuild on device")
            subprocess.call(
                [batchFolder + r'C2C_copydefaultFiles_SPvalidation.bat',
                 onboarding_Type, deviceSerailNo])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles_SPvalidation.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")


def cleanUp_IVI_script(self, onboarding_Type, chipset_type):
    print("============================================================\n")
    print("Set up device for fresh onboarding : \n")
    if onboardingTypeFlag == "Yes":
        print(
            f"=> Device Onboard/Provision Flag is set to {onboardingTypeFlag}, thus reads onboarding type from c2cTestData-> DeviceOnboardingData")
    else:
        print(
            f"=> Device Onboard/Provision Flag is set to {onboardingTypeFlag}, thus device is onbaorded based on selected test case")
    if onboarding_Type == deviceType_IVI:
        print("=> Device Onboard/Provision option selected : Standalone IVI Onboarding/Provisioning ")
    else:
        print(f"Invalid  onboarding type")
    print("============================================================\n")

    # Remove/Delete all old files & logs.
    deleteFoldersForUpdate(self, "DeviceOnboarding_backup")
    deleteFoldersForUpdate(self, "OTA")

    # Clean up all old logs and replace conf with default ones.
    if onboarding_Type == deviceType_IVI:
        copy_default_IVI_files(self, onboarding_Type, chipset_type)
    else:
        print("Incorrect input")

    print("## Setting up device(s) for fresh onboarding/provision ##")


if __name__ == '__main__':
    print("\n")


def get_SystemId(self, onboarding_Type):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, "6155")
        systemId = states[5]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        systemIdl = states[5]
    print("System Id : => ", systemId)
    return systemId


def getModel(self, option, onboarding_Type):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, "6155")
        model = states[4]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        model = states[4]
    print("Model Name : => ", model)
    return model


def getVIN(self, option, onboarding_Type):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, "6155")
        vin = states[2]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        vin = states[2]
    return vin

# ============================================================
# Save VIN no in file for SKU/Feature Update
# ============================================================
def saveVIN_IVI(self, onboarding_Type, chipset_type):
    states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)
    path = folderPath + r'C2CtestData\VinNo.txt'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    # print(max_file)
    text_file = open(max_file, "w")
    text_file.write(states[2])
    text_file.close()


def set_telemetry_flags(self):
    folderPath_ivi = C2CtestData_c2c2Path + 'dm.conf'
    folderPath_ivi_c2cdeafult = C2CtestData_c2c2Path + 'c2c_default.conf'

    replaceLineWithText(self, folderPath_ivi, "telemetry_log=n", "telemetry_log=y")
    replaceLineWithText(self, folderPath_ivi, "telemetry_capability=n", "telemetry_capability=y")
    replaceLineWithText(self, folderPath_ivi_c2cdeafult, "telemetry_log=n", "telemetry_log=y")


def push_dmFile_on_IVI_device(self, onboarding_Type, chipset_type):
    set_telemetry_flags(self)
    push_desired_file_on_primary_IVI(self, onboarding_Type, chipset_type, "dm_conf")
    time.sleep(5)
    push_desired_file_on_primary_IVI(self, onboarding_Type, chipset_type, "c2cDefault_conf")


def run_dm_service_on_IVI_device(self, onboarding_Type, chipset_type):
    run_desired_service_on_primary_IVI(self, onboarding_Type, chipset_type, "dmService")


def pull_logs_from_IVI_device(self, onboarding_Type, chipset_type):
    pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "C2Clogs")



def verify_msg_details_pub2Cloud(self, msg_type, msg_attribute):
    # verify Command Control message published to cloud
    if msg_type == commndctrl_msg_type_code:
        msg = commndctrl_msg_type_code
        msg_text = "Command & control"
    if msg_type == telemetry_msg_type_code_tel:
        msg = telemetry_msg_type_code_tel
        msg_text = "Telemetry"
    ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, msg)

    if telemetry_msg_id_published2Cloud in str(ls[0]) and msg in str(ls[0]):
        status = "Found"
        print(
            f"Command & control message published to cloud' {telemetry_msg_id_published2Cloud} with {msg} '")
        testResult(self, "passed", msg_text + "message should be published to cloud via Hub ",
                   msg_text + " message is published to cloud and device logs are updated accordingly, pls refer "
                              "device logs for detailed info")

        print("c2c logs line data : => ", ls[0])

        try:

            ls1 = str(ls[0]).split('"body": "')

            data = str(ls1[1])
            lenmax = len(data) - len(data) % 4
            decodedBytes = base64.b64decode(data[0:lenmax]).decode()

            msg_body_data = str(decodedBytes)
            print("Decoded message body :", msg_body_data)

            if msg_attribute in msg_body_data:
                testResult(self, "passed",
                           msg_attribute + " value should be present in the telemetry message published to the cloud",
                           msg_attribute + " value is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
                           "device logs for detailed info")
            if msg_attribute not in msg_body_data:
                testResult(self, "verificationFailed",
                           msg_attribute + " value should be present in the telemetry message published to the cloud",
                           msg_attribute + " value is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
                           "device logs for detailed info")
        except:
            print("Unable to decode message body data due to truncated logs")

    elif str(ls[0]) == "Error":
        status = "NotFound"
        print(
            msg_text + " message is not published to cloud or device logs are not updated. pls refer device logs in detail")
        testResult(self, "verificationFailed", "Command & control message should be published to cloud via Hub ",
                   msg_text + " message is not published to cloud or device logs are not updated. pls refer device "
                              "logs in detail ")
    else:
        status = "NotFound"
    print("----------------------------------------------------------")
    return status



def decode_msg_body(data):
    ls1 = str(data).split('"body": "')

    data = str(ls1[1])
    lenmax = len(data) - len(data) % 4
    decodedBytes = base64.b64decode(data[0:lenmax]).decode()

    msg_body_data = str(decodedBytes)
    print("Decoded message body :", msg_body_data)

    return msg_body_data

# ============================================================
# Push files on device function
# ============================================================

def push_files_on_primary_IVI1(self, onboarding_Type, chipset_type):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
            time.sleep(5)
            print(drimaes_batchPath1)
            subprocess.call(
                [drimaes_batchPath1 + r'C2C_pushFilesOnIVIdevice.bat',
                 drimaes_ivi_adbSerialNo, drimaes_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [b2c_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 b2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 c2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path])
    except FileNotFoundError:
        print(f"Sorry, the push files on device (batch file) does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while pushing files on device")


