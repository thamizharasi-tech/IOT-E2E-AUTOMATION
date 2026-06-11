@echo off

:: Set the source folder path for conf & sh files
set tcu_folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set tcu_conf_dest_path= /data/c2c/common/

SET HOUR=%time:~0,2%
SET dtStamp9=%date:~-4%%date:~4,2%%date:~7,2%0%time:~1,1%%time:~3,2% 
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%%time:~0,2%%time:~3,2%

if "%HOUR:~0,1%" == " " (SET dtStamp=%dtStamp9%) else (SET dtStamp=%dtStamp24%)

::ECHO %dtStamp%

set mydate=%date:~-4%%date:~4,2%%date:~7,2%
::echo %mydate%

IF "%2%"=="reboot" goto rebootdevice
IF "%2%"=="root" goto root
IF "%2%"=="createFolder" goto createFolder
IF "%2%"=="remount" goto remountdevice
IF "%2%"=="currentSlot" goto currentSlot
IF "%2%"=="firmwareVer" goto firmwareVer
IF "%2%"=="uname-a" goto uname-a
IF "%2%"=="packageList" goto appList
IF "%2%"=="pushSotaSession" goto pushSotaSession
IF "%2%"=="pushotaSession" goto pushotaSession
IF "%2%"=="firmwareVer_tcu" goto firmwareVer_tcu
IF "%2%"=="firmwareVer_vt" goto firmwareVer_vt
IF "%2%"=="firmwareVer_tcuvt" goto firmwareVer_tcuvt
IF "%2%"=="tcu_logs" goto tcu_logs
IF "%2%"=="vt_logs" goto vt_logs
IF "%2%"=="ivi_logs" goto ivi_logs
IF "%2%"=="connectivityCheck" goto connectivityCheck
echo invalid argument.
goto Exit

:rebootdevice
cmd /k "adb -s %1 reboot"

goto Exit

:root
cmd /k "adb -s %1 root"

goto Exit

:createFolder
adb -s %1 shell mkdir /data/vendor/c2c
adb -s %1 shell mkdir /data/usr/local/certs

goto Exit

:remountdevice
cmd /k "adb -s %1 remount"

goto Exit

:firmwareVer
cmd /k "adb -s %1 shell cat /vendor/firmware_mnt/verinfo/ver_info.txt & adb -s %1 root"

goto Exit

:firmwareVer_vt
cmd /k "adb -s %1 shell cat /firmware/verinfo/ver_info.txt & adb -s %1 pull /firmware/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\vt_files\ & adb -s %1 shell date --s %mydate% & adb -s %1 root"

goto Exit

:firmwareVer_tcu
cmd /k "adb -s %1 shell cat /firmware/image/Ver_Info.txt & adb -s %1 pull /firmware/image/Ver_Info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\tcu_files\ & adb -s %1 shell date --s %dtStamp% & adb -s %1 shell ifconfig eth0 192.168.10.102 up & adb -s %1 root"

goto Exit

:firmwareVer_tcuvt
cmd /k "adb -s %1 shell cat /firmware/verinfo/ver_info.txt & adb -s %1 push %tcu_folder_path%\shFiles\firmwareDetails_tcuvt.sh %tcu_conf_dest_path% & adb -s %1 shell chmod +x %tcu_conf_dest_path%/firmwareDetails_tcuvt.sh & adb -s %1 shell sh %tcu_conf_dest_path%/firmwareDetails_tcuvt.sh %dtStamp% & adb -s %1 pull %tcu_conf_dest_path%/Ver_Info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\tcu_files\ & adb -s %1 root"

goto Exit

:uname-a
cmd /k "adb -s %1 shell uname -a"

goto Exit

:currentSlot
cmd /k "adb -s %1 shell bootctl get-current-slot"

goto Exit

:appList
cmd /k "adb -s %1 shell app status"

goto Exit

:pushSotaSession
cmd /k "adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ota_session.json /etc/c2c/ & adb -s %1 shell app restart tafUpdateSvc & adb -s %1 shell systemctl restart c2c_sota_manager"

goto Exit

:pushotaSession
cmd /k "adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ota_session.json /etc/c2c/ & adb -s %1 shell app restart tafUpdateSvc & adb -s %1 shell systemctl restart c2c_ota_manager"

goto Exit

:tcu_logs
cmd /k "adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\tcu_files\tcu_c2clogs.txt"

goto Exit

:vt_logs
cmd /k "adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\vt_files\vt_c2clogs.txt"

goto Exit

:ivi_logs
cmd /k "adb -s %1 shell logcat -d > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\ivi_c2clogs.txt"

goto Exit

:connectivityCheck
cmd /k "adb -s %1 shell ping -c 3 8.8.8.8"

goto Exit

:firmwareVer_ivi
cmd /k "adb -s %1 shell cat /vendor/firmware_mnt/verinfo/ver_info.txt & adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\"

goto Exit

:currentSlot
cmd /k "adb -s %1 shell bootctl get-current-slot"

goto Exit

:packageList
cmd /k "adb -s %1 shell pm list packages"

goto Exit

:connectivityCheck_ping
cmd /k "adb -s %1 shell ping -c 3 8.8.8.8"

:connectivityCheck_curl
cmd /k "adb -s %1 shell curl www.google.com"



:Exit

