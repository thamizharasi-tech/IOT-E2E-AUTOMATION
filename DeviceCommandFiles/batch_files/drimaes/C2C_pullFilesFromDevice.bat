@echo off

:: Set the destination folder path for conf & sh files
set conf_dest_path= /mnt/vendor/persist/data/c2c/
set execution_backup_folder =C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup 

IF "%2%"=="DeviceOnboarding" (
REM: print new line
echo.
adb -s %1 pull %conf_dest_path% C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\
::adb -s %1 pull %conf_dest_path% %execution_backup_folder%\DeviceOnboarding_backup\ivi_files\
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\ivi_c2clogs.txt

)
IF "%2%"=="OTA" (
REM: print new line
echo.
cmd /k "adb -s %1 pull %conf_dest_path%ota_session.json C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ & adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ivi_c2clogs_ota.txt & adb -s %1 shell aota -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\c2c_aota.txt & adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ivi_c2clogs.txt"
)

IF "%2%"=="SOTA" (
REM: print new line
echo.
cmd /k "adb -s %1 pull %conf_dest_path%sota_session.json C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ & adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ivi_c2clogs_sota.txt & adb -s %1 shell aota -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\c2c_aota.txt & adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ivi_c2clogs.txt"
)

IF "%2%"=="OTA_firmwareVer_before" (
REM: print new line
echo.
cmd /k "adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\"
)

IF "%2%"=="OTA_firmwareVer_after" (
REM: print new line
echo.
cmd /k "adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\"
)

IF "%2%"=="c2clogger" (
REM: print new line
echo.
adb -s %1 pull %conf_dest_path%c2c_c2clogger.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\
adb -s %1 shell > %conf_dest_path%c2c_c2clogger.txt
)

IF "%2%"=="aota" (
REM: print new line
echo.
adb -s %1 pull %conf_dest_path%c2c_aota.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\
adb -s %1 shell aota > %conf_dest_path%sota_session.json C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\c2c_aota.txt
)

IF "%2%"=="OTAlogs" (
REM: print new line
echo.
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\ivi_files\ivi_c2clogs.txt
)

IF "%2%"=="C2Clogs" (
REM: print new line
echo.
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\c2clogs.txt
)



