import os
import subprocess


def create_folder_structure_for_execution_backup(self):
    # Common folder structure for backup
    folder_name = 'C:\Car2Cloud_E2ETesting_new'
    folder_name_ex_backup = 'C2CtestReport\e2eExecution_Backup'

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

        folders = ['C2CtestData', 'C2CtestReport']
        for folder in folders:
            if not os.path.exists(os.path.join(folder_name, folder)):
                os.mkdir(os.path.join(folder_name, folder))

        if not os.path.exists(os.path.join(folder_name, r'C2CtestReport\UI_Screenshots')):
            os.mkdir(os.path.join(folder_name, r'C2CtestReport\UI_Screenshots'))

        if not os.path.exists(os.path.join (folder_name, folder_name_ex_backup)):
            os.mkdir(os.path.join(folder_name, folder_name_ex_backup))

            # Create output subdirectories
            folders = ['API_responses', 'c2cLogs', 'DeviceOnboarding_backup', 'DeviceOnboarding_Pos_backup', 'DeviceOnboarding_Neg_backup',
                       'NetworkStatus', 'OTA', 'OTA_backup','FeatureUpdateByGroup','SKUupdateByGroup','SKUupdateByVIN']
            for folder in folders:
                if not os.path.exists(os.path.join(folder_name,folder_name_ex_backup, folder)):
                    os.mkdir(os.path.join(folder_name, folder_name_ex_backup,folder))

                if folder == 'DeviceOnboarding_backup' or folder == 'OTA' or folder == 'FeatureUpdateByGroup' or folder == 'SKUupdateByGroup'or folder == 'SKUupdateByVIN':

                    # Create output subdirectories
                    folders1 = ['API_Responses', 'ivi_files', 'tcu_files', 'vt_files']
                    for folder1 in folders1:
                        if not os.path.exists(
                                os.path.join(folder_name, folder_name_ex_backup, folder, folder1)):
                            os.mkdir(
                                os.path.join(folder_name, folder_name_ex_backup, folder, folder1))
                    if folder == "OTA":
                        folders2 = ['afterOTA', 'beforeOTA']
                        for folder2 in folders2:
                            if not os.path.exists(
                                    os.path.join(folder_name, folder_name_ex_backup, folder, folder2)):
                                os.mkdir(
                                    os.path.join(folder_name, folder_name_ex_backup, folder, folder2))




