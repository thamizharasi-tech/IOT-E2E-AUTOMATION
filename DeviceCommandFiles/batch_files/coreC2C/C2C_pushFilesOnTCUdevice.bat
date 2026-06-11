@echo off

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR TELEMATICS DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo TCUdeviceSerialNo : %1
echo pushBinLibFlag : %2
echo pushConfFlag : %3
echo Is TCU a NAD device : %4

REM: print new line
echo.
REM: print new line
echo.

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path= /etc/
set conf_dest_path1= /data/c2c/common/certs

:: Set the destination folder path for certs files
set cert_dest_path= /data/usr/local/

:: Set the source brooks folder path for TCU binaries
set tcu_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\TCU\bin\

:: Set the source brooks folder path for NAD binaries
set nad_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\NAD_TCU\bin\

:: Set the source brooks folder path for TCU libraries
set tcu_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\TCU\lib\

:: Set the source brooks folder path for NAD libraries
set nad_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\NAD_TCU\lib\

:: Set the destination folder path for bin & lib files
set dest_binLib_path= /data/usr/

:: Set the destination folder path for bin & lib files
set confdest_path= /data/c2c/




IF "%4" == "No" (
IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON TCU DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %tcu_bin_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%bin/**"
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON TCU DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

cmd /k "adb -s %1 push %tcu_lib_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%lib/**"
)
)

IF "%4" == "Yes" (
IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON NAD DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %nad_bin_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%bin/**"
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON NAD DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

cmd /k "adb -s %1 push %nad_lib_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%lib/**"
)
)

IF "%3%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON TELEMATICS DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
adb -s %1 push %folder_path%\c2c\ %conf_dest_path% 
adb -s %1 push %folder_path%\c2c\ %conf_dest_path1%/ 
adb -s %1 shell chmod +x %conf_dest_path1%/c2c/* 
adb -s %1 shell dos2unix %conf_dest_path1%/c2c/* 
adb -s %1 shell cp %conf_dest_path1%/c2c/** %conf_dest_path%/c2c/ 
adb -s %1 push %folder_path%\certs\ %cert_dest_path% 
adb -s %1 shell chmod +x %conf_dest_path%c2c/* 
adb -s %1 shell chmod +x %cert_dest_path%certs/** 
adb -s %1 shell dos2unix %conf_dest_path%c2c/** 
adb -s %1 shell dos2unix %cert_dest_path%certs/** 
adb -s %1 push %folder_path%\certs\token_cert /data/qwes/ 
adb -s %1 shell dos2unix /data/qwes/token_cert 
adb -s %1 shell rm /persist/data/pfm/licenses/* 
adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* 
adb -s %1 push %folder_path%\c2c\ %conf_dest_path1% 
adb -s %1 shell dos2unix %conf_dest_path1%/c2c/*
)