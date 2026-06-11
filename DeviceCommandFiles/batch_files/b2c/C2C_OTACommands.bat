@echo off
CLS
SETLOCAL enabledelayedexpansion

IF "%2%"=="SOTA_before" goto SOTA_before
IF "%2%"=="SOTA_after" goto SOTA_after
IF "%2%"=="FOTA_before" goto FOTA_before
IF "%2%"=="FOTA_after" goto FOTA_after
echo invalid argument.
goto Exit

:SOTA_before
cmd /k "adb -s %1 shell pm list packages --user 10 > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\appList_%3%.txt"
goto Exit

:SOTA_after
cmd /k "adb -s %1 shell pm list packages --user 10 > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\appList_%3%.txt"
goto Exit

:FOTA_before
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/ota_session.json
adb -s %1 shell uname -a > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\uname-a.txt 
adb -s %1 shell bootctl get-current-slot > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\currentSlot.txt
adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\
goto Exit

:FOTA_after
cmd /k "adb -s %1 shell uname -a > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\uname-a.txt & adb -s %1 shell bootctl get-current-slot > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\currentSlot.txt & adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\"
goto Exit

:Exit


