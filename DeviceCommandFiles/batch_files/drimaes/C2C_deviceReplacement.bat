@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files

:: Set the destination folder path for conf & sh files
set conf_dest_path=/mnt/vendor/persist/data/

:: Set the destination folder path for certs files
set cert_dest_path=/mnt/vendor/persist/data/

:: Set the source brooks folder path for IVI binaries
set ivi_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\fota\ota_bins_libs

:: Set the source brooks folder path for IVI libraries
set ivi_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\fota\ota_bins_libs

:: Set the destination folder path for bin & lib files
set dest_bin_path=/data/

:: Set the destination folder path for bin & lib files
set dest_lib_path=/data/

:: Set the source folder path for ota conf files
set ota_folder_path=\\brooks\qces_logs2\C2C\R1.4\Client\fota\ota_conf

:: Set the destination folder path for ota conf
set ota_conf_dest_path=/mnt/vendor/persist/data/c2c/


REM: print new line

SET HOUR=%time:~0,2%
SET dtStamp9=%date:~-4%%date:~4,2%%date:~7,2%0%time:~1,1%%time:~3,2% 
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%%time:~0,2%%time:~3,2%

if "%HOUR:~0,1%" == " " (SET dtStamp=%dtStamp9%) else (SET dtStamp=%dtStamp24%)

::ECHO %dtStamp%

set mydate=%date:~-4%%date:~4,2%%date:~7,2%
::echo %mydate%

IF "%2%"=="IVI" goto IVI

:IVI
adb -s %1 shell cat /vendor/firmware_mnt/verinfo/ver_info.txt
adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting_Drimaes\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ 
::adb -s %1 shell date --s %dtStamp% 
::adb -s %1 shell ifconfig eth0 192.168.10.102 up 
adb -s %1 root
adb -s %1 push %folder_path%\c2c\ %conf_dest_path% 
adb -s %1 push %folder_path%\certs\clientcert.pem.crt %cert_dest_path%c2c/ 
adb -s %1 push %folder_path%\certs\private.pem.key %cert_dest_path%c2c/ 
adb -s %1 push %folder_path%\certs\cacert.pem %cert_dest_path%c2c/
adb -s %1 shell chmod +x %conf_dest_path%c2c/* 
::adb -s %1 shell chmod +x %cert_dest_path%certs/* 
adb -s %1 shell dos2unix %conf_dest_path%c2c/*
adb -s %1 shell dos2unix %conf_dest_path%c2c/c2c_default.conf
adb -s %1 shell dos2unix %conf_dest_path%c2c/car2cloud.conf 
adb -s %1 shell dos2unix %conf_dest_path%c2c/side_loaded.conf 
adb -s %1 shell dos2unix %conf_dest_path%c2c/dm.conf
adb -s %1 shell dos2unix %conf_dest_path%c2c/c2c_vehicle.json  
::adb -s %1 shell dos2unix %cert_dest_path%certs/* 
adb -s %1 push %folder_path%\shFiles\start_IVI_services.sh %dest_bin_path% 
adb -s %1 shell chmod 777 %dest_bin_path%/start_IVI_services.sh 
adb -s %1 shell dos2unix %ota_conf_dest_path%\ota.conf 
adb -s %1 push %folder_path%\shFiles\start_IVI_OTAservices.sh %dest_bin_path% 
adb -s %1 shell chmod 777 %dest_bin_path%/start_IVI_OTAservices.sh
adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/*
adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/dm.conf
adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/c2c_default.conf

:Exit
