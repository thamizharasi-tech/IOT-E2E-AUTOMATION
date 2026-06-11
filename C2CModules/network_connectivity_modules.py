import inspect
import logging
import os.path
import subprocess
import sys
import time

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from C2CModules.c2c_modules import deviceOnboardingType
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import drimaes_ivi_chipset, drimaes_batchPath, drimaes_ivi_adbSerialNo, b2c_ivi_chipset, \
    b2c_ivi_adbSerialNo, c2c_ivi_chipset, c2c_ivi_adbSerialNo, deviceType_IVI, \
    C2CtestData_batchPath, C2CtestReport_NetworkStatusPath, deviceType_TCU, c2c_tcu_chipset, tcu_adbSerialNo, c2c_vt_chipset, vt_adbSerialNo, \
    deviceType_IVI_nonPrimary, deviceType_VT

# try:
#     from axiom.ttypes import *
# except:
#     from Axiom.ttypes import *

sys.path.insert(1, r'C:\Car2Cloud_E2ETesting')

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

# =======================================
# Set internet connectivity on device
# =======================================

def verify_network_connectivity_on_device(self, deviceSerialNo, network_type):
    try:
        proc = subprocess.Popen(['adb', '-s', deviceSerialNo, 'shell', 'ping -c 3 8.8.8.8'], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        output, errors = proc.communicate()
        proc.wait()
        outputer = output.decode('utf-8')
        proc1 = subprocess.Popen(['adb', '-s', deviceSerialNo, 'shell', 'curl www.google.com'], stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        output, errors = proc1.communicate()
        proc.wait()
        outputer1 = output.decode('utf-8')
        # print(f"=> Ping response : {format(outputer)}")
        # print("\n=> Ping response : \n", output)
    except OSError:
        print(f"Sorry, Something went wrong while reading ping/curl response")
        outputer = "Network is unreachable"
    except:
        try:
            outputer = subprocess.call(
                [drimaes_batchPath + r'C2C_adbCommands.bat',
                 deviceSerialNo, "connectivityCheck_ping"])
            outputer1 = subprocess.call(
                [drimaes_batchPath + r'C2C_adbCommands.bat',
                 deviceSerialNo, "connectivityCheck_curl"])
        except FileNotFoundError:
            print(f"Sorry, the file 'C2C_adbCommands.bat' does not exist or incorrect file path/name")
    # print(f"=> Ping response : {format(outputer)}")
    print(f"=> curl response : {format(outputer1)}")
    return outputer, outputer1


def estabilish_network_connectivity_on_device(self, device_type, chipset_type, network_type):
    print("\n==========================================================")
    print(f"Network Connectivity on {device_type} - {chipset_type} device")
    print("==========================================================")
    if device_type == deviceType_TCU and chipset_type == c2c_tcu_chipset:
        device_adbSerialNo = tcu_adbSerialNo

    elif device_type == deviceType_VT and chipset_type == c2c_vt_chipset:
        device_adbSerialNo = vt_adbSerialNo

    elif device_type == deviceType_IVI_nonPrimary and chipset_type == c2c_ivi_chipset:
        device_adbSerialNo = c2c_ivi_adbSerialNo

    elif device_type == deviceType_IVI and chipset_type == drimaes_ivi_chipset:
        device_adbSerialNo = drimaes_ivi_adbSerialNo

    elif device_type == deviceType_IVI and chipset_type == b2c_ivi_chipset:
        device_adbSerialNo = b2c_ivi_adbSerialNo

    elif device_type == deviceType_IVI and chipset_type == c2c_ivi_chipset:
        device_adbSerialNo = c2c_ivi_adbSerialNo

    if network_type == "Ethernet":
        try:
            response_1 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)
            if "icmp_seq=2" in str(response_1[0]):
                print(f"Network connectivity is already established on {device_type}-{chipset_type} device")
            elif "icmp_seq=2" not in response_1 or 'Network is unreachable' in response_1:
                subprocess.call(
                    [C2CtestData_batchPath + r'C2C_setupNetwork.bat',
                     device_adbSerialNo, network_type], timeout=90)
                time.sleep(15)
                response_2 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)
                if "icmp_seq=2" in str(response_2[0]):
                    print(f"{network_type} network connectivity is established on {device_type}-{chipset_type} ")
                else:
                    print(f"{network_type} network connectivity is not established on {device_type}-{chipset_type} ")

        except FileNotFoundError:
            print(f"Sorry, the file does not exist or incorrect file path/name")
        except:
            response_2 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)
            if "icmp_seq=2" in str(response_2[0]):
                print(f"{network_type} network connectivity is established on {device_type}-{chipset_type} ")
                testResult(self, "failed", 'Establish network connectivity',
                           'Network connectivity is not established on device')
                assert False
            else:
                print(f"{network_type} network connectivity is not established on {device_type}-{chipset_type} ")
                testResult(self, "failed", 'Establish network connectivity',
                           'Network connectivity is not established on device')
                assert False

    elif network_type == "WiFi":
        try:
            print("First try : ")
            response_1 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)
            # print(response_1)

            if 'not found' in str(response_1[1]):
                print(f" => Device is not available to setup network connectivity")
                testResult(self, "failed", 'Establish network connectivity',
                           'Device is not available to setup network connectivity')
            elif 'Could not resolve host: www.google.com' not in str(response_1[1]):
                print(f" => Network connectivity is already established on {device_type} - {chipset_type} device")
                testResult(self, "passed", 'Establish network connectivity',
                           'Network connectivity is already established on device')
            elif 'Could not resolve host: www.google.com' in str(response_1[1]):
                print(
                    "-----------------------------------------------------------------------------------------------------------------")
                print(
                    f" => Network connectivity is not available on {device_type}-{chipset_type} device, hence configuring device for n/w connectivity : ")
                print(
                    "-----------------------------------------------------------------------------------------------------------------")
                subprocess.call(
                    [drimaes_batchPath + r'C2C_setupNetwork.bat',
                     device_adbSerialNo, network_type], timeout=60)
                time.sleep(10)
                response_2 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)

                with open(C2CtestReport_NetworkStatusPath + 'networkStatus.txt', 'r') as f:
                    status = f.read()
                if 'Could not resolve host: www.google.com' not in str(
                        response_2[1]) or status == 'Connection initiated':
                    print(f" => {network_type} network connectivity is established on {device_type}-{chipset_type} ")
                    testResult(self, "passed", 'Establish network connectivity',
                               'Network connectivity is established on device')
                if 'Could not resolve host: www.google.com' in str(response_2[1]) or status == 'Connection failed':
                    print(
                        f" => {network_type} network connectivity is not established on {device_type}-{chipset_type} ")
                    testResult(self, "failed", 'Establish network connectivity',
                               'Network connectivity is not established on device')
        except FileNotFoundError:
            print(f"Sorry, the file does not exist or incorrect file path/name")
        except:
            print("Second try : ")
            response_2 = verify_network_connectivity_on_device(self, device_adbSerialNo, network_type)
            if 'not found' in str(response_2[1]):
                print(f" => Device is not available to setup network connectivity")
                testResult(self, "failed", 'Establish network connectivity',
                           'Device is not available to setup network connectivity')
            elif 'Could not resolve host: www.google.com' not in str(response_2[1]):
                print(f" => {network_type} network connectivity is established on {device_type}-{chipset_type} ")
                testResult(self, "failed", 'Establish network connectivity',
                           'Network connectivity is established on device')
            else:
                print(f"{network_type} network connectivity is not established on {device_type}-{chipset_type} ")
                testResult(self, "failed", 'Establish network connectivity',
                           'Network connectivity is not established on device')
        print("=====================================================================================")


# ===================================
# IVI N/w Connectivity
# ===================================

def set_network_connectivity_on_device(self, onboarding_Type, chipset_type, network_type):
    onboardingType = deviceOnboardingType(self, onboarding_Type)
    singleDeviceOnboarding_IVI = str(onboardingType[0])
    comboDeviceOnboarding_TCUIVI = str(onboardingType[1])
    comboDeviceOnboarding_TCUVT_fusion = str(onboardingType[2])
    comboDeviceOnboarding_TCUVT = str(onboardingType[3])
    comboDeviceOnboarding_TCUIVIVT = str(onboardingType[4])
    comboDeviceOnboarding_TCUVTIVI_fusion = str(onboardingType[5])
    singleDeviceOnboarding_IVI = str(onboardingType[6])

    if comboDeviceOnboarding_TCUVT_fusion == "Yes":
        estabilish_network_connectivity_on_device(self, deviceType_VT, chipset_type, network_type)
    elif comboDeviceOnboarding_TCUIVI == "Yes":
        estabilish_network_connectivity_on_device(self, deviceType_TCU, chipset_type, network_type)
        estabilish_network_connectivity_on_device(self, deviceType_IVI, chipset_type, network_type)
    elif comboDeviceOnboarding_TCUVT == "Yes":
        estabilish_network_connectivity_on_device(self, deviceType_TCU, chipset_type, network_type)
        estabilish_network_connectivity_on_device(self, deviceType_VT, chipset_type, network_type)
    elif comboDeviceOnboarding_TCUIVIVT == "Yes":
        estabilish_network_connectivity_on_device(self, deviceType_TCU, chipset_type, network_type)
        estabilish_network_connectivity_on_device(self, deviceType_VT, chipset_type, network_type)
        estabilish_network_connectivity_on_device(self, deviceType_IVI, chipset_type, network_type)
    elif comboDeviceOnboarding_TCUVTIVI_fusion == "Yes":
        estabilish_network_connectivity_on_device(self, deviceType_VT, chipset_type, network_type)
        estabilish_network_connectivity_on_device(self, deviceType_IVI, chipset_type, network_type)

    elif onboarding_Type == deviceType_IVI or singleDeviceOnboarding_IVI == "Yes":
        if chipset_type == drimaes_ivi_chipset:
            estabilish_network_connectivity_on_device(self, deviceType_IVI, drimaes_ivi_chipset, network_type)
        elif chipset_type == b2c_ivi_chipset:
            estabilish_network_connectivity_on_device(self, deviceType_IVI, b2c_ivi_chipset, network_type)
        elif chipset_type == c2c_ivi_chipset:
            estabilish_network_connectivity_on_device(self, deviceType_IVI, c2c_ivi_chipset, network_type)
    else:
        print("Incorrect input")
