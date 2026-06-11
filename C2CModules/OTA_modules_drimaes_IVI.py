import json
import random
import subprocess
import time

from C2CModules.OTA_reuse_modules import fileVer, uploadFile, presignedUrl, sotaFileVer, read_scheduleId, \
    listFirmwareSchedules, listFirmwareScheduleStatus, appCheck, listPackageScheduleStatus, listPackageSchedules, \
    uploadFile_fota
from C2CModules.c2c_modules import saveAPIrespIntoFile
from C2CModules.e2e_testData import otaPackagePath, deviceType_IVI, testData, \
    C2CtestReport_otaPath, drimaes_ivi_chipset, drimaes_batchPath, drimaes_ivi_adbSerialNo
# Test Data for FOTA
from C2CModules.fota_api_modules import FOTA_firmwareUpload, FOTA_createScript
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import getModel, run_otaServices_on_primary_IVI, rebootOrRunAsRoot
from C2CModules.sota_api_modules import SOTA_uploadPackage, SOTA_CreateScript, \
    get_preCondition_from_preconditionDetails_api
from C2CModules.testResults import testResult

selectModelFlag_fota = testData("FotaData_Drimaes_IVI", 4, 2)
reqModelName_fota = testData("FotaData_Drimaes_IVI", 4, 3)
VinNoFlag_fota = testData("FotaData_Drimaes_IVI", 5, 2)
reqVinNo_fota = testData("FotaData_Drimaes_IVI", 5, 3)
system_tcu_fota = testData("FotaData_Drimaes_IVI", 6, 3)
system_ivi_fota = testData("FotaData_Drimaes_IVI", 7, 3)
baseFirmwareFlag_fota = testData("FotaData_Drimaes_IVI", 8, 2)
filename_base_fota = testData("FotaData_Drimaes_IVI", 8, 3)
diffFirmwareFlag_fota = testData("FotaData_Drimaes_IVI", 9, 2)
filename_update_fota = testData("FotaData_Drimaes_IVI", 9, 3)
filepath_base_fota = otaPackagePath + filename_base_fota
filepath_update_fota = otaPackagePath + filename_update_fota
ecuType_tcu_fota = "TCU"
ecuType_ivi_fota = "IVI"
downloadConsent_fota = testData("FotaData_Drimaes_IVI", 10, 3)
installConsent_fota = testData("FotaData_Drimaes_IVI", 11, 3)
rebootConsent_fota = testData("FotaData_Drimaes_IVI", 12, 3)
releaseNotes_fota = testData("FotaData_Drimaes_IVI", 13, 3)
baseFirmwareVerFlag_fota = testData("FotaData_Drimaes_IVI", 14, 2)
baseFirmwareVersion_fota = testData("FotaData_Drimaes_IVI", 14, 3)
diffFirmwareVerFlag_fota = testData("FotaData_Drimaes_IVI", 15, 2)
diffFirmwareVersion_fota = testData("FotaData_Drimaes_IVI", 15, 4)

# Test Data for SOTA
selectModelFlag_sota = testData("SotaData_Drimaes_IVI", 4, 2)
reqModelName_sota = testData("SotaData_Drimaes_IVI", 4, 3)
VinNoFlag_sota = testData("SotaData_Drimaes_IVI", 5, 2)
reqVinNo_sota = testData("SotaData_Drimaes_IVI", 5, 3)
system_tcu_sota = testData("SotaData_Drimaes_IVI", 6, 3)
system_ivi_sota = testData("SotaData_Drimaes_IVI", 7, 3)
ecuType_tcu_sota = "TCU"
ecuType_ivi_sota = "IVI"
downloadConsent_sota = testData("SotaData_Drimaes_IVI", 8, 3)
installConsent_sota = testData("SotaData_Drimaes_IVI", 9, 3)
rebootConsent_sota = testData("SotaData_Drimaes_IVI", 10, 3)
filename_sota = testData("SotaData_Drimaes_IVI", 11, 3)
filepath_sota = otaPackagePath + filename_sota
releaseNotes_sota = testData("SotaData_Drimaes_IVI", 12, 3)
packageNameFlag_sota = testData("SotaData_Drimaes_IVI", 13, 2)
packageName_sota = testData("SotaData_Drimaes_IVI", 13, 3)
packageVersionFlag_sota = testData("SotaData_Drimaes_IVI", 14, 2)
packageVersion_sota = testData("SotaData_Drimaes_IVI", 14, 3)
baseFirmwareFilename_sota = testData("SotaData_Drimaes_IVI", 15, 3)
baseFirmware_sota = otaPackagePath + str(baseFirmwareFilename_sota)


# FOTA Functions:

def uploadFirmware(self, firmware, onboarding_type, chipset_type):
    filename = firmwareVer = ''
    firmwareId = 0
    model = getModel(self, onboarding_type, chipset_type)
    # print("Model Name : => ", model)

    if firmware == "baseFirmware":
        filename = filename_base_fota
        print("Base Firmware filename : => ", filename)
        firmwareVer = fileVer(self, filename_base_fota, "baseFirmware", baseFirmwareVerFlag_fota,
                              baseFirmwareVersion_fota)
        upload_url = presignedUrl(self, model, filename_base_fota, "fota", deviceType_IVI)
        uploadFile_fota(self, model, upload_url, filepath_base_fota, filename)
        isDiffImage = "false"
        isBase = "true"
        isFull = "false"

    if firmware == "updateFirmware":
        filename = filename_update_fota
        print("Diff/Update Firmware filename : => ", filename)
        firmwareVer = fileVer(self, filename_update_fota, "updateFirmware", diffFirmwareVerFlag_fota,
                              diffFirmwareVersion_fota)
        upload_url = presignedUrl(self, model, filename_update_fota, "fota", deviceType_IVI)
        uploadFile_fota(self, model, upload_url, filepath_update_fota, filename)
        isDiffImage = "true"
        isBase = "false"
        isFull = "false"

    if firmware == "baseFirmware_sota":
        filename = baseFirmwareFilename_sota
        print("Base Firmware filename : => ", filename)
        # firmwareVer = fileVer(self, filename_base_fota, "baseFirmware", baseFirmwareVerFlag_fota, baseFirmwareVersion_fota)
        upload_url = presignedUrl(self, model, baseFirmwareFilename_sota, "fota", deviceType_IVI)
        uploadFile(self, model, upload_url, baseFirmware_sota)
        isDiffImage = "false"
        isBase = "true"
        isFull = "false"

    response = FOTA_firmwareUpload(self, model, system_ivi_fota, releaseNotes_fota, isDiffImage, isBase, isFull,
                                   downloadConsent_fota, installConsent_fota, rebootConsent_fota, filename, firmwareVer,
                                   "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("uploadFirmware_" + firmware + '_' + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(14000):
        # print(response_body["responseData"]["message"])
        firmwareId = int(response_body["responseData"]["firmwareId"])
        testResult(self, "passed", "Firmware package should be uploaded successfully",
                   "Firmware package is uploaded successfully")

    elif response_body["responseCode"] == str(14048) or response_body["responseCode"] == str(14029):
        # print(response_body["responseData"]["message"])
        testResult(self, "passed", "Firmware package should be uploaded successfully",
                   "Firmware package already uploaded for this model or Model already has a base version : => " +
                   response_body["responseData"]["message"])
        firmwareId = 1
    elif response_body["responseCode"] != str(14000):
        if response_body["responseCode"] != str(14048):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Firmware package should be uploaded successfully",
                       "Firmware package is not uploaded successfully." + " Reason for failure is : " +
                       response_body["responseData"]["message"])

    else:
        print("Something went wrong")
    return firmwareId


def createFirmwareScript(self, onboarding_type, chipset_type):
    model = getModel(self, onboarding_type, chipset_type)
    random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
    ScriptName = "Firmware_" + random_id
    sourceVersion = fileVer(self, filename_base_fota, "baseFirmware", baseFirmwareVerFlag_fota,
                            baseFirmwareVersion_fota)
    targetVersion = fileVer(self, filename_update_fota, "updateFirmware", diffFirmwareVerFlag_fota,
                            diffFirmwareVersion_fota)
    # print(sourceVersion, targetVersion)

    # Act: convert dict to json by json.dumps() for body data and send POST request.

    response = FOTA_createScript(self, model, ScriptName, "startstop_0", ecuType_ivi_fota, sourceVersion, targetVersion,
                                 releaseNotes_fota, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("createFirmwareScript_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(14000):
        # print(response_body["responseData"]["message"])
        scriptId = str(response_body["responseData"]["scriptId"])
        testResult(self, "passed", "Firmware script should be created successfully",
                   ScriptName + " - Firmware script is created successfully")

    elif response_body["responseCode"] != str(14000):
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "Firmware script should be created successfully",
                   ScriptName + "- Firmware script is not created successfully" + " Reason for failure is : " +
                   response_body["responseData"]["message"])

    else:
        print("Something went wrong")
        assert False
    return scriptId


# SOTA Functions:

def uploadPackage(self, onboarding_type, chipset_type):
    packageId = 0
    model = getModel(self, onboarding_type, chipset_type)
    print("Model name for uploading package : => ", model)

    FileVer = sotaFileVer(self, packageNameFlag_sota, packageName_sota, packageVersionFlag_sota, packageVersion_sota,
                          filename_sota)
    print(FileVer, model, filename_sota)
    upload_url = presignedUrl(self, model, filename_sota, "sota", deviceType_IVI)
    uploadFile(self, model, upload_url, filepath_sota)
    isDiffImage = "true"
    isBase = "false"
    isFull = "false"

    response = SOTA_uploadPackage(self, model, system_ivi_sota, releaseNotes_sota, isDiffImage, isBase, isFull,
                                  downloadConsent_sota, installConsent_sota, rebootConsent_sota, filename_sota,
                                  str(FileVer[1]), "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("uploadPackage_" + model, str(response_body), "OTA")

    if response_body["responseCode"] == str(15000):
        # print(response_body["responseData"]["message"])
        packageId = int(response_body["responseData"]["packageId"])
        testResult(self, "passed", "SOTA Package should be uploaded successfully",
                   "SOTA package is uploaded successfully")

    elif response_body["responseCode"] == str(15040):
        # print(response_body["responseData"]["message"])
        testResult(self, "passed", "SOTA Package should be uploaded successfully",
                   "SOTA package already uploaded for this model")

    elif response_body["responseCode"] != str(15000):
        if response_body["responseCode"] != str(15040):
            # print(response_body["responseData"]["message"])
            # print("SOTA package is not uploaded successfully")
            testResult(self, "failed", "SOTA Package should be uploaded successfully",
                       "SOTA package is not uploaded successfully" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
    else:
        print("Something went wrong")
    return packageId


def createSOTAScript(self, command, onboarding_type, chipset_type):
    model = getModel(self, onboarding_type, chipset_type)
    scriptId = ''
    fileDetails = sotaFileVer(self, packageNameFlag_sota, packageName_sota, packageVersionFlag_sota,
                              packageVersion_sota, filename_sota)
    print(fileDetails)
    random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
    ScriptName = "SOTA_" + command + "_" + random_id

    precondition = get_preCondition_from_preconditionDetails_api(self)

    # Act: convert dict to json by json.dumps() for body data and send POST request.

    response = SOTA_CreateScript(self, model, ecuType_ivi_sota, ScriptName, command, fileDetails[0], fileDetails[1],
                                 releaseNotes_sota, precondition, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    saveAPIrespIntoFile("createSOTAScript_" + model + "_" + command, str(response_body), "OTA")
    # print(response_body)
    try:
        if response_body['responseCode'] == str(15000):
            # print("Message : ", response_body['responseData']['message'])
            scriptId = response_body['responseData']['scriptId']
            testResult(self, "passed", "SOTA script should be created successfully",
                       "SOTA script is created successfully")

        elif response_body['responseCode'] == str(15062) or response_body['responseCode'] == str(15006) or \
                response_body['responseCode'] != str(15000):
            testResult(self, "failed", "SOTA script should be created successfully",
                       "SOTA script is not created successfully. Reason for failure is :=> " +
                       response_body['responseData']['message'])
        else:
            testResult(self, "failed", "SOTA script should be created successfully",
                       "SOTA script is not created successfully. Reason for failure is :=> " +
                       response_body['responseData']['message'])
    except:
        print('\n')

    return scriptId


def start_OTAservices_on_drimaes_IVI(self, onboarding_type, chipset_type):
    try:
        run_otaServices_on_primary_IVI(self, onboarding_type, chipset_type)
        time.sleep(5)
    except:
        print("Something went wrong while ota service run")


def pull_OTA_sessionfile_from_drimaes_IVI(self, option):
    try:
        state = ''
        if option == "fota":
            subprocess.call(
                [drimaes_batchPath + 'C2C_pullFilesFromDevice.bat',
                 drimaes_ivi_adbSerialNo, "OTA"])
            otaSessionFile = C2CtestReport_otaPath + 'ivi_files\ota_session.json'

            with open(otaSessionFile, 'r') as file:
                json_data = json.load(file)
                state = json_data['session']['state']
        elif option == "sota":
            subprocess.call(
                [drimaes_batchPath + 'C2C_pullFilesFromDevice.bat',
                 drimaes_ivi_adbSerialNo, "SOTA"])
            sotaSessionFile = C2CtestReport_otaPath + 'ivi_files\sota_session.json'

            with open(sotaSessionFile, 'r') as file:
                json_data = json.load(file)
                state = json_data['session']['state']
    except:
        if option == "fota":
            print(
                "ota_session.json file is not pulled or updated or cleared post update, pls check logs & ota_manager service on device")
            print("Current state in ota_session json file is : ", state)
        elif option == "sota":
            print(
                "sota_session.json file is not pulled or updated or cleared post update, pls check logs & sota_manager service on device")
            print("Current state in sota_session json file is : ", state)
    print(state)
    return state


def get_firmware_version_from_drimaes_IVI(self):
    try:
        # get firmware Version
        firmware_ver = subprocess.run(
            [drimaes_batchPath + 'C2C_adbCommands.bat',
             drimaes_ivi_adbSerialNo, "firmwareVer"], capture_output=True, text=True, timeout=10)
        firmware_ver = firmware_ver.stdout
        current_slot = subprocess.run(
            [drimaes_batchPath + 'C2C_adbCommands.bat',
             drimaes_ivi_adbSerialNo, "currentSlot"], capture_output=True, text=True, timeout=10)
        current_slot = current_slot.stdout
        uname = subprocess.run(
            [drimaes_batchPath + 'C2C_adbCommands.bat',
             drimaes_ivi_adbSerialNo, "uname-a"], capture_output=True, text=True, timeout=60)
        uname = uname.stdout
        time.sleep(5)
    except subprocess.TimeoutExpired:
        print('Timeout')
    return firmware_ver, current_slot, uname


def check_OTA_status_drimaes_IVI(self, option):
    state = pull_OTA_sessionfile_from_drimaes_IVI(self, option)
    if state == "DOWNLOADING":
        print("Current state in session file is : ", state)
        print("Downloading is in progress")
        time.sleep(180)
    elif state == "downloadComplete":
        print("Current state in session file is : ", state)
        print("Download is complete")
        time.sleep(180)
    elif state == "INSTALLING":
        print("Current state in session file is : ", state)
        print("Installation is in progress")
        time.sleep(180)
    elif state == "installSuccess":
        print("Current state in session file is : ", state)
        print("Install is Success")
        time.sleep(180)
    elif state == "Rebooting":
        print("Current state in session file is : ", state)
        print("Firmware is installed on device but device is not rebooted yet")
        print("=> Waiting for device to be up post reboot")
        time.sleep(180)
        state = pull_OTA_sessionfile_from_drimaes_IVI(self, option)
        print("Current state in session file post device reboot is : ", state)
    return state


def check_FirwareVer_drimaes_IVI(self, option, onboarding_type, chipset_type):
    # rebootOrRunAsRoot(self, ivi_adbSerialNo, "root")
    if option == "beforeFOTAupdate":
        try:
            # pushOTAsessionFile(self, "fota")
            # get firmware Version
            firmwareVer_beforeFOTA = subprocess.call(
                [drimaes_batchPath + 'C2C_OTACommands.bat',
                 drimaes_ivi_adbSerialNo, "FOTA_before"], timeout=60)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('\n')

    elif option == "afterFOTAupdate":
        time.sleep(180)
        i = 1
        while i <= 20:
            state = check_OTA_status_drimaes_IVI(self, "fota")
            # print(state)
            if state == "Success" or state == "Rebooted" or state == None or state == 'Rebooting':
                rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
                time.sleep(60)
                set_network_connectivity_on_device(self, onboarding_type, drimaes_ivi_chipset, "WiFi")
                time.sleep(10)
                # runServices(self, onboarding_type)
                print('break')
                break
            else:
                time.sleep(180)
            i += 1
        try:
            time.sleep(180)
            state = check_OTA_status_drimaes_IVI(self, "fota")
            print(state)
            if state == 'Rebooting':
                rebootOrRunAsRoot(self, drimaes_ivi_adbSerialNo, "root")
                time.sleep(60)
                set_network_connectivity_on_device(self, onboarding_type, drimaes_ivi_chipset, "WiFi")
                time.sleep(10)
                # runServices(self, onboarding_type)
            firmwareVer_beforeFOTA = subprocess.call(
                [drimaes_batchPath + 'C2C_OTACommands.bat',
                 drimaes_ivi_adbSerialNo, "FOTA_after"], timeout=10)
        except subprocess.TimeoutExpired:
            print('\n')
        with open(C2CtestReport_otaPath + r'beforeOTA\ver_info.txt',
                  "r") as file:
            json_data = json.load(file)
            Meta_Build_ID_beforeFOTAupdate = json_data['Metabuild_Info']['Meta_Build_ID']
            Version_beforeFOTAupdate_ver = json_data['Version']

        currentSlot_beforeFOTAupdate = \
            open(C2CtestReport_otaPath + r'beforeOTA\currentSlot.txt',
                 "r").read()
        currentSlot_afterFOTAupdate = \
            open(C2CtestReport_otaPath + r'afterOTA\currentSlot.txt',
                 "r").read()
        uname_beforeFOTAupdate = \
            open(C2CtestReport_otaPath + r'beforeOTA\uname-a.txt',
                 "r").read()
        uname_afterFOTAupdate = \
            open(C2CtestReport_otaPath + r'afterOTA\uname-a.txt',
                 "r").read()
        with open(C2CtestReport_otaPath + r'afterOTA\ver_info.txt',
                  "r") as file:
            json_data = json.load(file)
            Meta_Build_ID_afterFOTAupdate = json_data['Metabuild_Info']['Meta_Build_ID']
            Version_afterFOTAupdate_ver = json_data['Version']

        print("=======================================================================================================")
        print('-------------------------------------------------')
        print("Device Side Details Before & After FOTA Update : ")
        print('-------------------------------------------------')
        # print('\n')
        print("BEFORE FOTA UPDATE : ")
        print('---------------------')
        print("Firmware - Metabuild ID before FOTA update : ", Meta_Build_ID_beforeFOTAupdate)
        print("Firmware - Version before FOTA update : ", Version_beforeFOTAupdate_ver)
        print("Firmware - details before FOTA update : ", uname_beforeFOTAupdate)
        print("Current Slot before FOTA update : ", currentSlot_beforeFOTAupdate)
        # print('\n')
        print('---------------------')
        print("AFTER FOTA UPDATE :  ")
        print('---------------------')
        print("Firmware - Metabuild ID after FOTA update : ", Meta_Build_ID_afterFOTAupdate)
        print("Firmware - Version before FOTA update : ", Version_afterFOTAupdate_ver)
        print("Firmware - details after FOTA update : ", uname_afterFOTAupdate)
        print("Current Slot after FOTA update : ", currentSlot_afterFOTAupdate)

        print('---------------------------------------')
        print("Device Side Final E2E Validation Results : ")
        print('---------------------------------------')
        # print('\n')
        if currentSlot_beforeFOTAupdate == currentSlot_afterFOTAupdate:
            time.sleep(180)

        if Meta_Build_ID_beforeFOTAupdate != Meta_Build_ID_afterFOTAupdate or Version_beforeFOTAupdate_ver != Version_afterFOTAupdate_ver or uname_beforeFOTAupdate != uname_afterFOTAupdate:
            testResult(self, "passed", "Firmware Metabuild Id/Version/details should be updated successfully on device",
                       "Firmware Metabuild Id/Version/details is updated successfully on device")
        else:
            testResult(self, "verificationFailed",
                       "Firmware Metabuild/Version/details should be updated successfully on device",
                       "Firmware Metabuild Id/Version/details is not updated on device")

        if currentSlot_beforeFOTAupdate != currentSlot_afterFOTAupdate:
            testResult(self, "passed", "Current slot should be updated successfully on device",
                       "Current slot is updated successfully on device")
        else:
            testResult(self, "verificationFailed", "Current slot should be updated successfully on device",
                       "Current slot is not updated on device")

        # print('\n')
        print("=======================================================================================================")
        print('-------------------------------------------------')
        print("Cloud Side Final E2E Validation Results :            ")
        print('-------------------------------------------------')
        # print('\n')
        scheduleId = read_scheduleId(self, "fota")
        percentages = listFirmwareSchedules(self, scheduleId, onboarding_type, chipset_type)
        status = percentages[0]
        offered = percentages[1]
        accepted = percentages[2]
        complete = percentages[3]

        if status == "SUCCESS":
            testResult(self, "passed", "Status should be 'SUCCESS' on SMP UI -> Updates -> Firmware Updates Page",
                       "Status is " + status + " on SMP UI -> Updates -> Firmware Updates Page")
        else:
            testResult(self, "failed", "Status should be 'SUCCESS' on SMP UI -> Updates -> Firmware Updates Page",
                       "Status is " + status + " on SMP UI -> Updates -> Firmware Updates Page")
        if float(offered) != float(0.0):
            testResult(self, "passed",
                       "Offered Status should be '100%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Offered is " + str(
                           int(offered)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")
        else:
            testResult(self, "failed",
                       "Offered Status should be '100%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Offered Status is " + str(
                           int(offered)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")
        if float(accepted) == float(0.0):
            testResult(self, "passed",
                       "Accepted Status should be '0%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Accepted Status is " + str(
                           int(accepted)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")
        else:
            testResult(self, "failed",
                       "Accepted Status should be '0%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Accepted Status is " + str(
                           int(accepted)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")
        if float(complete) == float(100.0):
            testResult(self, "passed",
                       "Complete Status should be '100%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Complete Status is " + str(
                           int(complete)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")
            status1 = listFirmwareScheduleStatus(self, onboarding_type, chipset_type)
            print('-------------------------------------------------')
            print('Firmware Update Status : ')
            print('-------------------------------------------------')
            if status1 == "SUCCESS":

                testResult(self, "passed", "Firmware Status for desired VIN on SMP UI should be 'SUCCESS'",
                           "Firmware Status for desired VIN on SMP UI is " + status1 + " ")
            else:
                testResult(self, "failed", "Firmware Status for desired VIN on SMP UI should be 'SUCCESS'",
                           "Firmware Status for desired VIN is on SMP UI  " + status1 + "  ")
        else:
            status1 = listFirmwareScheduleStatus(self, onboarding_type, chipset_type)
            print('-------------------------------------------------')
            print('Firmware Update Status : ')
            print('-------------------------------------------------')
            if status1 == "SUCCESS":

                testResult(self, "passed", "Firmware Status for desired VIN on SMP UI should be 'SUCCESS'",
                           "Firmware Status for desired VIN on SMP UI is " + status1 + " ")
            else:
                testResult(self, "verificationFailed", "Firmware Status for desired VIN on SMP UI should be 'SUCCESS'",
                           "Firmware Status for desired VIN is on SMP UI  " + status1 + "  ")

            testResult(self, "failed",
                       "Complete Status should be '100%' on SMP UI -> Updates -> Firmware Updates Page",
                       "Complete Status is " + str(
                           int(complete)) + '%' + " on SMP UI -> Updates -> Firmware Updates Page")

        print("=======================================================================================================")


def checkPackage(self, option, command, onboarding_type, chipset_type):
    # rebootOrRunAsRoot(self, ivi_adbSerialNo, "root")
    if onboarding_type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        batchPath = drimaes_batchPath
        adbSerialNo = drimaes_ivi_adbSerialNo
    if option == "beforeSOTAupdate":
        try:
            # pushOTAsessionFile(self, "sota")
            time.sleep(10)
            # get package list
            package_beforeSOTA = subprocess.call(
                [batchPath + 'C2C_OTACommands.bat',
                 adbSerialNo, "SOTA_before", command], timeout=10)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('Timedout')
        except:
            print('Something went wrong')
    elif option == "afterSOTAupdate":
        time.sleep(30)
        state = check_OTA_status_drimaes_IVI(self, "sota")
        time.sleep(30)
        i = 1
        while i >= 10:
            state = check_OTA_status_drimaes_IVI(self, "sota")
            print(state)
            if state != "Success" or state != "Rebooted":
                # print(i)
                time.sleep(60)
                state = check_OTA_status_drimaes_IVI(self, "sota")
            else:
                break
            i += 1
        else:
            print("\n")
        try:
            # get package list
            package_afterSOTA = subprocess.call(
                [batchPath + 'C2C_OTACommands.bat',
                 adbSerialNo, "SOTA_after", command], timeout=10)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('Timedout')
        except:
            print('Something went wrong')

        packageList_beforeSOTAupdate = C2CtestReport_otaPath + 'beforeOTA' + "\\" "appList" + "_" + command + ".txt"
        appName = str(filename_sota).split('_')
        appName = str(appName[0])
        appCheckStatus_beforeSOTAupdate = appCheck(self, packageList_beforeSOTAupdate, appName)
        try:
            appCheckStatus_beforeSOTAupdate = appCheckStatus_beforeSOTAupdate.split(' ')
            appStatus_beforeSOTAupdate = str(appCheckStatus_beforeSOTAupdate[0])
            appName_beforeSOTAupdate = str(appCheckStatus_beforeSOTAupdate[1])
            # print(appStatus_beforeSOTAupdate, appName_beforeSOTAupdate)
        except:
            appName_beforeSOTAupdate = ''

        packageList_afterSOTAupdate = C2CtestReport_otaPath + 'afterOTA' + "\\" "appList" + "_" + command + ".txt"

        appCheckStatus_afterSOTAupdate = appCheck(self, packageList_afterSOTAupdate, appName)
        try:
            appCheckStatus_afterSOTAupdate = appCheckStatus_afterSOTAupdate.split(' ')
            appStatus_afterSOTAupdate = str(appCheckStatus_afterSOTAupdate[0])
            appName_afterSOTAupdate = str(appCheckStatus_afterSOTAupdate[1])
        except:
            appName_afterSOTAupdate = ''
        # print(appStatus_afterSOTAupdate,appName_afterSOTAupdate)

        packageList_beforeSOTAupdate = open(
            C2CtestReport_otaPath + 'beforeOTA' + "\\" "appList" + "_" + command + ".txt",
            "r").readlines()
        packageList_beforeSOTAupdate = str(packageList_beforeSOTAupdate).replace('\n', '')
        # print(packageList_beforeSOTAupdate)
        packageList_afterSOTAupdate = \
            open(
                C2CtestReport_otaPath + 'afterOTA' + "\\" "appList" + "_" + command + ".txt",
                "r").readlines()
        packageList_afterSOTAupdate = str(packageList_afterSOTAupdate).replace('\n', '')
        # print(packageList_afterSOTAupdate)

        status1 = listPackageScheduleStatus(self, onboarding_type, chipset_type)
        status1 = status1[0]
        appNamefromCloud = str(status1[1])

        print("=======================================================================================================")
        print('-------------------------------------------------')
        print("Device Side Details Before & After SOTA Update : ")
        print('-------------------------------------------------')
        # print('\n')
        print("BEFORE SOTA - " + command + " UPDATE : ")
        print('-------------------------------------------------')
        # print("package list before SOTA update : ", appName_beforeSOTAupdate)
        if command == "INSTALL":
            if appName == appName_beforeSOTAupdate or appName in packageList_beforeSOTAupdate:
                print("Package : " + appName + ' is already available on device')
            else:
                print("Package : " + appName + ' is not available on device')
        # print('\n')
        if command == "START" or command == "STOP" or command == "UNINSTALL":
            if appName == appName_beforeSOTAupdate or appName in packageList_beforeSOTAupdate:
                print("Package : " + appName + ' is available on device with ' + appStatus_beforeSOTAupdate + " status")
            else:
                print("Package : " + appName + ' is not available on device')
        print('-------------------------------------')
        print("AFTER SOTA - " + command + " UPDATE : ")
        # print('-------------------------------------')
        # print("package list after SOTA update : ", appName_afterSOTAupdate)
        # print("State in sota_session.json file after SOTA update is :", state)
        # print('---------------------------------------')
        print("Device Side Final E2E Validation Results : ")
        print('---------------------------------------')
        if command == "INSTALL":

            if appName in packageList_afterSOTAupdate or appStatus_afterSOTAupdate in packageList_afterSOTAupdate:

                print("Installed package name is : ", appName)

                testResult(self, "passed",
                           "sota_session.json file should be cleared and deleted",
                           "sota_session.json file is cleared and deleted")

                if appName in appStatus_afterSOTAupdate:

                    testResult(self, "passed",
                               "Package : " + appName + " should be installed successfully on device",
                               "Package : " + appName + " is installed & listed successfully with " + appStatus_afterSOTAupdate)
                else:
                    testResult(self, "failed",
                               "Package : " + appName + " should be installed successfully on device with 'stopped' status",
                               "Package : " + appName + " is not installed on device " + appStatus_afterSOTAupdate)

            else:
                testResult(self, "failed",
                           "Package : " + appName + " should be installed successfully on device",
                           "Package : " + appName + " is not installed successfully on device")
                testResult(self, "failed",
                           "sota_session.json file should be cleared or updated with Success/Rebooted state on device",
                           "sota_session.json file is not cleared or updated with Success/Rebooted state on device")

        if command == "START":
            if "running" in appStatus_afterSOTAupdate:

                testResult(self, "passed",
                           "Package : " + appName + " should be in 'running' mode/status",
                           "Package : " + appName + " is listed with " + appStatus_afterSOTAupdate + ' status on device')
            else:
                testResult(self, "failed",
                           "Package : " + appName + " should be listed with 'running' status",
                           "Package : " + appName + " is not listed with 'running' status. Rather displayed with " + appStatus_afterSOTAupdate + ' status on device')
        if command == "STOP":
            if "stopped" in appStatus_afterSOTAupdate:

                testResult(self, "passed",
                           "Package : " + appName + " should be in 'stopped' mode/status",
                           "Package : " + appName + " is listed with " + appStatus_afterSOTAupdate + ' status on device')
            else:
                testResult(self, "failed",
                           "Package : " + appName + " should be listed with 'stopped' status",
                           "Package : " + appName + " is not listed with 'stopped' status. Rather displayed with " + appStatus_afterSOTAupdate + ' status on device')

        if command == "UNINSTALL":
            if appName != appName_afterSOTAupdate and appName not in packageList_afterSOTAupdate:

                # print("Uninstalled package name is : ", appName_afterSOTAupdate)

                testResult(self, "passed",
                           "Package : " + appName + " should be uninstalled successfully on device",
                           "Package : " + appName + " is uninstalled successfully on device")

            else:
                testResult(self, "failed",
                           "Package : " + appName + " should be uninstalled successfully on device",
                           "Package : " + appName + " is not uninstalled successfully on device, rather displayed/listed with " + appStatus_afterSOTAupdate + " status")

        # print('\n')
        print("=======================================================================================================")
        print('-------------------------------------------------')
        print("Cloud Side Final E2E Validation Results :            ")
        print('-------------------------------------------------')
        # print('\n')
        scheduleId = read_scheduleId(self, "sota")
        percentages = listPackageSchedules(self, scheduleId, onboarding_type, chipset_type)
        status = percentages[0]
        offered = percentages[1]
        accepted = percentages[2]
        complete = percentages[3]

        if status == "SUCCESS":
            testResult(self, "passed",
                       "Status should be 'SUCCESS' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Status is " + status + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        else:
            testResult(self, "failed",
                       "Status should be 'SUCCESS' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Status is " + status + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        if float(offered) != float(0.0):
            testResult(self, "passed",
                       "Offered Status should be '100%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Offered is " + str(
                           int(offered)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        else:
            testResult(self, "failed",
                       "Offered Status should be '100%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Offered Status is " + str(
                           int(offered)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        if float(accepted) == float(0.0):
            testResult(self, "passed",
                       "Accepted Status should be '0%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Accepted Status is " + str(
                           int(accepted)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        else:
            testResult(self, "failed",
                       "Accepted Status should be '0%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Accepted Status is " + str(
                           int(accepted)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        if float(complete) == float(100.0):
            testResult(self, "passed",
                       "Complete Status should be '100%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Complete Status is " + str(
                           int(complete)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")
        else:
            testResult(self, "failed",
                       "Complete Status should be '100%' on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page",
                       "Complete Status is " + str(
                           int(complete)) + '%' + " on SMP UI-> Updates -> OTA -> OTA Updates -> SOTA page")

        print('-------------------------------------------------')
        print('Pacakge Update Status : ')
        print('-------------------------------------------------')
        if "SUCCESS" in status1:
            testResult(self, "passed", "Pacakge update status for desired VIN on SMP UI should be 'SUCCESS'",
                       "Package update status for desired VIN on SMP UI is " + status1 + " ")
        else:
            testResult(self, "failed", "Package update status for desired VIN on SMP UI should be 'SUCCESS'",
                       "Package update status for desired VIN is on SMP UI  " + status1 + "  ")
        try:
            # get logs
            subprocess.call(
                [drimaes_batchPath + 'C2C_pullFilesFromDevice.bat',
                 drimaes_ivi_adbSerialNo, "OTAlogs"], timeout=10)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('Timedout')
        except:
            print('Something went wrong')

        print("=======================================================================================================")


def startOTAservices(self, option):
    try:
        subprocess.run(
            [drimaes_batchPath + 'C2C_startServicesOnDevices.bat',
             drimaes_ivi_adbSerialNo, option], timeout=10)
    except subprocess.TimeoutExpired:
        print('\n')
