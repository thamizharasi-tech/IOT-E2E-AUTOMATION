@echo off

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR IVI DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo IVIdeviceSerialNo : %1
echo pushBinariesFlag : %2
echo pushLibrariesFlag : %2
echo pushConfFlag : %3
echo Is IVI device primary : %4

REM: print new line
echo.

IF "%4%"=="No" goto NonPrimary
IF "%4%"=="Yes" goto Primary

:NonPrimary

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path= /vendor/etc/

:: Set the destination folder path for certs files
set cert_dest_path= /data/usr/local/

:: Set the source brooks folder path for IVI binaries
set ivi_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\IVI\bin

:: Set the source brooks folder path for IVI libraries
set ivi_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\IVI\lib

:: Set the destination folder path for bin & lib files
set dest_bin_path= /vendor/bin/

:: Set the destination folder path for bin & lib files
set dest_lib_path= /vendor/lib64/
IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %ivi_bin_path%\softsku %dest_bin_path% & adb -s %1 shell chmod +x %dest_bin_path%softsku & adb -s %1 push %ivi_bin_path%\dm %dest_bin_path% & adb -s %1 shell chmod +x %dest_bin_path%dm"
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

cmd /k "adb -s %1 push %ivi_lib_path%\libc2cutils.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libc2cutils.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libjson.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3c.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libsoa.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3c.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3cs.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libjson.so %dest_lib_path%"
)

IF "%3%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %folder_path%\iviconfNew\dm.conf %conf_dest_path% & adb -s %1 shell chmod +x %conf_dest_path%dm.conf & adb -s %1 shell dos2unix %conf_dest_path%dm.conf & adb -s %1 push %folder_path%\iviconfNew\car2cloud.conf %conf_dest_path% & adb -s %1 shell chmod +x %conf_dest_path%car2cloud.conf & adb -s %1 push %folder_path%\iviconfNew\block_data_registry.bin %conf_dest_path% & adb -s %1 push %folder_path%\iviconfNew\cmd_registry.bin %conf_dest_path% & adb -s %1 push %folder_path%\iviconfNew\data_holder_registry.bin %conf_dest_path% & adb -s %1 push %folder_path%\iviconfNew\cmd_svc.conf %conf_dest_path% & adb -s %1 push %folder_path%\iviconfNew\sim_comm_info.json %conf_dest_path% & adb -s %1 push %folder_path%\iviconfNew\tele_service.conf %conf_dest_path% & adb -s %1 push %folder_path%\shFiles\start_IVI_services.sh %dest_bin_path% & adb -s %1 shell chmod +x %dest_bin_path%start_IVI_services.sh & adb -s %1 shell dos2unix %dest_bin_path%start_IVI_services.sh"
)

goto Exit

:Primary

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path= /vendor/

:: Set the destination folder path for certs files
set cert_dest_path= /data/usr/local/

:: Set the source brooks folder path for IVI binaries
set ivi_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\IVI\bin

:: Set the source brooks folder path for IVI libraries
set ivi_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\IVI\lib

:: Set the destination folder path for bin & lib files
set dest_bin_path= /vendor/bin/

:: Set the destination folder path for bin & lib files
set dest_lib_path= /vendor/lib64/
IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %ivi_bin_path%\softsku %dest_bin_path% & adb -s %1 shell chmod +x %dest_bin_path%softsku & adb -s %1 push %ivi_bin_path%\dm %dest_bin_path% & adb -s %1 shell chmod +x %dest_bin_path%dm"
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

cmd /k "adb -s %1 push %ivi_lib_path%\libc2cutils.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libc2cutils.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libjson.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3c.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libsoa.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3c.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libpaho-mqtt3cs.so %dest_lib_path% & adb -s %1 push %ivi_lib_path%\libjson.so %dest_lib_path%"
)

IF "%3%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %folder_path%\c2c\ %conf_dest_path% & adb -s %1 push %folder_path%\certs\ %cert_dest_path% & adb -s %1 shell chmod +x %conf_dest_path%c2c/** & adb -s %1 shell chmod +x %cert_dest_path%certs/** & adb -s %1 shell dos2unix %conf_dest_path%c2c/** & adb -s %1 shell dos2unix %cert_dest_path%certs/** & adb -s %1 push %folder_path%\shFiles\start_IVI_services_primary.sh %dest_binLib_path%bin/ & adb -s %1 shell chmod +x %dest_binLib_path%bin/start_IVI_services_primary.sh"
)

:Exit
