import glob
import inspect
import os
import os.path
import sys
from datetime import datetime

import openpyxl

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

sys.path.insert(1, r'C:\Car2Cloud_E2ETesting')
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

# ===============================
# Test folder Path
# ===============================
folderPath = r'C:\Car2Cloud_E2ETesting' + '\\'
C2CtestData_batchPath1 = folderPath + r'C2CtestData\usr\local\C2Cbat' + '\\'
C2CtestData_batchPath = parent_dir + '\\' + r'DeviceCommandFiles\batch_files' + '\\' + 'coreC2C' + '\\'
C2CtestData_jsonPath = folderPath + r'C2CtestData\usr\local\json' + '\\'
C2CtestData_c2c2Path = folderPath + r'C2CtestData\usr\local\c2c' + '\\'
C2CtestData_certsPath = folderPath + r'C2CtestData\usr\local\certs' + '\\'
C2CtestData_DepPackagePath = folderPath + r'C2CtestData\usr\local\deploymentPackages' + '\\'
C2CtestData_iviconfNewPath = folderPath + r'C2CtestData\usr\local\iviconfNew' + '\\'
C2CtestData_vtconfNewPath = folderPath + r'C2CtestData\usr\local\vtconfNew' + '\\'
C2CtestData_vtconfNew_c2cPath = C2CtestData_vtconfNewPath + r'c2c'
C2CtestReport_exeBackupPath = folderPath + r'C2CtestReport\e2eExecution_Backup' + '\\'

C2CtestReport_APIresponsesPath = C2CtestReport_exeBackupPath + r'API_responses' + '\\'
C2CtestReport_c2cLogsPath = C2CtestReport_exeBackupPath + r'c2cLogs' + '\\'
C2CtestReport_DeviceOnbrdng_backupPath = C2CtestReport_exeBackupPath + r'DeviceOnboarding_backup' + '\\'
C2CtestReport_otaPath = C2CtestReport_exeBackupPath + r'OTA' + '\\'
C2CtestReport_OTA_backupPath = C2CtestReport_exeBackupPath + r'OTA_backup' + '\\'
C2CtestReport_backupPath = C2CtestReport_exeBackupPath + r'DeviceOnboarding_Pos_backup' + '\\'
C2CtestReport_NetworkStatusPath = C2CtestReport_exeBackupPath + r'NetworkStatus' + '\\'
C2CtestReport_SKUupdateByGroupPath = C2CtestReport_exeBackupPath + r'SKUupdateByGroup' + '\\'
C2CtestReport_FeatureUpdateByGroupPath = C2CtestReport_exeBackupPath + r'FeatureUpdateByGroup' + '\\'
C2CtestReport_SKUupdateByVINPath = C2CtestReport_exeBackupPath + r'SKUupdateByVIN' + '\\'

# print(parent_dir)
# xlsx_apiTestData_file = os.path.join(parent_dir, r'API_Testing\testData\c2c_api_test.xlsx')
payload_filepath = payloadPath = os.path.join(parent_dir, r'API_Testing\testData\payloads')
headers_filepath = os.path.join(parent_dir, r'API_Testing\testData\headers')
schema_filepath = os.path.join(parent_dir, r'API_Testing\testData\schema')
api_responseFolderPath = parent_dir + r'\API_Testing\testReports\api_responses' + '\\'

# ===============================
# Test Data File Path
# ===============================
data_file = folderPath + r'C2CtestData\c2cTestData.xlsx'
xlsx_apiTestData_file = folderPath + r'C2CtestData\API_testData.xlsx'

# ===============================
# Test Data - Sheet Names
# ===============================
api_common_data_sheetName = "API_Common_Data"
env_details_sheetName = "Env_Details"
c2c_api_data_sheetName = "C2C_API_Data"
b2c_api_data_sheetName = "B2C_API_Data"
re_api_data_sheetName = "RE_API_Data"
kafka_data_sheetName = "KAFKA"
env_data_sheetName = "ENV"

# ---------------------------------------
# Cloud Environment Test data
# ---------------------------------------
# Cloud Environment Details
GCP_QA = "GCP-QA"
GCP_QA2 = "GCP-QA2"
GCP_QA3 = "GCP-QA3"
GCP_QA4 = "GCP-QA4"
GCP_DEV = "GCP-DEV"
GCP_REP = "GCP-REP"
GCP_REP2 = "GCP-REP2"
RE_DEV = "RE-DEV"
QC_QA = "QC-QA"
QC_INTG = "QC-INTG"
GCP_PERF = "GCP-PERF"
GCP_PEN = "GCP-PEN"
GCP_DEMO2 = "GCP-DEMO2"
GCP_PERF2 = "GCP-PERF2"
GCP_UAT = "GCP-UAT"
GCP_DM1 = "GCP-DM1"
GCP_QA6 = "GCP-QA6"
GCP_QA5 = "GCP-QA5"
GCP_QA7 = "GCP-QA7"
GCP_QA8 = "GCP-QA8"
GCP_QA9 = "GCP-QA9"
GCP_QA10 = "GCP-QA10"
RE_UAT = "RE-UAT"
RE_DM1 = "RE-DM1"
PRE_PROD = "PRE-PROD"
GCP_QA2_EU = "GCP-QA2-EU"

# ---------------------------------------
# RE Cloud Environment Test data
# ---------------------------------------
# Env Array
r3_envs = ["RE_DEV_R3", GCP_REP2, GCP_PERF]
r5_envs = [GCP_QA, GCP_UAT]
r7_envs = [GCP_PEN]
r8_envs = [RE_DM1, GCP_QA6]  # Active envs -> DM1:R8S4
r8_patch1_envs = [GCP_QA3, RE_DEV]  # Active envs -> RE-INTG/DEV:R8P1
r8_patch2_envs = [GCP_QA4]
r8_patch3_envs = [GCP_QA5, PRE_PROD]  # Active envs -> QA5:R8P3SP4, PRE-PROD:R8P3

r8_patch_envs_hmac = [GCP_QA5, GCP_QA8, GCP_QA2, PRE_PROD, GCP_PERF2, GCP_DEMO2, GCP_QA9, RE_UAT,
                      GCP_DEV, GCP_QA10, GCP_QA2_EU]  # R8 patch4 - Active envs -> DM2:R8P4.4 QA8:R8P4SP7 QA10:R8P4.4 DEV:R8P4.7
# QA2:P8P4SP17 RE-UAT:R8P4, PT2:R8P4.2

gcp_envs = [GCP_REP2, GCP_PERF, GCP_QA, GCP_DEMO2, GCP_UAT, GCP_DEV, GCP_QA3, RE_DM1, RE_DEV, GCP_PEN, GCP_QA4,
            GCP_PERF2, GCP_QA6, GCP_QA5, GCP_QA7, GCP_QA8, GCP_QA2, GCP_QA9, PRE_PROD, RE_UAT, GCP_QA2_EU]

gcp_kafka_configured_envs = [GCP_QA5, GCP_QA8, GCP_QA2, GCP_DEMO2, GCP_QA9]

r8_patch4_sp17_envs = [GCP_QA2, GCP_QA2_EU]  # for change in Command control Precondition,Vehicle modes, alerts, trip etc.


# ===============================
# Read folder path
# ===============================
def commonFolderPath():
    path = folderPath
    return path


# ===============================
# Read test data from excel file
# ===============================

def testData(sheetname, rowNo, colNo):
    files = glob.glob(data_file)
    max_file = max(files, key=os.path.getctime)
    wb_obj = openpyxl.load_workbook(max_file)
    sheet_obj = wb_obj[sheetname]
    cell_obj = sheet_obj.cell(row=rowNo, column=colNo)
    return cell_obj.value


# ===================================
# Valid Test Data for test execution
# ===================================

BaseUrl_gbl = testData("DeviceOnboardingData", 18, 2)
BaseUrl_reg = testData("DeviceOnboardingData", 19, 2)

carota_backend_url = testData("DeviceOnboardingData", 21, 2)

drimaes_firm_reg = testData("FotaData_Drimaes_IVI", 2, 3)
drimaes_sota_reg = testData("SotaData_Drimaes_IVI", 2, 3)

pickDeviceId = testData("DeviceSerialNo", 2, 2)

# tcu_adbSerialNo = str(testData("DeviceSerialNo", 3, 2))
ivi_adbSerialNo = str(testData("DeviceSerialNo", 4, 2))
# vt_adbSerialNo = str(testData("DeviceSerialNo", 5, 2))

# SP validation flag
spvalidationFlag = testData("DeviceSetup", 2, 2)

pushBinariesLibrariesOnTCU = testData("DeviceSetup", 3, 2)
pushBinariesLibrariesOnIVI = testData("DeviceSetup", 4, 2)
pushBinariesLibrariesOnVT = testData("DeviceSetup", 5, 2)
pushBinariesLibrariesOnTCU_fusion = testData("DeviceSetup", 6, 2)

# Stability details
stability_intervalTime_flag_TCU = testData("DeviceSetup", 7, 2)
stability_intervalTime_TCU = testData("DeviceSetup", 7, 3)

# Device onboarding details
onboardingTypeFlag = testData("DeviceOnboardingData", 2, 2)
onboardingEnv = testData("DeviceOnboardingData", 18, 3)
tcuDevice_NAD = testData("DeviceOnboardingData", 8, 2)
deviceIdFlag = testData("DeviceOnboardingData", 9, 2)
reqDeviceId_tcu = testData("DeviceOnboardingData", 10, 2)
reqDeviceId_ivi = testData("DeviceOnboardingData", 11, 2)
vinNoFlag = testData("DeviceOnboardingData", 12, 2)
reqVinNo = testData("DeviceOnboardingData", 13, 2)
OTA_ModelFlag = testData("DeviceOnboardingData", 14, 2)
reqModelNameFlag = testData("DeviceOnboardingData", 15, 2)
reqModelName = testData("DeviceOnboardingData", 16, 2)
filepath = testData("DeviceOnboardingData", 17, 2)
tcu_brokerAddress_flag = testData("DeviceOnboardingData", 22, 2)

# SkU license Flag
skuLicenseFlag = testData("DeviceOnboardingData", 20, 2)

ex_singleDeviceOnboarding_TCU = testData("DeviceOnboardingData", 3, 2)
ex_singleDeviceOnboarding_IVI = testData("DeviceOnboardingData", 3, 2)
ex_comboDeviceOnboarding_TCUVT_fusion = testData("DeviceOnboardingData", 4, 2)
ex_comboDeviceOnboarding_TCUIVI = testData("DeviceOnboardingData", 5, 2)
ex_comboDeviceOnboarding_TCUVT = testData("DeviceOnboardingData", 6, 2)
ex_comboDeviceOnboarding_TCUIVIVT = testData("DeviceOnboardingData", 7, 2)
ex_comboDeviceOnboarding_TCUVTIVI_fusion = "No"

# Connectivity
ethernet = "Ethernet"
wifi = "WiFi"

# device combo options
DeviceOnboarding_option = "DeviceOnboarding"
DeviceOnboarding_ivi_option = 'DeviceOnboarding_ivi'
DeviceOnboarding_tcuvt_fusion_option = "DeviceOnboarding_tcuvt_fusion"
DeviceOnboarding_tcuvt_option = "DeviceOnboarding_tcuvt"
SKUupdateByVIN_option = "SKUupdateByVIN"
SKUupdateByGroup_option = "SKUupdateByGroup"
FeatureUpdateByGroup_option = "FeatureUpdateByGroup"
SKUupdateByVIN_vt_option = "SKUupdateByVIN_vt"
SKUupdateByGroup_vt_option = "SKUupdateByGroup_vt"
FeatureUpdateByGroup_vt_option = "FeatureUpdateByGroup_vt"
DeviceOnboarding_tcuvt_fusion_skuVIN_option = "DeviceOnboarding_tcuvt_fusion_skuVIN"
DeviceOnboarding_tcuvt_fusion_skuGrp_option = "DeviceOnboarding_tcuvt_fusion_skuGrp"
DeviceOnboarding_tcuvt_fusion_FeatUp_option = "DeviceOnboarding_tcuvt_fusion_FeatUp"

# Enter TCU device program details
PrgmSkuId = testData("TCUConfFileDetails", 2, 4)
SkuId = testData("TCUConfFileDetails", 3, 4)
PrgmId = testData("TCUConfFileDetails", 4, 4)
chipsetType = str(testData("TCUConfFileDetails", 5, 4)).split('=')[1]
chipsetSpVer = str(testData("TCUConfFileDetails", 6, 4)).split('=')[1]

# Enter IVI device program details
IVI_PrgmSkuId = testData("IVIConfFileDetails", 2, 4)
IVI_SkuId = testData("IVIConfFileDetails", 3, 4)
IVI_PrgmId = testData("IVIConfFileDetails", 4, 4)
IVI_chipsetType = str(testData("IVIConfFileDetails", 5, 4)).split('=')[1]
IVI_chipsetSpVer = str(testData("IVIConfFileDetails", 6, 4)).split('=')[1]

# Enter VT device program details
VT_PrgmSkuId = testData("VTConfFileDetails", 2, 4)
VT_SkuId = testData("VTConfFileDetails", 3, 4)
VT_PrgmId = testData("VTConfFileDetails", 4, 4)
VT_chipsetType = str(testData("VTConfFileDetails", 5, 4)).split('=')[1]
VT_chipsetSpVer = str(testData("VTConfFileDetails", 6, 4)).split('=')[1]

# Default mandatory conf details for text replace
defaultVIN = testData("DefaultConfFileDetails", 2, 2)
defaultSystemID = testData("DefaultConfFileDetails", 3, 2)
defaultSubSystemId = testData("DefaultConfFileDetails", 4, 2)
defaultDeviceId = testData("DefaultConfFileDetails", 5, 2)
ivi_defaultDeviceId = testData("DefaultConfFileDetails", 6, 2)
dm_defaultDeviceId = testData("DefaultConfFileDetails", 7, 2)

# Default TCU device program details for text replace
defaultPrgmSkuId = testData("TCUConfFileDetails", 2, 3)
defaultSkuId = testData("TCUConfFileDetails", 3, 3)
defaultPrgmId = testData("TCUConfFileDetails", 4, 3)
defaultchipsetType = testData("TCUConfFileDetails", 5, 3)
defaultchipsetSpVer = testData("TCUConfFileDetails", 6, 3)
defaultchipsetName = testData("TCUConfFileDetails", 7, 3)

# Default IVI device program details
defaultIVI_PrgmSkuId = testData("IVIConfFileDetails", 2, 3)
defaultIVI_SkuId = testData("IVIConfFileDetails", 3, 3)
defaultIVI_PrgmId = testData("IVIConfFileDetails", 4, 3)
defaultIVI_chipsetType = testData("IVIConfFileDetails", 5, 3)
defaultIVI_chipsetSpVer = testData("IVIConfFileDetails", 6, 3)
defaultIVI_chipsetName = testData("IVIConfFileDetails", 7, 3)

# Default VT device program details
defaultVT_PrgmSkuId = testData("VTConfFileDetails", 2, 3)
defaultVT_SkuId = testData("VTConfFileDetails", 3, 3)
defaultVT_PrgmId = testData("VTConfFileDetails", 4, 3)
defaultVT_chipsetType = testData("VTConfFileDetails", 5, 3)
defaultVT_chipsetSpVer = testData("VTConfFileDetails", 6, 3)
defaultVT_chipsetName = testData("VTConfFileDetails", 7, 3)

# TCU device Configuration ->  File Paths

sideloadedFile = C2CtestData_c2c2Path + r'side_loaded.conf'
c2cvehicleFile = C2CtestData_c2c2Path + r'c2c_vehicle.json'
car2cloudFile = C2CtestData_c2c2Path + r'car2cloud.conf'
dmconfFile = C2CtestData_c2c2Path + r'dm.conf'
c2cDefaultConfFile = C2CtestData_c2c2Path + r'c2c_default.conf'

# IVI device Configuration ->  File Paths
ivi_car2cloudFile = C2CtestData_iviconfNewPath + 'car2cloud.conf'
ivi_dmconfFile = C2CtestData_iviconfNewPath + 'dm.conf'

# VT device Configuration ->  File Paths
vt_car2cloudFile = C2CtestData_vtconfNew_c2cPath + '\\' + 'car2cloud.conf'
vt_dmconfFile = C2CtestData_vtconfNew_c2cPath + '\\' + 'dm.conf'

# ========================================
# Invalid Test Data for negative scenarios
# ========================================

invalidVIN_lessCharLen = testData("InvalidData", 2, 2)
invalidVIN_grtrCharLen = testData("InvalidData", 2, 4)
invalidVIN_withSpace = testData("InvalidData", 2, 6)
invalidVIN_withSplchar = testData("InvalidData", 2, 8)

duplicateVIN = testData("InvalidData", 3, 2)

invalidDeviceId_lessCharLen = testData("InvalidData", 4, 2)
invalidDeviceId_grtrCharLen = testData("InvalidData", 4, 4)
invalidDeviceId_withSpace = testData("InvalidData", 4, 6)
invalidDeviceId_withSplchar = testData("InvalidData", 4, 8)

invalid_systemId = testData("InvalidData", 5, 2)

invalidSubSysId_lessCharLen = testData("InvalidData", 6, 2)
invalidSubSysId_grtrCharLen = testData("InvalidData", 6, 4)
invalidSubSysId_withSpace = testData("InvalidData", 6, 6)
invalidSubSysId_withSplchar = testData("InvalidData", 6, 8)

invalidGlbUrl = testData("InvalidData", 7, 2)

devOnbrdWithRegionalUrl = testData("InvalidData", 8, 2)

dupDeviceId = testData("InvalidData", 9, 2)  # device onboarding with device id doesnot match with system id and certs

emptyVIN = emptyDeviceID = emptySystemID = emptySubSystemID = emptyUrl = emptyPrgmSkuId = emptySkuId = emptyPrgmId = emptyChipsetType = emptyChipsetName = emptychipsetSp = ""

invalidPrgmSkuId = testData("InvalidData", 15, 2)
invalidSkuId = testData("InvalidData", 16, 2)
invalidPrgmId = testData("InvalidData", 17, 2)
invalidchipsetType = testData("InvalidData", 18, 2)
invalidchipsetSp = testData("InvalidData", 19, 2)
invalidChipsetName = testData("InvalidData", 20, 2)

invalidSystemState = testData("InvalidData", 33, 2)
invalidChipsetState = testData("InvalidData", 34, 2)
invalidChipsetsCount = testData("InvalidData", 35, 2)
invalidRegionCode = testData("InvalidData", 36, 2)
invalidCountryCode = testData("InvalidData", 37, 2)
invalidDeviceState = testData("InvalidData", 38, 2)
invalidBrokerName = testData("InvalidData", 39, 2)
invalidBrokerPort = testData("InvalidData", 40, 2)

# Test Folder Path.


DeviceCommandFiles_path = parent_dir + '\\' + r'DeviceCommandFiles'
shellFile_path = parent_dir + '\\' + r'DeviceCommandFiles\shFiles'
pahoFile_path = parent_dir + '\\' + r'DeviceCommandFiles\paho_files'

# ===============================
# Drimaes Test folder Path
# ===============================
drimaes_batchPath1 = C2CtestData_batchPath + 'drimaes' + '\\'
drimaes_batchPath = parent_dir + '\\' + r'DeviceCommandFiles\batch_files' + '\\' + 'drimaes' + '\\'
drimaes_defaultConfNew = folderPath + r'C2CtestData\usr\local\drimaes_defaultConfNew' + '\\'

# ===============================
# B2C Test folder Path
# ===============================
b2c_batchPath1 = C2CtestData_batchPath + 'b2c' + '\\'
b2c_batchPath = parent_dir + '\\' + r'DeviceCommandFiles\batch_files' + '\\' + 'b2c' + '\\'
b2c_defaultConfNew = folderPath + r'C2CtestData\usr\local\b2c_defaultConfNew' + '\\'

# ===============================
# C2C Primary IVI Test folder Path
# ===============================
c2c_ivi_batchPath = C2CtestData_batchPath + 'c2c_ivi' + '\\'
c2c_ivi_defaultConfNew = folderPath + r'C2CtestData\usr\local\c2c_ivi_defaultConfNew' + '\\'

# ===============================
# Mahindra Test folder Path
# ===============================
mahindra_batchPath = parent_dir + '\\' + r'DeviceCommandFiles\batch_files' + '\\' + 'mahindra' + '\\'
mahindra_defaultConfNew = folderPath + r'C2CtestData\usr\local\mahindra_defaultConfNew' + '\\'

# ===================================
# Valid Test Data for test execution
# ===================================
tcu_adbSerialNo = str(testData("DeviceSerialNo", 3, 2))
c2c_ivi_adbSerialNo = str(testData("DeviceSerialNo", 4, 2))
vt_adbSerialNo = str(testData("DeviceSerialNo", 5, 2))
drimaes_ivi_adbSerialNo = str(testData("DeviceSerialNo", 6, 2))
b2c_ivi_adbSerialNo = str(testData("DeviceSerialNo", 7, 2))
mahindra_ivi_adbSerialNo = str(testData("DeviceSerialNo", 8, 2))

drimaes_pushBinariesLibrariesOnIVI = testData("DeviceSetup", 7, 2)
b2c_pushBinariesLibrariesOnIVI = testData("DeviceSetup", 8, 2)
c2c_pushBinariesLibrariesOnIVI = testData("DeviceSetup", 4, 2)
mahindra_pushBinariesLibrariesOnIVI = testData("DeviceSetup", 9, 2)

# ===================================
# Read Flag & path to flash images on device
# ===================================
c2c_tcu_ecrmImage_flag = c2c_tcu_hlosImage_flag = testData("DeviceSetup", 10, 2)
c2c_tcu_ecrmImage_path = c2c_tcu_hlosImage_path = testData("DeviceSetup", 10, 3)
c2c_tcu_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU\conf_files'
c2c_tcu_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU\ecrm_Image'
c2c_tcu_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU\hlos_Image'

c2c_vt_ecrmImage_flag = c2c_vt_hlosImage_flag = testData("DeviceSetup", 11, 2)
c2c_vt_ecrmImage_path = c2c_vt_hlosImage_path = testData("DeviceSetup", 11, 3)
c2c_vt_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\VT\conf_files'
c2c_vt_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\VT\ecrm_Image'
c2c_vt_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\VT\hlos_Image'

c2c_ivi_ecrmImage_flag = c2c_ivi_hlosImage_flag = testData("DeviceSetup", 12, 2)
c2c_ivi_ecrmImage_path = c2c_ivi_hlosImage_path = testData("DeviceSetup", 12, 3)
c2c_ivi_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\IVI\conf_files'
c2c_ivi_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\IVI\ecrm_Image'
c2c_ivi_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\IVI\hlos_Image'

drimaes_ecrmImage_flag = testData("DeviceSetup", 13, 2)
drimaes_ecrmImage_path = testData("DeviceSetup", 13, 3)
drimaes_hlosImage_flag = testData("DeviceSetup", 14, 2)
drimaes_hlosImage_path = testData("DeviceSetup", 14, 3)
drimaes_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Drimaes\conf_files'
drimaes_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Drimaes\ecrm_Image'
drimaes_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Drimaes\hlos_Image'

b2c_ecrmImage_flag = testData("DeviceSetup", 15, 2)
b2c_ecrmImage_path = testData("DeviceSetup", 15, 3)
b2c_hlosImage_flag = testData("DeviceSetup", 16, 2)
b2c_hlosImage_path = testData("DeviceSetup", 16, 3)
b2c_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\B2C\conf_files'
b2c_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\B2C\ecrm_Image'
b2c_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\B2C\hlos_Image'

mahindra_ecrmImage_flag = testData("DeviceSetup", 17, 2)
mahindra_ecrmImage_path = testData("DeviceSetup", 17, 3)
mahindra_hlosImage_flag = testData("DeviceSetup", 18, 2)
mahindra_hlosImage_path = testData("DeviceSetup", 18, 3)
mahindra_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Mahindra\conf_files'
mahindra_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Mahindra\ecrm_Image'
mahindra_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\Mahindra\hlos_Image'

c2c_tcu_sa525_ecrmImage_flag = c2c_tcu_sa525_hlosImage_flag = testData("DeviceSetup", 19, 2)
c2c_tcu_sa525_ecrmImage_path = c2c_tcu_sa525_hlosImage_path = testData("DeviceSetup", 19, 3)
c2c_tcu_sa525_confFiles_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU_SA525\conf_files'
c2c_tcu_sa525_ecrmImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU_SA525\ecrm_Image'
c2c_tcu_sa525_hlosImage_brooksPath = r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_Automation_Files\coreC2C\TCU_SA525\hlos_Image'

# ===================================
# Devices
# ===================================
deviceType_TCU = "TCU"
deviceType_IVI = "IVI"
deviceType_VT = "VT"
deviceType_IVI_nonPrimary = "IVI"

c2c_ivi_chipset1 = "SA8195"
c2c_ivi_chipset = "SA8295"
c2c_tcu_chipset = "SA515"
c2c_tcu_chipset_525 = "SA525"
c2c_vt_chipset = "SA2150"

drimaes_ivi_chipset = "6155"
b2c_ivi_chipset = "2290"
mahindra_ivi_chipset = "8295"

# ===================================
# Folder names
# ===================================
tcu_files = "tcu_files"
vt_files = "vt_files"
ivi_files = "ivi_files"

# Enter IVI device program details
drimaes_IVI_PrgmSkuId = testData("IVIConfFileDetails_Drimaes", 2, 4)
drimaes_IVI_SkuId = testData("IVIConfFileDetails_Drimaes", 3, 4)
drimaes_IVI_PrgmId = testData("IVIConfFileDetails_Drimaes", 4, 4)
drimaes_IVI_chipsetType = str(testData("IVIConfFileDetails_Drimaes", 5, 4)).split('=')[1]
drimaes_IVI_chipsetSpVer = str(testData("IVIConfFileDetails_Drimaes", 6, 4)).split('=')[1]

# Enter IVI device program details
b2c_IVI_PrgmSkuId = testData("IVIConfFileDetails_B2C", 2, 4)
b2c_IVI_SkuId = testData("IVIConfFileDetails_B2C", 3, 4)
b2c_IVI_PrgmId = testData("IVIConfFileDetails_B2C", 4, 4)
b2c_IVI_chipsetType = str(testData("IVIConfFileDetails_B2C", 5, 4)).split('=')[1]
b2c_IVI_chipsetSpVer = str(testData("IVIConfFileDetails_B2C", 6, 4)).split('=')[1]

# Enter IVI device program details
C2C_IVI_PrgmSkuId = testData("IVIConfFileDetails_Primary", 2, 4)
C2C_IVI_SkuId = testData("IVIConfFileDetails_Primary", 3, 4)
C2C_IVI_PrgmId = testData("IVIConfFileDetails_Primary", 4, 4)
C2C_IVI_chipsetType = str(testData("IVIConfFileDetails_Primary", 5, 4)).split('=')[1]
C2C_IVI_chipsetSpVer = str(testData("IVIConfFileDetails_Primary", 6, 4)).split('=')[1]

# ===================================
# Mahindra IVI device program details
# ===================================
mahindra_IVI_PrgmSkuId = testData("IVIConfFileDetails_Mahindra", 2, 4)
mahindra_IVI_SkuId = testData("IVIConfFileDetails_Mahindra", 3, 4)
mahindra_IVI_PrgmId = testData("IVIConfFileDetails_Mahindra", 4, 4)
mahindra_IVI_chipsetType = str(testData("IVIConfFileDetails_Mahindra", 5, 4)).split('=')[1]
mahindra_IVI_chipsetSpVer = str(testData("IVIConfFileDetails_Mahindra", 6, 4)).split('=')[1]

# ===================================
# Valid Test Data for test execution
# ===================================

# payload file path
# payloadPath = folderPath + r'C2CtestData\usr\local\json\OTA_Payload' + '\\'
otaPackagePath = str(folderPath) + r'C2CtestData\usr\local\OTApackages' + '\\'
otaExecutionPath = str(folderPath) + r'C2CtestReport\e2eExecution_Backup\OTA' + '\\'

# ===================================
# Valid Test Data for test execution
# ===================================

firm_reg = testData("FotaData", 2, 3)
sota_reg = testData("SotaData", 2, 3)

# Device states
ACTIVE_State = "ACTIVE"

# telemetry, Command & Control & FMS test data
telemetry_msg_id_published2Cloud = '"message_id": "msg-dev-'
telemetry_msg_id_published2Cloud1 = '"message_id": "msg-dev-'

trip_start_reason_code = 'trip_reason_code:74'
trip_stop_reason_code = 'trip_reason_code:75'
tripId_code = 'trip_id: '
tripId_code1 = 'Trip_id: '

trip_start_event_type_code = '"event_type": 4005'
trip_stop_event_type_code = '"event_type": 4006'

telemetry_msg_type_code = '"message_type": 601'
telemetry_recv_topic = "C2C_HUB/RECV/TELEMETRY"
Publishing_msg_to_cloud = "Publishing msg to cloud"
source_id_telematics = '"source_id": "telematics"'
target_id_telematics = '"target_id": "c2c-cloud"'

# tele attributes

telemetry_msg_type_code_tel = '"message_type": 304'
contextControl_msg_254 = '"message_type":254'
contextControl_msg_255 = '"message_type": 255'
contextControl_msg_256 = '"message_type": 256'

telemetry_odo_attribute = "odo:"
telemetry_odo_attribute1 = "VCU_Data5__Odometer_RX_V:"
telemetry_speed_attribute = "speed:"
telemetry_speed_attribute1 = "Display_info__Display_Vehicle_Speed_RX_V:"
telemetry_rpm_attribute = "rpm:"
telemetry_fuel_level_attribute = "fuel_level:"
telemetry_ev_battery_level_attribute = "ev_battery_level:"
telemetry_ev_battery_spec_current_attribute = "ev_battery_spec_current:"
telemetry_ev_battery_spec_watt_attribute = "ev_battery_spec_watt:"
telemetry_state_of_charge_attribute = "state_of_charge:"
telemetry_mileage_attribute = "mileage:"
telemetry_rpm_2_attribute = "rpm_2:"
inst_charge_rate = "inst_charge_rate:"
Outdoor_Temperature = "Outdoor_Temperature:"
fuel_efficiency = "fuel_efficiency:"
ev_motor_rpm1 = "ev_motor_rpm1:"
ev_motor_rpm2 = "ev_motor_rpm2:"
ev_battery_spec_voltage = "ev_battery_spec_voltage:"
latitude = "latitude:"
longitude = "longitude:"
altitude = "altitude:"
bearing = "bearing:"
velocity = "velocity:"

# tele values configured in stub (old values)
# telemetry_lat_value = "17.728162822"
# telemetry_long_value = "72.86781922"
# telemetry_alt_value = "72.22"
# telemetry_bar_value = "186.22"
# telemetry_vel_value = "85.22"
# telemetry_odo_value = "600000"
# telemetry_speed_value = ""
# telemetry_rpm_value = "500"
# telemetry_rpm_value1 = "500"
# telemetry_fuel_level_value = "30"
# telemetry_ev_battery_level_value = "5.2"
# telemetry_ev_battery_spec_current_value = "5"
# telemetry_ev_battery_spec_watt_value = "5"
# telemetry_state_of_charge_value = "2"
# telemetry_mileage_value = "52.2"
# telemetry_rpm_2_value = "50"

# Telemetry - Cloud evet type
telemetry_event_type = "3101"
telemetry_event_id = "291504644"

telemetry_lat_event_type = "3101"
telemetry_long_event_type = "3101"
telemetry_alt_event_type = "3101"
telemetry_bar_event_type = "3101"
telemetry_vel_event_type = "3101"
telemetry_odo_event_type = "2005"
telemetry_odo_event_type1 = "6500"
telemetry_speed_event_type = "2001"
telemetry_speed_event_type1 = "6500"
telemetry_rpm_event_type = "2002"
telemetry_fuel_level_event_type = "3250"
telemetry_ev_battery_level_event_type = "1001"
telemetry_ev_battery_spec_current_event_type = "1001"
telemetry_ev_battery_spec_watt_event_type = "1001"
telemetry_state_of_charge_event_type = "1001"
telemetry_mileage_event_type = "4001"
telemetry_rpm_2_event_type = "2002"  # not available for drimaes
telemetry_ignition_event_type = "2003"
telemetry_ignition_event_type1 = "1001"
telemetry_ignition_event_type2 = "1001"
telemetry_INFO_EV_BATTERY_CAPACITY = "1001"
EV_BMS_BATTERY_SOH = "1001"
EV_BMS_BATTERY_SOC = "1001"
EV_BATTERY_SPEC_VOLTAGE = "1001"
EV_BMS_BATTERY_TEMPERATURE = "1001"
EV_BMS_BATTERY_REMAINING_CHARGE_TIME = "1001"
EV_BATTERY_EFFICIENCY = "1001"
EV_CHARGING_STATE = "1001"
FUEL_LEVEL_LOW = "3250"
INFO_FUEL_CAPACITY = "3250"
FUEL_EFFICIENCY = "3250"
RANGE_REMAINING = "5002"
ENV_OUTSIDE_TEMPERATURE = "5003"
EV_BATTERY_INSTANTANEOUS_CHARGE_RATE = "1001"

# Command & Control

commndctrl_msg_type_code = '"message_type": 253'
notification_msg_type_code = '"message_type":502'
notification_msg_type_code1 = 'Message type: 502'

telemetry_HVAC_event_type = "3104"
telemetry_window_position_event_type = "3102"
telemetry_door_position_event_type = "3103"
telemetry_ignition_state_event_type = "2503"
telemetry_horn_event_type = "3201"
HVAC_SIDE_MIRROR_HEAT = "3104"
HVAC_STEERING_WHEEL_HEAT = "3104"
DEFROST = "3104"
WINDOW_POSITION = "3102"
DOOR_POSITION = "3103"
WINDOW_LOCK = "3102"
DOOR_LOCK = "3103"
HORN = "3201"  # not working
HVAC_SEAT_VENTILATION = "3104"
IGNITION_KEEPTIME = "2503"  # Not working
HAZARD_LIGHT = ""
Emergency_Light = ""
CHARGE_START = ""
CHARGE_STOP = ""
Ignition_start = ""
Ignition_stop = ""
Indoor_Temperature = ""
FUEL_LEVEL_ALERT_LIMIT = ""
EV_BMS_BATTERY_TEMPERATURE_MIN = ""
EV_BMS_BATTERY_TEMPERATURE_MAX = ""
MAX_BATTERY_CHARGING_LIMIT = ""

appid = testData("DeviceOnboardingData", 23, 2)

# Cloud attributes for telemetry-trip
telemetry_curr_Odo = "PERF_ODOMETER"
telemetry_curr_Odo1 = "VCU_Data5__Odometer_RX_V"
telemetry_curr_Fuel = "FUEL_LEVEL"
telemetry_curr_ev_battery_level = "EV_BATTERY_LEVEL"
telemetry_curr_Speed = "PERF_VEHICLE_SPEED"
telemetry_curr_rpm = "ENGINE_RPM"
telemetry_Curr_door_pos_old = "DOOR_POS"
telemetry_Curr_door_pos = "DOOR_POSITION"
telemetry_Curr_window_pos = "WINDOW_POS"
telemetry_Curr_ignition_keeptime = "IGNITION_KEEPTIME"
telemetry_Curr_ignition_state = "IGNITION_STATE"
telemetry_Curr_hvac_temp_set = "HVAC_TEMPERATURE_SET"
telemetry_Curr_hvac_temp_current = "HVAC_TEMPERATURE_CURRENT"
telemetry_Curr_hvac_seat_temp = "HVAC_SEAT_TEMPERATURE"
telemetry_Curr_hvac_seat_ventilation = "HVAC_SEAT_VENTILATION"
telemetry_Curr_hvac_side_mirror_heat = "HVAC_SIDE_MIRROR_HEAT"
telemetry_Curr_hvac_steering_wheel_heat = "HVAC_STEERING_WHEEL_HEAT"
telemetry_Curr_hvac_defroster = "HVAC_DEFROSTER"
telemetry_Curr_window_lock = "WINDOW_LOCK"
telemetry_Curr_door_lock = "DOOR_LOCK"
telemetry_Curr_emergency_light = "EMERGENCY_LIGHT"
telemetry_Curr_horn = "HORN"
telemetry_Curr_ev_bms_battery_temp = "EV_BMS_BATTERY_TEMPERATURE"
telemetry_Curr_ev_battery_capacity = "INFO_EV_BATTERY_CAPACITY"
telemetry_Curr_ev_charge_state = "EV_CHARGING_STATE"

# tele values configured in stub
telemetry_lat_value = "17.628162822"
telemetry_long_value = "72.816781922"
telemetry_alt_value = "72.22"
telemetry_bar_value = "186.22"
telemetry_vel_value = "85.22"
telemetry_odo_value = "600000"
telemetry_speed_value = "95"
telemetry_rpm_value = "11776"
telemetry_fuel_level_value = "30"
telemetry_ev_battery_level_value = "400"
telemetry_ev_battery_spec_current_value = ""
telemetry_ev_battery_spec_watt_value = ""
telemetry_state_of_charge_value = ""
telemetry_mileage_value = ""
telemetry_rpm_2_value = ""

# FMS - trip waypoint stub values:
trip_waypoint_rpm_value = float(300)
trip_waypoint_speed_value = float(75)

# FMS - trip summary stub values:
paho_trip_start = "paho_trip_start"
paho_trip_stop = "paho_trip_stop"
trip_summary_stub_option = "paho_telemetry_stub_trip"
trip_waypoint_stub_option = "paho_trip_waypoint"
trip_start_odometer_value = float(6000)
trip_start_fuelLevel_value_ev = float(60)
trip_start_fuelLevel_value_non_ev = float(60)
trip_start_batteryLevel_value_ev = float(400)
trip_start_batterySOCLevel_value_ev = float(90)
trip_start_batteryLevel_value_non_ev = float(400)
trip_start_speed_value_non_ev = float(75)

trip_end_odometer_value = float(6150)
trip_end_fuelLevel_value_ev = float(15)
trip_end_fuelLevel_value_non_ev = float(15)
trip_end_batteryLevel_value_ev = float(200)
trip_end_batterySOCLevel_value_ev = float(10)
trip_end_batteryLevel_value_non_ev = float(200)
trip_end_speed_value_non_ev = float(55)

trip_Fuel_Constant_ev = float(0)
trip_summary_tripFuelEfficiency_value_ev = float(0)  # Fuel Efficiency = Trip Distance/ Fuel Usage
trip_summary_co2Emission_value_ev = float(0)  # CO2(kg) = Fuel Usage * Fuel Constant
trip_summary_tripDistance_value_ev = float(150)  # Trip distance = ODO End – ODO Start
trip_summary_fuelConsumed_value_ev = float(0)  # Fuel Usage = Fuel Start - Fuel End
trip_summary_tripDuration_value_ev = float(0.02411138888888889)  # Trip duration = Trip End  time – Trip Start time
trip_summary_avgSpeed_value_ev = float(6221.126484717917)  # Avg Speed = Trip distance/ Trip Duration
trip_summary_batteryConsumed_value_ev = float(0.2)  # batteryConsumed = batterylevel_end-batterylevel_start/1000(inkwh)
trip_summary_tripBatteryEfficiency_value_ev = float(750)  # tripBatteryEfficiency = Trip distance/batteryConsumed
trip_summary_maxSpeed_value_ev = float(105)  # Max Speed = Max of Waypoints

# b2c - telemetry

b2c_off_status_ui = "Off"
b2c_on_status_ui = "On"

b2c_telemetry_rpm_attribute_ui = "Engine Rpm"
b2c_telemetry_rpm_value_ui = "11776 rpm"

b2c_telemetry_speed = 'Perf Vehicle Speed'
b2c_telemetry_speed_value = "32"
b2c_telemetry_speed_value_0 = "0"
b2c_telemetry_speed_value_ui = "32 km/hr"
b2c_telemetry_speed_notification_value = "128"

b2c_telemetry_odo = "Perf Odometer"
b2c_telemetry_odo_value = "65535"
b2c_telemetry_odo_value_ui = "65535 km"

b2c_telemetry_fuel_level = "Fuel Level"
b2c_telemetry_fuel_level_value = "8192"
b2c_telemetry_fuel_level_value_ui = "8192 ml"

b2c_telemetry_ev_battery_level = "Ev Battery Level"
b2c_telemetry_ev_battery_level_value = "128"
b2c_telemetry_ev_battery_level_value_ui = "128 wh"

b2c_telemetry_range_remaining_attribute = "range_remaining:"
b2c_telemetry_range_remaining_value = "160"
b2c_telemetry_range_remaining = "RANGE_REMAINING"
b2c_telemetry_range_remaining_attribute_ui = "Range Remaining"
b2c_telemetry_range_remaining_value_ui = "160 km"

b2c_ev_charge_port_open_attribute = 'ev_charge_port_open'
b2c_ev_charge_port_open = 'EV_CHARGE_PORT_OPEN'
b2c_ev_charge_port_open_state_ON = '1'
b2c_ev_charge_port_open_state_OFF = '0'
telemetry_ev_charge_port_open_event_type = "1003"
b2c_ev_charge_port_open_attribute_ui = "Ev Charge Port Open"

b2c_ev_charge_port_connected_attribute = 'ev_charge_port_connected:'
b2c_ev_charge_port_connected = 'EV_CHARGE_PORT_CONNECTED'
b2c_ev_charge_port_connected_state_ON = '1'
b2c_ev_charge_port_connected_state_OFF = '0'
telemetry_ev_charge_port_connected_event_type = "1003"
b2c_ev_charge_port_connected_attribute_ui = "Ev Charge Port Connected"

b2c_inst_charge_rate_attribute = 'inst_charge_rate:'
b2c_inst_charge_rate = 'EV_BATTERY_INSTANTANEOUS_CHARGE_RATE'
b2c_inst_charge_rate_value = '236'
b2c_no_inst_charge_rate_value = '0'
telemetry_inst_charge_rate_event_type = "4009"
b2c_inst_charge_rate_attribute_ui = "Ev Battery Instantaneous Charge Rate"
b2c_inst_charge_rate_value_ui = '236 mw'

# b2c - Command & Control
Command_Lock_ignition_attribute = "ignition:"
Command_Lock_ignition_value = "ignition:1"
Command_Unlock_ignition_value = "ignition:2"
Command_Acc_ignition_value = "ignition:3"
Command_On_ignition_value = "ignition:4"

b2c_telemetry_sidestand = 'SIDE_STAND'
b2c_telemetry_sidestand_attribute = 'side_stand:'
b2c_telemetry_sidestand_state_ON = "1"
b2c_telemetry_sidestand_state_OFF = "0"
telemetry_sidestand_event_type = "3106"
b2c_telemetry_sidestand_attribute_ui = 'Side Stand'

b2c_telemetry_headlight = 'HEAD_LIGHT'
b2c_telemetry_headlight_attribute = 'headlights:'
b2c_telemetry_headlight_state_ON = "1"
b2c_telemetry_headlight_state_OFF = "0"
telemetry_headlight_event_type = "3203"
b2c_telemetry_headlight_attribute_ui = 'Head Light'

b2c_telemetry_taillight = 'TAIL_LIGHT'
b2c_telemetry_taillight_attribute = 'tail_light:'
b2c_telemetry_taillight_state_ON = "1"
b2c_telemetry_taillight_state_OFF = "0"
telemetry_taillight_event_type = "3204"
b2c_telemetry_taillight_attribute_ui = "Tail Light"

b2c_telemetry_indicator = 'INDICATOR'
b2c_telemetry_indicator_attribute = 'turn_signal:'
b2c_telemetry_indicator_state_ON = "1"
b2c_telemetry_indicator_state_OFF = "0"

b2c_telemetry_high_beam = 'HIGH_BEAM_LIGHTS_STATE'
b2c_telemetry_high_beam_attribute = 'high_beam_state:'
b2c_telemetry_high_beam_state_ON = "1"
b2c_telemetry_high_beam_state_OFF = "0"
telemetry_high_beam_event_type = "3210"
b2c_telemetry_high_beam_attribute_ui = 'High Beam Lights State'

b2c_telemetry_hazard_light = 'HAZARD_LIGHT'
b2c_telemetry_hazard_light_attribute = 'hazard_lights_state:'
b2c_telemetry_hazard_light_state_ON = "1"
b2c_telemetry_hazard_light_state_OFF = "0"
telemetry_hazard_light_event_type = "3205"
b2c_telemetry_hazard_light_attribute_ui = 'Hazard Light'

b2c_telemetry_gear_position = 'GEAR_POSITION'
b2c_telemetry_gear_position_attribute = 'gear_position:'
b2c_telemetry_gear_position_state_4 = "4"  # (P: Park)
b2c_telemetry_gear_position_state_8 = "8"  # (D: Drive)
b2c_telemetry_gear_position_state_2 = "2"  # (R: Reverse)
telemetry_gear_position_event_type = "3109"
b2c_telemetry_gear_position_attribute_ui = "Gear Position"
b2c_telemetry_gear_position_state_8_ui = "Drive"

b2c_telemetry_ride_mode = 'RIDE_MODE'
b2c_telemetry_ride_mode_attribute = 'ride_mode:'
b2c_telemetry_ride_mode_state_0 = "0"  # (Normal)
b2c_telemetry_ride_mode_state_1 = "1"  # (Economic)
b2c_telemetry_ride_mode_state_2 = "2"  # (Vendor Specific/Sportz)
telemetry_ride_mode_event_type = "2008"
b2c_telemetry_ride_mode_attribute_ui = 'Ride Mode'
b2c_telemetry_ride_mode_state_2_ui = "Sportz"

b2c_telemetry_SOS = 'SOS'
b2c_telemetry_SOS_attribute = 'sos_status:'
b2c_telemetry_SOS_state_ON = "1"
b2c_telemetry_SOS_state_OFF = "0"
b2c_telemetry_SOS_attribute_ui = 'Sos'

b2c_telemetry_current_battery_temp = 'EV_BATTERY_TEMPERATURE'
b2c_telemetry_current_battery_temp_attribute = 'currentBatteryTemp:'
b2c_telemetry_battery_temp_attribute = 'BATTERY_TEMP:'
b2c_telemetry_normal_battery_temp_value = "48"
b2c_telemetry_warning_battery_temp_value = "66"
b2c_telemetry_critical_battery_temp_value = "101"
b2c_telemetry_current_battery_temp_attribute_ui = "Ev Battery Temperature"

b2c_telemetry_tire_pressure = 'TIRE_PRESSURE'
b2c_telemetry_left_front = 'LEFT_FRONT'
b2c_telemetry_front_tire_pressure_attribute = 'front_tire_pressure:'
b2c_telemetry_front_tire_pressure_value = '220'
b2c_telemetry_left_rear = 'LEFT_REAR'
b2c_telemetry_rear_tire_pressure_attribute = "rear_tire_pressure:"
b2c_telemetry_rear_tire_pressure_value = '225'
telemetry_tire_pressure_event_type = "3108"
b2c_telemetry_front_tire_pressure_attribute_ui = "Tire Pressure Front"
b2c_telemetry_front_tire_pressure_value_ui = '220 kilopascal'
b2c_telemetry_rear_tire_pressure_attribute_ui = "Tire Pressure Front"
b2c_telemetry_rear_tire_pressure_value_ui = '225 kilopascal'

b2c_telemetry_immobilize_state = 'MOBILIZE'
b2c_telemetry_immobilize_state_attribute = 'immobilize_state:'
b2c_telemetry_immobilize_state_ON = "1"
b2c_telemetry_immobilize_state_OFF = "0"
telemetry_immobilize_event_type = "2004"
b2c_telemetry_immobilize_state_attribute_ui = "Immobilize"

b2c_telemetry_evBatteryCapacity_attribute_ui = "Info Ev Battery Capacity"
b2c_telemetry_evBatteryCapacity_value_ui = "240 wh"

# FMS - trip summary stub values for B2C Device:
can_trip_start = "trip_start"
can_trip_stop = "trip_stop"
b2c_trip_start_odometer_value = float(65263)
b2c_trip_start_odometer_stub_value = float(6000)
b2c_trip_start_fuelLevel_value_ev = float(0)
b2c_trip_start_fuelLevel_value_non_ev = float(60)
b2c_trip_start_batteryLevel_value_ev = float(128)
b2c_trip_start_batteryLevel_stub_value_ev = float(128)
b2c_trip_start_batteryLevel_value_non_ev = float(0)
b2c_trip_start_speed_value_non_ev = float(75)

b2c_trip_end_odometer_value = float(65518)
b2c_trip_end_odometer_stub_value = float(6000)
b2c_trip_end_fuelLevel_value_ev = float(0)
b2c_trip_end_fuelLevel_value_non_ev = float(15)
b2c_trip_end_batteryLevel_value_ev = float(112)
b2c_trip_end_batteryLevel_value_non_ev = float(0)
b2c_trip_end_speed_value_non_ev = float(55)

b2c_trip_Fuel_Constant_ev = float(0)
b2c_trip_summary_tripFuelEfficiency_value_ev = float(0)  # Fuel Efficiency = Trip Distance/ Fuel Usage
b2c_trip_summary_co2Emission_value_ev = float(0)  # CO2(kg) = Fuel Usage * Fuel Constant
b2c_trip_summary_tripDistance_value_ev = float(255)  # Trip distance = ODO End – ODO Start
b2c_trip_summary_fuelConsumed_value_ev = float(0)  # Fuel Usage = Fuel Start - Fuel End
b2c_trip_summary_tripDuration_value_ev = float(0.004107222222222222)  # Trip duration = Trip End  time – Trip Start time
b2c_trip_summary_avgSpeed_value_ev = float(62085.756796970105)  # Avg Speed = Trip distance/ Trip Duration
b2c_trip_summary_batteryConsumed_value_ev = float(
    0.016)  # batteryConsumed = batterylevel_end-batterylevel_start/1000(inkwh)
b2c_trip_summary_tripBatteryEfficiency_value_ev = float(
    15937.5)  # tripBatteryEfficiency = Trip distance/batteryConsumed
b2c_trip_summary_maxSpeed_value_ev = float(80)

# ---------------------------------------------
# RE Test Data
# ---------------------------------------------

telemetry_attribute_gps_speed = "AL_GPS_SPEED"
telemetry_attribute_gps_speed1 = "AL_VELOCITY"
telemetry_attribute_gps_status = "AL_GPS_STATUS"
# telemetry_attribute_gps_signalStrength = "AL_GPS_SIGNAL_STRENGTH"
telemetry_attribute_gsm_signalStrength = "AL_GSM_SIGNAL_STRENGTH"
telemetry_attribute_gps_signalStrength = "AL_GPS_SIGNAL_STRENGTH"
telemetry_attribute_networkOpName = "AL_NETWORK_OP_NAME"
telemetry_attribute_timestamp = "AL_TIMESTAMP"
telemetry_attribute_deltaDistCovered = "AL_DELTA_DIST_COVERED"
telemetry_attribute_pdop = "AL_PDOP"
telemetry_attribute_hdop = "AL_HDOP"
telemetry_attribute_gps_fix = "AL_GPS_FIX"
telemetry_attribute_latitude_dir = "AL_LAT_DIR"
telemetry_attribute_longitude_dir = "AL_LONG_DIR"
telemetry_attribute_latitude = "AL_LATITUDE"
telemetry_attribute_longitude = "AL_LONGITUDE"
telemetry_attribute_altitude = "AL_ALTITUDE"
telemetry_attribute_direction = "AL_DIRECTION"
telemetry_attribute_direction1 = "AL_BEARING"
telemetry_attribute_ignition = "IGNITION_STATE"
telemetry_attribute_ignition_ev = "EV_IGNITION_STATE"
telemetry_attribute_ignition_ev1 = "Vehicle_Mode__Vehicle_Mode_Lvl_1_RX_V"
telemetry_attribute_ignition_ev2 = "VCU_Data__Ignition_Sts_RX_V"

# Speed - Device
b2c_telemetry_gps_speed_attribute = "Updated data velocity:"
b2c_telemetry_gps_speed_value = "32.000000"

# Ignition - Device
b2c_telemetry_ev_ignition_value = "ev_ridemode:3"
b2c_telemetry_ev_ignition_on_value = "ev_ridemode:4"

# Battery - Cloud

telemetry_battery_eventType = "1001"
telemetry_battery_eventType1 = "6503"

telemetry_attribute_ev_battery_soc = "EV_BATTERY_SOC"
telemetry_attribute_ev_battery_soc1 = "Batt_Sts_Info__Display_SoC_RX_V"
telemetry_attribute_ev_battery_level = "EV_BATTERY_LEVEL"
telemetry_attribute_ev_battery_voltage = "EV_BATTERY_VOLTAGE"
telemetry_attribute_ev_battery_current = "EV_BATTERY_CURRENT"
telemetry_attribute_ev_battery_temp = "EV_BATTERY_TEMPERATURE"
telemetry_attribute_ev_battery_soh = "EV-BATTERY_SOH"

# Battery - Device
b2c_telemetry_battery_level_attribute = "ev_battery_level:"
b2c_telemetry_battery_level_value = "19.000000"
b2c_telemetry_battery_soc_attribute = "state_of_charge:"
b2c_telemetry_battery_soc_value = "15.000000"
b2c_telemetry_battery_voltage_attribute = "ev_battery_voltage:"
b2c_telemetry_battery_voltage_value = "5.000000"
b2c_telemetry_battery_current_attribute = "ev_battery_current:"
b2c_telemetry_battery_current_value = "6.000000"
b2c_telemetry_battery_temperature_attribute = "ev_battery_temp:"
b2c_telemetry_battery_temperature_value = "60"
b2c_telemetry_battery_soh_attribute = "battery_SOH:"
b2c_telemetry_battery_soh_value = "16.000000"

b2c_telemetry_battery_block_msg = "constr_and_send_proto_msg success for 1001 : 0"

last_parked_expected_output = {"message": "Data Fetched Successfully", "responseData": {"signals": [
    [{"id": 559988750, "name": "AL_GPS_STATUS", "unit": "NA", "value": "92.001", "updatedTime": 1728366151217},
     {"id": 559988751, "name": "AL_GSM_SIGNAL_STRENGTH", "unit": "dbm", "value": "53.001",
      "updatedTime": 1728366151217},
     {"id": 559988752, "name": "AL_NETWORK_OP_NAME", "unit": "NA", "value": "13.89", "updatedTime": 1728366151217},
     {"id": 559988753, "name": "AL_TIMESTAMP", "unit": "NA", "value": "73.001", "updatedTime": 1728366151217},
     {"id": 559988759, "name": "AL_DELTA_DIST_COVERED", "unit": "NA", "value": "53.001", "updatedTime": 1728366151217},
     {"id": 559988760, "name": "AL_PDOP", "unit": "degrees", "value": "58.001", "updatedTime": 1728366151217},
     {"id": 559988761, "name": "AL_HDOP", "unit": "degrees", "value": "58.001", "updatedTime": 1728366151217},
     {"id": 559988762, "name": "AL_GPS_FIX", "unit": "NA", "value": "60.001", "updatedTime": 1728366151217},
     {"id": 559988754, "name": "AL_LAT_DIR", "unit": "degrees", "value": "19.19", "updatedTime": 1728366151217},
     {"id": 559988755, "name": "AL_LONG_DIR", "unit": "degrees", "value": "493", "updatedTime": 1728366151217},
     {"id": 559940097, "name": "AL_LATITUDE", "unit": "degrees", "value": "28.60886667", "updatedTime": 1728366151217},
     {"id": 559940098, "name": "AL_LONGITUDE", "unit": "degrees", "value": "77.2302", "updatedTime": 1728366151217},
     {"id": 559940099, "name": "AL_ALTITUDE", "unit": "meters", "value": "214.1", "updatedTime": 1728366151217},
     {"id": 559940100, "name": "AL_DIRECTION", "unit": "degrees", "value": "92.9", "updatedTime": 1728366151217},
     {"id": 559942149, "name": "AL_GPS_SPEED", "unit": "m/s", "value": "0", "updatedTime": 1728366151217}]]}}

last_parked_expected_output1 = {"message": "Data Fetched Successfully", "responseData": {"signals": [
    [{"id": 559988750, "name": "AL_GPS_STATUS", "unit": "NA", "value": "false", "updatedTime": 1748706333255},
     {"id": 559988751, "name": "AL_GSM_SIGNAL_STRENGTH", "unit": "dbm", "value": "[ { \"Satellite-11\": 46 } ]",
      "updatedTime": 1748706333255},
     {"id": 559988752, "name": "AL_NETWORK_OP_NAME", "unit": "NA", "value": "airtel", "updatedTime": 1748706333255},
     {"id": 559988753, "name": "AL_TIMESTAMP", "unit": "NA", "value": "1.7455642E12", "updatedTime": 1748706333255},
     {"id": 559988759, "name": "AL_DELTA_DIST_COVERED", "unit": "NA", "value": "100.0", "updatedTime": 1748706333255},
     {"id": 559988760, "name": "AL_PDOP", "unit": "degrees", "value": "58.001", "updatedTime": 1748706333255},
     {"id": 559988761, "name": "AL_HDOP", "unit": "degrees", "value": "58.001", "updatedTime": 1748706333255},
     {"id": 559988762, "name": "AL_GPS_FIX", "unit": "NA", "value": "1.0", "updatedTime": 1748706333255},
     {"id": 559988754, "name": "AL_LAT_DIR", "unit": "degrees", "value": "N", "updatedTime": 1748706333255},
     {"id": 559988755, "name": "AL_LONG_DIR", "unit": "degrees", "value": "E", "updatedTime": 1748706333255},
     {"id": 559940097, "name": "AL_LATITUDE", "unit": "degrees", "value": "28.608866", "updatedTime": 1748706333255},
     {"id": 559940098, "name": "AL_LONGITUDE", "unit": "degrees", "value": "77.2302", "updatedTime": 1748706333255},
     {"id": 559940099, "name": "AL_ALTITUDE", "unit": "meters", "value": "214.1", "updatedTime": 1748706333255},
     {"id": 559940100, "name": "AL_DIRECTION", "unit": "degrees", "value": "92.9", "updatedTime": 1748706333255},
     {"id": 559942149, "name": "AL_GPS_SPEED", "unit": "m/s", "value": "123.0", "updatedTime": 1748706333255}]]}}

last_parked_expected_output2 = {"message": "Data Fetched Successfully", "responseData": {"signals": [
    [{"id": 554745872, "name": "AL_NETWORK_OP_NAME", "unit": "NA", "value": "airtel", "updatedTime": 1758470958063},
     {"id": 559940097, "name": "AL_LATITUDE", "unit": "NA", "value": "28.608866", "updatedTime": 1758470958063},
     {"id": 554745874, "name": "AL_LAT_DIR", "unit": "NA", "value": "N", "updatedTime": 1758470958063},
     {"id": 559940098, "name": "AL_LONGITUDE", "unit": "NA", "value": "77.2302", "updatedTime": 1758470958063},
     {"id": 559940099, "name": "AL_ALTITUDE", "unit": "NA", "value": "214.1", "updatedTime": 1758470958063},
     {"id": 554745875, "name": "AL_LONG_DIR", "unit": "NA", "value": "E", "updatedTime": 1758470958063},
     {"id": 559940100, "name": "AL_BEARING", "unit": "NA", "value": "92.9", "updatedTime": 1758470958063},
     {"id": 559942149, "name": "AL_VELOCITY", "unit": "NA", "value": "123.0", "updatedTime": 1758470958063},
     {"id": 559988753, "name": "AL_TIMESTAMP", "unit": "NA", "value": "1.7455642E12", "updatedTime": 1758470958063},
     {"id": 559988759, "name": "AL_DELTA_DIST_COVERED", "unit": "NA", "value": "0.0", "updatedTime": 1758470958063},
     {"id": 559988760, "name": "AL_PDOP", "unit": "NA", "value": "58.001", "updatedTime": 1758470958063},
     {"id": 559988761, "name": "AL_HDOP", "unit": "NA", "value": "58.001", "updatedTime": 1758470958063},
     {"id": 559988762, "name": "AL_GPS_FIX", "unit": "NA", "value": "1.0", "updatedTime": 1758470958063},
     {"id": 554745870, "name": "AL_GPS_STATUS", "unit": "NA", "value": "false", "updatedTime": 1758470958063},
     {"id": 554745871, "name": "AL_GPS_SIGNAL_STRENGTH", "unit": "NA", "value": "[ { \"Satellite-11\": 46 } ]",
      "updatedTime": 1758470958063}]]}}

# For Bike Security & Safety - Alerts/Notifications
modeId = "802"
priority = "2"
msgInfo_area = "0"
msgInfo_value_0 = "0"
msgInfo_value_1 = "1"
msgInfo_value_2 = "2"

tamper_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 11 : 1006"
tamper_notification_name = "TAMPER NOTIFICATION PUSH"
tamper_categoryName = "TAMPER%20NOTIFICATION%20PUSH"
tamper_categoryId = "11"
tamper_modeId_old = "807"
tamper_notification_name_v2 = "TAMPER NOTIFICATION"
tamper_categoryName_v2 = "TAMPER%20NOTIFICATION"
tamper_propertyId = "557891597"
tamper_modeId = "802"

towAway_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 11 : 1006"
towAway_notification_name = "TOW AWAY NOTIFICATION PUSH"
towAway_categoryName = "TOW%20AWAY%20NOTIFICATION%20PUSH"
towAway_categoryId = "1"
towAway_notification_name_v2 = "TOW AWAY NOTIFICATION"
towAway_categoryName_v2 = "TOW%20AWAY%20NOTIFICATION"
towAway_propertyId = "559942149"
towAway_modeId = "802"

crash_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 14 : 1005"
crash_notification_name = "CRASH NOTIFICATION PUSH"
crash_categoryName = "CRASH%20NOTIFICATION%20PUSH"
crash_categoryId = "14"
crash_modeId = "807"
crash_notification_name_v2 = "CRASH NOTIFICATION"
crash_categoryName_v2 = "CRASH%20NOTIFICATION"
crash_propertyId = "557891597"

battery_heatCold_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 21 : 1007"
battery_heatCold_notification_name = "BATTERY HEAT COLD NOTIFICATION"
battery_heatCold_categoryName = "BATTERY%20HEAT%20COLD%20NOTIFICATION"
battery_heatCold_categoryId = "21"
battery_heatCold_modeId = "807"
batteryHeatCold_propertyId = "557891601"

ignition_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 22 : 1008"
ignition_notification_name = "VEHICLE STATE NOTIFICATION"
ignition_categoryName = "VEHICLE%20STATE%20NOTIFICATION"
ignition_categoryId = "22"
ignition_modeId = "807"

geofence_notification_name = "DEVICE GEOFENCE NOTIFICATION PUSH"
geofence_categoryName = "DEVICE%20GEOFENCE%20NOTIFICATION%20PUSH"
geofence_categoryId = "3"
geofence_modeId = "807"
geofence_notification_name_v2 = "DEVICE GEOFENCE NOTIFICATION"
geofence_categoryName_v2 = "DEVICE%20GEOFENCE%20NOTIFICATION"

dtc_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 4002 : 86"
dtc_notification_name = "DTC ALERT"
dtc_categoryName = "DTC%20ALERT"
dtc_categoryId = "87"
dtc_modeId = "807"
dtc_propertyId = "87"

# PIN EXPIRY NOTIFICATION alert
pinExpiry_notification_name = "PIN EXPIRY NOTIFICATION"
pinExpiry_categoryName = "PIN%20EXPIRY%20NOTIFICATION"
pinExpiry_categoryId = "24"
pinExpiry_propertyId = "557875711"
pinExpiry_modeId = "802"

service_remainder_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 20 : 1010"
service_remainder_notification_name = "SERVICE REMINDER NOTIFICATION"
service_remainder_categoryName = "SERVICE%20REMINDER%20NOTIFICATION"
service_remainder_categoryId = "20"
service_remainder_modeId = "807"
service_reminder_propertyId = "291504644"
service_reminder_msgInfo_value = "6000"

dtc_alert_notification_deviceLog_string1 = "constr_and_send_proto_msg success for 28"
dtc_notification_name1 = "DTC ALERT DEVICE"
dtc_categoryName1 = "DTC%20ALERT%20DEVICE"
dtc_categoryId1 = "28"
dtc_modeId1 = "807"

sos_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 25"
sos_notification_name = "SOS NOTIFICATION"
sos_categoryName = "SOS%20NOTIFICATION"
sos_categoryId = "25"
sos_modeId = "807"
sos_propertyId = "555749181"

# MODE CHANGE NOTIFICATION alert
modeChange_notification_name = "MODE CHANGE NOTIFICATION"
modeChange_categoryName = "MODE%20CHANGE%20NOTIFICATION"
modeChange_categoryId = "30"
modeChange_propertyId = "557875296"
modeChange_modeId = "802"

vehicleState_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 14 : 1005"
vehicleState_notification_name = "VEHICLE STATE NOTIFICATION"
vehicleState_categoryName = "VEHICLE%20STATE%20NOTIFICATION"
vehicleState_categoryId = "22"
vehicleState_propertyId = "557875295"
vehicleState_modeId = "802"

# PLUG IN & OUT NOTIFICATION alert
plugInOut_notification_name = "PLUG IN OUT NOTIFICATION"
plugInOut_categoryName = "PLUG%20IN%20OUT%20NOTIFICATION"
plugInOut_categoryId = "29"
plugInOut_propertyId = "557875711"
plugInOut_modeId = "802"

# Trip NOTIFICATION alert
trip_notification_name = "TRIP NOTIFICATION CLOUD"
trip_categoryName = "TRIP%20NOTIFICATION%20CLOUD"
trip_categoryId = "27"
trip_propertyId = "557875711"
trip_modeId = "802"

notified_status = "NOTIFIED"
notified_status_Id = "1"

inProgress_status = "INPROGRESS"
inProgress_status_Id = "4"

completed_status = "COMPLETED"
completed_status_Id = "5"

notification_type = "KAFKA"

# For Trip
ev_engineType = 2

expected_tripStart_odometer = float(6000)
expected_tripEnd_odometer = float(6150)
expected_tripEnd_odometer1 = float(6250)
expected_tripEnd_odometer2 = float(6000.8)

expected_tripStart_batteryLevel = float(400)
expected_tripEnd_batteryLevel = float(200)

expected_trip_summary_tripDistance = float(150)
expected_trip_summary_tripDistance1 = float(250)
expected_trip_summary_tripDistance2 = float(0.8)
expected_trip_summary_tripDistance3 = float(6000.8)
expected_trip_summary_tripDuration = float(0.024610555)
expected_trip_summary_tripDuration2 = float(0.05)
expected_trip_summary_avgSpeed = float(5572.9277)
expected_trip_summary_avgSpeed1 = float(5572.9)
expected_trip_summary_avgSpeed2 = float(24.763033)
expected_trip_summary_avgSpeed3 = float(52.0)
expected_trip_summary_idleTime = float(0.002793611)
expected_trip_summary_idleTime_1 = float(0.006146389)
expected_trip_summary_batteryConsumed = float(200)
expected_trip_summary_tripBatteryEfficiency = float(0.75)
expected_trip_summary_tripBatteryEfficiency1 = float(1.25)
expected_trip_summary_maxSpeed = float(121)

expected_trip_summary_violation_ha = '1'
expected_trip_summary_violation_hb = '1'
expected_trip_summary_violation_overSpeed = '1'
expected_trip_summary_violation_overSpeed1 = '2'

# For Command & Control

command_vehicleLock = "VEHICLE_LOCK"
command_vehicleUnLock = "VEHICLE_UNLOCK"
# new command
command_vehicleHonk = "VEHICLE_HONK"
command_vehicleHeadLight = "VEHICLE_HEADLIGHT"
command_appId = "RE_app"
command_time = datetime.utcnow().isoformat() + 'Z'
command_area = "0"
command_value_0 = "0"
command_value_1 = "1"
command_timeout = -1
Command_ignition_lvl1_attribute = "Vehicle_Mode__Vehicle_Mode_Lvl_1_RX_V"
Command_ignition_lvl1_value = "0"

expected_triggered_status = "TRIGGERED"
expected_success_status = "SUCCESS"

# HA data
telemetry_HA_event_type = "4446"
telemetry_attribute_HA = "HARSH ACCELERATION"
telemetry_HA_value = "1"
telemetry_HA_reason_code = "104"
b2c_telemetry_ha_attribute = "constr_and_send_proto_msg success for 4446 : 104 : 0"

# HB data
telemetry_HB_event_type = "4447"
telemetry_attribute_HB = "HARSH BRAKING"
telemetry_HB_value = "1"
telemetry_HB_reason_code = "105"
b2c_telemetry_hb_attribute = "constr_and_send_proto_msg success for 4447 : 105 : 0"

# OverSpeed data
telemetry_attribute_speed = "SPEED"
telemetry_attribute_speed1 = "Display_info__Display_Vehicle_Speed_RX_V"
telemetry_over_speed_value = "130"
telemetry_over_speed_reason_code = "103"
b2c_telemetry_over_speed_attribute = "constr_and_send_proto_msg success for 4445 : 103 : 0"

# Odometer data
telemetry_odometer_reason_code = "24"
telemetry_odometer_value = "6000"
telemetry_odometer_value1 = "6900"
telemetry_attributeId_odo = 557875743
telemetry_attribute_odo = "VCU_Data5__Odometer_RX_V"

# ignition data
telemetry_ignition_attribute = "ev_ridemode:3"
telemetry_ignition_reason_code = "69"
telemetry_ignition_value = "3"

# dtc clear data
dtcClr_req_msg_type_code = "Message type: 309"
dtcClr_res_msg_type_code = "Message type: 310"

# vehicle health report data
b2c_telemetry_battery_soc_value1 = "25.000000"
b2c_telemetry_battery_soh_value1 = "15.000000"
b2c_telemetry_battery_soc_value2 = "15.000000"
b2c_telemetry_battery_soh_value2 = "25.000000"
telemetry_attributeId_ev_battery_soc = 559943684
telemetry_attributeId_ev_battery_soh = 559943685
telemetry_attributeId_ev_battery_soc1 = 557875417
telemetry_attributeId_ev_battery_soc2 = 557876173
telemetry_attributeId_ev_battery_soh1 = 559972670

# digital pin data
digitalPin_generate_msg_type_code = "Message type: 801"
digitalPin_reset_req_msg_type_code = "Message type: 803"
digitalPin_reset_res_msg_type_code = "Message type: 805"
digitalPin_vehicle_unlock_msg_type_code = "Message type: 807"
digitalPin_expiry_msg_type_code = "Message type: 809"

telemetry_attributeId_ignition = "557875295"
telemetry_attribute_ignition = "Vehicle_Mode__Vehicle_Mode_Lvl_1_RX_V"

telemetry_attributeId_ignition1 = "557875730"
telemetry_attribute_ignition1 = "VCU_Data__Ignition_Sts_RX_V"
telemetry_ignition_on_value = "1"
telemetry_ignition_off_value = "0"

telemetry_attributeId_device_authentication_flag = "557875729"
telemetry_attribute_device_authentication_flag = "VCU_Data__Veh_Authentication_Flag_RX_V"
telemetry_attribute_device_authentication_flag_value_1 = "1"
telemetry_event_type_6500 = 6500

# R8S3 - Alert

battery_heat_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 21"
battery_heat_notification_name = "BATTERY HEAT NOTIFICATION"
battery_heat_categoryName = "BATTERY%20HEAT%20NOTIFICATION"
battery_heat_categoryId = "21"
batteryHeat_propertyId = "557875613"
batteryHeat_modeId = "807"

battery_cold_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 32"
battery_cold_notification_name = "BATTERY COLD NOTIFICATION"
battery_cold_categoryName = "BATTERY%20COLD%20NOTIFICATION"
battery_cold_categoryId = "32"
batteryCold_propertyId = "557875605"
batteryCold_modeId = "807"

remote_lock_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 22"
remote_lock_notification_name = "REMOTE LOCK NOTIFICATION"
remote_lock_categoryName = "REMOTE%20LOCK%20NOTIFICATION"
remote_lock_categoryId = "22"
remoteLock_propertyId = "557875297"
remoteLock_modeId = "807"

remote_unlock_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 33"
remote_unlock_notification_name = "REMOTE UNLOCK NOTIFICATION"
remote_unlock_categoryName = "REMOTE%20UNLOCK%20NOTIFICATION"
remote_unlock_categoryId = "33"
remoteUnlock_propertyId = "557875297"
remoteUnlock_modeId = "807"

plug_in_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 29"
plug_in_notification_name = "PLUG IN NOTIFICATION"
plug_in_categoryName = "PLUG%20IN%20NOTIFICATION"
plug_in_categoryId = "29"
plugIn_propertyId = "557875711"
plugIn_modeId = "807"

plug_out_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 34"
plug_out_notification_name = "PLUG OUT NOTIFICATION"
plug_out_categoryName = "PLUG%20OUT%20NOTIFICATION"
plug_out_categoryId = "34"
plugOut_propertyId = "557875711"
plugOut_modeId = "807"

ignition_on_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 35"
ignition_on_notification_name = "IGNITION ON NOTIFICATION"
ignition_on_categoryName = "IGNITION%20ON%20NOTIFICATION"
ignition_on_categoryId = "35"
ignitionOn_propertyId = "557875730"
ignitionOn_modeId = "807"

ignition_off_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 36"
ignition_off_notification_name = "IGNITION OFF NOTIFICATION"
ignition_off_categoryName = "IGNITION%20OFF%20NOTIFICATION"
ignition_off_categoryId = "36"
ignitionOff_propertyId = "557875730"
ignitionOff_modeId = "807"

geofence_entry_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 3"
geofence_entry_notification_name = "DEVICE GEOFENCE ENTRY NOTIFICATION"
geofence_entry_categoryName = "DEVICE%20GEOFENCE%20ENTRY%20NOTIFICATION"
geofence_entry_categoryId = "3"
geofenceEntry_modeId = "807"

geofence_exit_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 31"
geofence_exit_notification_name = "DEVICE GEOFENCE EXIT NOTIFICATION"
geofence_exit_categoryName = "DEVICE%20GEOFENCE%20EXIT%20NOTIFICATION"
geofence_exit_categoryId = "31"
geofenceExit_modeId = "807"

geo_in_alert_text = "Vehicle has entered geofence"  # "Vehicle has entered geofence"
geo_out_alert_text = "Vehicle has exited geofence"

geo_polygon_in_alert_text = "Polygon geofence:Vehicle has entered geofence"  # "Vehicle has entered geofence"
geo_polygon_out_alert_text = "Polygon geofence:Vehicle has exited geofence"

# R8S3-vehicle state: Ride Mode testdata
telemetry_attribute_ridemode = "Vehicle_Mode__Vehicle_Mode_Lvl_2_RX_V"
telemetry_attributeId_ridemode = 557875296
telemetry_ridemode_value_0 = "0"
telemetry_ridemode_value_1 = "1"
telemetry_ridemode_value_2 = "2"
telemetry_ridemode_value_3 = "3"
telemetry_ridemode_value_4 = "4"
telemetry_ridemode_value_5 = "5"
telemetry_ridemode_value_6 = "6"
telemetry_ridemode_value_7 = "7"
telemetry_ridemode_value_8 = "8"
telemetry_ridemode_value_9 = "9"
telemetry_ridemode_value_10 = "10"
telemetry_ridemode_value_11 = "11"
telemetry_ridemode_value_12 = "12"
telemetry_ridemode_value_13 = "13"
telemetry_ridemode_value_14 = "14"
telemetry_ridemode_value_15 = "15"
telemetry_ridemode_value_16 = "16"
telemetry_ridemode_value_17 = "17"

# R8S4- Alerts Test Data

transaction_control_indicator_alert_deviceLog_string = "constr_and_send_proto_msg success for 42"
traction_control_indicator_alert_notification_name = "TRACTION CONTROL STATE NOTIFICATION"
traction_control_indicator_categoryName = "TRACTION%20CONTROL%20STATE%20NOTIFICATION"
traction_control_indicator_categoryId = "42"
traction_control_indicator_propertyId = "557876104"
traction_control_indicator_modeId = "807"

cruise_control_state_alert_deviceLog_string = "constr_and_send_proto_msg success for 44"
cruise_control_state_notification_name = "CRUISE CONTROL STATE NOTIFICATION"
cruise_control_state_categoryName = "CRUISE%20CONTROL%20STATE%20NOTIFICATION"
cruise_control_state_categoryId = "44"
cruise_control_state_propertyId = "557875291"
cruise_control_state_alert_modeId = "807"

harsh_acceleration_notification_deviceLog_string = "constr_and_send_proto_msg success for 69"
harsh_acceleration_notification_name = "HARSH ACCELERATION NOTIFICATION"
harsh_acceleration_categoryName = "HARSH%20ACCELERATION%20NOTIFICATION"
harsh_acceleration_categoryId = "69"
harsh_acceleration_propertyId = "557876191"
harsh_acceleration_modeId = "807"

harsh_breaking_notification_deviceLog_string = "constr_and_send_proto_msg success for 70"
harsh_breaking_notification_name = "HARSH BRAKING NOTIFICATION"
harsh_breaking_categoryName = "HARSH%20BRAKING%20NOTIFICATION"
harsh_breaking_categoryId = "70"
harsh_breaking_propertyId = "557876189"
harsh_breaking_modeId = "807"

limp_mode_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 59"
limp_mode_notification_name = "LIMP MODE NOTIFICATION"
limp_mode_categoryName = "LIMP%20MODE%20NOTIFICATION"
limp_mode_categoryId = "59"
limp_mode_propertyId = "557876073"
limp_mode_modeId = "807"

motor_temp_warn_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 41"
motor_temp_warn_notification_name = "MOTOR TEMPERATURE WARNING NOTIFICATION"
motor_temp_warn_categoryName = "MOTOR%20TEMPERATURE%20WARNING%20NOTIFICATION"
motor_temp_warn_categoryId = "41"
motor_temp_warn_propertyId = "557876073"
motor_temp_warn_alert_modeId = "807"

hill_hold_state_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 46"
hill_hold_state_notification_name = "HILL HOLD STATE NOTIFICATION"
hill_hold_state_categoryName = "HILL%20HOLD%20STATE%20NOTIFICATION"
hill_hold_state_categoryId = "46"
hill_hold_state_propertyId = "557876054"
hill_hold_state_alert_modeId = "807"

bike_charge_state_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 51"
bike_charge_state_notification_name = "BIKE CHARGING STATE NOTIFICATION"
bike_charge_state_categoryName = "BIKE%20CHARGING%20STATE%20NOTIFICATION"
bike_charge_state_categoryId = "51"
bike_charge_state_propertyId = "557875425"
bike_charge_state_alert_modeId = "807"

vehicle_fully_charged_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 47"
vehicle_fully_charged_notification_name = "VEHICLE FULLY CHARGED NOTIFICATION"
vehicle_fully_charged_categoryName = "VEHICLE%20FULLY%20CHARGED%20NOTIFICATION"
vehicle_fully_charged_categoryId = "47"
vehicle_fully_charged_propertyId = "559972569"
vehicle_fully_charged_alert_modeId = "807"

low_battery_state_1_notification_deviceLog_string = "constr_and_send_proto_msg success for 62"
low_battery_state_1_notification_name = "LOW BATTERY STATE 1 NOTIFICATION"
low_battery_state_1_categoryName = "LOW%20BATTERY%20STATE%201%20NOTIFICATION"
low_battery_state_1_categoryId = "62"
low_battery_state_1_propertyId = "557876173"
low_battery_state_1_modeId = "807"

low_battery_state_2_notification_deviceLog_string = "constr_and_send_proto_msg success for 63"
low_battery_state_2_notification_name = "LOW BATTERY STATE 2 NOTIFICATION"
low_battery_state_2_categoryName = "LOW%20BATTERY%20STATE%202%20NOTIFICATION"
low_battery_state_2_categoryId = "63"
low_battery_state_2_propertyId = "557876173"
low_battery_state_2_modeId = "807"

# To verify alerts in the c2c logs
battery_health_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 71"

battery_high_temp_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 72"

motor_health_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 73"

mcu_high_temp_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 75"

thermal_run_away_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 77"

brake_control_fail_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 78"

handlebar_controls_fail_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 79"

bms_communication_fail_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 80"

mcu_communication_fail_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 82"

obc_communication_fail_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 82"

flat_tire_error_for_front_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for "

flat_tire_error_for_rear_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 93"

low_pressure_for_rear_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 94"

low_pressure_for_front_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 92"

high_pressure_for_rear_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 92"

high_pressure_for_front_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 94"

pin_error_alert_notification_deviceLog_string = "constr_and_send_proto_msg success for 25"

# Vehicle states:
connected = "CONNECTED"

# Vehicle configuration paths
# Normal Mode:
vehicle_mode_normal = "NORMAL_MODE"
normal_mode_path = "vehicle_settings.vehicle_mode.normal_mode"  # till r8 patch1
normal_mode_path_v1 = "vehicle_settings.user_settings.vehicle_mode.normal_mode"  # for r8 patch2 onwards

# Privacy Mode:
vehicle_mode_privacy = "PRIVACY_MODE"
privacy_mode_path = "vehicle_settings.vehicle_mode.privacy_mode"  # till r8 patch1
privacy_mode_path_v1 = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"  # for r8 patch2 onwards

# Incognito Mode:
incognito_mode_privacy = "INCOGNITO_MODE"
incognito_mode_path = "vehicle_settings.vehicle_mode.incognito_mode"  # till r8 patch1
incognito_mode_path_v1 = "vehicle_settings.user_settings.vehicle_mode.incognito_mode"  # for r8 patch2 onwards


telemetry_remote_diagnostic_event_type1 = "6504"
telemetry_remote_diagnostic_event_type2 = "6505"
telemetry_remote_diagnostic_event_type3 = "6506"

command_dtcClear = "CLEARALL_DTCS"
command_dtcRequest = "DTC_REQUEST"

