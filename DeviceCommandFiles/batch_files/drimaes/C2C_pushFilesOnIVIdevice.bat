@echo off

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR IVI DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo IVIdeviceSerialNo : %1
echo pushBinariesLibrariesFlag : %2

REM: print new line
echo.

:Primary

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

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
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
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

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
adb -s %1 root
adb -s %1 push %ivi_bin_path%\ota_manager %dest_bin_path% 
adb -s %1 shell chmod +x %dest_bin_path%ota_manager
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
adb -s %1 push %ivi_bin_path%\c2c_ivi_fota.so %dest_bin_path% 
)


