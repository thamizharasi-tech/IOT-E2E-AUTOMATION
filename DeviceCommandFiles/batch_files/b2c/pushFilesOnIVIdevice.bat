@echo off

REM: print new line

echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR IVI DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo IVIdeviceSerialNo : %1

REM: print new line
echo.

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path=/mnt/vendor/persist/data/
set conf_dest_path1=/mnt/vendor/persist/

:: Set the destination folder path for certs files
set cert_dest_path=/mnt/vendor/persist/data/
set cert_dest_path1=/mnt/vendor/persist/

IF "%2%"=="conf_file_path1" (

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
adb -s %1 root
echo ------------------------------------------------------------
echo *** REMOVE BIN FILES ON IVI DEVICE FOR FRESH ONBOARDING ***
echo ------------------------------------------------------------
adb -s %1 shell rm -rf /mnt/vendor/persist/data/c2c/*.bin*
adb -s %1 push %folder_path%\c2c\ %conf_dest_path%
adb -s %1 push %folder_path%\certs\clientcert.pem.crt %cert_dest_path%c2c/
adb -s %1 push %folder_path%\certs\private.pem.key %cert_dest_path%c2c/
adb -s %1 push %folder_path%\certs\cacert.pem %cert_dest_path%c2c/
adb -s %1 shell chmod +x %conf_dest_path%c2c/*
adb -s %1 shell dos2unix %conf_dest_path%c2c/*
adb -s %1 shell dos2unix %conf_dest_path%c2c/c2c_default.conf
adb -s %1 shell dos2unix %conf_dest_path%c2c/side_loaded.conf
adb -s %1 shell dos2unix %conf_dest_path%c2c/dm.conf
adb -s %1 shell dos2unix %conf_dest_path%c2c/c2c_vehicle.json

)


IF "%2%"=="conf_file_path2" (

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
adb -s %1 root
echo ------------------------------------------------------------
echo *** REMOVE BIN FILES ON IVI DEVICE FOR FRESH ONBOARDING ***
echo ------------------------------------------------------------
adb -s %1 shell rm -rf /mnt/vendor/persist/data/c2c/*.bin*
adb -s %1 push %folder_path%\c2c\ %conf_dest_path1%
adb -s %1 push %folder_path%\certs\clientcert.pem.crt %cert_dest_path1%c2c/
adb -s %1 push %folder_path%\certs\private.pem.key %cert_dest_path1%c2c/
adb -s %1 push %folder_path%\certs\cacert.pem %cert_dest_path1%c2c/
adb -s %1 shell chmod +x %conf_dest_path1%c2c/*
adb -s %1 shell dos2unix %conf_dest_path1%c2c/*
adb -s %1 shell dos2unix %conf_dest_path1%c2c/c2c_default.conf
adb -s %1 shell dos2unix %conf_dest_path1%c2c/side_loaded.conf
adb -s %1 shell dos2unix %conf_dest_path1%c2c/dm.conf
adb -s %1 shell dos2unix %conf_dest_path1%c2c/c2c_vehicle.json

)
