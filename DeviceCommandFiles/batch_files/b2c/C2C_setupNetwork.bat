@echo off

REM: print new line
set execution_backup_folder =C:\Car2Cloud_E2ETesting_Drimaes\C2CtestReport\e2eExecution_Backup 

IF "%2%"=="WiFi" goto WiFi
IF "%2%"=="WiFi_disable" goto WiFi_disable
IF "%2%"=="WiFi_enable" goto WiFi_enable

:WiFi
adb -s %1 shell cmd wifi set-wifi-enabled enabled
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3 > %execution_backup_folder%\NetworkStatus\networkStatus.txt

:WiFi_disable

adb -s %1 shell svc wifi disable

:WiFi_enable_enabled

adb -s %1 shell svc wifi enable

