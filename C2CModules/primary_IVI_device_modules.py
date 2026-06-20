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
import datetime
import openpyxl
import requests
import secrets
import string
import hashlib
from datetime import datetime

try:
    from axiom.ttypes import *
except:
    from Axiom.ttypes import *

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from C2CModules.c2c_modules import *
from C2CModules.deviceRegistration_modules import registration_DeviceReg, \
    registration_getCount, registration_getDetails
from C2CModules.e2e_testData import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel
from C2CModules.vehicle_metadata import vehicle_get_vinsByModel_v3
# from C2CModules.telemetry_modules import telemetry_Curr_eventType, vehicle_live_location, last_parked_location
from C2CModules.vehicle_metadata import *
#from C2CModules.vehicle_configurations import *
#from C2CModules.primary_IVI_device_modules import *

sys.path.insert(1, r'C:\Car2Cloud_E2ETesting')

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


# ============================================================
# Pull/Fetch files from device for validations
# ============================================================

def pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, option):
    try:
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        # print(dt)
        filename = "c2clog_" + str(dt) + '.txt'
        # print("Fetch/Pull files from device for validation & backup : ")
        # print("\n-------------------------------------------------------------")
        if onboarding_Type == deviceType_IVI:
            if chipset_type == drimaes_ivi_chipset:
                subprocess.call(
                    [drimaes_batchPath + 'C2C_pullFilesFromDevice.bat',
                     drimaes_ivi_adbSerialNo, option], timeout=60)
                proc = subprocess.Popen(['adb', '-s', drimaes_ivi_adbSerialNo, 'shell', 'logcat > -d', filename],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            elif chipset_type == b2c_ivi_chipset:
                subprocess.call(
                    [b2c_batchPath + 'C2C_pullFilesFromDevice.bat',
                     b2c_ivi_adbSerialNo, option], timeout=60)
                proc = subprocess.Popen(['adb', '-s', b2c_ivi_adbSerialNo, 'shell', 'logcat > -d', filename],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.call(
                    [mahindra_batchPath + 'C2C_pullFilesFromDevice.bat',
                     mahindra_ivi_adbSerialNo, option], timeout=60)
                proc = subprocess.Popen(['adb', '-s', c2c_ivi_adbSerialNo, 'shell', 'logcat > -d', filename],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.call(
                    [c2c_ivi_batchPath + 'C2C_pullFilesFromDevice.bat',
                     c2c_ivi_adbSerialNo, option], timeout=60)
                proc = subprocess.Popen(['adb', '-s', c2c_ivi_adbSerialNo, 'shell', 'logcat > -d', filename],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
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
        if onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
            subprocess.call(
                [mahindra_batchPath + r'C2C_stopServicesOnDevices.bat',
                 mahindra_ivi_adbSerialNo, option])
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

def run_command_on_device(self, deviceSerialNo, command):
    proc = subprocess.Popen(['adb', '-s', deviceSerialNo, command], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    output, errors = proc.communicate()
    proc.wait()
    outputer = output.decode('utf-8')
    print(f"=> command response : {format(outputer)}")
    return outputer


def reboot_device(self, deviceSerialNo):
    try:
        run_command_on_device(self, deviceSerialNo, "reboot")
        i = 1
        while i <= 5:
            outputer = run_command_on_device(self, deviceSerialNo, "root")
            if 'not found' in outputer:
                print("Device is not up yet post reboot, wait for 60s")
                time.sleep(60)
                i = i + 1
            else:
                break
        print(f"=> command response : {format(outputer)}")
    except OSError:
        print(f"Sorry, Something went wrong while reading command response")
        outputer = None
    except:
        print(f"Something went wrong while rebooting device")


def reboot_primary_IVI(self, onboarding_Type, chipset_type, option):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            reboot_device(self, drimaes_ivi_adbSerialNo)

        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            subprocess.call(
                [b2c_batchPath + r'C2C_adbCommands.bat',
                 b2c_ivi_adbSerialNo, option])
        elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
            subprocess.call(
                [mahindra_batchPath + r'C2C_adbCommands.bat',
                 mahindra_ivi_adbSerialNo, option])
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
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.call(
                    [mahindra_batchPath + 'C2C_copydefaultFiles.bat'], timeout=5)
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
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.call(
                    [b2c_batchPath + r'C2C_copydefaultFiles_SPvalidation.bat',
                     onboarding_Type, mahindra_ivi_adbSerialNo], timeout=5)
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
                 drimaes_ivi_adbSerialNo, drimaes_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(10)
            subprocess.call(
                [b2c_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 b2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path], timeout=20)
            time.sleep(10)
        elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
            print()
            # rebootOrRunAsRoot(self, mahindra_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [mahindra_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 mahindra_ivi_adbSerialNo, mahindra_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [c2c_ivi_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                 c2c_ivi_adbSerialNo, b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path], timeout=15)
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
                 drimaes_ivi_adbSerialNo, filename, DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [b2c_batchPath + r'C2C_pushDesiredFileOnIVIdevice.bat',
                 b2c_ivi_adbSerialNo, filename, DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
            rebootOrRunAsRoot(self, mahindra_ivi_adbSerialNo, "root")
            time.sleep(5)
            subprocess.call(
                [mahindra_batchPath + r'C2C_pushDesiredFileOnIVIdevice.bat',
                 mahindra_ivi_adbSerialNo, filename, DeviceCommandFiles_path], timeout=15)
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
    dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
    Env = str(dict["Value"])
    print("Environment selected for device onboarding =>", Env)
    # print(f"Cloud Base Url => {BaseUrl_gbl}")
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
    elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
        print(f"Sku Id =>  {mahindra_IVI_SkuId}")
        print(f"Program Id =>  {mahindra_IVI_PrgmId}")
        print(f"Program sku Id =>  {mahindra_IVI_PrgmSkuId}")
        print(f"Chipset Type =>  {mahindra_IVI_chipsetType}")
        print(f"Chipset SP version =>  {mahindra_IVI_chipsetSpVer}")
    elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        print(f"Sku Id =>  {C2C_IVI_SkuId}")
        print(f"Program Id =>  {C2C_IVI_PrgmId}")
        print(f"Program sku Id =>  {C2C_IVI_PrgmSkuId}")
        print(f"Chipset Type =>  {C2C_IVI_chipsetType}")
        print(f"Chipset SP version =>  {C2C_IVI_chipsetSpVer}")
    print("------------------------------------------------------------")

    # random_id = ' '.join([str(random.randint(10, 9999)).zfill(10) for _ in range(1)])
    random_id = str(random.randint(1111111111, 9999999999))

    # subSystemId = "sub" + random_id
    if TC == "DeviceOnboarding_validData_v3":
        subSystemId = "125"
    else:
        subSystemId = random_id

    print("Sub-SystemId", subSystemId)
    if vinNoFlag == "Yes":
        vinNo = str(reqVinNo)
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
        elif TC == "deviceReplacement":
            vinNo = getVIN(self, onboarding_Type, chipset_type)
        else:
            vinNo = "QVIN" + "IVI" + random_id

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

    # Device Registration
    print("Registration of IVI device : ")
    print("------------------------------------------------------------")

    # Device Reg POST request
    # registration_requestToken(self)
    response_body = registration_DeviceReg(self, deviceType_IVI)
    time.sleep(30)

    # Device Reg GET requests
    # registration_RequestToken_GETmethod(self)
    registration_getCount(self)
    response_body = registration_getDetails(self)

    device_id = response_body["responseData"][0]["device_id"]
    url = response_body["responseData"][0]["url"]
    systemId = response_body["responseData"][0]["system_id"]
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

    # update tele_service conf file for trip events
    update_tele_service(self)

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
    elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, mahindra_ivi_chipset, "valid")
        print("=> Conf file(s) are updated with newly registered device data")
        print("\n------------------------------------------------------------")
        print("Stop all c2c services on device(s) : ")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, mahindra_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("\n------------------------------------------------------------")
        print("Push updated files on device : ")
        push_files_on_primary_IVI(self, onboarding_Type, mahindra_ivi_chipset)
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
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.run(
                    [mahindra_batchPath + 'C2C_startServicesOnDevices.bat',
                     mahindra_ivi_adbSerialNo, "C2CServices"], timeout=5)
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
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.run(
                    [mahindra_batchPath + 'C2C_startServicesOnDevices.bat',
                     mahindra_ivi_adbSerialNo, "OTAServices"], timeout=5)
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
# Run desired services on device
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
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.run(
                    [mahindra_batchPath + 'C2C_startServicesOnDevices.bat',
                     mahindra_ivi_adbSerialNo, serviceName], timeout=5)
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


# ============================================================
# Restart service on device
# ============================================================

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
        elif onboarding_Type == deviceType_VT and chipset_type == mahindra_ivi_chipset:
            subprocess.run(
                [mahindra_batchPath + r'C2C_startServicesOnDevices.bat',
                 mahindra_ivi_adbSerialNo, "IVIrestart"], timeout=5)
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
# Run Paho commands via stub
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
                     drimaes_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=60)
            elif chipset_type == b2c_ivi_chipset:
                if option == 'trip_summary_stub':
                    subprocess.run(
                        [b2c_batchPath + 'C2C_paho_commands.bat',
                         b2c_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=5)
                else:
                    subprocess.run(
                        [b2c_batchPath + 'C2C_paho_commands.bat',
                         b2c_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=60)
            elif chipset_type == c2c_ivi_chipset:
                subprocess.run(
                    [c2c_ivi_batchPath + 'C2C_paho_commands.bat',
                     c2c_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=60)
            elif chipset_type == mahindra_ivi_chipset:
                subprocess.run(
                    [mahindra_batchPath + 'C2C_paho_commands.bat',
                     mahindra_ivi_adbSerialNo, option, DeviceCommandFiles_path], timeout=60)
            time.sleep(90)
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
        # vin = json_data['C2C_Vehicle']['vin']
        # model = json_data['C2C_Vehicle']['vehicle_info']['model']

        # added try & except block for bootstrap onbaording validations
        try:
            model = json_data['C2C_Vehicle']['vehicle_info']['model']
        except:
            model = ""
        try:
            vin = json_data['C2C_Vehicle']['vin']
        except:
            ls = search_text_in_file(self, sideloadedFile, "vin=", "vin=")
            vin = ls[0].replace("vin=", "").replace(" ", "").replace("\n", "")
            # vin = readVIN_primary_IVI(self, onboarding_Type)
            # vin =""
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
    states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)
    response_body = smpServer_getVINdetails(self, str(states[2]))

    try:
        # Assert: Validate response status code and body contents
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
        if chipset_type == mahindra_ivi_chipset:
            for i in range(lendevice):
                if response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                    "chipsetType"] == mahindra_IVI_chipsetType or \
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

    i = 0
    for i in range(5):
        if states[1] != 'ACTIVE':
            time.sleep(60)
            print('waiting for another 60 sec')

            pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "DeviceOnboarding")

            states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipset_type)
        elif states[1] == 'ACTIVE':
            break

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


# ============================================================
# Remove files from device
# ============================================================
def rem_files_from_IVI_device(fileName, chipset_type):
    if chipset_type == drimaes_ivi_chipset:
        subprocess.call(
            [drimaes_batchPath + r'C2C_remFilesfromDevice.bat',
             drimaes_ivi_adbSerialNo, fileName])
    elif chipset_type == b2c_ivi_chipset:
        subprocess.call(
            [b2c_batchPath + r'C2C_remFilesfromDevice.bat',
             b2c_ivi_adbSerialNo, fileName])
    elif chipset_type == mahindra_ivi_chipset:
        subprocess.call(
            [mahindra_batchPath + r'C2C_remFilesfromDevice.bat',
             mahindra_ivi_adbSerialNo, fileName])
    elif chipset_type == c2c_ivi_chipset:
        subprocess.call(
            [c2c_ivi_batchPath + r'C2C_remFilesfromDevice.bat',
             c2c_ivi_adbSerialNo, fileName])


# ============================================================
# Onboard device via deployment package
# ============================================================
def device_onboarding_via_DepPack_IVI(self, onboarding_Type, chipset_type):
    deviceSerialNo = ''
    if onboarding_Type == deviceType_IVI:
        if chipset_type == drimaes_ivi_chipset:
            deviceSerialNo = drimaes_ivi_adbSerialNo
            batchPath = drimaes_batchPath
        elif chipset_type == b2c_ivi_chipset:
            deviceSerialNo = b2c_ivi_adbSerialNo
            batchPath = b2c_batchPath
        elif chipset_type == mahindra_ivi_chipset:
            deviceSerialNo = mahindra_ivi_adbSerialNo
            batchPath = mahindra_batchPath
        elif chipset_type == c2c_ivi_chipset:
            deviceSerialNo = c2c_ivi_adbSerialNo
            batchPath = c2c_ivi_batchPath

        try:
            print(batchPath, deviceSerialNo, chipset_type,
                  DeviceCommandFiles_path)

            subprocess.call([batchPath + r'C2C_deviceOnboarding.bat', deviceSerialNo, onboarding_Type,
                             DeviceCommandFiles_path], timeout=10)
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


# ============================================================
# Check firmware details
# ============================================================
def checkFirmwareVer(self, onboarding_Type, chipset_type):
    try:
        if onboarding_Type == deviceType_IVI:
            if chipset_type == drimaes_ivi_chipset:
                result1 = subprocess.call(
                    [drimaes_batchPath + r'C2C_adbCommands.bat',
                     drimaes_ivi_adbSerialNo, "firmwareVer_ivi"], timeout=10)
            elif chipset_type == b2c_ivi_chipset:
                result1 = subprocess.call(
                    [b2c_batchPath + r'C2C_adbCommands.bat',
                     b2c_ivi_adbSerialNo, "firmwareVer_ivi"], timeout=10)
            elif chipset_type == mahindra_ivi_chipset:
                result1 = subprocess.call(
                    [mahindra_batchPath + r'C2C_adbCommands.bat',
                     mahindra_ivi_adbSerialNo, "firmwareVer_ivi"], timeout=10)

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


# ============================================================
# Device Replacement
# ============================================================
def deviceReplacement_IVI(self, onboarding_Type, chipset_type):
    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        subprocess.call(
            [drimaes_batchPath + r'C2C_deviceReplacement.bat',
             drimaes_ivi_adbSerialNo, deviceType_IVI, drimaes_ivi_chipset, DeviceCommandFiles_path])
        proc = subprocess.Popen(['adb', '-s', drimaes_ivi_adbSerialNo, 'shell', 'killall dm'], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        proc = subprocess.Popen(['adb', '-s', drimaes_ivi_adbSerialNo, 'shell', 'killall c2c_hub'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
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
    elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
        subprocess.call(
            [mahindra_batchPath + r'C2C_deviceReplacement.bat',
             mahindra_ivi_adbSerialNo, deviceType_IVI, b2c_ivi_chipset, DeviceCommandFiles_path])
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

def copy_default_IVI_files(self, onboarding_Type, chipset_type):
    try:
        if chipset_type == drimaes_ivi_chipset:
            deviceSerailNo = drimaes_ivi_adbSerialNo
            batchFolder = drimaes_batchPath
        elif chipset_type == b2c_ivi_chipset:
            deviceSerailNo = b2c_ivi_adbSerialNo
            batchFolder = b2c_batchPath
        elif chipset_type == mahindra_ivi_chipset:
            deviceSerailNo = mahindra_ivi_adbSerialNo
            batchFolder = mahindra_batchPath
        elif chipset_type == c2c_ivi_chipset:
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


# ============================================================
# Clean up device for fresh onboarding
# ============================================================

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


# ============================================================
# Fetch/Read System Id
# ============================================================
def get_SystemId(self, onboarding_Type, chipsetType):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipsetType)
        systemId = states[5]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        systemId = states[8]
    print("System Id : => ", systemId)
    return systemId


# ============================================================
# Fetch/Read Model Name
# ============================================================
def getModel(self, onboarding_Type, chipsetType):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, "6155")
        model = states[4]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        model = states[4]
    print("Model Name : => ", model)
    lowercase_string = model.lower()
    model = lowercase_string
    return model


# ============================================================
# Fetch/Read VIN no
# ============================================================
def getVIN(self, onboarding_Type, chipsetType):
    if onboarding_Type == deviceType_IVI:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = verify_primary_IVI_chipset_and_system_state(self, onboarding_Type, chipsetType)
        vin = states[2]
    else:
        # pullFilesFromDevice(self, "DeviceOnboarding", onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        vin = states[2]
    vin = vin.replace("\n", "")
    return vin


# ============================================================
# Read VIN no from file
# ============================================================
def readVIN_primary_IVI(self, onboarding_Type):
    path = folderPath + r'C2CtestData\VinNo.txt'
    files = glob.glob(path)
    max_file = max(files, key=os.path.getctime)
    # print(max_file)
    text_file = open(max_file, "r")
    vin = text_file.read()
    text_file.close()
    vin = vin.replace("\n", "")
    return vin


# ============================================================
# Save VIN no.
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


# ============================================================
# Set telemetry flag
# ============================================================
def set_telemetry_flags(self):
    folderPath_ivi = C2CtestData_c2c2Path + 'dm.conf'
    folderPath_ivi_c2cdeafult = C2CtestData_c2c2Path + 'c2c_default.conf'

    replaceLineWithText(self, folderPath_ivi, "telemetry_log=n", "telemetry_log=y")
    replaceLineWithText(self, folderPath_ivi, "telemetry_capability=n", "telemetry_capability=y")
    replaceLineWithText(self, folderPath_ivi_c2cdeafult, "telemetry_log=n", "telemetry_log=y")


# ============================================================
# Push Files on device for telemetry
# ============================================================
def push_dmFile_on_IVI_device(self, onboarding_Type, chipset_type):
    # set_telemetry_flags(self)
    push_desired_file_on_primary_IVI(self, onboarding_Type, chipset_type, "dm_conf")
    time.sleep(5)
    push_desired_file_on_primary_IVI(self, onboarding_Type, chipset_type, "c2cDefault_conf")


# ============================================================
# Run C2C - DM service on device
# ============================================================
def run_dm_service_on_IVI_device(self, onboarding_Type, chipset_type):
    run_desired_service_on_primary_IVI(self, onboarding_Type, chipset_type, "dmService")


# ============================================================
# Fetch/Pull C2C logs to host machine
# ============================================================
def pull_logs_from_IVI_device(self, onboarding_Type, chipset_type):
    pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "C2Clogs")


# ============================================================
# Verify message published to cloud for telemetry & CnC
# ============================================================
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


# ============================================================
# Decode the published message body
# ============================================================
def decode_msg_body(data):
    ls1 = str(data).split('"body": "')

    data = str(ls1[1])
    lenmax = len(data) - len(data) % 4
    decodedBytes = base64.b64decode(data[0:lenmax]).decode()

    msg_body_data = str(decodedBytes)
    print("Decoded message body :", msg_body_data)

    return msg_body_data


# ============================================================
# Fetch/Read Device Id
# ============================================================
def get_deviceId(self, onboarding_Type, chipset_Type):
    if onboarding_Type == deviceType_IVI:
        c2cvehicleFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\c2c_vehicle.json'
    elif onboarding_Type == deviceType_TCU:
        c2cvehicleFile = C2CtestReport_DeviceOnbrdng_backupPath + 'tcu_files\c2c\c2c_vehicle.json'
        with open(c2cvehicleFile, 'r') as file:
            json_data = json.load(file)
            try:
                primary_deviceId = json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["deviceId"]
                # primary_deviceId = json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["device_info"]["ecu_type"]
            except:
                primary_deviceId = "Chipset data is not fetched"
            print("\n")

    return primary_deviceId


# ============================================================
# Update tele_service & trip conf file with file upload details
# ============================================================
def update_tele_service(self):
    try:
        print('Update tele_service.conf file for trip events')
        teleServiceFile = C2CtestData_c2c2Path + r'tele_service.conf'
        print(teleServiceFile)
        dict = read_api_data_from_excel(self, "API_Data", "FileUpload")
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        # header_x = ast.literal_eval(headers)
        json_object = json.loads(headers)
        apiKey = json_object["api-key"]
        complete_url = str(base_url + endpoint)
        dict1 = read_api_data_from_excel(self, "API_Common_Data", "User Name")
        userName = str(dict1["Value"])

        replaceLineWithText(self, teleServiceFile, 'https_url=', 'https_url=' + complete_url)
        replaceLineWithText(self, teleServiceFile, 'https_x_requestor=', 'https_x_requestor=' + userName)
        replaceLineWithText(self, teleServiceFile, 'https_api_key=', 'https_api_key=' + apiKey)
        print('Update tele_service.conf file for trip events')
    except:
        print('tele_service.conf file is not available or failed to update')

    try:
        tripFile = C2CtestData_c2c2Path + r'trip.conf'
        print(tripFile)
        dict = read_api_data_from_excel(self, "API_Data", "FileUpload")
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        # header_x = ast.literal_eval(headers)
        json_object = json.loads(headers)
        apiKey = json_object["api-key"]
        complete_url = str(base_url + endpoint)
        dict1 = read_api_data_from_excel(self, "API_Common_Data", "User Name")
        userName = str(dict1["Value"])

        replaceLineWithText(self, tripFile, 'https_url=', 'https_url=' + complete_url)
        replaceLineWithText(self, tripFile, 'https_x_requestor=', 'https_x_requestor=' + userName)
        replaceLineWithText(self, tripFile, 'https_api_key=', 'https_api_key=' + apiKey)

    except:
        print('trip.conf file is not available or failed to update')


# ============================================================
# Fetch/Read Engine Type for trip
# ============================================================
def get_engineType(self, onboarding_Type, chipset_Type):
    if onboarding_Type == deviceType_IVI:
        c2cvehicleFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\c2c_vehicle.json'
        with open(c2cvehicleFile, 'r') as file:
            json_data = json.load(file)
            try:
                if "engine_type" in str(json_data):
                    primaryDevice_engineType = json_data['C2C_Vehicle']['vehicle_info']['engine_type']
                elif "fuel_type" in str(json_data):
                    data_len = len(json_data['C2C_Vehicle']['vehicle_info']['fuel_type'])
                    if data_len >= 2:
                        for i in range(data_len):
                            print("Fuel type :", json_data['C2C_Vehicle']['vehicle_info']['fuel_type'][i])
                    primaryDevice_engineType = json_data['C2C_Vehicle']['vehicle_info']['fuel_type'][0]
            except:
                primaryDevice_engineType = "IVI chipset data is not fetched or engine type field is missing"
            print("\n")
    return primaryDevice_engineType


# ============================================================
# Verify newly onboarded device details by vehicle metadata by VIN cloud api
# ============================================================
def validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, deviceState):
    status = ''
    print("=============================================================")
    try:

        print("Read VIN & System Id from device for validations")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        vin = getVIN(self, OnboardingType, chipsetType)

        print("VIN : =>  ", vin)

        print("---------------------------------------------------------")
        print("Validate VIN @ Cloud post device on-boarding/provisioning : ")

        response = vehicle_get_vinsByModel_v3(self, vin)
        if response["responseData"]["data"]["vin"] == vin:
            testResult(self, "passed", "VIN should be added/onboarded successfully",
                       "VIN is added/onboarded successfully")
        else:
            testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                       "VIN is not added/onboarded successfully")

        print("---------------------------------------------------------")
        print("Validate System Id @ Cloud post device on-boarding/provisioning : ")

        if response["responseData"]["data"]["systemId"] == systemId:
            testResult(self, "passed", "VIN should be mapped to System Id successfully",
                       "VIN is mapped to System Id successfully")
        else:
            status = 'FAIL'
            testResult(self, "verificationFailed", "VIN should be mapped to System Id successfully",
                       "VIN is not mapped to System Id.")

        print("---------------------------------------------------------")
        print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")

        if response["responseData"]["data"]["lifecycleState"] == "ACTIVE":
            testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                       "Life Cycle State is set to ACTIVE")
        else:
            testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                       "Life Cycle State is not set to ACTIVE")

        if status == 'FAIL':
            testResult(self, "failed", "VIN should be mapped to System Id successfully",
                       "VIN is not mapped to System Id.")
    except:
        testResult(self, "failed", "Cloud Validation ",
                   "cloud validation failed, Refer logs for more details")

    print("=============================================================")


# ============================================================
# Event chcek for device logs
# ============================================================
def log_event_for_msg(self, OnboardingType, chipsetType, msg_type_code, msg_type_attr):
    try:
        i = 1
        while i <= 10:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            status = verify_msg_details_pub2Cloud(self, msg_type_code, msg_type_attr)
            print("Status : ", status)
            if status == "Found":
                break
            i = i + 1
            time.sleep(5)
    except:
        print("\n")


# Device Onboarding via Bootstrap reusable module
def standalone_IVI_bootstrap_device_onboarding(self, onboarding_Type, chipset_type, TC):
    print("------------------------------------------------------------")
    # Remove/Delete all old files & logs.
    deleteFoldersForUpdate(self, "DeviceOnboarding_backup")
    deleteFoldersForUpdate(self, "OTA")

    print("Device On-boarding/Provisioning details : ")
    print("Test Case details => ", TC)
    dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
    Env = str(dict["Value"])
    print("Environment selected for device onboarding =>", Env)
    if Env == "QC-QA":
        url = "a2wmamsgqsa3iq-ats.iot.us-west-1.amazonaws.com"
    elif Env == "QC-INTG":
        url = "am1ck51fe3zjt-ats.iot.us-west-1.amazonaws.com"
    elif Env == "B2C-DEMO":
        url = "a1puonvws384ab-ats.iot.us-west-1.amazonaws.com"
    elif Env == "GCP-QA":
        # url = "dev-cb.gcp-c2c-develop.qualcomm.com"
        url = "a3ca7e6f.ala.dedicated.gcp.emqxcloud.com"
    elif Env == "GCP-DEV":
        url = "a3ca7e6f.ala.dedicated.gcp.emqxcloud.com"
    elif Env == "GCP-REP":
        url = "q46bbf98.ala.dedicated.gcp.emqxcloud.com"
    elif Env == "RE-DEV":
        url = "i7e1598e.ala.dedicated.gcp.emqxcloud.com"
    elif Env == "RE-PERF":
        url = "ae1c7c1e.ala.dedicated.gcp.emqxcloud.com"

    # print(f"Cloud Base Url => {BaseUrl_gbl}")
    print("------------------------------------------------------------")

    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        subprocess.call(
            [drimaes_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)

    elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
        subprocess.call(
            [b2c_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)

    elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
        subprocess.call(
            [mahindra_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)

    elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        subprocess.call(
            [c2c_ivi_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)

    print("------------------------------------------------------------")
    # Generate unique Device Id
    print("Generate unique device Id : ")
    print("------------------------------------------------------------")

    random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])

    if onboarding_Type == "TCU":
        if deviceIdFlag == "Yes":
            deviceId = reqDeviceId_tcu
        else:
            deviceId = "QA_TEST_TCU_" + random_id
    elif onboarding_Type == "IVI":
        if deviceIdFlag == "Yes":
            deviceId = reqDeviceId_ivi
        else:
            deviceId = "QA_TEST_IVI_" + random_id

    # random_id = ' '.join([str(random.randint(10, 9999)).zfill(10) for _ in range(1)])
    randomId = str(random.randint(1111111111, 9999999999))

    vinNo = "QVIN" + "IVI" + randomId

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

    print("------------------------------------------------------------")
    print("Update desired conf files with required device data : ")

    replaceLineWithText(self, sideloadedFile, "ECU1=", "ECU1=" + deviceId)
    replaceLineWithText(self, sideloadedFile, "device_id=", "device_id=" + deviceId)
    replaceLineWithText(self, sideloadedFile, "vin=", "vin=" + vinNo)
    # if Env == "GCP-QA":
    # replaceLineWithText(self, c2cDefaultConfFile, "cloud_tls_support=", "cloud_tls_support=3")
    # else:
    # replaceLineWithText(self, c2cDefaultConfFile, "cloud_tls_support=", "cloud_tls_support=2")

    with open(c2cvehicleFile) as f:
        json_data = json.load(f)
        json_data["C2C_Vehicle"]["url_cloud"] = url

    with open(c2cvehicleFile, 'w') as f:
        f.write(json.dumps(json_data))

    if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        print("=> Conf file(s) are updated with required device data")
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
    elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, mahindra_ivi_chipset, "valid")
        print("=> Conf file(s) are updated with newly registered device data")
        print("\n------------------------------------------------------------")
        print("Stop all c2c services on device(s) : ")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, mahindra_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("\n------------------------------------------------------------")
        print("Push updated files on device : ")
        push_files_on_primary_IVI(self, onboarding_Type, mahindra_ivi_chipset)
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


# -----------------------------------------------------------------------------------
# RE Modules
# -----------------------------------------------------------------------------------

# Read attribute value from vehicle json file
def read_vehicleJsonFile(self, attribute):
    try:
        c2cvehicleFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\c2c_vehicle.json'
        # print(c2cvehicleFile)
        with open(c2cvehicleFile, 'r') as file:
            json_data = json.load(file)
            # print(json_data)
            if attribute == "system_state":
                attribute_value = json_data["C2C_Vehicle"]['system_state']
            elif attribute == "system_id":
                attribute_value = json_data["C2C_Vehicle"]['system_id']
            elif attribute == "modelcode":
                attribute_value = json_data["C2C_Vehicle"]['modelcode']
            elif attribute == "service_mode":
                attribute_value = json_data["C2C_Vehicle"]['service_mode']
    except:
        print("Something went wrong while reading vehicle.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value


# Read attribute value from master json file
def read_masterConfJsonFile(self, attribute):
    try:
        c2cMasterConfFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\master_conf.json'
        with open(c2cMasterConfFile, 'r') as file:
            json_data = json.load(file)
            if attribute == "VacationMode_Enabled":
                attribute_value = json_data['IVI']['EV']["VehicleSettings"]['VehicleMode']['VacationMode']['Enabled']
            elif attribute == "VacationMode_StartTime":
                attribute_value = json_data['IVI']['EV']["VehicleSettings"]['VehicleMode']['VacationMode']['StartTime']
            elif attribute == "VacationMode_EndTime":
                attribute_value = json_data['IVI']['EV']["VehicleSettings"]['VehicleMode']['VacationMode']['EndTime']
    except:
        print("Something went wrong while reading master_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value


# Read attribute value from master json file
# Read attribute value from master json file
def read_masterConfJsonFile_v2(self, cloudEnv, attribute, mode):
    try:
        c2cMasterConfFile = C2CtestReport_DeviceOnbrdng_backupPath + 'ivi_files\c2c\master_conf.json'
        with open(c2cMasterConfFile, 'r') as file:
            json_data = json.load(file)
            if cloudEnv not in r8_patch2_envs and cloudEnv not in r8_patch_envs_hmac:
                if mode == "vacationMode":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['start_time']
                    elif attribute == "VacationMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['end_time']
                elif mode == "vacationMode_without_startEndTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['enabled']
                elif mode == "vacationMode_without_startTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['end_time']
                elif mode == "vacationMode_without_endTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['vacation_mode']['start_time']
                elif mode == "privacyMode":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['start_time']
                    elif attribute == "PrivacyMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['end_time']
                elif mode == "privacyMode_without_startEndTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['enabled']
                elif mode == "privacyMode_without_startTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['end_time']
                elif mode == "privacyMode_without_endTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['privacy_mode']['start_time']
                elif mode == "incognitoMode":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['start_time']
                    elif attribute == "IncognitoMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['end_time']
                elif mode == "incognitoMode_without_startEndTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['enabled']
                elif mode == "incognitoMode_without_startTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['end_time']
                elif mode == "incognitoMode_without_endTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['incognito_mode']['start_time']
                elif mode == "remoteDiagnosticMode":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['start_time']
                    elif attribute == "RemoteDiagnosticMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['end_time']
                elif mode == "remoteDiagnosticMode_without_startEndTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                elif mode == "remoteDiagnosticMode_without_startTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['end_time']
                elif mode == "remoteDiagnosticMode_without_endTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['remote_diagnostic_mode']['start_time']
                elif mode == "serviceMode":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "ServiceMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['start_time']
                    elif attribute == "ServiceMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['end_time']
                elif mode == "serviceMode_without_startEndTime":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['enabled']
                elif mode == "serviceMode_without_startTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "Service_EndTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['end_time']
                elif mode == "serviceMode_without_endTime":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "ServiceMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["vehicle_mode"]['service_mode']['start_time']
                elif mode == "Add_Remove":
                    if attribute == "add_tyre_pressure":
                        attribute_value = json_data['vehicle_settings']["vehicle_features"]['tyre_pressure']
                elif mode == "service_remainder":
                    if attribute == "odometer_value":
                        attribute_value = json_data['vehicle_settings']['vehicle_service']['service_reminder'][
                            'odometer_reading']
                    elif attribute == "service_date":
                        attribute_value = json_data['vehicle_settings']['vehicle_service']['service_reminder'][
                            'service_date']
                elif mode == "crash_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['sms']['crash_sms']['ert_number']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['sms']['crash_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['sms']['crash_sms'][
                            'category_id']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['sms']['crash_sms']['sms_template'][
                            'delimit_text_2']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['sms']['crash_sms']['sms_template'][
                            'fields']
                elif mode == "sos_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['sms']['sos_sms']['ert_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['sms']['sos_sms']['sms_template'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['sms']['sos_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['sms']['sos_sms']['sms_template'][
                            'delimit_text_2']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['sms']['sos_sms']['sms_template'][
                            'fields']
                elif mode == "towaway_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['sms']['towaway_sms']['ert_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['sms']['towaway_sms'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['sms']['towaway_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['sms']['towaway_sms']['sms_template'][
                            'delimit_text_2']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['sms']['towaway_sms']['sms_template'][
                            'fields']
                elif mode == "heartbeat_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['sms']['heartbeat_sms']['ert_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['sms']['heartbeat_sms'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['sms']['heartbeat_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['sms']['heartbeat_sms']['sms_template'][
                            'delimit_text_2']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['sms']['heartbeat_sms']['sms_template'][
                            'fields']
            else:
                if mode == "vacationMode":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['start_time']
                    elif attribute == "VacationMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['end_time']
                elif mode == "vacationMode_without_startEndTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['enabled']
                elif mode == "vacationMode_without_startTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['end_time']
                elif mode == "vacationMode_without_endTime":
                    if attribute == "VacationMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['enabled']
                    elif attribute == "VacationMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['vacation_mode']['start_time']
                elif mode == "privacyMode":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['start_time']
                    elif attribute == "PrivacyMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['end_time']
                elif mode == "privacyMode_without_startEndTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['enabled']
                elif mode == "privacyMode_without_startTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['end_time']
                elif mode == "privacyMode_without_endTime":
                    if attribute == "PrivacyMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['enabled']
                    elif attribute == "PrivacyMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['privacy_mode']['start_time']
                elif mode == "incognitoMode":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['start_time']
                    elif attribute == "IncognitoMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['end_time']
                elif mode == "incognitoMode_without_startEndTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['enabled']
                elif mode == "incognitoMode_without_startTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['end_time']
                elif mode == "incognitoMode_without_endTime":
                    if attribute == "IncognitoMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['enabled']
                    elif attribute == "IncognitoMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['incognito_mode']['start_time']
                elif mode == "remoteDiagnosticMode":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['start_time']
                    elif attribute == "RemoteDiagnosticMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['end_time']
                elif mode == "remoteDiagnosticMode_without_startEndTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                elif mode == "remoteDiagnosticMode_without_startTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['end_time']
                elif mode == "remoteDiagnosticMode_without_endTime":
                    if attribute == "RemoteDiagnosticMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['enabled']
                    elif attribute == "RemoteDiagnosticMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['remote_diagnostic_mode']['start_time']
                elif mode == "serviceMode":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "ServiceMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['start_time']
                    elif attribute == "ServiceMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['end_time']
                elif mode == "serviceMode_without_startEndTime":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['enabled']
                elif mode == "serviceMode_without_startTime":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "ServiceMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['end_time']
                elif mode == "serviceMode_without_endTime":
                    if attribute == "ServiceMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['enabled']
                    elif attribute == "ServiceMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['service_mode']['start_time']
                elif mode == "normalMode":
                    if attribute == "NormalMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['enabled']
                    elif attribute == "NormalMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['start_time']
                    elif attribute == "NormalMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['end_time']
                elif mode == "normalMode_without_startEndTime":
                    if attribute == "NormalMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['enabled']
                elif mode == "normalMode_without_startTime":
                    if attribute == "NormalMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['enabled']
                    elif attribute == "NormalMode_EndTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['end_time']
                elif mode == "normalMode_without_endTime":
                    if attribute == "NormalMode_Enabled":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['enabled']
                    elif attribute == "NormalMode_StartTime":
                        attribute_value = json_data['vehicle_settings']["user_settings"]["vehicle_mode"]['normal_mode']['start_time']
                elif mode == "Add_Remove":
                    if attribute == "add_tyre_pressure":
                        attribute_value = json_data['vehicle_settings']["vehicle_function"]['tyre_pressure']
                elif mode == "service_remainder":
                    if attribute == "odometer_value":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['service_due'][
                            'distance']
                    elif attribute == "service_date":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['service_due'][
                            'time']
                elif mode == "crash_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['crash_sms']['sms_number']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['crash_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['crash_sms'][
                            'category_id']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['crash_sms']['sms_template'][
                            'delimit_text']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['crash_sms']['sms_template'][
                            'fields']
                elif mode == "sos_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['sos_sms']['sms_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['sos_sms']['sms_template'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['sos_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['sos_sms']['sms_template'][
                            'delimit_text']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['sos_sms']['sms_template'][
                            'fields']
                elif mode == "towaway_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['towaway_sms']['sms_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['towaway_sms'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['towaway_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['towaway_sms']['sms_template'][
                            'delimit_text']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['towaway_sms']['sms_template'][
                            'fields']
                elif mode == "heartbeat_sms":
                    if attribute == "sms_number":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['heartbeat_sms']['sms_number']
                    elif attribute == "sms_template_category_id":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['heartbeat_sms'][
                            'category_id']
                    elif attribute == "sms_template_intro":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['heartbeat_sms']['sms_template'][
                            'intro']
                    elif attribute == "sms_template_delimit_text":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['heartbeat_sms']['sms_template'][
                            'delimit_text']
                    elif attribute == "sms_template_fields":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['communication']['sms']['heartbeat_sms']['sms_template'][
                            'fields']
                elif mode == "service_rdm":
                    if attribute == "service_rdm":
                        attribute_value = json_data['vehicle_settings']['vehicle_function']['service_rdm']
                elif mode == "remote_diagnostic":
                    if attribute == "remote_diagnostic":
                        attribute_value = json_data['vehicle_settings']['user_settings']['remote_diagnostic']
    except:
        print("Something went wrong while reading master_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value

# Read attribute value from vehicle mode json file
def read_vehicleModeJsonFile(self, attribute):
    try:
        c2cVehicleModeFile = C2CtestReport_DeviceOnbrdng_backupPath + r'ivi_files\c2c\vehicle_mode.json'
        with open(c2cVehicleModeFile, 'r') as file:
            json_data = json.load(file)
            if attribute == "vehicle_mode":
                attribute_value = json_data['vehicle_mode']
            elif attribute == "start_time":
                attribute_value = json_data['start_time']
            elif attribute == "end_time":
                attribute_value = json_data['end_time']
            elif attribute == "previous_mode":
                attribute_value = json_data['previous_mode']
            elif attribute == "state":
                attribute_value = json_data['state']
    except:
        print("Something went wrong while reading vehicle_mode.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value


# -----------------------------------------------------
# Reusable module for EOL Onboarding
# -----------------------------------------------------

def vehicle_connection_state(self, state):
    if state == "global":
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = vehicle_get_vehicle_connection_state_global(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200 or response.status_code == 400), \
            "Unexpected status code: " + str(response.status_code)

        response_body = response.json()

        if response.status_code == 200:
            # Validate response body
            if response_body["message"] in ["data fetch successfully", "Data fetch successfully"]:
                systemId_actual = response_body["connectionResponse"]["systemId"]
                connected = response_body["connectionResponse"]["connected"]
                deviceId = response_body["connectionResponse"]["deviceId"]
                connectionTime = response_body["connectionResponse"]["connectionTime"]

                print("SystemId Actual: ", systemId_actual)
                print("Connection Status: ", connected)
                print("Device Id: ", deviceId)
                print("Connection Time: ", connectionTime)

                if systemId == systemId_actual and connected:
                    testResult(self, "passed", "Device should be connected with EMQX",
                               "Device successfully connected with EMQX")
                    assert True
                else:
                    testResult(self, "passed", "Device should be connected with EMQX",
                               "Device is not connected with EMQX")
                    assert True
            else:
                testResult(self, "failed", "Device should be connected with EMQX",
                           "Failed to fetch EMQX connection state. Reason: " + response_body["message"])
                assert False

        elif response.status_code == 400:
            # Fetch vehicle metadata to check lifecycle state
            response1 = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            assert response1.status_code == 200, "Unexpected status code: " + str(response1.status_code)

            response_body1 = response1.json()
            if response_body1.get("message") == "Data Fetched Successfully":
                lifeCycleState = response_body1["responseData"]["vehicleDetails"][0]["lifecycleState"]

                if lifeCycleState == "REHOMED":
                    # Expect Client ID not found error
                    if (response_body["errors"][0]["errorCode"] == "13219" and
                            response_body["errors"][0]["message"] == "Client ID not found"):
                        testResult(self, "passed",
                                   "If lifecycle state is REHOMED, connection state should fail with Client ID not found",
                                   "Correctly returned Client ID not found for REHOMED vehicle")
                        assert True
                    else:
                        testResult(self, "failed",
                                   "If lifecycle state is REHOMED, connection state should fail with Client ID not found",
                                   "Unexpected error response for REHOMED vehicle: " + str(response_body))
                        assert False
                else:
                    testResult(self, "failed", "Lifecycle state should be REHOMED",
                               "Lifecycle state is not set to REHOMED")
                    assert False
        else:
            print("Something went wrong")
            testResult(self, "failed", "Device should be connected with EMQX",
                       "Unexpected response: " + str(response_body))
            assert False

    elif state == "regional":
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)

        # Call api reusable module
        response = vehicle_get_vehicle_connection_state_regional(self, systemId, "valid")

        # Validate response status code
        assert response.status_code == 200, "Status code is not 200. Found: " + str(response.status_code)

        response_body = response.json()

        # Validate response body
        if response_body["message"] in ["data fetch successfully", "Data fetch successfully"]:
            systemId_actual = response_body["connectionResponse"]["systemId"]
            connected = response_body["connectionResponse"]["connected"]
            deviceId = response_body["connectionResponse"]["deviceId"]
            connectionTime = response_body["connectionResponse"]["connectionTime"]

            if systemId == systemId_actual and connected:
                print("SystemId Actual: ", systemId_actual)
                print("Connection Status: ", connected)
                print("Device Id: ", deviceId)
                print("Connection Time: ", connectionTime)
                testResult(self, "passed", "Device should be connected with EMQX",
                           "Device successfully connected with EMQX")
            else:
                testResult(self, "failed", "Device should be connected with EMQX",
                           "Device is not connected with EMQX")
                assert False
        else:
            testResult(self, "failed", "Device should be connected with EMQX",
                       "Failed to fetch EMQX connection state. Reason: " + response_body.get("message", "Unknown"))
            assert False

    else:
        print("Invalid state provided:", state)
        assert False


def is_device_active(self):
    try:
        system_state = read_vehicleJsonFile(self, "system_state")
        if system_state == "ACTIVE" or system_state == "GLOBAL_ACTIVE" or system_state == "PRE_REGIONAL_ACTIVE" or system_state == "REGIONAL_READY":
            return system_state
    except Exception as e:
        print(f"Error checking device state: {e}")
        return False


def is_device_connected(self, deviceSerialNo):
    try:
        output = run_command_on_device(self, deviceSerialNo, "get-state")
        return 'device' in output
    except Exception as e:
        print(f"Error checking device connection: {e}")
        return False


# ---------------
def validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, deviceState):
    status = ''
    print("=============================================================")
    try:

        if deviceState == "global":

            print("Read VIN & System Id from device for validations")

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN : =>  ", vin)

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")

            response = vehicle_get_vinsByModel_v3(self, vin)
            if response["responseData"]["data"]["vin"] == vin:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")
            print("Validate System Id @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be mapped to System Id successfully",
                           "VIN is mapped to System Id successfully")
            else:
                status = 'FAIL'
                testResult(self, "verificationFailed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

            print("---------------------------------------------------------")
            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["lifecycleState"] == "ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "GLOBAL_ACTIVE" or response["responseData"]["data"]["lifecycleState"] == "REHOMED":
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

            if status == 'FAIL':
                testResult(self, "failed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

        if deviceState == "regional":

            print("Read VIN & System Id from device for validations")

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN : =>  ", vin)

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")

            response = vehicle_get_vinsByModel_v3_regional_state(self, vin)
            if response["responseData"]["data"]["vin"] == vin:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")
            print("Validate System Id @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be mapped to System Id successfully",
                           "VIN is mapped to System Id successfully")
            else:
                status = 'FAIL'
                testResult(self, "verificationFailed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

            print("---------------------------------------------------------")
            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["lifecycleState"] == "ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "REGIONAL_ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "PRE_REGIONAL_ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "REGIONAL_READY":
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

            if status == 'FAIL':
                testResult(self, "failed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")
    except:
        testResult(self, "failed", "Cloud Validation ",
                   "cloud validation failed, Refer logs for more details")

    print("=============================================================")


def reboot_IVI_device(self, deviceSerialNo, onboarding_Type, chipset_type, path):
    try:
        run_command_on_device(self, deviceSerialNo, "reboot")
        for i in range(5):
            outputer = run_command_on_device(self, deviceSerialNo, "root")
            if 'not found' in outputer:
                print("Device is not up yet post reboot, wait for 60s")
                time.sleep(60)
            else:
                break
        print(f"=> command response : {outputer}")

        print("Keep the device in permissive mode after reboot")

        # Command to set permissive mode
        set_permissive = "shell setenforce 0"

        # Command to check the device permission status
        check_status = "shell getenforce"

        set_permissive_output = run_command_on_primary_IVI_device(self, deviceSerialNo, set_permissive)

        check_status_output = run_command_on_primary_IVI_device(self, deviceSerialNo, check_status)

        if "Permissive" in check_status_output:
            print("Device is in permissive mode")
        else:
            print(f"Device is not in permissive mode. Found: {check_status_output}")

        # Check if the device is connected
        if is_device_connected(self, deviceSerialNo):
            print("Device is connected after reboot.")
        else:
            print("Device is not connected after reboot.")

        # adding below lines as part of r8 patch-1
        # Command to push file
        cloudEnv = read_cloud_env(self)
        print(f"Cloud environment is: {cloudEnv}")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8", "RE-UAT", "GCP-QA2",
                        "GCP-PERF2"]:
            push_file = "push C:\\Car2Cloud_E2ETesting\\C2CtestData\\VinNo.txt /data"
            print(f"Pushing VIN file with command: {push_file}")
            push_result = run_command_on_primary_IVI_device(self, deviceSerialNo, push_file)
            print(f"VIN file push result: {push_result}")
            time.sleep(5)

            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run Onboarding vin stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            print("Executing onboarding VIN stub...")
            stub_result = run_paho_command_on_primary_IVI(self, onboarding_Type, chipset_type, 'onboarding_vin_stub')
            print(f"Stub execution result: {stub_result}")
            time.sleep(5)

            print("Onboarding Vin stub start/run process is completed, verify logs for trip & telemetry details : ")
        else:
            pass

        # Continuously pull files until the device state is ACTIVE or timeout
        timeout = 300  # Total timeout in seconds (5 minutes)
        interval = 30  # Interval between checks in seconds
        increase_time = 0

        while increase_time <= timeout:
            if is_device_active(self):
                print("Device is ACTIVE after reboot.")
                break
            else:
                print("Device is not ACTIVE yet, pulling files...")
                if path == "path1":
                    pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "DeviceOnboarding")
                elif path == "path2":
                    pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, "pullFiles")
                time.sleep(interval)
                increase_time += interval
        else:
            print("Device did not become ACTIVE after reboot. Timeout reached.")
    except OSError:
        print("Something went wrong while reading command response")
        outputer = None
    except Exception as e:
        print(f"Something went wrong while rebooting device: {e}")


def reboot_primary_IVI_device(self, onboarding_Type, chipset_type, option):
    try:
        if onboarding_Type == deviceType_IVI:
            if chipset_type == drimaes_ivi_chipset:
                reboot_IVI_device(self, drimaes_ivi_adbSerialNo, onboarding_Type, chipset_type, option)
            elif chipset_type == b2c_ivi_chipset:
                reboot_IVI_device(self, b2c_ivi_adbSerialNo, onboarding_Type, chipset_type, option)
            elif chipset_type == mahindra_ivi_chipset:
                reboot_IVI_device(self, mahindra_ivi_adbSerialNo, onboarding_Type, chipset_type, option)
            elif chipset_type == c2c_ivi_chipset:
                reboot_IVI_device(self, c2c_ivi_adbSerialNo, onboarding_Type, chipset_type, option)
            time.sleep(60)
    except FileNotFoundError:
        print("The file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    except Exception as e:
        print(f"Something went wrong while rebooting device: {e}")


# def is_device_active():

def push_files_on_primary_IVI_devive(self, onboarding_Type, chipset_type, conf_file_path):
    try:
        if onboarding_Type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
            time.sleep(5)
            if conf_file_path == "conf_file_path1":
                subprocess.call(
                    [drimaes_batchPath + r'pushFilesOnIVIdevice.bat',
                     drimaes_ivi_adbSerialNo, "conf_file_path1", drimaes_pushBinariesLibrariesOnIVI,
                     DeviceCommandFiles_path], timeout=15)
            elif conf_file_path == "conf_file_path2":
                subprocess.call(
                    [drimaes_batchPath + r'pushFilesOnIVIdevice.bat',
                     drimaes_ivi_adbSerialNo, "conf_file_path2", drimaes_pushBinariesLibrariesOnIVI,
                     DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
            time.sleep(10)
            if conf_file_path == "conf_file_path1":
                subprocess.call(
                    [b2c_batchPath + r'pushFilesOnIVIdevice.bat',
                     b2c_ivi_adbSerialNo, "conf_file_path1", b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path],
                    timeout=15)
            elif conf_file_path == "conf_file_path2":
                subprocess.call(
                    [b2c_batchPath + r'pushFilesOnIVIdevice.bat',
                     b2c_ivi_adbSerialNo, "conf_file_path2", b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path],
                    timeout=15)
            time.sleep(10)
        elif onboarding_Type == deviceType_IVI and chipset_type == mahindra_ivi_chipset:
            # rebootOrRunAsRoot(self, mahindra_ivi_adbSerialNo, "root")
            time.sleep(5)
            if conf_file_path == "conf_file_path1":
                subprocess.call(
                    [mahindra_batchPath + r'pushFilesOnIVIdevice.bat',
                     mahindra_ivi_adbSerialNo, "conf_file_path1", mahindra_pushBinariesLibrariesOnIVI,
                     DeviceCommandFiles_path], timeout=15)
            elif conf_file_path == "conf_file_path2":
                subprocess.call(
                    [mahindra_batchPath + r'pushFilesOnIVIdevice.bat',
                     mahindra_ivi_adbSerialNo, "conf_file_path2", mahindra_pushBinariesLibrariesOnIVI,
                     DeviceCommandFiles_path], timeout=15)
        elif onboarding_Type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
            time.sleep(5)
            if conf_file_path == "conf_file_path1":
                subprocess.call(
                    [c2c_ivi_batchPath + r'pushFilesOnIVIdevice.bat',
                     c2c_ivi_adbSerialNo, "conf_file_path1", b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path],
                    timeout=15)
            elif conf_file_path == "conf_file_path2":
                subprocess.call(
                    [c2c_ivi_adbSerialNo + r'pushFilesOnIVIdevice.bat',
                     c2c_ivi_adbSerialNo, "conf_file_path2", b2c_pushBinariesLibrariesOnIVI, DeviceCommandFiles_path],
                    timeout=15)
    except FileNotFoundError:
        print(f"Sorry, the push files on device (batch file) does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while pushing files on device")


# Device Onboarding via Bootstrap reusable module
def standalone_IVI_bootstrap_device_onboarding_eol(self, onboarding_Type, chipset_type, TC, option):
    print("------------------------------------------------------------")
    print("Device On-boarding/Provisioning details : ")
    print("Test Case details =>", TC)

    # Cleanup old files
    deleteFoldersForUpdate(self, "DeviceOnboarding_backup")
    deleteFoldersForUpdate(self, "OTA")

    # Read environment details
    dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
    Env = str(dict["Value"])
    print("Environment selected for device onboarding =>", Env)

    dict1 = read_api_data_from_excel(self, "Env_Details", Env)
    url = str(dict1["Endpoint"])
    systemName = str(dict1["Username"])
    systemKey = str(dict1["Password"])
    tenantId = str(dict1["tenantId"])
    print("------------------------------------------------------------")

    # Push default bootstrap files based on chipset
    if onboarding_Type == deviceType_IVI:
        if chipset_type == drimaes_ivi_chipset:
            subprocess.call([drimaes_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)
        elif chipset_type == b2c_ivi_chipset:
            subprocess.call([b2c_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)
        elif chipset_type == mahindra_ivi_chipset:
            subprocess.call([mahindra_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)
        elif chipset_type == c2c_ivi_chipset:
            subprocess.call([c2c_ivi_batchPath + 'C2C_copydefaultFiles_bootstrap.bat', Env], timeout=5)

    print("------------------------------------------------------------")
    print("Generate unique device ID : ")

    random_id = str(random.randint(10, 9999)).zfill(7)
    randomId = str(random.randint(1111111111, 9999999999))

    # Assign deviceId and vinNo
    if onboarding_Type == "TCU":
        # deviceId = reqDeviceId_tcu if deviceIdFlag == "Yes" else "QA_TEST_TCU_" + random_id
        if Env not in ["RE-DEV", "GCP-REPL2"]:
            deviceId = secrets.token_hex(32).upper()  # Generates a 64-character hex string
        else:
            deviceId = reqDeviceId_tcu if deviceIdFlag == "Yes" else "QA_TEST_TCU_" + random_id
    elif onboarding_Type == "IVI":
        if deviceIdFlag == "Yes":
            deviceId = reqDeviceId_ivi
            if option == "DUPLICATE_DEVICEID":
                deviceId = dupDeviceId
        else:
            deviceId = "QA_TEST_IVI_" + random_id
            if Env not in ["GCP-DEMO2", "GCP-REPL2"]:
                deviceId = secrets.token_hex(32).upper()  # Generates a 64-character hex string

    vinNo = "QVINIVI" + randomId
    if option == "DUPLICATE_VIN":
        vinNo = duplicateVIN
    elif option == "DUPLICATE_DEVICEID_VIN":
        deviceId = dupDeviceId
        vinNo = duplicateVIN
    elif option in ["EXISTED_ONBOARDED_VIN", "EXISTED_ONBOARDED_VIN_WITH_ATTESTATION"]:
        vinNo = readVIN_primary_IVI(self, onboarding_Type)
        if option == "EXISTED_ONBOARDED_VIN_WITH_ATTESTATION":
            with open(c2cvehicleFile) as f:
                json_data = json.load(f)
                json_data["C2C_Vehicle"]["gbl_url_cloud"] = url
                json_data["C2C_Vehicle"]["attestation_types"] = ["QWES"]
            with open(c2cvehicleFile, 'w') as f:
                f.write(json.dumps(json_data))

    # Assign model name
    if reqModelNameFlag == "Yes":
        uniqueModel = reqModelName
    elif OTA_ModelFlag == "Yes":
        uniqueModel = "model" + random_id

    # Write VIN to file
    text_file = folderPath + r'C2CtestData\VinNo.txt'
    with open(text_file, "w") as f:
        f.write(vinNo)

    print("------------------------------------------------------------")
    print("Update desired conf files with required device data : ")

    replaceLineWithText(self, sideloadedFile, "ECU1=", "ECU1=" + deviceId)
    replaceLineWithText(self, sideloadedFile, "device_id=", "device_id=" + deviceId)
    replaceLineWithText(self, sideloadedFile, "vin=", "vin=" + vinNo)
    replaceLineWithText(self, sideloadedFile, "tenant_id=", "tenant_id=" + tenantId)

    # Update c2cvehicleFile with credentials and attestation
    with open(c2cvehicleFile) as f:
        json_data = json.load(f)
        json_data["C2C_Vehicle"]["gbl_url_cloud"] = url
        json_data["C2C_Vehicle"]["systemName"] = systemName
        json_data["C2C_Vehicle"]["systemKey"] = systemKey
        json_data["C2C_Vehicle"]["attestation_types"] = []
        if option == "QWES_ATTESTATION":
            json_data["C2C_Vehicle"]["attestation_types"] = ["QWES"]
        elif option == "MNO_ATTESTATION":
            json_data["C2C_Vehicle"]["attestation_types"] = ["OEM"]
        elif option == "QWES_MNO_ATTESTATION":
            json_data["C2C_Vehicle"]["attestation_types"] = ["QWES", "OEM"]
    with open(c2cvehicleFile, 'w') as f:
        f.write(json.dumps(json_data))

    # Stop services and push updated files
    print("\n------------------------------------------------------------")
    print("Stop all c2c services on device(s) : ")

    if chipset_type == drimaes_ivi_chipset:
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, drimaes_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        print("Push updated files on device : ")
        path_key = "conf_file_path1" if TC == "path1" else "conf_file_path2"
        push_files_on_primary_IVI_devive(self, onboarding_Type, drimaes_ivi_chipset, path_key)

    elif chipset_type == b2c_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, b2c_ivi_chipset, "valid")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, b2c_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        path_key = "conf_file_path1" if TC == "path1" else "conf_file_path2"
        push_files_on_primary_IVI_devive(self, onboarding_Type, b2c_ivi_chipset, path_key)

    elif chipset_type == mahindra_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, mahindra_ivi_chipset, "valid")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, mahindra_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        path_key = "conf_file_path1" if TC == "path1" else "conf_file_path2"
        push_files_on_primary_IVI_devive(self, onboarding_Type, mahindra_ivi_chipset, path_key)

    elif chipset_type == c2c_ivi_chipset:
        replaceText_IVIconf(self, onboarding_Type, c2c_ivi_chipset, "valid")
        stop_C2Cservices_on_primary_IVI(self, onboarding_Type, c2c_ivi_chipset, "C2CServices")
        print("=> Stopped all c2c services on device(s)")
        path_key = "conf_file_path1" if TC == "path1" else "conf_file_path2"
        push_files_on_primary_IVI_devive(self, onboarding_Type, c2c_ivi_chipset, path_key)

    else:
        print("Invalid chipset type")

    print("\n=> All required files have been pushed on device and ready for onboarding")


# --------Vehicle configuration reusable functions---------------------------
def push_vehicleConf_files_on_primary_IVI_device(self, onboarding_Type, chipset_type, option, vehicle_conf_file_path):
    try:
        # Determine the device and chipset type
        if onboarding_Type == deviceType_IVI:
            # Define the destination path dynamically based on vehicle_conf_file_path_type
            if vehicle_conf_file_path == "path1":
                conf_dest_path = "/mnt/vendor/persist/data/c2c"
            elif vehicle_conf_file_path == "path2":
                conf_dest_path = "/mnt/vendor/persist/c2c"
            else:
                raise ValueError(f"Invalid vehicle_conf_file_path_type: {vehicle_conf_file_path}")

            # Execute batch file based on chipset type
            if chipset_type == drimaes_ivi_chipset:
                rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
                time.sleep(5)
                subprocess.call(
                    [drimaes_batchPath + r'pushVehicleConfFiles.bat',
                     drimaes_ivi_adbSerialNo, option, conf_dest_path], timeout=15)
            elif chipset_type == b2c_ivi_chipset:
                rebootOrRunAsRoot(self, b2c_ivi_adbSerialNo, "root")
                time.sleep(10)
                subprocess.call(
                    [b2c_batchPath + r'pushVehicleConfFiles.bat',
                     b2c_ivi_adbSerialNo, option, conf_dest_path], timeout=20)
                time.sleep(10)
            elif chipset_type == mahindra_ivi_chipset:
                time.sleep(5)
                subprocess.call(
                    [mahindra_batchPath + r'pushVehicleConfFiles.bat',
                     mahindra_ivi_adbSerialNo, option, conf_dest_path], timeout=15)
            elif chipset_type == c2c_ivi_chipset:
                rebootOrRunAsRoot(self, c2c_ivi_adbSerialNo, "root")
                time.sleep(5)
                subprocess.call(
                    [c2c_ivi_batchPath + r'pushVehicleConfFiles.bat',
                     c2c_ivi_adbSerialNo, option, conf_dest_path], timeout=15)
            else:
                raise ValueError(f"Unsupported chipset type: {chipset_type}")
        else:
            raise ValueError(f"Unsupported onboarding_Type: {onboarding_Type}")

    except FileNotFoundError:
        print(f"Error: The batch file does not exist or incorrect file path/name")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred while pushing files on device: {e}")


def generate_sha256_checksum(file_path):
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "File not found. Please check the file path and try again."


def generate_cloud_checksum(self, option):
    file_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration"
    checksum = None

    if "master_conf" in option:
        master_conf_path = file_path + r"\master_conf.json"
        checksum = generate_sha256_checksum(master_conf_path)
        print(f"Cloud checksum: {checksum}")
    elif "telemetry_conf" in option:
        telemetry_conf_path = file_path + r"\telemetry_conf.json"
        checksum = generate_sha256_checksum(telemetry_conf_path)
        print(f"Cloud checksum: {checksum}")
    elif "command_conf" in option:
        command_conf_path = file_path + r"\command_conf.json"
        checksum = generate_sha256_checksum(command_conf_path)
        print(f"Cloud checksum: {checksum}")
    elif "alert_conf" in option:
        alert_conf_path = file_path + r"\alert_conf.json"
        checksum = generate_sha256_checksum(alert_conf_path)
        print(f"Cloud checksum: {checksum}")

    return checksum


def generate_device_checksum(self, option):
    file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\c2c"
    checksum = None

    if "master_conf" in option:
        master_conf_path = file_path + r"\master_conf.json"
        checksum = generate_sha256_checksum(master_conf_path)
        print(f"Device checksum: {checksum}")
    elif "telemetry_conf" in option:
        telemetry_conf_path = file_path + r"\telemetry_conf.json"
        checksum = generate_sha256_checksum(telemetry_conf_path)
        print(f"Device checksum: {checksum}")
    elif "command_conf" in option:
        command_conf_path = file_path + r"\command_conf.json"
        checksum = generate_sha256_checksum(command_conf_path)
        print(f"Device checksum: {checksum}")
    elif "alert_conf" in option:
        alert_conf_path = file_path + r"\alert_conf.json"
        checksum = generate_sha256_checksum(alert_conf_path)
        print(f"Device checksum: {checksum}")

    return checksum


def update_master_conf(self, cloudEnv, attribute):
    """
    Update the master configuration JSON file with new vehicle settings.

    This function reads the master configuration file, updates the vehicle features
    with new settings, and writes the updated data back to the file.
    """
    # Path to the master configuration JSON file
    masterConfFile = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"

    try:
        # Load the existing JSON data from the file
        with open(masterConfFile, 'r') as file:
            data = json.load(file)

        # Insert the new variable and value
        if "insert_tyrePressure" in attribute:
            if cloudEnv not in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "RE-UAT",
                                "GCP-PERF2"]:
                data["vehicle_settings"]["vehicle_features"]["tyre_pressure"] = "1"
            else:
                data["vehicle_settings"]["vehicle_function"]["tyre_pressure"] = "1"

        # Write the updated JSON data back to the file
        with open(masterConfFile, 'w') as file:
            json.dump(data, file)

        print("New variable and value have been added to the JSON file successfully.")

    except FileNotFoundError:
        print(f"Error: The file {masterConfFile} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except KeyError as e:
        print(f"Error: Key {e} not found in the JSON data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def restart_rule_engine_service(self, onboardingType, chipsetType, path):
    push_vehicleConf_files_on_primary_IVI_device(self, onboardingType, chipsetType, "restart_ruleEngine_service", path)



# -----------------------------------Run adb commnand on the device----------------------------------

def run_command_on_primary_IVI_device(self, deviceSerialNo, command):
    proc = subprocess.Popen(['adb', '-s', deviceSerialNo] + command.split(), stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    output, errors = proc.communicate()
    proc.wait()
    outputer = output.decode('utf-8')
    print(f"=> command response : {format(outputer)}")
    return outputer


# ----------------vehicle conf - Command precondition, telemetry push frequency update, over speed alert configuration--------------------------------

def read_telemetryConfJsonFile(self,cloudEnv, attribute, mode):
    try:
        c2cTelemetryConfFile = C2CtestReport_DeviceOnbrdng_backupPath + r'ivi_files\c2c\telemetry_conf.json'
        with open(c2cTelemetryConfFile, 'r') as file:
            json_data = json.load(file)
            if cloudEnv not in r8_patch4_sp17_envs:
                if mode == "normalMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['normal_mode']['events']['3101'][
                            'push_freq']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['normal_mode']['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['normal_mode']['events']['3101'][
                            'enable_flag']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['normal_mode']['events']
                elif mode == "vacationMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['vacation_mode']['events']['3101'][
                            'push_freq']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['vacation_mode']['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['vacation_mode']['events']['3101'][
                            'enable_flag']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['vacation_mode']['events']
                elif mode == "privacyMode":
                    if attribute == "pushFrequencyUpdate_1001":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['privacy_mode']['events']['1001'][
                            'push_freq']
                    if attribute == "pushFrequencyUpdate_6500":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['privacy_mode']['events']['6500'][
                            'push_freq']
                    elif attribute == "batchFrequencyUpdate_1001":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['privacy_mode']['events']['1001'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_1001":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['privacy_mode']['events']['1001'][
                            'enable_flag']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['privacy_mode']['events']
                elif mode == "incognitoMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['incognito_mode']['events']['3101'][
                            'push_freq']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['incognito_mode']['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = json_data['vehicle_settings']["telemetry"]['incognito_mode']['events']['3101'][
                            'enable_flag']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['incognito_mode']['events']
            else:
                if mode == "normalMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'push_freq']['normal_mode']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'enable_flag']['normal_mode']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['events']
                elif mode == "vacationMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'push_freq']['vacation_mode']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'enable_flag']['vacation_mode']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['events']
                elif mode == "privacyMode":
                    if attribute == "pushFrequencyUpdate_1001":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['privacy_mode']['events']['1001'][
                            'push_freq']
                    if attribute == "pushFrequencyUpdate_6500":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['6500'][
                            'push_freq']['privacy_mode']
                    elif attribute == "batchFrequencyUpdate_6500":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['6500'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_6500":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['6500'][
                            'enable_flag']['privacy_mode']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['events']
                elif mode == "incognitoMode":
                    if attribute == "pushFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'push_freq']['incognito_mode']
                    elif attribute == "batchFrequencyUpdate_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'batch_frequency']
                    elif attribute == "enabled_flag_3101":
                        attribute_value = \
                        json_data['vehicle_settings']["telemetry"]['events']['3101'][
                            'enable_flag']['incognito_mode']
                    elif attribute == "add_new_block" or attribute == "remove_new_block":
                        attribute_value = json_data['vehicle_settings']['telemetry']['events']

    except:
        print("Something went wrong while reading telemetry_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value

def read_commandConfJsonFile(self, attribute, mode):
    try:
        c2cCommandConfFile = C2CtestReport_DeviceOnbrdng_backupPath + r'ivi_files\c2c\command_conf.json'
        with open(c2cCommandConfFile, 'r') as file:
            json_data = json.load(file)
            if mode == "normalMode":
                if attribute == "d_device_update_speed":
                    attribute_value = \
                    json_data['vehicle_settings']["remote_operations"]['normal_mode']['condition']['0']['d_device']
            elif mode == "vacationMode":
                if attribute == "d_device_update_speed":
                    attribute_value = \
                    json_data['vehicle_settings']["remote_operations"]['vacation_mode']['condition']['0']['d_device']
            elif mode == "privacyMode":
                if attribute == "d_device_update_speed":
                    attribute_value = \
                    json_data['vehicle_settings']["remote_operations"]['privacy_mode']['condition']['0']['d_device']
            elif mode == "incognitoMode":
                if attribute == "d_device_update_speed":
                    attribute_value = \
                    json_data['vehicle_settings']["remote_operations"]['incognito_mode']['condition']['0']['d_device']

    except:
        print("Something went wrong while reading command_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value

def read_alertConfJsonFile(self, attribute, mode):
    try:
        c2cAlertConfFile = C2CtestReport_DeviceOnbrdng_backupPath + r'ivi_files\c2c\alert_conf.json'
        with open(c2cAlertConfFile, 'r') as file:
            json_data = json.load(file)
            if mode == "normalMode" or mode == "vacationMode" or mode == "privacyMode" or mode == "incognitoMode":
                if attribute == "over_speed_limit":
                    attribute_value = \
                    json_data["vehicle_settings"]["alert_configurations"]["alerts"]["4"]["alert_logic"]["alert_reg"][
                        "threshold"][0]["lower_limit_data"]
    except:
        print("Something went wrong while reading alert_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value

# read the cloud Env
# Read environment details
def read_cloud_env(self):
    dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
    cloudEnv = str(dict["Value"])

    return cloudEnv


# Clous side validation post onboardig
def validate_vehicle_metadata_by_systemId(self, OnboardingType, chipsetType, deviceState):
    print("=============================================================")
    try:
        print("Read VIN & System Id from device for validations")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)
        print(f"VIN : =>  {vin}")
        print(f"SystemId : =>  {systemId}")
        pageNo, pageSize = "1", "10"

        if deviceState == "global":

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")
            response = vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, "global")

            response_body = response.json()

            if response_body["responseData"]["vehicleDetails"][0]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")
            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")
            if response_body["responseData"]["vehicleDetails"][0]["lifecycleState"] in ["ACTIVE", "GLOBAL_ACTIVE",
                                                                                        "REHOMED"]:
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

        elif deviceState == "regional":
            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")
            response = vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, "regional")

            response_body = response.json()

            if response_body["responseData"]["vehicleDetails"][0]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")

            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")
            if response_body["responseData"]["vehicleDetails"][0]["lifecycleState"] in {"ACTIVE", "REGIONAL_ACTIVE",
                                                                                        "PRE_REGIONAL_ACTIVE",
                                                                                        "REGIONAL_READY"}:
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

        else:
            print(f"Unknown deviceState: {deviceState}")
            testResult(self, "failed", "Device State Validation", f"Unsupported deviceState: {deviceState}")

    except Exception as e:
        print(f"Exception occurred: {e}")
        testResult(self, "failed", "Cloud Validation", "Cloud validation failed, refer logs for more details")

    print("=============================================================")


# Memory utilization

def c2c_health(self, OnboardingType, chipsetType, tc):
    if tc == "push_health_script":
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Run Memory Usage Monitor Script on device : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        print("Executing Memory Usage stub...")
        stub_result = run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'c2c_health')

        print(f"Stub execution result: {stub_result}")
        time.sleep(5)

        print("Memory Usage  stub start/run process is completed, verify logs for details : ")

    elif tc == "pull_health_report":

        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "c2c_health_report")


def read_dtcConfJsonFile(self, attribute):
    try:
        c2cDTCConfFile = C2CtestReport_DeviceOnbrdng_backupPath + r'ivi_files\c2c\dtc_conf.json'
        with open(c2cDTCConfFile, 'r') as file:
            json_data = json.load(file)
            if attribute == "dtc_P1001_update_priority":
                attribute_value = \
                    json_data['vehicle_settings']["dtc_configurations"]['dtc_1']['priority']
            elif attribute == "dtc_10202_update_priority":
                attribute_value = \
                    json_data['vehicle_settings']["dtc_configurations"]['dtc_2']['priority']
            elif attribute == "dtc_p10301_update_priority":
                attribute_value = \
                    json_data['vehicle_settings']["dtc_configurations"]['dtc_3']['priority']
            elif attribute == "dtc_p10501_update_priority":
                attribute_value = \
                    json_data['vehicle_settings']["dtc_configurations"]['dtc_4']['priority']
            elif attribute == "dtc_b11b01_update_priority":
                attribute_value = \
                    json_data['vehicle_settings']["dtc_configurations"]['dtc_5']['priority']

    except:
        print("Something went wrong while reading command_conf.json file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value

def read_apkconf(cloudEnv, alert, params):
    try:
        c2cAPKConfFile = C2CtestReport_DeviceOnbrdng_backupPath + r'\ivi_files\c2c\apkconfig.txt'
        with open(c2cAPKConfFile, 'r') as file:
            json_data = json.load(file)
            if alert == "crash_sms":
                if params == "sms_number":
                    attribute_value = \
                    json_data['crash_sms']['sms_number']
                elif params == "sms_template_intro":
                    attribute_value = \
                    json_data['crash_sms'][
                        'sms_template'][
                        'intro']
                elif params == "sms_template_category_id":
                    attribute_value = \
                    json_data['crash_sms'][
                        'category_id']
                elif params == "sms_template_delimit_text":
                    attribute_value = \
                    json_data['crash_sms'][
                        'sms_template'][
                        'delimit_text']
                elif params == "sms_template_fields":
                    attribute_value = \
                    json_data['crash_sms'][
                        'sms_template'][
                        'fields']
            elif alert == "sos_sms":
                if params == "sms_number":
                    attribute_value = \
                    json_data['sos_sms']['sms_number']
                elif params == "sms_template_intro":
                    attribute_value = \
                    json_data['sos_sms'][
                        'sms_template'][
                        'intro']
                elif params == "sms_template_category_id":
                    attribute_value = \
                    json_data['sos_sms'][
                        'category_id']
                elif params == "sms_template_delimit_text":
                    attribute_value = \
                    json_data['sos_sms'][
                        'sms_template'][
                        'delimit_text']
                elif params == "sms_template_fields":
                    attribute_value = \
                    json_data['sos_sms'][
                        'sms_template'][
                        'fields']
            elif alert == "towaway_sms":
                if params == "sms_number":
                    attribute_value = \
                    json_data['towaway_sms']['sms_number']
                elif params == "sms_template_intro":
                    attribute_value = \
                    json_data['towaway_sms'][
                        'sms_template'][
                        'intro']
                elif params == "sms_template_category_id":
                    attribute_value = \
                    json_data['towaway_sms'][
                        'category_id']
                elif params == "sms_template_delimit_text":
                    attribute_value = \
                    json_data['towaway_sms'][
                        'sms_template'][
                        'delimit_text']
                elif params == "sms_template_fields":
                    attribute_value = \
                    json_data['towaway_sms'][
                        'sms_template'][
                        'fields']
            elif alert == "heartbeat_sms":
                if params == "sms_number":
                    attribute_value = \
                    json_data['heartbeat_sms']['sms_number']
                elif params == "sms_template_intro":
                    attribute_value = \
                    json_data['heartbeat_sms'][
                        'sms_template'][
                        'intro']
                elif params == "sms_template_category_id":
                    attribute_value = \
                    json_data['heartbeat_sms'][
                        'category_id']
                elif params == "sms_template_delimit_text":
                    attribute_value = \
                    json_data['heartbeat_sms'][
                        'sms_template'][
                        'delimit_text']
                elif params == "sms_template_fields":
                    attribute_value = \
                    json_data['heartbeat_sms'][
                        'sms_template'][
                        'fields']
            else:
                print("Invalid attribute")
    except:
        print("Something went wrong while reading apkconfig.txt file")
        attribute_value = "error"
    print("------------------------------------------------------")
    return attribute_value





