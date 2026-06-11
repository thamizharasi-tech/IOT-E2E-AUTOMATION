@echo off

REM: print new line
set execution_backup_folder =C:\Car2Cloud_E2ETesting_Drimaes\C2CtestReport\e2eExecution_Backup 

IF "%2%"=="WiFi" goto WiFi

:WiFi
adb -s %1 shell cmd wifi set-wifi-enabled enabled
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3 > %execution_backup_folder%\NetworkStatus\networkStatus.txt