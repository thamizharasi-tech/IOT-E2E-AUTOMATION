@echo off

IF "%2%"=="TCU" goto SingleTCUdevice
IF "%2%"=="IVI" goto SingleIVIdevice
IF "%2%"=="TCUIVI" goto ComboTCUIVIdevice
IF "%2%"=="TCUVT" goto ComboTCUIVIdevice
IF "%2%"=="TCUVTIVI" goto ComboTCUIVIVTdevice
echo invalid argument.
goto Exit

:: Set the source folder path for conf files
set conf_source_path_tcu= /etc/c2c/

:: Set the destination folder
set conf_dest_path_tcu= C:\Users\suttarak\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\

:: Set the source folder path for conf files
set conf_source_path_ivi= /vendor/etc/

:: Set the destination folder
set conf_dest_path_ivi= ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\iviconfNew\

:: Set the source folder path for conf files
set conf_source_path_vt= /etc/c2c/

:: Set the destination folder
set conf_dest_path_vt= ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\

:SingleTCUdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU device***
echo -----------------------------------------
REM: print new line
REM: print new line

adb -s %1 pull %conf_source_path_tcu% %conf_dest_path_tcu% 
copy ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\c2c_vehicle.json ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 

goto Exit

:SingleIVIdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for IVi device***
echo -----------------------------------------
REM: print new line
REM: print new line

adb -s %1 pull %conf_source_path_ivi% %conf_dest_path_ivi% 
copy ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\c2c_vehicle.json ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 


goto Exit

:ComboTCUIVIdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU IVI devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

adb -s %1 pull %conf_source_path_tcu% %conf_dest_path_tcu% 
copy ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\comboDevice\c2c_vehicle.json ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 
adb -s %1 pull %conf_source_path_ivi%/dm.conf %conf_dest_path_ivi% 
adb -s %1 pull %conf_source_path_ivi%/car2cloud.conf %conf_dest_path_ivi% 

goto Exit

:ComboTCUIVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

adb -s %1 pull %conf_source_path_tcu% %conf_dest_path_tcu% 
copy ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\c2c_vehicle.json ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 
adb -s %1 pull %conf_source_path_vt% %conf_dest_path_vt% 

goto Exit

:ComboTCUIVIVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT IVI devices ***
echo -----------------------------------------
REM: print new line
REM: print new line

adb -s %1 pull %conf_source_path_tcu% %conf_dest_path_tcu% 
copy ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\comboDevice\c2c_vehicle.json ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 
adb -s %1 pull %conf_source_path_ivi%/dm.conf %conf_dest_path_ivi% 
adb -s %1 pull %conf_source_path_ivi%/car2cloud.conf %conf_dest_path_ivi% 
adb -s %1 pull %conf_source_path_vt% %conf_dest_path_vt% 

:Exit
