import base64
import datetime
import os.path
import shutil
import subprocess

from C2CModules.deviceRegistration_modules import *
from C2CModules.e2e_testData import *
from C2CModules.smpServer_modules import *


# ===================================
# Core C2C modules
# ===================================

def deviceOnboardingType(self, onboardingType):
    try:
        if onboardingTypeFlag == "No":
            singleDeviceOnboarding_TCU = "No"
            comboDeviceOnboarding_TCUVT_fusion = "No"
            comboDeviceOnboarding_TCUIVI = "No"
            comboDeviceOnboarding_TCUVT = "No"
            comboDeviceOnboarding_TCUIVIVT = "No"
            comboDeviceOnboarding_TCUVTIVI_fusion = "No"
            singleDeviceOnboarding_IVI = "No"

            if onboardingType == deviceType_TCU:
                singleDeviceOnboarding_TCU = "Yes"
            if onboardingType == deviceType_IVI:
                singleDeviceOnboarding_IVI = "Yes"
            elif onboardingType == "TCUIVI":
                comboDeviceOnboarding_TCUIVI = "Yes"
            elif onboardingType == "TCUVT_fusion":
                comboDeviceOnboarding_TCUVT_fusion = "Yes"
            elif onboardingType == "TCUVT_nonfusion":
                comboDeviceOnboarding_TCUVT = "Yes"
            elif onboardingType == "TCUIVIVT":
                comboDeviceOnboarding_TCUIVIVT = "Yes"
            elif onboardingType == "TCUVTIVI_fusion":
                comboDeviceOnboarding_TCUVTIVI_fusion = "Yes"
            else:
                print(f"Invalid  onboarding type")
        elif onboardingTypeFlag == "Yes":
            singleDeviceOnboarding_TCU = testData("DeviceOnboardingData", 3, 2)
            singleDeviceOnboarding_IVI = testData("DeviceOnboardingData", 3, 2)
            comboDeviceOnboarding_TCUVT_fusion = testData("DeviceOnboardingData", 4, 2)
            comboDeviceOnboarding_TCUIVI = testData("DeviceOnboardingData", 5, 2)
            comboDeviceOnboarding_TCUVT = testData("DeviceOnboardingData", 6, 2)
            comboDeviceOnboarding_TCUIVIVT = testData("DeviceOnboardingData", 7, 2)
            comboDeviceOnboarding_TCUVTIVI_fusion = "No"
    except:
        print("Something Went Wrong! or Invalid  onboarding type")
        assert False
    return singleDeviceOnboarding_TCU, comboDeviceOnboarding_TCUIVI, comboDeviceOnboarding_TCUVT_fusion, comboDeviceOnboarding_TCUVT, comboDeviceOnboarding_TCUIVIVT, comboDeviceOnboarding_TCUVTIVI_fusion, singleDeviceOnboarding_IVI


# ===================================
# Delete folder & files
# ===================================

def deleteFiles(self, dirPath):
    try:
        for files in os.listdir(dirPath):
            path = os.path.join(dirPath, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
    except:
        print(f"Folder/File does not exist or failed to remove file(s)")


def deleteFoldersForUpdate(self, option):
    try:
        src_dir = C2CtestReport_exeBackupPath + option + '\\'
        finalPath_api = os.path.join(src_dir, 'API_Responses')
        deleteFiles(self, finalPath_api)
        finalPath_tcu = os.path.join(src_dir, tcu_files)
        deleteFiles(self, finalPath_tcu)
        finalPath_vt = os.path.join(src_dir, vt_files)
        deleteFiles(self, finalPath_vt)
        finalPath_ivi = os.path.join(src_dir, ivi_files)
        deleteFiles(self, finalPath_ivi)
        if option == "OTA":
            finalPath = os.path.join(src_dir, 'beforeOTA')
            deleteFiles(self, finalPath)
            finalPath = os.path.join(src_dir, 'afterOTA')
            deleteFiles(self, finalPath)
    except:
        print(f"Folder does not exist or failed to remove desired folder(s)")


def deleteLicenseFolderForUpdate(self, device, option):
    if device == deviceType_TCU:
        folder = tcu_files
    elif device == deviceType_VT:
        folder = vt_files
    elif device == deviceType_IVI:
        folder = ivi_files
        rebootDevice(self, ivi_adbSerialNo, "reboot")
        time.sleep(10)
        rebootDevice(self, ivi_adbSerialNo, "root")
        time.sleep(5)
    else:
        print(f"Invalid device type to remove license folder")

    try:
        if option == SKUupdateByVIN_option:
            shutil.rmtree(
                C2CtestReport_SKUupdateByVINPath + folder + '\licenses')
        elif option == SKUupdateByGroup_option:
            shutil.rmtree(
                C2CtestReport_SKUupdateByGroupPath + folder + '\licenses')
        elif option == FeatureUpdateByGroup_option:
            shutil.rmtree(
                C2CtestReport_FeatureUpdateByGroupPath + folder + '\licenses')
    except:
        print(f"Folder does not exist or failed to remove license folder(s)")


# ============================================================
# Pull/Fetch files from device for validations
# ============================================================

def pullFilesFromDevice(self, option, onboarding_Type):
    try:
        # print("Fetch/Pull files from device for validation & backup : ")
        # print("\n-------------------------------------------------------------")
        onboardingType = deviceOnboardingType(self, onboarding_Type)
        singleDeviceOnboarding_TCU = str(onboardingType[0])
        comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
        comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
        comboDeviceOnboarding_TCUVT = str(onboardingType[3])
        comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
        comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
        if option == DeviceOnboarding_tcuvt_fusion_option or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            subprocess.call([C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat', vt_adbSerialNo,
                             DeviceOnboarding_tcuvt_fusion_option])

        elif option == DeviceOnboarding_tcuvt_option or option == SKUupdateByVIN_vt_option or option == SKUupdateByGroup_vt_option or option == FeatureUpdateByGroup_vt_option:
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                 vt_adbSerialNo,
                 option])

        else:
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                 tcu_adbSerialNo,
                 option])
            if comboDeviceOnboarding_TCUVT == "Yes":
                subprocess.call(
                    [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                     vt_adbSerialNo,
                     DeviceOnboarding_tcuvt_option])

        if comboDeviceOnboarding_TCUIVIVT == "Yes":
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                 vt_adbSerialNo,
                 DeviceOnboarding_tcuvt_option])
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                 tcu_adbSerialNo,
                 DeviceOnboarding_option])
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat',
                 ivi_adbSerialNo,
                 DeviceOnboarding_ivi_option])
        time.sleep(10)
        if comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat', ivi_adbSerialNo, DeviceOnboarding_ivi_option])

        if option == DeviceOnboarding_tcuvt_fusion_skuVIN_option:
            subprocess.call([C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat', vt_adbSerialNo,
                             DeviceOnboarding_tcuvt_fusion_skuVIN_option])
        if option == DeviceOnboarding_tcuvt_fusion_skuGrp_option:
            subprocess.call([C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat', vt_adbSerialNo,
                             DeviceOnboarding_tcuvt_fusion_skuGrp_option])
        if option == DeviceOnboarding_tcuvt_fusion_FeatUp_option:
            subprocess.call([C2CtestData_batchPath + r'C2C_pullFilesFromDevice.bat', vt_adbSerialNo,
                             DeviceOnboarding_tcuvt_fusion_FeatUp_option])

    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_pullFilesFromDevice.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while fetching/pulling files from device")


# ==============================================================
# Get License details fetched from device fro invalid scenarios
# ==============================================================

def licenseFileCheck(self, val, path):
    # print("\n=============================================================")
    print("License files : =>")
    print("-----------------------------")
    max_file = m_ti = max_file1 = ''
    try:
        file_type = r'\*pfm'
        files = glob.glob(path + file_type)
        directory = os.listdir(path)
        print(directory)
        if len(directory) == 0:
            # print(f"Empty directory")
            fileExist = False
        else:
            # print(f"Not empty directory")
            fileExist = True
        if fileExist == True:
            max_file = max(files, key=os.path.getctime)
            # print(max_file)
            max_file1 = max_file

            # Both the variables would contain time
            # elapsed since EPOCH in float
            ti_c = os.path.getctime(max_file)
            ti_m = os.path.getmtime(max_file)

            # Converting the time in seconds to a timestamp
            c_ti = time.ctime(ti_c)
            m_ti = time.ctime(ti_m)
            print("\n")
            if val == "LicenseFile":
                print(
                    f"\nThe license file located at the path {path} was created at {c_ti} and was last modified at {m_ti} ")
                max_file = max_file.replace(path, '')
                max_file = max_file.replace(c_ti, '')
                assert True
            elif val == "NoLicenseFile":
                print(
                    f"\nThe license file located at the path {path} was created at {c_ti} and was last modified at {m_ti} ")
                assert False
        else:
            if val == "LicenseFile":
                max_file = 'No license file  exists'
                m_ti = ''
                print("\n")
                print(f"No license file exists")
                assert False
            elif val == "NoLicenseFile":
                max_file = 'No license file  exists'
                m_ti = ''
                print("\n")
                print(f"No license file exists")
                assert True
    except:
        max_file = m_ti = max_file1 = ''
        print("Something went wrong while reading license files")
    return max_file, m_ti, max_file1


def getLicenseDetails(self, val, tc, onboarding_Type):
    max_file1 = ''
    try:
        if tc == DeviceOnboarding_option:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)
            path = C2CtestReport_exeBackupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)
        elif tc == DeviceOnboarding_tcuvt_option:
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_option, onboarding_Type)
            path = C2CtestReport_exeBackupPath + vt_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        if tc == DeviceOnboarding_tcuvt_fusion_option:
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_option, onboarding_Type)
            path = C2CtestReport_exeBackupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == DeviceOnboarding_tcuvt_fusion_skuVIN_option:
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_skuVIN_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByVINPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == DeviceOnboarding_tcuvt_fusion_skuGrp_option:
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_skuGrp_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByGroupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == DeviceOnboarding_tcuvt_fusion_FeatUp_option:
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_FeatUp_option, onboarding_Type)
            path = C2CtestReport_FeatureUpdateByGroupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == SKUupdateByGroup_option:
            pullFilesFromDevice(self, SKUupdateByGroup_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByGroupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == FeatureUpdateByGroup_option:
            pullFilesFromDevice(self, FeatureUpdateByGroup_option, onboarding_Type)
            path = C2CtestReport_FeatureUpdateByGroupPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == SKUupdateByVIN_vt_option:
            pullFilesFromDevice(self, SKUupdateByVIN_vt_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByVINPath + vt_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == SKUupdateByGroup_vt_option:
            pullFilesFromDevice(self, SKUupdateByGroup_vt_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByGroupPath + vt_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == FeatureUpdateByGroup_vt_option:
            pullFilesFromDevice(self, FeatureUpdateByGroup_vt_option, onboarding_Type)
            path = C2CtestReport_FeatureUpdateByGroupPath + vt_files + '\licenses'
            ls = licenseFileCheck(self, val, path)

        elif tc == SKUupdateByVIN_option:
            pullFilesFromDevice(self, SKUupdateByVIN_option, onboarding_Type)
            path = C2CtestReport_SKUupdateByVINPath + tcu_files + '\licenses'
            ls = licenseFileCheck(self, val, path)
    except:
        ls = []
        ls[0] = ls[1], ls[2] = "No file"
        print(
            "No license file present or error occured while fetching license file, check license folder & logs")
    return ls[0], ls[1], ls[2]


# =========================================
# Save API response in a file
# =========================================

def saveAPIrespIntoFile(filename, response, tc):
    try:
        if tc == DeviceOnboarding_option:
            reportpath = C2CtestReport_DeviceOnbrdng_backupPath + 'API_Responses' + '\\'

        elif tc == SKUupdateByGroup_option:
            reportpath = C2CtestReport_SKUupdateByGroupPath + 'API_Responses' + '\\'

        elif tc == FeatureUpdateByGroup_option:
            reportpath = C2CtestReport_FeatureUpdateByGroupPath + 'API_Responses' + '\\'

        elif tc == SKUupdateByVIN_option:
            reportpath = C2CtestReport_SKUupdateByVINPath + 'API_Responses' + '\\'

        elif tc == "OTA":
            reportpath = C2CtestReport_otaPath + 'API_responses' + '\\'

        else:
            reportpath = C2CtestReport_APIresponsesPath

        file = open(reportpath + filename + "_resp" + ".txt", "w")
        file.write(response)
        file.close()
    except FileNotFoundError:
        print(f"Sorry, the file does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while saving API response into file")


# ======================================================================================
# Replace default value with required value in c2c config files for device onboarding
# ======================================================================================
def convert2unix(filename):
    text = open(filename, 'rb').read()
    open(filename, 'wb').write(text)


def replaceLineWithText(self, filepath, oldtext, replacedtext):
    try:
        # READ FILE
        filename = glob.glob(filepath)
        filename = max(filename, key=os.path.getctime)
        df = open(filename)
        # read file
        read = df.read()
        # return cursor to the beginning of the file.
        df.seek(0)
        read
        # create empty list
        arr = []
        # count number of lines in the file
        line = 1
        for word in read:
            if word == '\n':
                line += 1
        # print("Number of lines in file is: ", line)
        for i in range(line):
            # readline() method, reads one line at a time
            arr.append(df.readline())
        for i in range(len(arr)):
            if oldtext in arr[i]:
                i + 1
                linenumb = i
                break
        # print(linenumb)
        with open(filename, 'r') as givenfilecontent:
            filelines = givenfilecontent.readlines()
            replacedtext = replacedtext
            filelines[linenumb] = replacedtext + '\n'
            # print(filelines)
        with open(filename, 'w') as givenfilecontent:
            givenfilecontent.writelines(filelines)
        givenfilecontent.close()
        convert2unix(filename)
        print(f' => The {oldtext} contain linenumber = ', linenumb, ' is replaced with {', replacedtext,
              '} in ',
              filename)
    except FileNotFoundError:
        print(f"Sorry, the {filename} conf file does not exist or incorrect file path/name")
    except:
        print(f"Error while updating {filename} conf files")


def inplace_change(filename, old_string, new_string):
    try:
        # Safely read the input filename using 'with'
        filename = glob.glob(filename)
        filename = max(filename, key=os.path.getctime)
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                print(f'{old_string} not found in {filename}.'.format(**locals()))
                return
        # Safely write the changed content, if found in the file
        with open(filename, 'w') as f:
            print(f'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
            s = s.replace(old_string, new_string)
            f.write(s)
            f.close()
        convert2unix(filename)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist or incorrect file path/name")
    except:
        print("Error while updating conf files")


# ============================================================
# Stop services on device
# ============================================================

def stopC2Cservices(self, deviceSerialNo, deviceType):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_stopServicesOnDevices.bat',
             deviceSerialNo, deviceType])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_stopServicesOnDevices.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while stopping c2c services")


# ============================================================
# reboot/remount device
# ============================================================

def rebootDevice(self, deviceSerialNo, option):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_adbCommands.bat',
             deviceSerialNo, option])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while rebooting device")


# ============================================================
# Copy default files
# ============================================================

def copyDefaultFiles(self, deviceOnbordingType):
    try:
        if spvalidationFlag != "Yes":
            print(
                f" => SP Validation flag is set  to {spvalidationFlag}, thus conf files are replaced with deafult confiles")
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_copydefaultFiles.bat',
                 deviceOnbordingType])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")
    try:
        if spvalidationFlag == "Yes":
            print(
                f"=> SP Validation flag is set  to {spvalidationFlag}, thus conf files are fetched/pulled from flashed metabuild on device")
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_copydefaultFiles_SPvalidation.bat',
                 deviceOnbordingType, tcu_adbSerialNo, ivi_adbSerialNo, vt_adbSerialNo])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_copydefaultFiles_SPvalidation.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while copying default conf files for updation")


# ============================================================
# CleanUp and copy default files for fresh device onboarding
# ============================================================

def cleanUpScript(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    print("============================================================\n")
    print("Set up device for fresh onboarding : \n")
    if onboardingTypeFlag == "Yes":
        print(
            f"=> Device Onboard/Provision Flag is set to {onboardingTypeFlag}, thus reads onboarding type from c2cTestData-> DeviceOnboardingData")
    else:
        print(
            f"=> Device Onboard/Provision Flag is set to {onboardingTypeFlag}, thus device is onbaorded based on selected test case")
    if singleDeviceOnboarding_TCU == "Yes":
        print("=> Device Onboard/Provision option selected : Standalone TCU Onboarding/Provisioning ")
    elif comboDeviceOnboarding_TCUIVI == "Yes":
        print("=> Device Onboard/Provision option selected : Combo TCU+IVI Onboarding/Provisioning ")
    elif comboDeviceOnboarding_TCUVT_fusion == "Yes":
        print("=> Device Onboard/Provision option selected : Combo TCU+VT fusion Onboarding/Provisioning ")
    elif comboDeviceOnboarding_TCUVT == "Yes":
        print("=> Device Onboard/Provision option selected : Combo TCU+VT non-fusion Onboarding/Provisioning ")
    elif comboDeviceOnboarding_TCUIVIVT == "Yes":
        print("=> Device Onboard/Provision option selected : Combo non-fusion (TCU+VT)+IVI Onboarding/Provisioning ")
    elif comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("=> Device Onboard/Provision option selected : Combo fusion (TCU+VT)+IVI Onboarding/Provisioning ")
    else:
        print(f"Invalid  onboarding type")
    print("============================================================\n")

    # Remove/Delete all old files & logs.
    deleteFoldersForUpdate(self, "DeviceOnboarding_backup")
    deleteFoldersForUpdate(self, "OTA")

    # Clean up all old logs and replace conf with default ones.
    if singleDeviceOnboarding_TCU == "Yes":
        copyDefaultFiles(self, deviceType_TCU)
    elif comboDeviceOnboarding_TCUVT_fusion == "Yes":
        copyDefaultFiles(self, "TCUVT_fusion")
    elif comboDeviceOnboarding_TCUIVI == "Yes":
        copyDefaultFiles(self, "TCUIVI")
    elif comboDeviceOnboarding_TCUVT == "Yes":
        copyDefaultFiles(self, "TCUVT")
    elif comboDeviceOnboarding_TCUIVIVT == "Yes":
        copyDefaultFiles(self, "TCUIVIVT")
    elif comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        copyDefaultFiles(self, "TCUIVIVT_fusion")
    else:
        print("Incorrect input")

    if singleDeviceOnboarding_TCU == "Yes" or comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUVT == "Yes":
        stopC2Cservices(self, tcu_adbSerialNo, deviceType_TCU)

        if comboDeviceOnboarding_TCUIVI == 'Yes':
            stopC2Cservices(self, ivi_adbSerialNo, deviceType_IVI)
            rebootDevice(self, ivi_adbSerialNo, "reboot")

        if comboDeviceOnboarding_TCUVT == 'Yes':
            rebootDevice(self, vt_adbSerialNo, "reboot")
            time.sleep(10)
            stopC2Cservices(self, vt_adbSerialNo, deviceType_VT)
    else:
        print(f"Select correct option for device onboarding")
    print("## Setting up device(s) for fresh onbaording/provision ##")


# ============================================================
# Push files on device function
# ============================================================

def pushFilesOnDevices(self, onboarding_Type):
    try:
        onboardingType = deviceOnboardingType(self, onboarding_Type)
        singleDeviceOnboarding_TCU = str(onboardingType[0])
        comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
        comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
        comboDeviceOnboarding_TCUVT = str(onboardingType[3])
        comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
        comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
        time.sleep(5)
        if singleDeviceOnboarding_TCU == "Yes" or comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes":
            if pushBinariesLibrariesOnTCU == "Yes":
                subprocess.call(
                    [C2CtestData_batchPath + r'C2C_pushFilesOnTCUdevice.bat',
                     tcu_adbSerialNo, pushBinariesLibrariesOnTCU, "No", tcuDevice_NAD])

            subprocess.call(
                [C2CtestData_batchPath + r'C2C_pushFilesOnTCUdevice.bat',
                 tcu_adbSerialNo, "No", "Yes", tcuDevice_NAD])

            if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes":
                subprocess.call(
                    [
                        C2CtestData_batchPath + r'C2C_pushFilesOnVTdevice.bat',
                        vt_adbSerialNo, "No", "Yes"])
                if pushBinariesLibrariesOnVT == "Yes":
                    subprocess.call(
                        [
                            C2CtestData_batchPath + r'C2C_pushFilesOnVTdevice.bat',
                            vt_adbSerialNo, pushBinariesLibrariesOnVT, "No"])

                # subprocess.call(
                #     [
                #         C2CtestData_batchPath + r'C2C_pushFilesOnVTdevice.bat',
                #         vt_adbSerialNo, "No", "Yes"])

            if comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes":
                subprocess.call(
                    [
                        C2CtestData_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                        ivi_adbSerialNo, "No", "Yes", "No"])

                if pushBinariesLibrariesOnIVI == "Yes":
                    subprocess.call(
                        [C2CtestData_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                         ivi_adbSerialNo, pushBinariesLibrariesOnIVI, "No", "No"])


        elif comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            subprocess.call(
                [
                    C2CtestData_batchPath + r'C2C_pushFilesOnTCUVTdevice.bat',
                    vt_adbSerialNo])
            if comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                subprocess.call(
                    [
                        C2CtestData_batchPath + r'C2C_pushFilesOnIVIdevice.bat',
                        ivi_adbSerialNo, "No", "Yes", "No"])

    except FileNotFoundError:
        print(f"Sorry, the push files on device (batch file) does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while pushing files on device")


def replaceText_TCUconf(self, TC):
    try:
        lfolderPath = folderPath + r'C2CtestData\usr\local\c2c'
        files = glob.glob(data_file)
        max_file = max(files, key=os.path.getctime)
        wb_obj = openpyxl.load_workbook(max_file)
        sheet_obj = wb_obj["TCUConfFileDetails"]
        for i in range(2, int(sheet_obj.max_row + 1)):
            fileName = str(testData("TCUConfFileDetails", int(i), 2))
            oldString = str(testData("TCUConfFileDetails", int(i), 3))
            newString = str(testData("TCUConfFileDetails", int(i), 4))
            if fileName != None and oldString != None and newString != None:
                finalPath = lfolderPath + fileName
                replaceLineWithText(self, finalPath, oldString, newString)
            else:
                break
                print("\n")
        if TC == "invalidPrgmSkuId":
            replaceLineWithText(self, dmconfFile, defaultPrgmSkuId, defaultPrgmSkuId + invalidPrgmSkuId)
        elif TC == "invalidSkuId":
            replaceLineWithText(self, car2cloudFile, defaultSkuId, defaultSkuId + invalidSkuId)
        elif TC == "invalidPrgmId":
            replaceLineWithText(self, car2cloudFile, defaultPrgmId, defaultPrgmId + invalidPrgmId)
        elif TC == "invalidchipsetType":
            replaceLineWithText(self, dmconfFile, defaultchipsetType, defaultchipsetType + invalidchipsetType)
        elif TC == "invalidchipsetSp":
            replaceLineWithText(self, dmconfFile, defaultchipsetSpVer, defaultchipsetSpVer + invalidchipsetSp)
        elif TC == "invalidChipsetName":
            replaceLineWithText(self, dmconfFile, defaultchipsetName, defaultchipsetName + invalidChipsetName)
        elif TC == "emptyPrgmSkuId":
            replaceLineWithText(self, dmconfFile, defaultPrgmSkuId, defaultPrgmSkuId + emptyPrgmSkuId)
        elif TC == "emptySkuId":
            replaceLineWithText(self, car2cloudFile, defaultSkuId, defaultSkuId + emptySkuId)
        elif TC == "emptyPrgmId":
            replaceLineWithText(self, car2cloudFile, defaultPrgmId, defaultPrgmId + emptyPrgmId)
        elif TC == "emptyChipsetType":
            replaceLineWithText(self, dmconfFile, defaultchipsetType, defaultchipsetType + emptyChipsetType)
        elif TC == "emptychipsetSp":
            replaceLineWithText(self, dmconfFile, defaultchipsetSpVer, defaultchipsetSpVer + emptychipsetSp)
        elif TC == "emptyChipsetName":
            replaceLineWithText(self, dmconfFile, defaultchipsetName, defaultchipsetName + emptyChipsetName)
    except FileNotFoundError:
        print("Sorry, the conf file does not exist or incorrect file path/name")
    except:
        print("Something went wrong while updating conf file")


# ============================================================
# replace text in IVI conf files
# ============================================================

def replaceText_IVIconf(self, TC):
    try:
        folderPath_ivi = folderPath + r'C2CtestData\usr\local\iviconfNew'
        files = glob.glob(data_file)
        max_file = max(files, key=os.path.getctime)
        wb_obj = openpyxl.load_workbook(max_file)
        sheet_obj = wb_obj["IVIConfFileDetails"]
        for i in range(2, int(sheet_obj.max_row + 1)):
            fileName = str(testData("IVIConfFileDetails", int(i), 2))
            oldString = str(testData("IVIConfFileDetails", int(i), 3))
            newString = str(testData("IVIConfFileDetails", int(i), 4))
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
        if tcu_brokerAddress_flag == "Yes":
            tcu_brkAdrs = ipAddress(self)
            print("Primary TCU IP Address :", tcu_brkAdrs)
            broker_addr = str("broker_addr=" + tcu_brkAdrs)
            broker_url = str("broker_url=" + tcu_brkAdrs + ":1883")
            replaceLineWithText(self, ivi_car2cloudFile, "broker_addr=", broker_addr)
            replaceLineWithText(self, ivi_dmconfFile, "broker_url=", broker_url)
    except FileNotFoundError:
        print("Sorry, the conf file does not exist or incorrect file path/name")
    except:
        print("Something went wrong while updating conf file")


# ============================================================
# replace text in VT conf files
# ============================================================

def replaceText_VTconf(self, TC):
    try:
        folderPath_vt = folderPath + r'C2CtestData\usr\local\vtconfNew\c2c'
        files = glob.glob(data_file)
        max_file = max(files, key=os.path.getctime)
        wb_obj = openpyxl.load_workbook(max_file)
        sheet_obj = wb_obj["VTConfFileDetails"]
        for i in range(2, int(sheet_obj.max_row + 1)):
            fileName = str(testData("VTConfFileDetails", int(i), 2))
            oldString = str(testData("VTConfFileDetails", int(i), 3))
            newString = str(testData("VTConfFileDetails", int(i), 4))
            if fileName != None and oldString != None and newString != None:
                finalPath = folderPath_vt + fileName
                replaceLineWithText(self, finalPath, oldString, newString)
            else:
                break
                print('\n')
        if TC == "invalidPrgmSkuId":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_PrgmSkuId, defaultVT_PrgmSkuId + invalidPrgmSkuId)
        elif TC == "invalidSkuId":
            replaceLineWithText(self, vt_car2cloudFile, defaultVT_SkuId, defaultVT_SkuId + invalidSkuId)
        elif TC == "invalidPrgmId":
            replaceLineWithText(self, vt_car2cloudFile, defaultVT_PrgmId, defaultVT_PrgmId + invalidPrgmId)
        elif TC == "invalidchipsetType":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetType, defaultVT_chipsetType + invalidchipsetType)
        elif TC == "invalidchipsetSp":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetSpVer, defaultVT_chipsetSpVer + invalidchipsetSp)
        elif TC == "invalidChipsetName":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetName, defaultVT_chipsetName + invalidChipsetName)
        elif TC == "emptyPrgmSkuId":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_PrgmSkuId, defaultVT_PrgmSkuId + emptyPrgmSkuId)
        elif TC == "emptySkuId":
            replaceLineWithText(self, vt_car2cloudFile, defaultVT_SkuId, defaultVT_SkuId + emptySkuId)
        elif TC == "emptyPrgmId":
            replaceLineWithText(self, vt_car2cloudFile, defaultVT_PrgmId, defaultVT_PrgmId + emptyPrgmId)
        elif TC == "emptyChipsetType":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetType, defaultVT_chipsetType + emptyChipsetType)
        elif TC == "emptychipsetSp":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetSpVer, defaultVT_chipsetSpVer + emptychipsetSp)
        elif TC == "emptyChipsetName":
            replaceLineWithText(self, vt_dmconfFile, defaultVT_chipsetName, defaultVT_chipsetName + emptyChipsetName)
        if tcu_brokerAddress_flag == "Yes":
            tcu_brkAdrs = ipAddress(self)
            print(tcu_brkAdrs)
            broker_addr = str("broker_addr=" + tcu_brkAdrs)
            broker_url = str("broker_url=" + tcu_brkAdrs + ":1883")
            replaceLineWithText(self, vt_car2cloudFile, "broker_addr=", broker_addr)
            replaceLineWithText(self, vt_dmconfFile, "broker_url=", broker_url)
    except FileNotFoundError:
        print(f"Sorry, the conf file does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while updating conf file")


# ============================================================
# Check licenses
# ============================================================

def checkLicense(self, onboarding_Type):
    try:
        onboardingType = deviceOnboardingType(self, onboarding_Type)
        singleDeviceOnboarding_TCU = str(onboardingType[0])
        comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
        comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
        comboDeviceOnboarding_TCUVT = str(onboardingType[3])
        comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
        comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
        if skuLicenseFlag == "Yes":
            if singleDeviceOnboarding_TCU == "Yes" or comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                # print("TCU License file details : => ")
                ls = subprocess.call([
                    C2CtestData_batchPath + r'C2C_checkLicense.bat',
                    tcu_adbSerialNo])
            if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                print('\n')
                # print("VT License file details : => ")
                subprocess.call([
                    C2CtestData_batchPath + r'C2C_checkLicense.bat',
                    vt_adbSerialNo])
        else:
            print("skuLicenseFlag is set to No")
    except FileNotFoundError:
        print(f"Sorry, the 'C2C_checkLicense.bat' file does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while checking license file")


# ============================================================
# Stop running c2c services on TCU device
# ============================================================

def stopC2Cservices(self, deviceSerialNo, deviceType):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_stopServicesOnDevices.bat',
             deviceSerialNo, deviceType])
    except FileNotFoundError:
        print(f"Sorry, the 'C2C_stopServicesOnDevices.bat' file does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while stopping c2c service")


# ============================================================
# Stop running c2c services on IVI device
# ============================================================

def stopC2CservicesOnPrimaryIVI(self):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_stopServices_IVI_primary.bat',
             ivi_adbSerialNo])
        print("Stopped all c2c services on IVI device")
    except FileNotFoundError:
        print(f"Sorry, the 'C2C_stopServices_IVI_primary.bat' file does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while stopping c2c service")


# =======================================================================
# Device Registration To Cloud Connection Establishment with valid & invalid data
# =======================================================================


def deviceRegistrationToCldConnEstb(self, TC, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    singleDeviceOnboarding_IVI = str(onboardingType[6])
    print("------------------------------------------------------------")
    print("Device On-boarding/Provisioning details : ")
    print("Test Case details => ", TC)
    print(f"Environment selected for device onboarding => {onboardingEnv}")
    # print(f"Cloud Base Url => {BaseUrl_gbl}")
    print("------------------------------------------------------------")
    print("TCU device chipset program details configured for onboarding : ")
    print(f"Sku Id =>  {SkuId}")
    print(f"Program Id =>  {PrgmId}")
    print(f"Program sku Id =>  {PrgmSkuId}")
    print(f"Chipset Type =>  {chipsetType}")
    print(f"Chipset SP version =>  {chipsetSpVer}")
    print("------------------------------------------------------------")

    if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("IVI device chipset program details configured for onboarding : ")
        print("Sku Id =>  ", IVI_SkuId)
        print("Program Id =>  ", IVI_PrgmId)
        print("Program sku Id =>  ", IVI_PrgmSkuId)
        print("Chipset Type =>  ", IVI_chipsetType)
        print("Chipset SP version =>  ", IVI_chipsetSpVer)
        print("------------------------------------------------------------")

    if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("VT device chipset program details configured for onboarding : ")
        print("Sku Id =>  ", VT_SkuId)
        print("Program Id =>  ", VT_PrgmId)
        print("Program sku Id =>  ", VT_PrgmSkuId)
        print("Chipset Type =>  ", VT_chipsetType)
        print("Chipset SP version =>  ", VT_chipsetSpVer)
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
            vinNo = "VIN" + "QCOMTCU" + random_id

    groupName = "TestGroup" + random_id

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

    print("Stop all c2c services on device(s) : ")
    stopC2Cservices(self, tcu_adbSerialNo, deviceType_TCU)
    print("=> Stopped all c2c services on device(s)")
    print("------------------------------------------------------------")

    print("Registration of TCU device : ")
    print("------------------------------------------------------------")

    # Device Reg POST request
    response_body = registration_DeviceReg(self, deviceType_TCU)

    # Device Reg GET requests
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
    print("Update desired conf files with newly registered TCU device data : ")

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
        # json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["device_info"]["ecu_type"] = deviceType_TCU
        # json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["device_info"]["primary"] = "true"
        if OTA_ModelFlag == "Yes" or reqModelNameFlag == "Yes":
            json_data["C2C_Vehicle"]["vehicle_info"]["model"] = uniqueModel

        if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["chipsets_count"] = 2
        else:
            json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][0]["chipsets_count"] = 1

    with open(c2cvehicleFile, 'w') as f:
        f.write(json.dumps(json_data))

    if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("\nUpdate desired VT conf files with newly registered TCU device data : ")
        replaceLineWithText(self, vt_car2cloudFile, defaultVIN, defaultVIN + vinNo)
        replaceLineWithText(self, vt_car2cloudFile, defaultSubSystemId, defaultSubSystemId + subSystemId)
        replaceLineWithText(self, vt_car2cloudFile, defaultDeviceId, defaultDeviceId + device_id)
        replaceLineWithText(self, vt_dmconfFile, dm_defaultDeviceId, dm_defaultDeviceId + device_id)
        replaceText_VTconf(self, "valid")
        time.sleep(2)

    replaceText_TCUconf(self, "valid")
    print("=> Conf file(s) are updated with newly registered device data")

    if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        # IVI device setup

        rebootDevice(self, ivi_adbSerialNo, "root")
        rebootDevice(self, ivi_adbSerialNo, "remount")

        print("Registration of IVI device : ")
        print("------------------------------------------------------------")

        # Device Reg POST request
        response_body = registration_DeviceReg(self, deviceType_IVI)

        # Device Reg GET requests
        registration_getCount(self)
        response_body = registration_getDetails(self)

        ividevice_id = response_body["responseData"][0]["device_id"]
        status = response_body["responseData"][0]["status"]
        url = response_body["responseData"][0]["url"]
        systemId = response_body["responseData"][0]["system_id"]
        deviceType = response_body["responseData"][0]["device_type"]
        # print(device_id, status, url, systemId)
        assert (status == "REGISTERED")
        assert (response_body["responseData"][0]["attestation"] == "X.509")
        assert (deviceType == deviceType_IVI)

        print("------------------------------------------------------------")
        print("Update desired conf files with newly registered IVI device data")
        print("------------------------------------------------------------")

        if TC == "ivi_invalidDeviceId_lessCharLen":
            ividevice_id = invalidDeviceId_lessCharLen
        elif TC == "ivi_invalidDeviceId_grtrCharLen":
            ividevice_id = invalidDeviceId_grtrCharLen
        elif TC == "ivi_invalidDeviceId_withSpace":
            ividevice_id = invalidDeviceId_withSpace
        elif TC == "ivi_invalidDeviceId_withSplchar":
            ividevice_id = invalidDeviceId_withSplchar
        elif TC == "ivi_dupDeviceId":
            ividevice_id = dupDeviceId
        elif TC == "ivi_emptyDeviceID":
            ividevice_id = emptyDeviceID

        if TC == "ivi_invalidSubSysId_lessCharLen":
            subSystemId = invalidSubSysId_lessCharLen
        elif TC == "ivi_invalidSubSysId_grtrCharLen":
            subSystemId = invalidSubSysId_grtrCharLen
        elif TC == "ivi_invalidSubSysId_withSpace":
            subSystemId = invalidSubSysId_withSpace
        elif TC == "ivi_invalidSubSysId_withSplchar":
            subSystemId = invalidSubSysId_withSplchar
        elif TC == "ivi_emptySubSystemID":
            subSystemId = emptySubSystemID

        # Update IVI Conf files
        with open(c2cvehicleFile) as f:
            json_data = json.load(f)
            json_data["C2C_Vehicle"]["Subsystems"][0]["Devices"][1]["deviceId"] = ividevice_id

        with open(c2cvehicleFile, 'w') as f:
            f.write(json.dumps(json_data))

        time.sleep(2)
        replaceLineWithText(self, ivi_car2cloudFile, defaultVIN, defaultVIN + vinNo)
        replaceLineWithText(self, ivi_car2cloudFile, defaultSubSystemId, defaultSubSystemId + subSystemId)
        replaceLineWithText(self, ivi_car2cloudFile, ivi_defaultDeviceId, ivi_defaultDeviceId + ividevice_id)
        # replaceLineWithText(self,c2cvehicleFile, ivi_defaultDeviceId, ividevice_id+'\n')
        replaceLineWithText(self, ivi_dmconfFile, dm_defaultDeviceId, dm_defaultDeviceId + ividevice_id)

        replaceText_IVIconf(self, "valid")
        time.sleep(5)
        print("=> Conf file(s) are updated with newly registered device data")

    print("\n------------------------------------------------------------")
    print("Push updated files on device : ")
    pushFilesOnDevices(self, onboarding_Type)
    print("\n=>All required files have been pushed on device and ready for onboarding")

    print("\n------------------------------------------------------------")
    print("Delete old license file from device : ")
    checkLicense(self, onboarding_Type)
    print('\n')
    print("=>Old License file is deleted from device")
    print("------------------------------------------------------------")
    print("=>Device setup is completed for fresh provisioning/onboarding")


# ============================================================
# Run all c2c services on device
# ============================================================
def runServices(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    # print("------------------------------------------------------------")
    print("\n============================================================")
    print("Run/Start c2c services on device(s) : ")
    print("============================================================")

    if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        try:
            # Start services on IVI device
            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 ivi_adbSerialNo, deviceType_IVI], timeout=10)
            time.sleep(5)
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on IVI device")

    try:
        if pushBinariesLibrariesOnTCU == "Yes":
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 tcu_adbSerialNo, "startC2CServices_bin"])
        else:
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 tcu_adbSerialNo, deviceType_TCU])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while starting c2c service on TCU device")
    time.sleep(5)

    if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes":
        try:
            ##Start services on VT device
            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 vt_adbSerialNo, deviceType_VT], timeout=10)
            time.sleep(5)
        except FileNotFoundError:
            print(
                f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on VT device")

    if comboDeviceOnboarding_TCUIVIVT == "Yes":
        restartServices(self, deviceType_VT, onboarding_Type)
        time.sleep(2)
        restartServices(self, deviceType_TCU, onboarding_Type)
        time.sleep(2)
        restartServices(self, deviceType_IVI, onboarding_Type)

    if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        try:
            ##Start services on TCUVT fusion device
            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 vt_adbSerialNo, "TCUVT_fusion"], timeout=10)
            time.sleep(5)
        except FileNotFoundError:
            print(
                f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while starting c2c service on TCUVT_fusion device")
    print("\n=> All c2c service are up and running for device onboarding")
    print("------------------------------------------------------------")
    time.sleep(60)


# ============================================================
# restart services on TCU & VT devices for TCU+VT+IVI combo
# ============================================================

def restartServices(self, device, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    if comboDeviceOnboarding_TCUIVIVT == "Yes" and device == deviceType_VT:
        try:
            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 vt_adbSerialNo, "VTrestart"], timeout=5)
        except FileNotFoundError:
            print(
                f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while re-starting c2c service on VT device")
    if comboDeviceOnboarding_TCUIVIVT == "Yes" and device == deviceType_TCU:
        try:
            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 tcu_adbSerialNo, "TCUrestart"], timeout=5)
        except FileNotFoundError:
            print(
                f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while re-starting c2c service on TCU device")

    if comboDeviceOnboarding_TCUIVIVT == "Yes" and device == deviceType_IVI:

        try:

            subprocess.run(
                [C2CtestData_batchPath + r'C2C_startServicesOnDevices.bat',
                 ivi_adbSerialNo, "IVIrestart"], timeout=5)
        except FileNotFoundError:
            print(
                f"Sorry, the file 'C2C_startServicesOnDevices.bat' does not exist or incorrect file path/name")
        except subprocess.TimeoutExpired:
            print(f'process ran too long')
        except:
            print(f"Something went wrong while re-starting c2c service on IVI device")


# ============================================================
# Check chipset and system states in c2c_vehicle json file
# ============================================================

def checkChipsetAndSystemState(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    primaryDevice_chipset1_state = system_state = vin = nonPrimaryDevice_chipset1_state = primaryDevice_chipset_count = nonPrimaryDevice_chipset_count = model = primaryDevice_chipset2_state = ''
    if singleDeviceOnboarding_TCU == "Yes" or comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        c2cvehicleFile = C2CtestReport_exeBackupPath + tcu_files + '\c2c\c2c_vehicle.json'
        with open(c2cvehicleFile, 'r') as file:
            json_data = json.load(file)
            primaryDevice_chipset_count = json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets_count']
            # print("Total TCU Chipsets : ", primaryDevice_chipset_count)
            try:
                primaryDevice_chipset1_type = json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][0][
                    "type"]
                if primaryDevice_chipset_count >= 2:
                    if primaryDevice_chipset1_type == c2c_tcu_chipset:
                        primaryDevice_chipset1_state = \
                            json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][0]["state"]
                    else:
                        primaryDevice_chipset1_state = \
                            json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][1]["state"]
                else:
                    primaryDevice_chipset1_state = \
                        json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][0]["state"]
            except:
                primaryDevice_chipset1_state = "TCU chipset data is not fetched"
            # print("=> TCU Chipset State is : ", primary_chipset_state)
            print("\n")
            if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                try:
                    if primaryDevice_chipset_count >= 2:
                        if primaryDevice_chipset1_type == c2c_vt_chipset:
                            primaryDevice_chipset2_state = \
                                json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][0]["state"]
                        else:
                            primaryDevice_chipset2_state = \
                                json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][0]['chipsets'][1]["state"]
                except:
                    primaryDevice_chipset2_state = "VT chipset data is not fetched"
                # print("=> VT Chipset State is : ", primaryDevice_chipset2_state)
                print("\n")
            if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                nonPrimaryDevice_chipset_count = json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][1][
                    'chipsets_count']
                # print("Total IVI Chipsets : ", nonPrimary1_chipset_count)
                try:
                    nonPrimaryDevice_chipset1_state = \
                        json_data['C2C_Vehicle']['Subsystems'][0]['Devices'][1]['chipsets'][0]["state"]
                except:
                    nonPrimaryDevice_chipset1_state = "IVI chipset data is not fetched"
                # print("=> IVI Chipset State is : ", nonPrimaryDevice_chipset1_state)
                print("\n")

        system_state = json_data['C2C_Vehicle']['system_state']
        print("\n")
        vin = json_data['C2C_Vehicle']['vin']
        model = json_data['C2C_Vehicle']['vehicle_info']['model']

    return primaryDevice_chipset1_state, system_state, vin, nonPrimaryDevice_chipset1_state, primaryDevice_chipset_count, nonPrimaryDevice_chipset_count, model, primaryDevice_chipset2_state


# ============================================================
# Save VIN no in file for SKU/Feature Update
# ============================================================
def saveVIN(self, onboarding_Type):
    states = checkChipsetAndSystemState(self, onboarding_Type)
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

def getVINdetails(self, val, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    # Get VIN details
    states = checkChipsetAndSystemState(self, onboarding_Type)

    NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_option, onboarding_Type)

    response_body = smpServer_getVINdetails(self, str(states[2]))
    saveAPIrespIntoFile("FetchNewVINRegistration_details", response_body, val)

    try:
        lendevice = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"])
        for i in range(lendevice):
            if response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                "chipsetType"] == chipsetType or \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                        "chipsetType"] == c2c_tcu_chipset:
                skuIdChk = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                    "skuId"]
                skuNameChk = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                    "skuName"]
                print("=============================================================")
                print("Onboarded VIN/device chipset details fetched via Cloud API : ")
                print("=============================================================")
                print("Telematics Device Sku Id =>  ", skuIdChk)
                print("Telematics Device Sku Name =>  ", skuNameChk)
                featlen = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                                  "featureInfo"])
                for j in range(featlen):
                    try:
                        featureID = \
                            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                                "featureInfo"][j]["featureId"]
                        featureName = \
                            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                                "featureInfo"][j]["featureName"]
                        # print(featureID, featureName)
                        output1 = open(NewLicense[0], "r")
                        output1 = output1.read()
                        # print(output1)
                        if featureID in output1:
                            print(f"{featureID} is present")
                        else:
                            print(f"{featureID} is not present")

                        if featureName in output1:
                            print(f"{featureName} is present")
                        else:
                            print(f"{featureName} is not present")
                    except:
                        print("\n")
            elif response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                "chipsetType"] == VT_chipsetType or \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0][
                        "chipsetType"] == c2c_vt_chipset:
                skuIdChk = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                    "skuId"]
                skuNameChk = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                    "skuName"]
                print("-------------------------------------------------------------")
                # print("Onboarded VIN/device chipset details fetched via Cloud API : ")
                # print("-------------------------------------------------------------")
                print("Telematics Device Sku Id =>  ", skuIdChk)
                print("Telematics Device Sku Name =>  ", skuNameChk)
                featInforLen = len(
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"])
                for j in range(featInforLen):
                    try:
                        featureID = \
                            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                                "featureInfo"][j]["featureId"]
                        featureName = \
                            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                                "featureInfo"][j]["featureName"]
                        # print(featureID, featureName)
                        output1 = open(NewLicense[0], "r")
                        output1 = output1.read()
                        # print(output1)
                        if featureID in output1:
                            print(f"{featureID} is present")
                        else:
                            print(f"{featureID} is not present")

                        if featureName in output1:
                            print(f"{featureName} is present")
                        else:
                            print(f"{featureName} is not present")
                    except:
                        print("\n")
            elif comboDeviceOnboarding_TCUIVI == 'Yes':
                try:
                    skuIdChk = \
                        response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                            "skuId"]
                    skuNameChk = \
                        response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["skuInfo"][
                            "skuName"]
                    print("-------------------------------------------------------------")
                    print("Non-Primary Device Sku Id =>  ", skuIdChk)
                    print("Non-Primary Device Sku Name =>  ", skuNameChk)
                except:
                    print("\n")
    except:
        print("=> Refer FetchNewVINRegistration_details json response for detailed info")


# ============================================================
# Get SKU update list via API
# ============================================================

def getSKUupdateList(self, val, name):
    response_body = smpServer_getSKUupdateList(self)

    saveAPIrespIntoFile("SkuUpdateList", response_body, val)

    if val == SKUupdateByVIN_option or name == "VIN_SKU_UPDATE_GROUP":
        name = "VIN_SKU_UPDATE_GROUP"
    elif val == DeviceOnboarding_option or name == "NEW_VIN_REGISTRATION":
        name = "NEW_VIN_REGISTRATION"

    try:
        # Assert: Validate response status code and body contents
        skulist_len = len(response_body["skuResponse"]["skuList"])
        for i in range(skulist_len):
            if response_body["skuResponse"]["skuList"][i]["groupName"] == name:
                status = response_body["skuResponse"]["skuList"][i]["delivered"]
                SKUid = response_body["skuResponse"]["skuList"][i]["skuId"]
                SKUName = response_body["skuResponse"]["skuList"][i]["skuName"]
                break
        else:
            print(f"Group : ' {name} ' is not listed in first 10 records")
        print("=============================================================")
        print("New VIN details are fetched successfully : ")
        if status == 100:
            testResult(self, "passed", 'SMP UI should show 100% delivered status',
                       "SMP UI shows 100% delivered status after installation of " + SKUName + " FeaturePkg/SKU for " + name + " vehicle group")
            assert True
        else:
            testResult(self, "passed", 'SMP UI should show 100% delivered status',
                       "SMP UI is showing " + status + "% => Check logs for additional details")
        print("=============================================================")
    except:
        print("Something went wrong, refer SkuUpdateList json response")
        status = ""
    return status


def getFeatureUdateList(self, val, name):
    try:
        response_body = smpServer_getFeatureUpdateList(self)
        saveAPIrespIntoFile("FeatureUpdateList", response_body, val)

        # totalRecords = response_body["featureResponse"]["totalRecords"]
        upFeat_len = len(response_body["featureResponse"]["updateFeatures"])

        for i in range(upFeat_len):
            grpName = response_body["featureResponse"]["updateFeatures"][i]["groupName"]
            if grpName == name:
                status = response_body["featureResponse"]["updateFeatures"][i]["delivered"]
                featureId = response_body["featureResponse"]["updateFeatures"][i]["featuresList"][0]["featureId"]
                featureName = response_body["featureResponse"]["updateFeatures"][i]["featuresList"][0]["featureName"]
                # print(1, status,featureId,featureName)
                break
        else:
            print(f"Group : ' {name} ' is not listed in first 10 records")
        print("====================================================================================================")
        if status == 100:
            print(
                f"SMP UI shows 100% delivered status post installation of '{featureName}' feature for '{name}' vehicle group")
            assert True
        else:
            print(f"SMP UI is showing {status}% => Check logs for additional details")
        print("====================================================================================================")
    except:
        ("Refer featureUpdateList json response or SMP UI")
        status = ""

    return status


# ============================================================
# Execution backup post execution for debugging
# ============================================================
def executionBackup(self, TC, testType):
    try:
        print("=============================================================")
        print("Execution Backup : ")
        print("=============================================================")

        vin = readVINno(self)

        if TC == SKUupdateByVIN_option:
            src_dir = C2CtestReport_exeBackupPath + SKUupdateByVIN_option
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_backupPath + 'executionBackup' + '_' + TC + '_' + testType + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_backupPath}")
        elif TC == SKUupdateByGroup_option:
            src_dir = C2CtestReport_exeBackupPath + SKUupdateByGroup_option
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_backupPath + 'executionBackup' + '_' + TC + '_' + testType + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_backupPath}")
        elif TC == FeatureUpdateByGroup_option:
            src_dir = C2CtestReport_exeBackupPath + FeatureUpdateByGroup_option
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_backupPath + 'executionBackup' + '_' + TC + '_' + testType + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_backupPath}")

        elif testType == "Positive":
            src_dir = C2CtestReport_exeBackupPath + 'DeviceOnboarding_backup'
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_backupPath + 'executionBackup' + '_' + TC + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_backupPath}")
        elif testType == "Negative":
            src_dir = C2CtestReport_exeBackupPath + 'DeviceOnboarding_backup'
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_backupPath + 'executionBackup_Neg_' + '_' + TC + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_backupPath}")

        elif TC == "OTA":
            src_dir = C2CtestReport_exeBackupPath + 'OTA'
            allfiles = os.listdir(src_dir)
            date_time = datetime.datetime.now()
            unix_timestamp = int(datetime.datetime.timestamp(date_time))
            dest_dir = C2CtestReport_OTA_backupPath + 'executionBackup_' + TC + '_' + testType + '_' + vin + '_' + str(
                unix_timestamp)
            print(f"{C2CtestReport_OTA_backupPath}")
        shutil.copytree(src_dir, dest_dir)
        print("Refer detailed c2c logs & json responses at below location : ")
        print(f"{C2CtestReport_exeBackupPath}")
    except:
        print("Refer detailed c2c logs & json responses at below location : ")
        print(f"{C2CtestReport_exeBackupPath}")


# ============================================================
# Error Code Search function
# ============================================================

def errorCodeSearch(self, message_type):
    try:
        max_file = C2CtestReport_exeBackupPath + tcu_files + r'\tcu_c2clogs.txt'
        # files = glob.glob(LogPath)
        # max_file = max(files, key=os.path.getctime)
        # Safely read the input filename using 'with'
        freq = 0
        with open(max_file) as f:
            s = f.read()
            if message_type not in s:
                print('"{message_type}" not found in {max_file}.'.format(**locals()))
                freq = 0
                return freq
        # Safely write the changed content, if found in the file
        with open(max_file, 'r') as f:
            if message_type in s:
                print('"{message_type}" found in {max_file}.'.format(**locals()))
                freq = int(freq) + 1
                return freq
    except:
        freq = "log file is empty or contain undefined chars that cannot be decoded"
    print(freq)
    return freq


def corruptORwithoutCerts(self, option):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_remFilesfromDevice.bat',
             tcu_adbSerialNo, option])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_remFilesfromDevice.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while removing files from device")


# ===========================================================================================
# Validate chipset & system state
# ===========================================================================================
def validateChipsetSystemState(self, val, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    states = checkChipsetAndSystemState(self, onboarding_Type)

    print("=============================================================")
    print("Validate Chipset & System type post device onboarding/provisioning")
    print("=============================================================")

    if states[3] != 'ACTIVE':
        time.sleep(60)
        print('waiting for another 60 sec')

        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_option, onboarding_Type)
        else:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)

        states = checkChipsetAndSystemState(self, onboarding_Type)

    print("=> TCU Chipset Count is : ", states[4])
    print("=> TCU Chipset State is : ", states[0])
    print("-----------------------------------------")
    if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("=> VT Chipset State is : ", states[7])
        print("-----------------------------------------")
    if comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        print("=> IVI Chipset Count is : ", states[5])
        print("=> IVI Chipset State is : ", states[3])
        print("-----------------------------------------")

    print("=> System State is : ", states[1])
    print('\n')
    print("-------------------------------------------------------------")

    if val == "ACTIVE":

        if states[0] == "ACTIVE":
            testResult(self, "passed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is set to ACTIVE")

        elif states[0] != "ACTIVE":
            testResult(self, "failed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is not set to ACTIVE")

        # assert (states[0] == "ACTIVE")
        if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes":

            if states[7] == "ACTIVE":
                testResult(self, "passed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is set to ACTIVE")

            elif states[7] != "ACTIVE":
                testResult(self, "failed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is not set to ACTIVE")

        if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes":

            if states[3] == "ACTIVE":
                testResult(self, "passed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is set to ACTIVE")

            elif states[3] != "ACTIVE":
                testResult(self, "failed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is not set to ACTIVE")

        if states[1] == "ACTIVE":
            testResult(self, "passed", "System State should be set to ACTIVE", "System State is set to ACTIVE")

        elif states[1] != "ACTIVE":
            testResult(self, "failed", "System State should be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed")

    elif val == "TCU_NOT-ACTIVE":

        if states[0] != "ACTIVE":
            testResult(self, "passed", "TCU Chipset State should not be set to ACTIVE",
                       "TCU Chipset State is not set to ACTIVE")

        elif states[0] == "ACTIVE":
            testResult(self, "failed", "TCU Chipset State should not be set to ACTIVE",
                       "TCU Chipset State is set to ACTIVE")

        if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes":

            if states[3] == "ACTIVE":
                testResult(self, "passed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is set to ACTIVE")

            elif states[3] != "ACTIVE":
                testResult(self, "failed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is not set to ACTIVE")

        if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":

            if states[7] == "ACTIVE":
                testResult(self, "passed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is set to ACTIVE")

            elif states[7] != "ACTIVE":
                testResult(self, "failed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is not set to ACTIVE")

        if states[1] != "ACTIVE":
            testResult(self, "passed", "System State should not be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed!")

        elif states[1] == "ACTIVE":
            testResult(self, "failed", "System State should not be set to ACTIVE",
                       "System State is set to ACTIVE, thus device is onboarded successfully!")

    elif val == "IVI_NOT-ACTIVE":

        if states[0] == "ACTIVE":
            testResult(self, "passed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is set to ACTIVE")

        elif states[0] != "ACTIVE":
            testResult(self, "failed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is not set to ACTIVE")

        if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":

            if states[3] != "ACTIVE":
                testResult(self, "passed", "IVI Chipset State should not be set to ACTIVE",
                           "IVI Chipset State is not set to ACTIVE")

            elif states[3] == "ACTIVE":
                testResult(self, "failed", "IVI Chipset State should not be set to ACTIVE",
                           "IVI Chipset State is set to ACTIVE")

        if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes":

            if states[7] == "ACTIVE":
                testResult(self, "passed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is set to ACTIVE")

            elif states[7] != "ACTIVE":
                testResult(self, "failed", "VT Chipset State should be set to ACTIVE",
                           "VT Chipset State is not set to ACTIVE")

        if states[1] != "ACTIVE":
            testResult(self, "passed", "System State should not be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed!")

        elif states[1] == "ACTIVE":
            testResult(self, "failed", "System State should not be set to ACTIVE",
                       "System State is set to ACTIVE, thus device is onboarded successfully!")

    elif val == "VT_NOT-ACTIVE":

        if states[0] == "ACTIVE":
            testResult(self, "passed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is set to ACTIVE")

        elif states[0] != "ACTIVE":
            testResult(self, "failed", "TCU Chipset State should be set to ACTIVE",
                       "TCU Chipset State is not set to ACTIVE")

        if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes":

            if states[3] == "ACTIVE":
                testResult(self, "passed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is set to ACTIVE")

            elif states[3] != "ACTIVE":
                testResult(self, "failed", "IVI Chipset State should be set to ACTIVE",
                           "IVI Chipset State is not set to ACTIVE")

        if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes":

            if states[7] != "ACTIVE":
                testResult(self, "passed", "VT Chipset State should not be set to ACTIVE",
                           "VT Chipset State is not set to ACTIVE")

            elif states[7] == "ACTIVE":
                testResult(self, "failed", "VT Chipset State should not be set to ACTIVE",
                           "VT Chipset State is set to ACTIVE")

        if states[1] != "ACTIVE":
            testResult(self, "passed", "System State should not be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed!")

        elif states[1] == "ACTIVE":
            testResult(self, "failed", "System State should not be set to ACTIVE",
                       "System State is set to ACTIVE, thus device is onboarded successfully!")

    elif val == "NOT_ACTIVE":

        if states[0] != "ACTIVE":
            testResult(self, "passed", "TCU Chipset State should not be set to ACTIVE",
                       "TCU Chipset State is not set to ACTIVE")

        elif states[0] == "ACTIVE":
            testResult(self, "failed", "TCU Chipset State should not be set to ACTIVE",
                       "TCU Chipset State is set to ACTIVE")

            # assert (states[0] != "ACTIVE")

        if comboDeviceOnboarding_TCUIVI == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":

            if states[3] != "ACTIVE":
                testResult(self, "passed", "IVI Chipset State should not be set to ACTIVE",
                           "IVI Chipset State is not set to ACTIVE")

            elif states[3] == "ACTIVE":
                testResult(self, "failed", "IVI Chipset State should not be set to ACTIVE",
                           "IVI Chipset State is set to ACTIVE")

        if comboDeviceOnboarding_TCUVT == 'Yes' or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":

            if states[7] != "ACTIVE":
                testResult(self, "passed", "VT Chipset State should not be set to ACTIVE",
                           "VT Chipset State is not set to ACTIVE")

            elif states[7] == "ACTIVE":
                testResult(self, "failed", "VT Chipset State should not be set to ACTIVE",
                           "VT Chipset State is set to ACTIVE")

        if states[1] != "ACTIVE":
            testResult(self, "passed", "System State should not be set to ACTIVE",
                       "System State is not set to ACTIVE, thus device onboarding failed!")

        elif states[1] == "ACTIVE":
            testResult(self, "failed", "System State should not be set to ACTIVE",
                       "System State is set to ACTIVE, thus device is onboarded successfully!")


# ===========================================================================================
# Get License file details
# ===========================================================================================

def licenseDetails(self, val, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    if skuLicenseFlag == "Yes":
        if val == "NoLicenseFile_tcu":
            NewLicense = getLicenseDetails(self, "NoLicenseFile", DeviceOnboarding_option, onboarding_Type)
        elif val == "LicenseFile" or val != "NoLicenseFile_tcu":
            NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_option, onboarding_Type)
        # print("New/Latest License File Path : ", NewLicense[0], NewLicense[1])  \
        print("=============================================================")
        print("TCU license details : =>")
        print("=============================================================")
        print("New/Latest License File Name : ", NewLicense[0])
        print("New/Latest License File timestamp : ", NewLicense[1])
        print("\n")
        if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            if val == "NoLicenseFile_tcu" or val == "LicenseFile":
                NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_option, onboarding_Type)
            elif val == "NoLicenseFile_vt":
                NewLicense = getLicenseDetails(self, "NoLicenseFile", DeviceOnboarding_tcuvt_option, onboarding_Type)
            # print("New/Latest License File Path : ", NewLicense[0], NewLicense[1])
            print("=============================================================")
            print("VT license details : =>")
            print("=============================================================")
            print("New/Latest License File Name : ", NewLicense[0])
            print("New/Latest License File timestamp : ", NewLicense[1])
            print("\n")
    else:
        print("skuLicenseFlag is set No")


# ===========================================================================================
# Read VIN no from text file for SKU/Feature Update
# ===========================================================================================
def readVINno(self):
    text_file = folderPath + r'C2CtestData\VinNo.txt'
    files = glob.glob(text_file)
    max_file = max(files, key=os.path.getctime)
    with open(max_file) as f:
        vinNo = f.read()
    # print("VIN number on which SKU/Feature Update will be triggered : ", vinNo)
    return vinNo


# ===========================================================================================
# Read palyload form json file
# ===========================================================================================

def readPayloadFromJSON(self, filename):
    text_file = C2CtestData_jsonPath + filename
    file = glob.glob(text_file)
    max_file = max(file, key=os.path.getctime)

    with open(max_file, 'r') as jsonFile:
        payload = json.load(jsonFile)
    return payload


# ===========================================================================================
# Trigger SKU update By VIN on TCU/IVI device
# ===========================================================================================

def triggerSKUupdateByVIN(self, device, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    print("=============================================================")
    print("Old license file details")
    print("=============================================================")
    if device == deviceType_TCU:
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            OldLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_skuVIN_option,
                                           onboarding_Type)
            print("Old License File : ", OldLicense[0], OldLicense[1])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")
        else:
            OldLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByVIN_option, onboarding_Type)
            print("Old License File : ", OldLicense[0], OldLicense[1])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")
    if device == deviceType_VT:
        OldLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByVIN_vt_option, onboarding_Type)
        print("Old License File : ", OldLicense[0], OldLicense[1])
        print("\n")
        print("Old License File timestamp : ", OldLicense[1])
        print("\n")

    if device == deviceType_IVI:
        restartServices(self, deviceType_IVI, onboarding_Type)

    # Arrange: Test data (url,header and payload) for POST request

    try:
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_option, onboarding_Type)
            saveVIN(self, onboarding_Type)
        else:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)
            saveVIN(self, onboarding_Type)

        states = checkChipsetAndSystemState(self, onboarding_Type)

        vinNo = states[2]

    except:
        vinNo = readVINno(self)

    print("=============================================================")

    print(f"Triggering SKU Update by VIN on newly onboarded Vin " + device + " - Device : ", vinNo)

    print("=============================================================")

    response_body = smpServer_VinGetuPvChipsetSpIdlist(self, vinNo)

    saveAPIrespIntoFile("FeatureUpdateList_" + device, response_body, SKUupdateByVIN_option)

    if device == deviceType_TCU:
        try:
            len_prgms = len(response_body["response"]["systemsData"][0]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
        except:
            print("Refer json response for additional details")
        try:
            # print(chipsetType)
            len_prgms = len(response_body["response"]["systemsData"][1]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for TCU device => ", pvChipsetSpId)
        print("----------------------------------------------------")

    if device == deviceType_VT:
        try:
            len_prgms = len(response_body["response"]["systemsData"][0]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
        except:
            print("\n")
        try:
            # print(VT_chipsetType)
            len_prgms = len(response_body["response"]["systemsData"][1]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    # print(pvChipsetSpId_vt)

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                        # print(pvChipsetSpId_vt)
        except:
            print("\n")
        print("----------------------------------------------------")
        print("pvChipsetSpId for VT device => ", pvChipsetSpId_vt)
        print("----------------------------------------------------")

    if device == deviceType_IVI:
        if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
            "chipset"] == IVI_chipsetType or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset1 or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
        else:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]

        print("----------------------------------------------------")
        print("pvChipsetSpId for IVI device => ", pvChipsetSpId)
        print("-----------------------------------------------------")
    # get SKU Id list through POST request.
    # Arrange: Test data (url,header and payload) for POST request
    time.sleep(5)

    if device != deviceType_VT:
        response_body = smpServer_VinGetSKUIdlist(self, pvChipsetSpId, vinNo)

    elif device == deviceType_VT:
        response_body = smpServer_VinGetSKUIdlist(self, pvChipsetSpId_vt, vinNo)

    saveAPIrespIntoFile("SkubyVIN_VinGetSKUidlist_" + str(device), response_body, SKUupdateByVIN_option)

    skuId = response_body["response"]["skus"][0]["skuId"]
    skuName = response_body["response"]["skus"][0]["skuName"]
    print("-----------------------------------------------------")
    print(f"skuId for " + device + " device is  => ", skuId)
    print(f"skuName for " + device + " device is  => ", skuName)
    print("-----------------------------------------------------")

    # Trigger SKU Update on VIN through POST request.
    # Arrange: Test data (url,header and payload) for POST request
    if device == deviceType_TCU:
        response_body = smpServer_VinUpdateSKU(self, pvChipsetSpId, vinNo, skuId, "Telematics")

    if device == deviceType_VT:
        response_body = smpServer_VinUpdateSKU(self, pvChipsetSpId_vt, vinNo, skuId, "Telematics")

    elif device == deviceType_IVI:
        response_body = smpServer_VinUpdateSKU(self, pvChipsetSpId, vinNo, skuId, "IVI")

    saveAPIrespIntoFile("SkubyVIN_TriggerSkUupdateByVIN_" + str(device), response_body, SKUupdateByVIN_option)

    print("=============================================================")
    print(f"Triggered SKU Update by VIN on onboarded VIN -> " + device + " - Device : ", vinNo)
    print("=============================================================")
    time.sleep(60)

    if device == deviceType_TCU:
        print("=============================================================")
        print("New license file details : ")
        print("=============================================================")
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_skuVIN_option,
                                           onboarding_Type)
            # print(f"New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print(f"New License File timestamp : ", NewLicense[1])
            # print("\n")
        else:
            NewLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByVIN_option, onboarding_Type)
            # print(f"New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print(f"New License File timestamp : ", NewLicense[1])
            # print("\n")

    elif device == deviceType_VT:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        NewLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByVIN_vt_option, onboarding_Type)
        # print("New License File : ", NewLicense[0], NewLicense[1])
        # print("\n")
        # print("New License File timestamp : ", NewLicense[1])
        # print("\n")

    # Get VIN details and SKU updated list to verify delivered status

    response_body = smpServer_getVINdetails(self, str(vinNo))
    saveAPIrespIntoFile("SkuUpdateByVINdetails_" + str(device), response_body, SKUupdateByVIN_option)

    # getVINdetails(SKUupdateByVIN_option)

    status = getSKUupdateList(self, SKUupdateByVIN_option, "VIN_SKU_UPDATE_GROUP")

    if device == deviceType_TCU or device == deviceType_VT:
        if NewLicense[0] != OldLicense[0] or status == "100" or status == 100:
            testResult(self, "passed",
                       "New SKU license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New SKU license is successfully installed on " + device + " device")
        else:
            testResult(self, "failed",
                       "New SKU license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New SKU license is not installed or multiple licenses are installed/exists on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")
            assert (NewLicense[0] != OldLicense[0])

    if device == deviceType_IVI:
        if status == "100" or status == 100:
            testResult(self, "passed", "New SKU license should be installed on device successfully",
                       "New SKU license is successfully installed on " + device + " device")
        else:
            testResult(self, "failed", "New SKU license should be installed on device successfully",
                       "New SKU license is not installed on " + device + " device or record is not listed in first page/10 records on SMP UI")


# ===========================================================================================
# Trigger SKU update By creating new Group on TCU/IVI device
# ===========================================================================================

def triggerSKUupdateByGroup(self, device, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    random_id = ' '.join([str(random.randint(10, 9999)).zfill(5) for _ in range(1)])

    newGroupName = "SKUupdate_" + random_id

    if device == deviceType_TCU:
        print("=============================================================")
        print("Old License file details : ")
        print("=============================================================")
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            OldLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_skuGrp_option,
                                           onboarding_Type)
            print("Old License File : ", OldLicense[0], OldLicense[1])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")
        else:
            OldLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByGroup_option, onboarding_Type)
            print("Old License File : ", OldLicense[0], OldLicense[1])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")

    elif device == deviceType_VT:
        print("=============================================================")
        print("Old License file details : ")
        print("=============================================================")
        OldLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByGroup_vt_option, onboarding_Type)
        print("Old License File : ", OldLicense[0], OldLicense[1])
        print("\n")
        print("Old License File timestamp : ", OldLicense[1])
        print("\n")

    elif device == deviceType_IVI:
        restartServices(self, deviceType_IVI, onboarding_Type)

    # Arrange: Test data (url,header and payload) for POST request
    try:
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_option, onboarding_Type)
            saveVIN(self, onboarding_Type)
        else:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)
            saveVIN(self, onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)

        vinNo = states[2]

    except:
        vinNo = readVINno(self)

    print("=============================================================")

    print("Triggering SKU Update by creating new Group on onboarded Vin " + device + " - Device : ", vinNo)

    print("=============================================================")

    response_body = smpServer_createGroup(self, newGroupName, vinNo)
    saveAPIrespIntoFile("SkubyGroup_CreateNewGroup_" + str(device), response_body, SKUupdateByGroup_option)

    groupId = response_body["groupResponse"]["groupId"]
    print("=============================================================")
    print("Newly created Group Name is : ", newGroupName)
    print("Newly created Group Id is : ", groupId)
    print("=============================================================")

    response_body = smpServer_GrpGetuPvChipsetSpIdlist(self, groupId)
    saveAPIrespIntoFile("SkubyGroup_VinGetSKUidlist_" + str(device), response_body, SKUupdateByGroup_option)

    if device == deviceType_TCU:
        try:
            len_prgms = len(response_body["response"]["systemsData"][0]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
        except:
            print("Refer json response for additional details")
        try:
            # print(chipsetType)
            len_prgms = len(response_body["response"]["systemsData"][1]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][0]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                0]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][1]["chipset"] == c2c_tcu_chipset:
                        pvChipsetSpId = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][
                                1]["pvChipsetSpId"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for TCU device => ", pvChipsetSpId)
        print("----------------------------------------------------")

    elif device == deviceType_VT:
        try:
            len_prgms = len(response_body["response"]["systemsData"][0]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                    elif \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
        except:
            print("\n")
        try:
            print(VT_chipsetType)
            len_prgms = len(response_body["response"]["systemsData"][1]["programs"])
            len_chipsetSps = len(
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"])
            if len_prgms <= 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)

            if len_prgms > 1:
                if len_chipsetSps <= 1:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                else:
                    if \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        0]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][0][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
                    elif \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "chipset"] == VT_chipsetType or \
                                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                        "chipsetSps"][
                                        1]["chipset"] == c2c_vt_chipset:
                        pvChipsetSpId_vt = \
                            response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0][
                                "chipsetSps"][1][
                                "pvChipsetSpId"]
                        print(pvChipsetSpId_vt)
        except:
            print("\n")
        print("----------------------------------------------------")
        print("pvChipsetSpId for VT device => ", pvChipsetSpId_vt)
        print("----------------------------------------------------")

    elif device == deviceType_IVI:
        if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
            "chipset"] == IVI_chipsetType or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset1 or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
        else:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]

        print("pvChipsetSpId for IVI device => ", pvChipsetSpId)
        print("----------------------------------------------------------")

    if device == deviceType_VT:
        response_body = smpServer_GrpGetSKUIdlist(self, pvChipsetSpId_vt, groupId)

    else:
        response_body = smpServer_GrpGetSKUIdlist(self, pvChipsetSpId, groupId)

    saveAPIrespIntoFile("SkubyGroup_TriggerSkUupdate_" + str(device), response_body, SKUupdateByGroup_option)

    skuId = response_body["response"]["skus"][0]["skuId"]
    print("-----------------------------------------------------")
    print("skuId for " + device + " device is  => ", skuId)
    print("-----------------------------------------------------")

    if device == deviceType_TCU:
        response_body = smpServer_GrpUpdateSKU(self, "Telematics", pvChipsetSpId, skuId, groupId)
    if device == deviceType_VT:
        response_body = smpServer_GrpUpdateSKU(self, "Telematics", pvChipsetSpId_vt, skuId, groupId)
    elif device == deviceType_IVI:
        response_body = smpServer_GrpUpdateSKU(self, "IVI", pvChipsetSpId, skuId, groupId)

    saveAPIrespIntoFile("SkubyGroup_TriggerSkUupdateByGroup_" + str(device), response_body, SKUupdateByGroup_option)

    print("=============================================================")
    print("Triggered SKU Update by creating new Group on onboarded Vin" + device + " - Device : ", vinNo)
    print("=============================================================")
    time.sleep(60)

    if device == deviceType_TCU:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_skuGrp_option,
                                           onboarding_Type)
            # print("New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")
        else:
            NewLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByGroup_option, onboarding_Type)
            # print("New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")

    elif device == deviceType_VT:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        NewLicense = getLicenseDetails(self, "LicenseFile", SKUupdateByGroup_vt_option, onboarding_Type)
        # print("New License File : ", NewLicense[0], NewLicense[1])
        # print("\n")
        # print("New License File timestamp : ", NewLicense[1])
        print("\n")

    # Compare/verify old and new license files on TCU device

    if device == deviceType_TCU or device == deviceType_VT:
        status = getSKUupdateList(self, SKUupdateByGroup_option, newGroupName)
        if NewLicense[0] != OldLicense[0] or status == "100" or status == 100:
            testResult(self, "passed",
                       "New SKU license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New SKU license is successfully installed on " + device + " device")

        else:
            testResult(self, "failed",
                       "New SKU license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New SKU license is not installed  or multiple licenses are installed/exists on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")
            assert (NewLicense[0] != OldLicense[0])

    # Get VIN details and SKU updated list to verify delivered status

    response_body = smpServer_getVINdetails(self, str(vinNo))
    saveAPIrespIntoFile("SkuUpdateByVINdetails_" + str(device), response_body, SKUupdateByVIN_option)

    status = getSKUupdateList(self, SKUupdateByGroup_option, newGroupName)

    if device == deviceType_IVI:
        if status == "100" or status == 100:
            testResult(self, "passed", "New SKU license should be installed on device successfully",
                       "New SKU license is successfully installed on " + device + " device")
        else:
            testResult(self, "failed", "New SKU license should be installed on device successfully",
                       "New SKU license is not installed on " + device + " device or record is not listed in first page/10 records on SMP UI")


# ===========================================================================================
# Feature update By creating new Group on TCU/IVI device
# ===========================================================================================

def triggerFeatureUpdate(self, device, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    random_id = ' '.join([str(random.randint(10, 9999)).zfill(5) for _ in range(1)])

    newGroupName = "featureUpdate_" + random_id

    # Arrange: Test data (url,header and payload) for POST request

    try:
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_FeatUp_option, onboarding_Type)
            # saveVIN(self, onboarding_Type)
        else:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)
            # saveVIN(self, onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        vinNo = states[2]
        saveVIN(self, onboarding_Type)

    except:
        vinNo = readVINno(self)

    if device == deviceType_IVI:
        restartServices(self, deviceType_IVI, onboarding_Type)

    # print("=============================================================")
    print("Triggering Feature Update by creating new Group on onboarded Vin " + device + " - Device : ", vinNo)
    print("=============================================================")

    response_body = smpServer_createGroup(self, newGroupName, vinNo)
    saveAPIrespIntoFile("FeatureUpdate_CreateNewGroup_" + str(device), response_body, FeatureUpdateByGroup_option)

    groupId = response_body["groupResponse"]["groupId"]

    print("=============================================================")
    print("Newly created Group Name is : ", newGroupName)
    print("Newly created Group Id is : ", groupId)
    print("=============================================================")

    response_body = smpServer_GetFilterValuesbyGroup(self, groupId)

    saveAPIrespIntoFile("FeatureUpdate_getFilterValuesbyGroup_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    if device == deviceType_TCU:
        try:
            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")
        try:
            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
            if response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for TCU device => ", pvChipsetSpId)
        print("----------------------------------------------------")

    elif device == deviceType_VT:

        try:
            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")
        try:
            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for VT device => ", pvChipsetSpId_vt)
        print("----------------------------------------------------")

    elif device == deviceType_IVI:
        if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
            "chipset"] == IVI_chipsetType or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset1 or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
            pvChipset_ivi = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"]
            pvChipsetsp_ivi = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "sp"]
            # print(pvChipsetsp_ivi")
        else:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
            pvChipset_ivi = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"]
            pvChipsetsp_ivi = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "sp"]
        print("-------------------------------------------------------------------")
        print("pvChipsetSpId for IVI device => ", pvChipsetSpId)
        print("-------------------------------------------------------------------")

    if device == deviceType_TCU or device == deviceType_IVI:
        response_body = smpServer_GetFeaturesforselectedFilters(self, pvChipsetSpId, groupId)
    if device == deviceType_VT:
        response_body = smpServer_GetFeaturesforselectedFilters(self, pvChipsetSpId_vt, groupId)

    saveAPIrespIntoFile("FeatureUpdate_getFeaturesforselectedFilters_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    if device == deviceType_TCU or device == deviceType_VT:
        print("=============================================================")
        print("Old License file details : ")
        print("=============================================================")

        if device == deviceType_TCU:
            if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                OldLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_FeatUp_option,
                                               onboarding_Type)
            else:
                OldLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_option, onboarding_Type)
        elif device == deviceType_VT:
            OldLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_vt_option, onboarding_Type)
        if device == deviceType_TCU or device == deviceType_VT:
            print("Old License File Name : ", OldLicense[0])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")
            print(OldLicense[2])
            output = open(OldLicense[2], "r")
            output = output.read()

        try:
            print("----------------------------------------------------")
            print("Installed Feature Check : ")
            print("----------------------------------------------------")
            is_looping = True
            len_featureAreaList = len(response_body["response"]["functionalAreaList"])
            for i in range(len_featureAreaList):
                len_featureList = len(response_body["response"]["functionalAreaList"][i]["featureList"])
                for j in range(len_featureList):
                    featureID = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureId"]
                    featureName = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureName"]
                    isBundle = response_body["response"]["functionalAreaList"][i]["featureList"][j]["bundle"]
                    description = response_body["response"]["functionalAreaList"][i]["featureList"][j]["description"]
                    vehiclesAlreadyInstalledThis = response_body["response"]["functionalAreaList"][i]["featureList"][j][
                        "vehiclesAlreadyInstalledThis"]
                    # print(vehiclesAlreadyInstalledThis)
                    featureID = str(featureID)
                    if str(featureID) in output and featureName in output or vehiclesAlreadyInstalledThis == 1:
                        print(
                            f"Feature Id : '{featureID}' : '{featureName}' is already present in existing/available license file on device")
                    else:
                        print(
                            f"Feature Id : '{featureID}' : '{featureName}' is not present in existing/available license file on device")
                        numb = i
                        numb1 = j
                        is_looping = False
                        break
                if is_looping == False:
                    break
            # print("----------------------------------------------------")
            featureID = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["bundle"]
            description = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["description"]
            featureID = str(featureID)
            # print("----------------------------------------------------")
        except:
            print("Selecting available feature for validating feature update functionality ")
            featureID = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][0]["featureList"][0]["bundle"]
            description = response_body["response"]["functionalAreaList"][0]["featureList"][0]["description"]
            featureID = str(featureID)

    if device == deviceType_IVI:
        print("----------------------------------------------------")
        print("Installed Feature Check : ")
        print("----------------------------------------------------")
        try:
            is_looping = True
            len_featureAreaList_ivi = len(response_body["response"]["functionalAreaList"])
            for i in range(len_featureAreaList_ivi):
                len_featureList_ivi = len(response_body["response"]["functionalAreaList"][i]["featureList"])
                for j in range(len_featureList_ivi):
                    vehiclesAlreadyInstalledThis = response_body["response"]["functionalAreaList"][i]["featureList"][j][
                        "vehiclesAlreadyInstalledThis"]
                    featureID = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureId"]
                    featureName = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureName"]
                    # print(featureID,featureName,vehiclesAlreadyInstalledThis)
                    if vehiclesAlreadyInstalledThis == 0 or vehiclesAlreadyInstalledThis == "0":
                        num = i
                        num1 = j
                        featureID = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "featureId"]
                        featureName = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "featureName"]
                        isBundle = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["bundle"]
                        description = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "description"]
                        featureID = str(featureID)
                        is_looping = False
                        break
                    else:
                        print(f"feature {featureID} : {featureName} is alreday present/installed on device")
                if is_looping == False:
                    break
            featureID = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["bundle"]
            description = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["description"]
            featureID = str(featureID)
            print("----------------------------------------------------")

            # print("featureID selected for IVI device :", featureID)
        except:
            featureID = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][0]["featureList"][0]["bundle"]
            description = response_body["response"]["functionalAreaList"][0]["featureList"][0]["description"]
            featureID = str(featureID)

    print("------------------------------------------------------------------------------------------------")
    print("New feature to be installed on " + device + " device => ", "featureID : " + featureID,
          "featureName : " + featureName)
    print("------------------------------------------------------------------------------------------------")

    action = "ADD_TO_ALL"
    if device == deviceType_TCU:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId, "Telematics",
                                                           pvChipset,
                                                           pvChipsetsp, featureID, featureName, isBundle, device,
                                                           action)

    elif device == deviceType_VT:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId_vt, "Telematics",
                                                           pvChipset_vt,
                                                           pvChipsetsp_vt, featureID, featureName, isBundle, device,
                                                           action)

    elif device == deviceType_IVI:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId, deviceType_IVI,
                                                           pvChipset_ivi,
                                                           pvChipsetsp_ivi, featureID, featureName, isBundle, device,
                                                           action)

    saveAPIrespIntoFile("FeatureUpdate_TriggerFeatureUpdate_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    print("Triggered Feature Update by creating new Group on onboarded Vin" + device + " - Device : ", vinNo)
    time.sleep(60)

    if device == deviceType_TCU:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_FeatUp_option,
                                           onboarding_Type)
            # print("New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")
        else:
            NewLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_option, onboarding_Type)
            # print("New License File Name : ", NewLicense[0])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")
    if device == deviceType_VT:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        NewLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_vt_option, onboarding_Type)
        # print("New License File Name : ", NewLicense[0])
        # print("\n")
        # print("New License File timestamp : ", NewLicense[1])
        print("\n")

    status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)

    if device == deviceType_TCU or device == deviceType_VT:
        # status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)
        # Compare/verify old and new license files on TCU device
        print("=============================================================")
        if NewLicense[0] != OldLicense[0] or status == "100" or status == 100:
            testResult(self, "passed",
                       "New Feature license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New Feature license is successfully installed on " + device + " device")

        else:
            testResult(self, "failed",
                       "New Feature license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New Feature license is not installed or multiple licenses are installed/exists on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")

            assert (NewLicense[0] != OldLicense[0])
        # print("=============================================================")

        output1 = open(NewLicense[2], "r")
        output1 = output1.read()
        # print(output1)

        print("------------------------------------------------------------------------------------------------")

        if str(featureID) in output1:
            print(f"Feature Id : '{featureID}' is present in newly installed license file on device")
        else:
            print(f"Feature Id : '{featureID}' is not present in newly installed license file on device")

        if featureName in output1:
            print(f"Feature Name : '{featureName}' is present in newly installed license file on device")
        else:
            print(f"Feature Name : '{featureName}' is not present in newly installed license file on device")
        print("------------------------------------------------------------------------------------------------")
    # status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)

    if device == deviceType_IVI:
        status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)
        if status == "100" or status == 100:
            testResult(self, "passed",
                       "New Feature license should be installed on device successfully and SMP UI should show 100% delivered status",
                       "New Feature license is successfully installed on " + device + " device")
        else:
            testResult(self, "failed", "New feature license should be installed on device successfully",
                       "New Feature license is not installed or multiple licenses are installed/exists on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")

    # Get VIN details and SKU updated list to verify delivered status

    response_body = smpServer_getVINdetails(self, str(vinNo))
    saveAPIrespIntoFile("FeatureUpdateByVINdetails_" + str(device), response_body, FeatureUpdateByGroup_option)


def remFilesfromDevice(fileName):
    subprocess.call(
        [C2CtestData_batchPath + r'C2C_remFilesfromDevice.bat',
         tcu_adbSerialNo, fileName])


def stopServiceOnDevice(deviceType, serviceName):
    if deviceType == deviceType_TCU:
        deviceSerialNo = tcu_adbSerialNo
        deviceServices = "TCUServices"
    elif deviceType == deviceType_IVI:
        deviceSerialNo = ivi_adbSerialNo
        deviceServices = "IVIServices"
    elif deviceType == deviceType_VT:
        deviceSerialNo = vt_adbSerialNo
        deviceServices = "VTServices"
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_stopServiceOnDevice.bat',
             deviceSerialNo, deviceServices, serviceName], timeout=60)
    except subprocess.TimeoutExpired:
        print('process ran too long')
    except:
        print('\n')


def deviceOnboardingViaDepPack(self, onboarding_Type, TCUtype):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    if singleDeviceOnboarding_TCU == "Yes":
        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', tcu_adbSerialNo, TCUtype], timeout=10)
            time.sleep(15)
        except subprocess.TimeoutExpired:
            print('process ran too long')

    elif comboDeviceOnboarding_TCUIVI == "Yes":
        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', ivi_adbSerialNo, deviceType_IVI],
                            timeout=10)
            time.sleep(15)
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', ivi_adbSerialNo, deviceType_IVI],
                            timeout=10)
        except subprocess.TimeoutExpired:
            print('process ran too long')
        time.sleep(15)
        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', tcu_adbSerialNo, TCUtype], timeout=10)
        except subprocess.TimeoutExpired:
            print('process ran too long')


    elif comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        if comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            try:
                subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', ivi_adbSerialNo, deviceType_IVI],
                                timeout=10)
                time.sleep(15)
            except subprocess.TimeoutExpired:
                print('process ran too long')
        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', vt_adbSerialNo, "TCUVT_fusion"],
                            timeout=10)
            time.sleep(15)
        except subprocess.TimeoutExpired:
            print('process ran too long')

    elif comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":

        if comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            try:
                subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', ivi_adbSerialNo, deviceType_IVI],
                                timeout=10)
            except subprocess.TimeoutExpired:
                print('process ran too long')
        time.sleep(15)

        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', vt_adbSerialNo, deviceType_VT],
                            timeout=10)
        except subprocess.TimeoutExpired:
            print('process ran too long')
        time.sleep(15)

        try:
            subprocess.call([C2CtestData_batchPath + r'deviceOnboarding.bat', tcu_adbSerialNo, TCUtype], timeout=10)
        except subprocess.TimeoutExpired:
            print('process ran too long')

    time.sleep(15)


# ============================================================
# reboot/remount device
# ============================================================

def rebootOrRunAsRoot(self, deviceSerialNo, option):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_adbCommands.bat',
             deviceSerialNo, option])
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    except:
        print(f"Something went wrong while rebooting device")


def checkFirmwareVer(self, option):
    try:
        if option == "TCUVT_fusion":
            try:
                result1 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     vt_adbSerialNo, "firmwareVer_tcuvt"], timeout=15)
                result2 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     vt_adbSerialNo, "firmwareVer_vt"], timeout=15)
                with open(
                        C2CtestReport_exeBackupPath + tcu_files + '\Ver_info.txt',
                        "r") as file:
                    json_data = json.load(file)
                    Meta_Build_ID_tcu = json_data['Metabuild_Info']['Meta_Build_ID']
                    Product_Flavor_tcu = json_data['Metabuild_Info']['Product_Flavor']
                    Time_Stamp_tcu = json_data['Metabuild_Info']['Time_Stamp']
                    Version_tcu = json_data['Version']
                with open(
                        C2CtestReport_exeBackupPath + vt_files + '\ver_info.txt',
                        "r") as file:
                    json_data1 = json.load(file)
                    Meta_Build_ID_vt = json_data1['Metabuild_Info']['Meta_Build_ID']
                    Product_Flavor_vt = json_data1['Metabuild_Info']['Product_Flavor']
                    Time_Stamp_vt = json_data1['Metabuild_Info']['Time_Stamp']
                    Version_vt = json_data1['Version']
                print("TCU device - Metabuild_Info : ")
                # print(json_data)
                print("Meta_Build_ID : ", Meta_Build_ID_tcu)
                print("Product_Flavor : ", Product_Flavor_tcu)
                print("Time_Stamp : ", Time_Stamp_tcu)
                print("VT device - Metabuild_Info : ")
                # print(json_data1)
                print("Meta_Build_ID : ", Meta_Build_ID_vt)
                print("Product_Flavor : ", Product_Flavor_vt)
                print("Time_Stamp : ", Time_Stamp_vt)
            except:
                print("\n")

        elif option == "TCUVT_nonfusion":
            try:
                result1 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     tcu_adbSerialNo, "uname-a"], timeout=15)
                result2 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     tcu_adbSerialNo, "firmwareVer_tcu"], timeout=15)
                result3 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     vt_adbSerialNo, "uname-a"], timeout=15)
                result4 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     vt_adbSerialNo, "firmwareVer_vt"], timeout=15)
                with open(
                        C2CtestReport_exeBackupPath + tcu_files + '\Ver_info.txt',
                        "r") as file:
                    json_data = json.load(file)
                    Meta_Build_ID_tcu = json_data['Metabuild_Info']['Meta_Build_ID']
                    Product_Flavor_tcu = json_data['Metabuild_Info']['Product_Flavor']
                    Time_Stamp_tcu = json_data['Metabuild_Info']['Time_Stamp']
                    Version_tcu = json_data['Version']
                with open(
                        C2CtestReport_exeBackupPath + vt_files + '\ver_info.txt',
                        "r") as file:
                    json_data1 = json.load(file)
                    Meta_Build_ID_vt = json_data1['Metabuild_Info']['Meta_Build_ID']
                    Product_Flavor_vt = json_data1['Metabuild_Info']['Product_Flavor']
                    Time_Stamp_vt = json_data1['Metabuild_Info']['Time_Stamp']
                    Version_vt = json_data1['Version']
                print("TCU device - Metabuild_Info : ")
                # print(json_data)
                print("Meta_Build_ID : ", Meta_Build_ID_tcu)
                print("Product_Flavor : ", Product_Flavor_tcu)
                print("Time_Stamp : ", Time_Stamp_tcu)
                print("VT device - Metabuild_Info : ")
                # print(json_data1)
                print("Meta_Build_ID : ", Meta_Build_ID_vt)
                print("Product_Flavor : ", Product_Flavor_vt)
                print("Time_Stamp : ", Time_Stamp_vt)
            except:
                print("\n")
        elif option == deviceType_TCU:
            try:
                result1 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     tcu_adbSerialNo, "uname-a"], timeout=15)
                result2 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     tcu_adbSerialNo, "firmwareVer_tcu"], timeout=15)
                with open(
                        C2CtestReport_exeBackupPath + tcu_files + '\Ver_info.txt',
                        "r") as file:
                    json_data = json.load(file)
                    Meta_Build_ID_tcu = json_data['Metabuild_Info']['Meta_Build_ID']
                    Product_Flavor_tcu = json_data['Metabuild_Info']['Product_Flavor']
                    Time_Stamp_tcu = json_data['Metabuild_Info']['Time_Stamp']
                    Version_tcu = json_data['Version']
                print("TCU device - Metabuild_Info : ")
                # print(json_data)
                print("Meta_Build_ID : ", Meta_Build_ID_tcu)
                print("Product_Flavor : ", Product_Flavor_tcu)
                print("Time_Stamp : ", Time_Stamp_tcu)
            except:
                print("\n")
        elif option == deviceType_IVI:
            try:
                result1 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     ivi_adbSerialNo, "uname-a"], timeout=15)
                result2 = subprocess.call(
                    [C2CtestData_batchPath + r'C2C_adbCommands.bat',
                     ivi_adbSerialNo, "firmwareVer"], timeout=15)
                with open(
                        C2CtestReport_exeBackupPath + ivi_files + '\Ver_info.txt',
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
                print("\n")
    except:
        print("Something went wrong, pls check logs")


def ipAddress(self):
    filename = C2CtestData_batchPath + r'ipAddressTCU.txt'
    filename = glob.glob(filename)
    filename = max(filename, key=os.path.getctime)
    with open(filename, 'r') as givenfilecontent:
        filelines = givenfilecontent.readlines()
        if filelines[1].find('netmask') >= 0:
            filelines = filelines[1]
            ipAddTCU = filelines.split('netmask')
            ipAddress_tcu = ipAddTCU[0].replace('inet', '').replace(' ', '')
        elif filelines[1].find('Bcast:') >= 0:
            filelines = filelines[1]
            try:
                ipAddress_tcu = str(filelines.split('Bcast:')[0])
                ipAddress_tcu = ipAddress_tcu.replace('inet', '').replace(' ', '')
                ipAddress_tcu = ipAddress_tcu.replace('addr:', '')
            except:
                ipAddress_tcu = ipAddress_tcu.replace('inet addr:', '')
        else:
            filelines = filelines[2]
            ipAddTCU = filelines.split('netmask')
            ipAddress_tcu = ipAddTCU[0].replace('inet', '').replace(' ', '')
        print(ipAddress_tcu)
    return ipAddress_tcu


# ===========================================================================================
# Validate feature list for TCU & VT devices
# ===========================================================================================
def featureList(self, deviceType, featureId, featureName):
    list_cld = ''
    if deviceType == deviceType_TCU:
        path = C2CtestReport_exeBackupPath + tcu_files + '\licenses'
    elif deviceType == deviceType_VT:
        path = C2CtestReport_exeBackupPath + vt_files + '\licenses'
    file_type = r'\*pfm'
    files = glob.glob(path + file_type)
    directory = os.listdir(path)
    if len(directory) == 0:
        # print("Empty directory")
        fileExist = False
    else:
        # print("Not empty directory")
        fileExist = True
    if fileExist == True:
        max_file = max(files, key=os.path.getctime)
        # print(max_file)
        max_file1 = max_file

        # Both the variables would contain time
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(max_file)
        ti_m = os.path.getmtime(max_file)

        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)
        m_ti = time.ctime(ti_m)
        max_file = max_file.replace(path, '')
        max_file = max_file.replace(c_ti, '')
    output1 = open(path + max_file, "r")
    output1 = output1.read()
    # print(output1)

    if str(featureId) in output1:
        print(f"Feature Id : '{featureId}' is present in newly installed license file on device")
    else:
        list_cld == "Not Same"
        print(f"Feature Id : '{featureId}' is not present in newly installed license file on device")

    if featureName in output1:
        print(f"Feature Name : '{featureName}' is present in newly installed license file on device")
    else:
        list_cld == "Not Same"
        print(f"Feature Name : '{featureName}' is not present in newly installed license file on device")

    if list_cld == "Not Same":
        testResult(self, "verificationFailed",
                   "Validate that feature is installed on device w.r.t Cloud DB feature list",
                   "Feature is not installed on device. Refer cloud and device feature list below")
    return output1


def validateFeatureList(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    vinNo = readVINno(self)  # VINQCOMTCU0000644

    list_dev_tcu = list_cld_tcu = list_dev_vt = list_cld_vt = ''

    response_body = smpServer_getVINdetails(self, str(vinNo))
    saveAPIrespIntoFile("featureList_" + str(vinNo), response_body, FeatureUpdateByGroup_option)

    tcu_list_cld = tcu_list_dev = tcu_cldFeature_notPresent_devLic = tcu_devFeature_notPresen_incld = []
    vt_list_cld = vt_list_dev = vt_cldFeature_notPresent_devLic = vt_devFeature_notPresen_incld = []
    for i in range(3):
        try:
            deviceType = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][i]["chipsetInfo"][0]["chipsetType"]
            if deviceType == c2c_tcu_chipset:
                dtcu = i
            if comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                if deviceType == c2c_vt_chipset:
                    dvt = i
            if comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                if deviceType == c2c_ivi_chipset or deviceType == c2c_ivi_chipset1:
                    divi = i
            if deviceType == None:
                break
        except:
            print("")
    chipsetType1 = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["chipsetType"]
    if chipsetType1 == c2c_tcu_chipset or chipsetType1 == defaultchipsetType:
        cldskuId_tcu = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
            "skuId"]
        cldskuName_tcu = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
            "skuName"]
        cldprogramId_tcu = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["programId"]

        devSkuId = str(SkuId).replace('sku_id=', '')
        devPrgmId = str(PrgmId).replace('program_id=', '')

        print("=============================================================")
        print("Validate SKU Id for TCU device : ")
        print("-------------------------------------------------------------")

        if cldskuId_tcu == int(devSkuId) and cldprogramId_tcu == int(devPrgmId):
            testResult(self, "passed", "Validate TCU chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "TCU Chipset metadata in Cloud DB is same as that of configured in conf files on device")
            print("TCU skuId in Cloud DB : ", cldskuId_tcu)
            print("TCU skuName in Cloud DB : ", cldskuName_tcu)
            assert True
        else:
            testResult(self, "verificationFailed",
                       "Validate TCU chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "TCU Chipset metadata in Cloud DB is not same as that of configured in the conf files on device")
            print(" => Device Chipset Metadata details : ", SkuId, PrgmId)
            print(" => Chipset Metadata details in Cloud DB : ", 'sku_id=' + str(cldskuId_tcu),
                  'program_id=' + str(cldprogramId_tcu))
            # assert False
        print("\n-------------------------------------------------------------")
        print("Validate all cloud DB feature Id's present in license file(s) : ")
        print("-------------------------------------------------------------")
        featureInfo = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
            "featureInfo"]
        len_feat = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
                           "featureInfo"])
        for i in range(len_feat):
            try:
                featureId = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureId"]
                featureName = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureName"]
                tcu_list_cld.append(featureId)
                print(" => cld_featureId_" + str(i) + ": ", featureId)
                licFile = featureList(self, deviceType_TCU, featureId, featureName)
                if featureId == None:
                    break
            except:
                break
        len_feat1 = len(
            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["alaCarteInfo"][
                "features"])
        for i in range(len_feat1):
            try:
                alaCarteFeatureId = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["alaCarteInfo"][
                        "features"][i]["featureId"]
                alaCarteFeatureName = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dtcu]["chipsetInfo"][0]["alaCarteInfo"][
                        "features"][i]["featureName"]
                print("alafeatureId_" + str(i) + ": ", alaCarteFeatureId)
                featureList(self, deviceType_TCU, alaCarteFeatureId, alaCarteFeatureName)
                if alaCarteFeatureId == None:
                    break
            except:
                licFile = ''
                break
    print("\n-------------------------------------------------------------")
    print("Validate License file feature Id's present in cloud DB feature list : ")
    print("-------------------------------------------------------------")
    filedata = licFile.split('"licenseFeaturesIds" : [ ')[1]
    tcu_list_dev = filedata.split(' ],  "licenseHardwareVersions"')[0].replace('"', '').split(',')
    noOfIds = len(tcu_list_dev)
    # print(tcu_list_cld)
    for i in range(noOfIds):
        print(" => devLic_featureId_" + str(i) + ": ", tcu_list_dev[i])
        if int(tcu_list_dev[i]) in tcu_list_cld:
            print('feature id : ' + tcu_list_dev[i] + ' exists in cloud DB feature id list')
        else:
            list_dev_tcu = "Not Same"
            print('feature id : ' + tcu_list_dev[i] + ' does not exists in cloud DB feature id list')

    print("\n-------------------------------------------------------------")
    print("TCU Feature list validation result : ")
    print("-------------------------------------------------------------")
    if list_dev_tcu == "Not Same" or list_cld_tcu == "Not Same":
        testResult(self, "verificationFailed",
                   "Validate TCU feature list installed on device w.r.t Cloud DB feature list",
                   "Cloud & Device feature list is not same. Please find below the list of cloud & device side feature id's ")
    else:
        testResult(self, "passed", "Validate TCU feature list installed on device w.r.t Cloud DB feature list",
                   "Cloud & Device feature list is same. Please find below the list of cloud & device side feature id's ")

    print(' => Cloud Feature List for TCU device : ', tcu_list_cld)
    print(' => Device Feature List for TCU device : ', tcu_list_dev)
    # print("-------------------------------------------------------------")
    if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVT == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        chipsetType = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["chipsetType"]
        if chipsetType == VT_chipsetType or chipsetType == c2c_vt_chipset:
            cldskuId_vt = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
                "skuId"]
            cldskuName_vt = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
                "skuName"]
            cldprogramId_vt = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["programId"]

            devSkuId_vt = str(VT_SkuId).replace('sku_id=', '')
            devPrgmId_vt = str(VT_PrgmId).replace('program_id=', '')

        print("\n=============================================================")
        print("Validate SKU Id for VT device : ")
        print("-------------------------------------------------------------")
        if cldskuId_vt == int(devSkuId_vt) and cldprogramId_vt == int(devPrgmId_vt):
            testResult(self, "passed", "Validate VT chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "VT Chipset metadata in Cloud DB is same as that of configured in conf files on device ")
            print("VT skuId in Cloud DB : ", cldskuId_vt)
            print("VT skuName in Cloud DB : ", cldskuName_vt)
            assert True
        else:
            testResult(self, "verificationFailed",
                       "Validate VT chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "VT Chipset metadata in Cloud DB is not same as that of configured in the conf files on device ")
            print(" => Device Chipset Metadata details : ", VT_SkuId, VT_PrgmId)
            print(" => Chipset Metadata details in Cloud DB : ", 'sku_id=' + str(cldskuId_vt),
                  'program_id=' + str(cldprogramId_vt))

        print("\n-------------------------------------------------------------")
        print("Validate all cloud DB feature Id's present in license file(s) : ")
        print("-------------------------------------------------------------")
        featureInfo = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
            "featureInfo"]
        feat_len = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
                           "featureInfo"])
        for i in range(feat_len):
            try:
                featureId = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureId"]
                featureName = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureName"]
                vt_list_cld.append(featureId)
                print(" => cld_featureId_" + str(i) + ": ", featureId)
                licFile_vt = featureList(self, deviceType_VT, featureId, featureName)
                if featureId == None:
                    break
            except:
                licFile_vt = ''
                break
        al_len = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0][
                         "alaCarteInfo"][
                         "features"])
        for i in range(al_len):
            try:
                alaCarteFeatureId = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0][
                        "alaCarteInfo"][
                        "features"][i]["featureId"]
                alaCarteFeatureName = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][dvt]["chipsetInfo"][0][
                        "alaCarteInfo"][
                        "features"][i]["featureName"]
                print("alafeatureId_" + str(i) + ": ", alaCarteFeatureId)
                featureList(self, deviceType_VT, alaCarteFeatureId, alaCarteFeatureName)
                if alaCarteFeatureId == None:
                    break
            except:
                break
        print("\n-------------------------------------------------------------")
        print("Validate License file feature Id's present in cloud DB feature list : ")
        print("-------------------------------------------------------------")
        filedata_vt = licFile_vt.split('"licenseFeaturesIds" : [ ')[1]
        vt_list_dev = filedata_vt.split(' ],  "licenseHardwareVersions"')[0].replace('"', '').split(',')
        noOfIds = len(vt_list_dev)
        # print(vt_list_cld)
        for i in range(noOfIds):
            print(" => devLic_featureId_" + str(i) + ": ", vt_list_dev[i])
            if int(vt_list_dev[i]) in vt_list_cld:
                print('feature id : ' + vt_list_dev[i] + ' exists in cloud DB feature id list')
            else:
                list_dev_vt = "Not Same"
                print('feature id : ' + vt_list_dev[i] + ' does not exists in cloud DB feature id list')
        print("\n-------------------------------------------------------------")
        print("VT Feature list validation result : ")
        print("-------------------------------------------------------------")
        if list_dev_vt == "Not Same" or list_cld_vt == "Not Same":
            testResult(self, "verificationFailed",
                       "Validate VT feature list installed on device w.r.t Cloud DB feature list",
                       "Cloud & Device feature list is not same. Please find below the list of cloud & device side feature id's ")
        else:
            testResult(self, "passed", "Validate VT feature list installed on device w.r.t Cloud DB feature list",
                       "Cloud & Device feature list is same. Please find below the list of cloud & device side feature id's ")
        print(' => Cloud Feature List for VT device : ', vt_list_cld)
        print(' => Device Feature List fro VT device : ', vt_list_dev)
        print("-------------------------------------------------------------")

    if comboDeviceOnboarding_TCUIVI == "Yes" or comboDeviceOnboarding_TCUIVIVT == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        chipsetType = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["chipsetType"]
        if chipsetType == c2c_ivi_chipset or chipsetType == c2c_ivi_chipset1 or chipsetType == IVI_chipsetType:
            cldskuId_ivi = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["skuInfo"][
                "skuId"]
            cldskuName_ivi = \
                response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["skuInfo"][
                    "skuName"]
            cldprogramId_ivi = response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["programId"]

            devSkuId_ivi = str(IVI_SkuId).replace('sku_id=', '')
            devPrgmId_ivi = str(IVI_PrgmId).replace('program_id=', '')
        print("\n=============================================================")
        print("Validate SKU Id for IVI device : ")
        print("-------------------------------------------------------------")

        if cldskuId_ivi == int(devSkuId_ivi) and cldprogramId_ivi == int(devPrgmId_ivi):
            testResult(self, "passed", "Validate IVI chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "IVI Chipset metadata in Cloud DB is same as that of configured in conf files on device")
            print("IVI skuId in Cloud DB : ", cldskuId_ivi)
            print("IVI skuName in Cloud DB : ", cldskuName_ivi)
            assert True
        else:
            testResult(self, "verificationFailed",
                       "Validate IVI chipset metadata(Sku Id) in Cloud DB w.r.t device conf file",
                       "IVI Chipset metadata in Cloud DB is not same as that of configured in the conf files on device")
            print(" => Device Chipset Metadata details : ", SkuId, PrgmId)
            print(" => Chipset Metadata details in Cloud DB : ", 'sku_id=' + str(cldskuId_tcu),
                  'program_id=' + str(cldprogramId_tcu))
        print("\n-------------------------------------------------------------")
        print("IVI feature id list : ")
        print("-------------------------------------------------------------")
        featureInfo_len = len(
            response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["skuInfo"][
                "featureInfo"])

        for i in range(featureInfo_len):
            try:
                featureId_ivi = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureId"]
                featureName_ivi = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0]["skuInfo"][
                        "featureInfo"][i]["featureName"]
                print("cld_featureId_" + str(i) + ": ", featureId_ivi)
                print("cld_featureName_" + str(i) + ": ", featureName_ivi)

                # featureList(self, deviceType_IVI, featureId_ivi, featureName_ivi)

                if featureId_ivi == None:
                    break
            except:
                break
        al_len2 = len(response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0][
                          "alaCarteInfo"]["features"])
        for i in range(al_len2):
            try:
                alaCarteFeatureId_ivi = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0][
                        "alaCarteInfo"][
                        "features"][i]["featureId"]
                alaCarteFeatureName_ivi = \
                    response_body["vehicles"][0]["vehicleInfo"]["deviceInfo"][divi]["chipsetInfo"][0][
                        "alaCarteInfo"][
                        "features"][i]["featureName"]
                print("alafeatureId_" + str(i) + ": ", alaCarteFeatureId_ivi)
                # featureList(self, deviceType_IVI, alaCarteFeatureId_ivi, alaCarteFeatureName_ivi)
                if alaCarteFeatureId_ivi == None:
                    break
            except:
                break
    print("-------------------------------------------------------------")


# ===================================
# Flash ecrm image on TCU device
# ===================================

def flashECRMimage_TCU(self, tcu_type):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_flashingECRMbuild_TCU.bat',
             tcu_adbSerialNo, tcu_type])
        time.sleep(10)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_flashingECRMbuild_TCU.bat' does not exist or incorrect file path/name")


# ===================================
# Flash ecrm image on VT device
# ===================================

def flashECRMimage_VT(self):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_flashingECRMbuild_VT.bat',
             vt_adbSerialNo])
        time.sleep(10)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_flashingECRMbuild_VT.bat' does not exist or incorrect file path/name")


# ===================================
# Flash ecrm image on IVI device
# ===================================

def flashECRMimage_IVI(self):
    try:
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_flashingECRMbuild_IVI.bat',
             ivi_adbSerialNo])
        time.sleep(10)
    except FileNotFoundError:
        print(f"Sorry, the file 'C2C_flashingECRMbuild_IVI.bat' does not exist or incorrect file path/name")


# =======================================
# Set internet connectivity on device
# =======================================

def connectivityCheck(self, device, network_type):
    try:
        proc = subprocess.Popen(['adb', '-s', device, 'shell', 'ping -c 3 8.8.8.8'], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        output, errors = proc.communicate()
        proc.wait()
        outputer = output.decode('utf-8')
        # print(f"=> Ping response : {format(outputer)}")
        # print("\n=> Ping response : \n", output)
    except OSError:
        print(f"Sorry, Something went wrong while reading ping response")
        outputer = "Network is unreachable"
    except:
        outputer = subprocess.call(
            [C2CtestData_batchPath + r'C2C_adbCommands.bat',
             device, "connectivityCheck"], text=True)
    print(f"=> Ping response : {format(outputer)}")
    return outputer


def estabilishInternetConnectivity(self, device, network_type):
    print("\n==========================================================")
    print(f"Network Connectivity on {device} device")
    print("==========================================================")
    if device == deviceType_TCU:
        device_adbSerialNo = tcu_adbSerialNo
    elif device == deviceType_IVI:
        device_adbSerialNo = ivi_adbSerialNo
    elif device == deviceType_VT:
        device_adbSerialNo = vt_adbSerialNo
    try:
        response_1 = connectivityCheck(self, device_adbSerialNo, network_type)
        if "icmp_seq=2" in response_1:
            print(f"Network connectivity is already established on {device} device")
        elif "icmp_seq=2" not in response_1 or 'Network is unreachable' in response_1:
            subprocess.call(
                [C2CtestData_batchPath + r'C2C_setupNetwork.bat',
                 device_adbSerialNo, network_type], timeout=90)
            time.sleep(10)
            response_2 = connectivityCheck(self, device_adbSerialNo, network_type)
            if "icmp_seq=2" in response_2:
                print(f"{network_type} network connectivity is established on {device} ")
            else:
                print(f"{network_type} network connectivity is not established on {device} ")
    except FileNotFoundError:
        print(f"Sorry, the file does not exist or incorrect file path/name")
    except:
        response_2 = connectivityCheck(self, device_adbSerialNo, network_type)
        if "icmp_seq=2" in response_2:
            print(f"{network_type} network connectivity is established on {device} ")
        else:
            print(f"{network_type} network connectivity is not established on {device} ")


def setInternetConnectivity(self, onboarding_Type, network_type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    if singleDeviceOnboarding_TCU == "Yes":
        estabilishInternetConnectivity(self, deviceType_TCU, "Ethernet")
    elif comboDeviceOnboarding_TCUVT_fusion == "Yes":
        estabilishInternetConnectivity(self, deviceType_VT, "Ethernet")
    elif comboDeviceOnboarding_TCUIVI == "Yes":
        estabilishInternetConnectivity(self, deviceType_TCU, "Ethernet")
        estabilishInternetConnectivity(self, deviceType_IVI, "Ethernet")
    elif comboDeviceOnboarding_TCUVT == "Yes":
        estabilishInternetConnectivity(self, deviceType_TCU, "Ethernet")
        estabilishInternetConnectivity(self, deviceType_VT, "Ethernet")
    elif comboDeviceOnboarding_TCUIVIVT == "Yes":
        estabilishInternetConnectivity(self, deviceType_TCU, "Ethernet")
        estabilishInternetConnectivity(self, deviceType_VT, "Ethernet")
        estabilishInternetConnectivity(self, deviceType_IVI, "Ethernet")
    elif comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        estabilishInternetConnectivity(self, deviceType_VT, "Ethernet")
        estabilishInternetConnectivity(self, deviceType_IVI, "Ethernet")

    else:
        print("Incorrect input")


def licensecleanup(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    if singleDeviceOnboarding_TCU == "Yes":
        vinNo = readVINno(self)
        print("------------------------------------------------")
        print("License Cleanup for VIN : ", vinNo)

        # Arrange: Test data (url,header and payload) for POST request
        # licensecleanup_url = BaseUrl_reg + "/licensecleanup/deleteLicense?vin=" + vinNo + "&system=TCU"
        time.sleep(5)

        response_body = license_cleanup(self, vinNo)

        # Save response full body as text in a file
        saveAPIrespIntoFile("licenseClean", response_body, DeviceOnboarding_option)

        # Assert: Validate response status code and body contents

        if '0 records deleted' not in response_body:
            testResult(self, "passed",
                       "License records should be deleted successfully",
                       "License records deleted successfully")
        else:
            testResult(self, "verificationFailed",
                       "License records should be deleted successfully",
                       "License records deleted successfully or does not have any records to delete")


# ===========================================================================================
# Device Replacement
# ===========================================================================================

def deviceReplacement(self, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])

    if singleDeviceOnboarding_TCU == "Yes":
        subprocess.call(
            [C2CtestData_batchPath + r'C2C_deviceReplacement.bat',
             tcu_adbSerialNo, deviceType_TCU], timeout=10)
        testResult(self, "passed",
                   "Device should be setup with c2c files",
                   "Device is setup with c2c files")


# ===========================================================================================
# Feature update for removal of exiting feature license from TCU/IVI device
# ===========================================================================================

def triggerFeatureUpdate_remove(self, device, onboarding_Type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_TCU = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    random_id = ' '.join([str(random.randint(10, 9999)).zfill(5) for _ in range(1)])

    newGroupName = "featureUpdate_" + random_id

    # Arrange: Test data (url,header and payload) for POST request

    try:
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            pullFilesFromDevice(self, DeviceOnboarding_tcuvt_fusion_FeatUp_option, onboarding_Type)
            # saveVIN(self, onboarding_Type)
        else:
            pullFilesFromDevice(self, DeviceOnboarding_option, onboarding_Type)
            # saveVIN(self, onboarding_Type)
        states = checkChipsetAndSystemState(self, onboarding_Type)
        vinNo = states[2]
        saveVIN(self, onboarding_Type)

    except:
        vinNo = readVINno(self)

    if device == deviceType_IVI:
        restartServices(self, deviceType_IVI, onboarding_Type)

    # print("=============================================================")
    print("Triggering Feature Update by creating new Group on onboarded Vin " + device + " - Device : ", vinNo)
    print("=============================================================")

    response_body = smpServer_createGroup(self, newGroupName, vinNo)
    saveAPIrespIntoFile("FU_CreateNewGroup_removal_" + str(device), response_body, FeatureUpdateByGroup_option)

    groupId = response_body["groupResponse"]["groupId"]

    print("=============================================================")
    print("Newly created Group Name is : ", newGroupName)
    print("Newly created Group Id is : ", groupId)
    print("=============================================================")

    response_body = smpServer_GetFilterValuesbyGroup(self, groupId)

    saveAPIrespIntoFile("FU_getFilterValuesbyGroup_removal_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    if device == deviceType_TCU:
        try:
            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")
        try:
            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
            if response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_tcu_chipset:
                pvChipsetSpId = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for TCU device => ", pvChipsetSpId)
        print("----------------------------------------------------")

    elif device == deviceType_VT:

        try:
            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")
        try:
            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
            elif response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "chipset"]
                pvChipsetsp_vt = \
                    response_body["response"]["systemsData"][1]["programs"][1]["programVersions"][0]["chipsetSps"][0][
                        "sp"]
        except:
            print("\n")
        try:

            if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                "chipset"] == VT_chipsetType or \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"] == c2c_vt_chipset:
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "pvChipsetSpId"]
                pvChipset_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "chipset"]
                pvChipsetSpId_vt = \
                    response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][1][
                        "sp"]
        except:
            print("\n")

        print("----------------------------------------------------")
        print("pvChipsetSpId for VT device => ", pvChipsetSpId_vt)
        print("----------------------------------------------------")

    elif device == deviceType_IVI:
        if response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
            "chipset"] == IVI_chipsetType or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset1 or \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"] == c2c_ivi_chipset:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
            pvChipset_ivi = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"]
            pvChipsetsp_ivi = \
                response_body["response"]["systemsData"][1]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "sp"]
            # print(pvChipsetsp_ivi")
        else:
            pvChipsetSpId = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "pvChipsetSpId"]
            pvChipset_ivi = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "chipset"]
            pvChipsetsp_ivi = \
                response_body["response"]["systemsData"][0]["programs"][0]["programVersions"][0]["chipsetSps"][0][
                    "sp"]
        print("-------------------------------------------------------------------")
        print("pvChipsetSpId for IVI device => ", pvChipsetSpId)
        print("-------------------------------------------------------------------")

    if device == deviceType_TCU or device == deviceType_IVI:
        response_body = smpServer_GetFeaturesforselectedFilters(self, pvChipsetSpId, groupId)
    if device == deviceType_VT:
        response_body = smpServer_GetFeaturesforselectedFilters(self, pvChipsetSpId_vt, groupId)

    saveAPIrespIntoFile("FU_getFeatForSelectedFilters_removal_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    if device == deviceType_TCU or device == deviceType_VT:
        print("=============================================================")
        print("Old License file details : ")
        print("=============================================================")

        if device == deviceType_TCU:
            if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
                OldLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_FeatUp_option,
                                               onboarding_Type)
            else:
                OldLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_option, onboarding_Type)
        elif device == deviceType_VT:
            OldLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_vt_option, onboarding_Type)
        if device == deviceType_TCU or device == deviceType_VT:
            print("Old License File Name : ", OldLicense[0])
            print("\n")
            print("Old License File timestamp : ", OldLicense[1])
            print("\n")
            print(OldLicense[2])
            output = open(OldLicense[2], "r")
            output = output.read()

        try:
            print("----------------------------------------------------")
            print("Installed Feature Check : ")
            print("----------------------------------------------------")
            is_looping = True
            len_featureAreaList = len(response_body["response"]["functionalAreaList"])
            for i in range(len_featureAreaList):
                len_featureList = len(response_body["response"]["functionalAreaList"][i]["featureList"])
                for j in range(len_featureList):
                    featureID = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureId"]
                    featureName = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureName"]
                    isBundle = response_body["response"]["functionalAreaList"][i]["featureList"][j]["bundle"]
                    description = response_body["response"]["functionalAreaList"][i]["featureList"][j]["description"]
                    vehiclesAlreadyInstalledThis = response_body["response"]["functionalAreaList"][i]["featureList"][j][
                        "vehiclesAlreadyInstalledThis"]
                    # print(vehiclesAlreadyInstalledThis)
                    featureID = str(featureID)
                    if str(featureID) not in output and featureName not in output or vehiclesAlreadyInstalledThis == 0:
                        print(
                            f"Feature Id : '{featureID}' : '{featureName}' is not present in existing/available license file on device")
                    else:
                        print(
                            f"Feature Id : '{featureID}' : '{featureName}' is present in existing/available license file on device")
                        numb = i
                        numb1 = j
                        is_looping = False
                        break
                if is_looping == False:
                    break
            # print("----------------------------------------------------")
            featureID = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["bundle"]
            description = response_body["response"]["functionalAreaList"][numb]["featureList"][numb1]["description"]
            featureID = str(featureID)
            # print("----------------------------------------------------")
        except:
            print("Selecting available feature for validating feature update functionality ")
            featureID = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][0]["featureList"][0]["bundle"]
            description = response_body["response"]["functionalAreaList"][0]["featureList"][0]["description"]
            featureID = str(featureID)

    if device == deviceType_IVI:
        print("----------------------------------------------------")
        print("Installed Feature Check : ")
        print("----------------------------------------------------")
        try:
            is_looping = True
            len_featureAreaList_ivi = len(response_body["response"]["functionalAreaList"])
            for i in range(len_featureAreaList_ivi):
                len_featureList_ivi = len(response_body["response"]["functionalAreaList"][i]["featureList"])
                for j in range(len_featureList_ivi):
                    vehiclesAlreadyInstalledThis = response_body["response"]["functionalAreaList"][i]["featureList"][j][
                        "vehiclesAlreadyInstalledThis"]
                    featureID = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureId"]
                    featureName = response_body["response"]["functionalAreaList"][i]["featureList"][j]["featureName"]
                    # print(featureID,featureName,vehiclesAlreadyInstalledThis)
                    if vehiclesAlreadyInstalledThis == 1 or vehiclesAlreadyInstalledThis == "1":
                        num = i
                        num1 = j
                        featureID = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "featureId"]
                        featureName = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "featureName"]
                        isBundle = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["bundle"]
                        description = response_body["response"]["functionalAreaList"][num]["featureList"][num1][
                            "description"]
                        featureID = str(featureID)
                        is_looping = False
                        break
                    else:
                        print(f"feature {featureID} : {featureName} is not present/installed on device")
                if is_looping == False:
                    break
            featureID = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["bundle"]
            description = response_body["response"]["functionalAreaList"][num]["featureList"][num1]["description"]
            featureID = str(featureID)
            print("----------------------------------------------------")

            # print("featureID selected for IVI device :", featureID)
        except:
            featureID = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureId"]
            featureName = response_body["response"]["functionalAreaList"][0]["featureList"][0]["featureName"]
            isBundle = response_body["response"]["functionalAreaList"][0]["featureList"][0]["bundle"]
            description = response_body["response"]["functionalAreaList"][0]["featureList"][0]["description"]
            featureID = str(featureID)

    print("------------------------------------------------------------------------------------------------")
    print("The feature to be removed from " + device + " device => ", "featureID : " + featureID,
          "featureName : " + featureName)
    print("------------------------------------------------------------------------------------------------")

    action = "REMOVE_FROM_ALL"

    if device == deviceType_TCU:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId, "Telematics",
                                                           pvChipset,
                                                           pvChipsetsp, featureID, featureName, isBundle, device,
                                                           action)

    elif device == deviceType_VT:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId_vt, "Telematics",
                                                           pvChipset_vt,
                                                           pvChipsetsp_vt, featureID, featureName, isBundle, device,
                                                           action)

    elif device == deviceType_IVI:
        response_body = smpServer_SendUpdateFeatureRequest(self, groupId, newGroupName, pvChipsetSpId, deviceType_IVI,
                                                           pvChipset_ivi,
                                                           pvChipsetsp_ivi, featureID, featureName, isBundle, device,
                                                           action)

    saveAPIrespIntoFile("FU_TriggerFeatureUpdate_removal_" + str(device), response_body,
                        FeatureUpdateByGroup_option)

    print("Triggered Feature Update by creating new Group on onboarded Vin" + device + " - Device : ", vinNo)
    print("Triggered Feature Update by creating new Group on onboarded Vin" + device + " - Device : ", vinNo)
    time.sleep(60)

    if device == deviceType_TCU:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        if comboDeviceOnboarding_TCUVT_fusion == "Yes" or comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
            NewLicense = getLicenseDetails(self, "LicenseFile", DeviceOnboarding_tcuvt_fusion_FeatUp_option,
                                           onboarding_Type)
            # print("New License File : ", NewLicense[0], NewLicense[1])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")
        else:
            NewLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_option, onboarding_Type)
            # print("New License File Name : ", NewLicense[0])
            # print("\n")
            # print("New License File timestamp : ", NewLicense[1])
            print("\n")
    if device == deviceType_VT:
        print("=============================================================")
        print("New License file details : ")
        print("=============================================================")
        NewLicense = getLicenseDetails(self, "LicenseFile", FeatureUpdateByGroup_vt_option, onboarding_Type)
        # print("New License File Name : ", NewLicense[0])
        # print("\n")
        # print("New License File timestamp : ", NewLicense[1])
        print("\n")

    status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)

    if device == deviceType_TCU or device == deviceType_VT:
        # status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)
        # Compare/verify old and new license files on TCU device
        print("=============================================================")
        if NewLicense[0] != OldLicense[0] or status == "100" or status == 100:
            testResult(self, "passed",
                       "Selected feature license should be removed/uninstalled on device successfully and SMP UI should show 100% delivered status",
                       "Selected feature license is successfully removed/uninstalled on " + device + " device and SMP UI shows 100% delivered status")

        else:
            testResult(self, "failed",
                       "Selected feature license should be removed/uninstalled on device successfully and SMP UI should show 100% delivered status",
                       "Selected feature license is not removed/uninstalled on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")

            assert (NewLicense[0] != OldLicense[0])
        # print("=============================================================")

        output1 = open(NewLicense[2], "r")
        output1 = output1.read()
        # print(output1)

        print("------------------------------------------------------------------------------------------------")

        if str(featureID) in output1:
            print(f"Feature Id : '{featureID}' is present in newly installed license file on device")
        else:
            print(f"Feature Id : '{featureID}' is not present in newly installed license file on device")

        if featureName in output1:
            print(f"Feature Name : '{featureName}' is present in newly installed license file on device")
        else:
            print(f"Feature Name : '{featureName}' is not present in newly installed license file on device")
        print("------------------------------------------------------------------------------------------------")
    # status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)

    if device == deviceType_IVI:
        status = getFeatureUdateList(self, FeatureUpdateByGroup_option, newGroupName)
        if status == "100" or status == 100:
            testResult(self, "passed",
                       "Selected feature license should be removed/uninstalled on device successfully  and SMP UI should show 100% delivered status",
                       "Selected feature license is successfully removed/uninstalled on " + device + " device and SMP UI shows 100% delivered status")
        else:
            testResult(self, "failed", "Selected feature license should be removed/uninstalled on device successfully ",
                       "Selected feature license is not removed/uninstalled on " + device + " device or record is not listed in first page/10 records on SMP UI. Refer logs and api response for additional details")

    # Get VIN details and SKU updated list to verify delivered status

    response_body = smpServer_getVINdetails(self, str(vinNo))
    saveAPIrespIntoFile("FeatureUpdateByVINdetails_" + str(device), response_body, FeatureUpdateByGroup_option)


# ===========================================================================================
# Fetch interval time for stability check
# ===========================================================================================

def stability_fetchIntervalTime(self, device):
    if device == deviceType_TCU:
        if stability_intervalTime_flag_TCU == "Yes":
            intervalTime_TCU = int(stability_intervalTime_TCU)
        else:
            intervalTime_TCU = 30
    return intervalTime_TCU


if __name__ == '__main__':
    print("\n")
