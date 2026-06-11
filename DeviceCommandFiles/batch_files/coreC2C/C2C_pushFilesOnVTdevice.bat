@echo off

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR TELEMATICS VT DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo VTdeviceSerialNo : %1
echo pushBinLibFlag : %2
echo pushConfFlag : %3
echo Is VT device primary : %4

REM: print new line
echo.
REM: print new line
echo.

:: Set the source folder path for conf & sh files
set cert_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew

:: Set the destination folder path for conf & sh files
set conf_dest_path= /etc/

:: Set the destination folder path for certs files
set cert_dest_path= /data/usr/local/

:: Set the source brooks folder path for TCU binaries
set vt_bin_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\VT\bin\

:: Set the source brooks folder path for TCU libraries
set vt_lib_path=\\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\C2C\VT\lib\

:: Set the destination folder path for bin & lib files
set dest_binLib_path= /data/usr/

IF "%4" == "No" (
IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH BINAREIES ON VT DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 push %tcu_bin_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%bin/**"
)

IF "%2%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH LIBRARIES ON VT DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

cmd /k "adb -s %1 push %tcu_lib_path% %dest_binLib_path% & adb -s %1 shell chmod +x %dest_binLib_path%lib/**"
)
)

IF "%3%"=="Yes" (
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON VT DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.
cmd /k "adb -s %1 shell mount -o remount, rw / & adb -s %1 push %folder_path%\c2c\ %conf_dest_path% & adb -s %1 push %folder_path%\c2c\ /data/ & adb -s %1 shell dos2unix /data/c2c/car2cloud.conf & adb -s %1 shell dos2unix /data/c2c/dm.conf & adb -s %1 shell cp /data/c2c/** /etc/c2c/ & adb -s %1 shell chmod +x %conf_dest_path%c2c/** & adb -s %1 shell dos2unix %conf_dest_path%c2c/** & adb -s %1 push %cert_path%\certs\token_cert /data/qwes/ & adb -s %1 shell dos2unix /data/qwes/token_cert & adb -s %1 shell rm /persist/data/pfm/licenses/* & adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]*"
)