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
cmd /k "adb -s %1 shell app status > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\appList_%3%.txt"
pause 2
goto Exit

:SOTA_after
cmd /k "adb -s %1 shell app status > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\appList_%3%.txt"
pause 2
goto Exit

:FOTA_before
cmd /k "adb -s %1 shell uname -a > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\uname-a.txt & adb -s %1 shell getslotsuffix > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\beforeOTA\currentSlot.txt"
pause 2
goto Exit

:FOTA_after
cmd /k "adb -s %1 shell uname -a > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\uname-a.txt & adb -s %1 shell getslotsuffix > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA\afterOTA\currentSlot.txt"
pause 2
goto Exit

:Exit


