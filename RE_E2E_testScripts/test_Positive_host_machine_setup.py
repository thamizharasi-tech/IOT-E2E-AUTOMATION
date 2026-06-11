import os
import re
import shutil
import subprocess

import pytest

from B2C_E2E_testScripts.test_Positive0_metabuild_flash_IVI import deviceType
from C2CModules import primary_IVI_device_modules
from C2CModules.e2e_testData import data_file
from C2CModules.token_generation import *
from utils.XLUtils import XlsxReader, get_rowNo_from_excel


class Test_hostMachineSetup:



    def test_setup_hostMachine_for_Drimaes(self):
        try:
            shutil.copytree(r'\\brooks\qces_logs2\C2C\C2C_E2E_AxiomAutomationSetup\Axiom_host_machine_setup_files\Car2Cloud_E2ETesting', 'C:\Car2Cloud_E2ETesting_new',dirs_exist_ok=True)

            # def devID(self):
            print("Starting device id fetching ")
            proc = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            output, errors = proc.communicate()
            proc.wait()
            outputer = output.decode('utf-8')
            l1 = outputer
            l2 = l1.split(" ")
            devlist = l2[3].split("\n")
            dev1 = devlist[1].split("\t")
            dev2 = devlist[2].split("\t")
            dev3 = devlist[3].split("\t")
            actualdevices = [dev1[0], dev2[0], dev3[0]]
            print("devices found:", actualdevices)
            for actualdevice in actualdevices:
                if actualdevice.isalnum() == True:
                    if actualdevice != '\r' or actualdevice != '':
                        proc = subprocess.Popen(['adb', '-s', actualdevice, 'shell', 'hostname'],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                        output, errors = proc.communicate()
                        proc.wait()
                        outputer1 = output.decode('utf-8')
                        outputer1 = str(outputer1).replace('\r', '').replace('\n', '')
                        print("hostname command resp : ", outputer1)
                        if outputer1 == 'localhost':
                            Product_Flavor_ivi = primary_IVI_device_modules.checkFirmwareVer(self, deviceType,
                                                                                             actualdevice)
                            #print(Product_Flavor_ivi)
                            IVI_devID = actualdevice
                            print("IVI Device Serial No is:", IVI_devID)
                            if Product_Flavor_ivi == 'asic':
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo_Primary(B2C)")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")
                            elif Product_Flavor_ivi == '6155':
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo_Primary(Drimaes)")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")
                            elif Product_Flavor_ivi == '8295':
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")
                            else:
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo_Primary(B2C)")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo_Primary(Drimaes)")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")
                                wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo",
                                                                             "ivi_adbSerialNo")
                                XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, IVI_devID)
                                print(
                                    f" => Updated {data_file} - row number : {rowNo} with IVI device serial no - {actualdevice} ")

                        elif outputer1 == 'sa515m':
                            devID = actualdevice
                            print("TCU Device Serial No is:", devID)
                            wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo", "tcu_adbSerialNo")
                            XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, devID)
                            print(
                                f" => Updated {data_file} - row number : {rowNo} with TCU device serial no - {actualdevice} ")
                        elif outputer1 == 'sa2150p':
                            devID = actualdevice
                            print("VT Device Serial No is:", devID)
                            wb_obj, wsheet, rowNo = get_rowNo_from_excel(data_file, "DeviceSerialNo", "vt_adbSerialNo")
                            XlsxReader.writeData(data_file, "DeviceSerialNo", rowNo, 2, devID)
                            print(
                                f" => Updated {data_file} - row number : {rowNo} with VT device serial no - {actualdevice} ")
        except:
            print("Something went wrong while host machine setup, pls try manually")


    def test_api_test_data_update(self):

        setup_Registration_testdata(self)
        setup_Registration_status_testdata(self)
        setup_Telemtery_testdata(self)
        setup_commandControl_testdata(self)
        setup_asset_testdata(self)
        setup_notify_testdata(self)
        setup_vehicle_testdata(self)
        setup_SOTA_testdata(self)
        setup_FOTA_testdata(self)
        setup_license_testdata(self)
        setup_SMP_testdata(self)
        setup_commandWrapper_testdata(self)
        setup_telPublisher_testdata(self)
        setup_statistics_testdata(self)
        setup_packageController_testdata(self)








