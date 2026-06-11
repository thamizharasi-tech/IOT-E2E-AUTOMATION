@echo off
CLS
SETLOCAL enabledelayedexpansion

IF "%2%"=="Ethernet" goto EthernetNetworkSetup
IF "%2%"=="CubicSIM" goto CubicSIMnetwork

echo invalid argument.
goto Exit


:EthernetNetworkSetup

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE NETWORK ON TELEMATICS DEVICE ***
echo --------------------------------------------------------------
REM: print new line
cmd /k "adb -s %1 shell QCMAP_CLI set /p name=< C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\C2Cbat\input.txt"
pause 2


goto Exit

:CubicSIMnetwork

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE CUBIC SIM NETWORK ON TELEMATICS DEVICE ***
echo --------------------------------------------------------------
REM: print new line

goto Exit

:Exit


