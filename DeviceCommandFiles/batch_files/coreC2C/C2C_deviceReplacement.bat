@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\tcu_files

:: Set the destination folder path for conf & sh files
set conf_dest_path= /etc/
set conf_dest_path1= /data/c2c/common/certs

REM: print new line

SET HOUR=%time:~0,2%
SET dtStamp9=%date:~-4%%date:~4,2%%date:~7,2%0%time:~1,1%%time:~3,2% 
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%%time:~0,2%%time:~3,2%

if "%HOUR:~0,1%" == " " (SET dtStamp=%dtStamp9%) else (SET dtStamp=%dtStamp24%)

::ECHO %dtStamp%

set mydate=%date:~-4%%date:~4,2%%date:~7,2%
::echo %mydate%

IF "%2%"=="TCU" goto TCU
IF "%2%"=="TCU1" goto TCU1

:TCU1
adb -s %1 push %folder_path%\c2c\ /data/c2c/
adb -s %1 push %folder_path%\c2c\ /etc/c2c/
adb -s %1 push %folder_path%\certs\ /data/usr/local/
adb -s %1 push %folder_path%\certs\token_certs /data/qwes/
adb -s %1 shell dos2unix /etc/c2c/*
adb -s %1 shell dos2unix /data/usr/local/certs/*
adb -s %1 shell dos2unix /data/qwes/token_certs

goto Exit

:TCU
adb -s 904ce5 shell systemctl stop c2c_dm
adb -s %1 shell cat /firmware/image/Ver_Info.txt
adb -s %1 pull /firmware/image/Ver_Info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\tcu_files\ 
adb -s %1 shell date --s %dtStamp% 
adb -s %1 shell ifconfig eth0 192.168.10.102 up 
adb -s %1 root
adb -s %1 push %folder_path%\c2c\ %conf_dest_path1% 
adb -s %1 push %folder_path%\certs\ %cert_dest_path%
adb -s %1 push %folder_path%\certs\token_cert /data/qwes/ 
adb -s %1 shell dos2unix %conf_dest_path1%\c2c\* 
adb -s %1 shell cp %conf_dest_path1%\c2c\** %conf_dest_path%\c2c\ 
adb -s %1 shell cp %conf_dest_path1%/c2c/* to /etc/c2c/
adb -s %1 shell chmod +x %conf_dest_path%c2c/* 
adb -s %1 shell chmod +x %cert_dest_path%certs/** 
adb -s %1 shell dos2unix %conf_dest_path%c2c/** 
adb -s %1 shell dos2unix %cert_dest_path%certs/** 
adb -s %1 shell dos2unix /data/qwes/token_cert 
adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* 
::adb -s %1 shell rm /persist/data/pfm/licenses/* 
::adb -s %1 shell chmod +x %conf_dest_path1%\c2c\* 
::adb -s %1 push %folder_path%\shFiles\start_services.sh %conf_dest_path1% 
::adb -s %1 shell chmod +x %conf_dest_path1%/start_services.sh 

:Exit
