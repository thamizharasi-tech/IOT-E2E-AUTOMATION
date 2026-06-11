import inspect
import logging
import os.path
import subprocess
import sys
import time

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

sys.path.insert(1, r'C:\Car2Cloud_E2ETesting')

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

# try:
#     from axiom.ttypes import *
# except:
#     from Axiom.ttypes import *
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *


# ===================================
# Flash ECRM image on base metabuild
# ===================================
def flash_ecrm_image_on_device(self, device_type, chipset_type):
    try:
        if device_type == deviceType_TCU and chipset_type == c2c_tcu_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashingECRMbuild_TCU.bat',
                 tcu_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_VT and chipset_type == c2c_vt_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashingECRMbuild_VT.bat',
                 vt_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI_nonPrimary and chipset_type == c2c_ivi_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashingECRMbuild_IVI.bat',
                 ivi_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            if drimaes_ecrmImage_flag == "Yes":
                path = drimaes_ecrmImage_path
            else:
                path = drimaes_ecrmImage_brooksPath
            output = subprocess.check_output(
                [drimaes_batchPath + 'C2C_flashingECRMbuild_IVI.bat',
                 drimaes_ivi_adbSerialNo, path], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            if b2c_ecrmImage_flag == "Yes":
                path = b2c_ecrmImage_path
            else:
                path = b2c_ecrmImage_brooksPath
            output = subprocess.check_output(
                [b2c_batchPath + 'C2C_flashingECRMbuild_IVI.bat',
                 b2c_ivi_adbSerialNo, path], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            output = subprocess.check_output(
                [c2c_ivi_batchPath + 'C2C_flashingECRMbuild_IVI.bat',
                 c2c_ivi_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        output1 = output.decode('utf-8')
        print(f"=> ECRM image flash response : {format(output1)}")
        time.sleep(5)

        if "FAILED" not in output1 or "FAIL" not in output1 or "error" not in output1 :
            testResult(self, "passed",
                       'ECRM image should be flashed on top of base metabuild without any failure/errors',
                       'Falshing of ECRM image on top of base metabuild is successfully completed')
        else:
            testResult(self, "failed",
                       'ECRM image should be flashed on top of base metabuild without any failure/errors',
                       'Falshing of ECRM image on top of base metabuild is completed, pls refer logs for failure results')

    except FileNotFoundError:
        testResult(self, "failed", 'Flash ECRM image on top of base metabuild',
                   'Sorry, the file "C2C_flashingECRMbuild_XXX.bat" does not exist or incorrect file path/name')
    except:
        testResult(self, "failed", 'Flash ECRM image on top of base metabuild',
                   'Something went wrong while flashing ECRM image, Please refer logs')


# ===================================
# Flash HLOS image
# ===================================
def flash_hlos_image_on_device(self, device_type, chipset_type):
    try:
        if device_type == deviceType_TCU and chipset_type == c2c_tcu_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashHLOSImage_TCU.bat',
                 tcu_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_VT and chipset_type == c2c_vt_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashHLOSImage_VT.bat',
                 vt_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI_nonPrimary and chipset_type == c2c_ivi_chipset:
            output = subprocess.check_output(
                [C2CtestData_batchPath + 'C2C_flashHLOSImage_IVI.bat',
                 ivi_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
            if drimaes_hlosImage_flag == "Yes":
                path = drimaes_hlosImage_path
            else:
                path = drimaes_hlosImage_brooksPath
            output = subprocess.check_output(
                [drimaes_batchPath + 'C2C_flashHLOSImage_IVI.bat',
                 drimaes_ivi_adbSerialNo,path], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
            if b2c_hlosImage_flag == "Yes":
                path = b2c_hlosImage_path
            else:
                path = b2c_hlosImage_brooksPath
            output = subprocess.check_output(
                [b2c_batchPath + 'C2C_flashHLOSImage_IVI.bat',
                 b2c_ivi_adbSerialNo, path], stderr=subprocess.STDOUT, shell=True, timeout=180)

        elif device_type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
            output = subprocess.check_output(
                [c2c_ivi_batchPath + 'C2C_flashHLOSImage_IVI.bat',
                 c2c_ivi_adbSerialNo], stderr=subprocess.STDOUT, shell=True, timeout=180)

        output1 = output.decode('utf-8')
        print(f"=> HLOS image flash response : {format(output1)}")
        time.sleep(5)
        if "FAILED" not in output1 or "FAIL" not in output1 or "error" not in output1:
            testResult(self, "passed",
                       'HLOS image should be flashed on top of base metabuild without any failure/errors',
                       'Falshing of HLOS image on top of base metabuild is successfully completed')
        else:
            testResult(self, "failed",
                       'HLOS image should be flashed on top of base metabuild without any failure/errors',
                       'Falshing of HLOS image on top of base metabuild is completed, pls refer logs for failure results')

    except FileNotFoundError:

        testResult(self, "failed", 'Flash HLOS image on top of base metabuild',
                   'Sorry, the file "C2C_flashHLOSImage_XXX.bat" does not exist or incorrect file path/name')
    except:

        testResult(self, "failed", 'Flash HLOS image on top of base metabuild',
                   'Something went wrong while flashing hlos image, Please refer logs')