@echo off
CLS
SETLOCAL enabledelayedexpansion

IF "%2%"=="Ethernet" goto EthernetNetworkSetup
IF "%2%"=="CubicSIM" goto CubicSIMnetwork
IF "%2%"=="WiFi" goto WiFinetwork

echo invalid argument.
goto Exit


:EthernetNetworkSetup

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE NETWORK ON DEVICE ***
echo --------------------------------------------------------------
REM: print new line
cmd /k "adb -s %1 shell QCMAP_CLI set /p name=< C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\C2Cbat\input.txt"
pause 2


goto Exit

:CubicSIMnetwork

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE CUBIC SIM NETWORK ON DEVICE ***
echo --------------------------------------------------------------
REM: print new line

goto Exit

:WiFinetwork

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE Wi-Fi NETWORK ON DEVICE ***
echo --------------------------------------------------------------
REM: print new line
adb -s %1 shell cmd wifi set-wifi-enabled enabled
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3
adb -s %1 shell cmd wifi connect-network Hydra wpa2 K5x48Vz3 > C:\Car2Cloud_E2ETesting_Drimaes\C2CtestReport\e2eExecution_Backup\NetworkStatus\networkStatus.txt

goto Exit


:Exit


