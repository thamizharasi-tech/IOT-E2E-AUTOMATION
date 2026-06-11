@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

IF "%1%"=="TCU" goto SingleTCUdevice
IF "%1%"=="IVI" goto SingleIVIdevice
IF "%1%"=="TCUIVI" goto ComboTCUIVIdevice
IF "%1%"=="TCUVT" goto ComboTCUVTdevice
IF "%1%"=="TCUIVIVT" goto ComboTCUIVIVTdevice
IF "%1%"=="TCUVT_fusion" goto ComboTCUVTdevice_fusion
echo invalid argument.
goto Exit

:SingleTCUdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU device***
echo -----------------------------------------
REM: print new line
REM: print new line

DEL %folder_path%\c2c\*.*?
adb -s %2 pull /etc/c2c/dm.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/car2cloud.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/side_loaded.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/c2c_default.conf %folder_path%\c2c\
copy %folder_path%\defaultConfNew\c2c_vehicle.json %folder_path%\c2c\ 
adb -s %2 shell rm /persist/data/pfm/licenses/[0-9]*


goto Exit

:SingleIVIdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for IVI device***
echo -----------------------------------------
REM: print new line
REM: print new line


goto Exit

:ComboTCUIVIdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU IVI devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

DEL %folder_path%\c2c\*.*?
DEL %folder_path%\iviconfNew\*.*?
adb -s %2 pull /etc/c2c/dm.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/car2cloud.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/side_loaded.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/c2c_default.conf %folder_path%\c2c\
adb -s %3 pull /vendor/etc/car2cloud.conf %folder_path%\iviconfNew\
adb -s %3 pull /vendor/etc/dm.conf %folder_path%\iviconfNew\
adb -s %2 shell ifconfig eth0 > %folder_path%\C2Cbat\ipAddressTCU.txt
copy %folder_path%\defaultConfNew\comboDevice\c2c_vehicle.json %folder_path%\c2c\ 
adb -s %2 shell rm /persist/data/pfm/licenses/[0-9]*

goto Exit

:ComboTCUVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

DEL %folder_path%\c2c\*.*?
DEL %folder_path%\vtconfNew\c2c\*.*?
adb -s %2 pull /etc/c2c/dm.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/car2cloud.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/side_loaded.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/c2c_default.conf %folder_path%\c2c\
adb -s %4 pull /etc/c2c/dm.conf %folder_path%\vtconfNew\c2c\
adb -s %4 pull /etc/c2c/car2cloud.conf %folder_path%\vtconfNew\c2c\
adb -s %2 shell ifconfig eth0 > %folder_path%\C2Cbat\ipAddressTCU.txt
copy %folder_path%\defaultConfNew\c2c_vehicle.json %folder_path%\c2c\ 
adb -s %2 shell rm /persist/data/pfm/licenses/[0-9]*
adb -s %4 shell rm /persist/data/pfm/licenses/[0-9]*

goto Exit

:ComboTCUVTdevice_fusion
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT fusion devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

DEL %folder_path%\c2c\*.*?
DEL %folder_path%\vtconfNew\c2c\*.*?
adb -s %4 shell mkdir /data/c2c/common/tcuFiles
adb -s %4 push %folder_path%\shFiles\pullTCUfiles_tuvt.sh /data/c2c/common/
adb -s %4 shell chmod +x /data/c2c/common/pullTCUfiles_tuvt.sh
adb -s %4 shell sh /data/c2c/common/pullTCUfiles_tuvt.sh
adb -s %4 pull /etc/c2c/dm.conf %folder_path%\vtconfNew\c2c\
adb -s %4 pull /etc/c2c/car2cloud.conf %folder_path%\vtconfNew\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/c2c_vehicle.json %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/dm.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/side_loaded.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/car2cloud.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/c2c_default.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/cmd_svc.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/tele_service.conf %folder_path%\c2c\
adb -s %4 pull /data/c2c/common/tcuFiles/ipAddressTCU.txt %folder_path%\C2Cbat\
copy %folder_path%\defaultConfNew\c2c_vehicle.json %folder_path%\c2c\ 
adb -s %4 shell rm /persist/data/pfm/licenses/[0-9]*

goto Exit

:ComboTCUIVIVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT IVI devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

DEL %folder_path%\c2c\*.*?
DEL %folder_path%\vtconfNew\c2c\*.*?
DEL %folder_path%\iviconfNew\*.*?
adb -s %2 pull /etc/c2c/dm.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/car2cloud.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/side_loaded.conf %folder_path%\c2c\
adb -s %2 pull /etc/c2c/c2c_default.conf %folder_path%\c2c\
adb -s %3 pull /vendor/etc/car2cloud.conf %folder_path%\iviconfNew\
adb -s %3 pull /vendor/etc/dm.conf %folder_path%\iviconfNew\
adb -s %4 pull /etc/c2c/dm.conf %folder_path%\vtconfNew\c2c\
adb -s %4 pull /etc/c2c/car2cloud.conf %folder_path%\vtconfNew\c2c\
adb -s %2 shell ifconfig eth0 > %folder_path%\C2Cbat\ipAddressTCU.txt
copy %folder_path%\defaultConfNew\comboDevice\c2c_vehicle.json %folder_path%\c2c\ 
adb -s %2 shell rm /persist/data/pfm/licenses/[0-9]*
adb -s %4 shell rm /persist/data/pfm/licenses/[0-9]*

:Exit
