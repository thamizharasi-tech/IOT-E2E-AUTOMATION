@echo off

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

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\


goto Exit

:SingleIVIdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for IVI device***
echo -----------------------------------------
REM: print new line

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\


goto Exit

:ComboTCUIVIdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU IVI devices ***
echo -----------------------------------------
REM: print new line

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\comboDevice\c2c_vehicle.json C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\iviconfNew\iviDeafultConfs\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\iviconfNew\

goto Exit

:ComboTCUVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT devices ***
echo -----------------------------------------
REM: print new line

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\vtDeafultConfs\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\c2c\

goto Exit

:ComboTCUVTdevice_fusion
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT fusion devices ***
echo -----------------------------------------
REM: print new line

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\vtDeafultConfs\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\c2c\

goto Exit

:ComboTCUIVIVTdevice
REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for TCU VT IVI devices ***
echo -----------------------------------------
REM: print new line

copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\iviconfNew\iviDeafultConfs\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\iviconfNew\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\vtDeafultConfs\** C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vtconfNew\c2c\
copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\defaultConfNew\comboDevice\c2c_vehicle.json C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\ 

:Exit
