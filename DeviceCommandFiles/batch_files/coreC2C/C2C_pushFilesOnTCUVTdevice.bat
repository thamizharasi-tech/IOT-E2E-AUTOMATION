@echo off

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PARAMETERS PASSED FOR TCUVT FUSION DEVICE ONBOARDING ***
echo ------------------------------------------------------------
REM: print new line
echo.

echo VTdeviceSerialNo : %1

REM: print new line
echo.
REM: print new line
echo.

:: Set the source folder path for conf & sh files
set tcu_folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set tcu_conf_dest_path= /data/c2c/common/files

:: Set the source folder path for conf & sh files
set cert_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\
set vt_folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew

:: Set the destination folder path for conf & sh files
set vt_conf_dest_path= /data/c2c/common/certs

:: Set the destination folder path for conf & sh files
set vt_conf_dest_path1= /etc/


cmd /k "adb -s %1 shell mkdir /data/c2c/common/files & adb -s %1 shell systemctl stop c2c_dm & adb -s %1 shell systemctl stop softsku & adb -s %1 push %vt_folder_path%\c2c\ %vt_conf_dest_path1%/ & adb -s %1 push %vt_folder_path%\c2c\ %vt_conf_dest_path% & adb -s %1 shell dos2unix %vt_conf_dest_path%/c2c/car2cloud.conf & adb -s %1 shell dos2unix %vt_conf_dest_path%/c2c/dm.conf & adb -s %1 shell cp %vt_conf_dest_path%/c2c/** /etc/c2c/ & adb -s %1 shell chmod +x %vt_conf_dest_path%/c2c/** & adb -s %1 shell dos2unix %vt_conf_dest_path%/c2c/** & adb -s %1 push %cert_path%\certs\token_cert /data/qwes/ & adb -s %1 shell dos2unix /data/qwes/token_cert & adb -s %1 shell rm /persist/data/pfm/licenses/** & adb -s %1 shell setenforce 0 & adb -s %1 push %tcu_folder_path%\c2c\ %tcu_conf_dest_path% & adb -s %1 push %tcu_folder_path%\certs\ %tcu_conf_dest_path% & adb -s %1 shell chmod +x %tcu_conf_dest_path%/c2c/** & adb -s %1 shell chmod +x %tcu_conf_dest_path%/certs/** & adb -s %1 shell dos2unix %tcu_conf_dest_path%/c2c/** & adb -s %1 shell dos2unix %tcu_conf_dest_path%/certs/** & adb -s %1 push %tcu_folder_path%\shFiles\deviceOnboarding_tcuvt.sh %tcu_conf_dest_path% & adb -s %1 shell chmod +x %tcu_conf_dest_path%/deviceOnboarding_tcuvt.sh & adb -s %1 shell sh %tcu_conf_dest_path%/deviceOnboarding_tcuvt.sh"

