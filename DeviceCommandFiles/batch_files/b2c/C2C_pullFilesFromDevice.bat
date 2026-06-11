@echo off

:: Set the destination folder path for conf & sh files
set conf_dest_path= /mnt/vendor/persist/data/c2c/
set conf_dest_path1= /mnt/vendor/persist/c2c/
set execution_backup_folder =C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup 

IF "%2%"=="DeviceOnboarding" (
REM: print new line
echo.
::adb -s %1 root
adb -s %1 pull %conf_dest_path% C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\
::adb -s %1 pull %conf_dest_path% %execution_backup_folder%\DeviceOnboarding_backup\ivi_files\
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\ivi_c2clogs.txt
adb -s %1 pull %conf_dest_path%
adb -s %1 shell logcat -d > c2clogs.txt
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
adb shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\log\c2clogs.txt
adb -s %1 shell logcat -d > c2clogs.txt
)

IF "%2%"=="Trip_waypoints" (
REM: print new line
echo.
adb -s %1 pull %conf_dest_path%/Trip_waypoints C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\
adb -s %1 pull %conf_dest_path%/Trip_waypoints
)

IF "%2%"=="stability_logs" (
REM: print new line
echo c2clogs_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Stability_logs\c2clogs_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt
adb shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Stability_logs\c2clogs_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt
)

:: Pull configuration files and logs
IF "%2%"=="pullFiles" (
REM: print new line
echo.
::adb -s %1 root
adb -s %1 pull %conf_dest_path1% C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\
::adb -s %1 pull %conf_dest_path% %execution_backup_folder%\DeviceOnboarding_backup\ivi_files\
adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\ivi_c2clogs.txt
adb -s %1 pull %conf_dest_path1%
adb -s %1 shell logcat -d > c2clogs.txt
)

:: Pull C2C health report
IF "%2%"=="c2c_health_report" (
REM: print new line
echo.
adb -s %1 pull /data/c2c.csv C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\
)