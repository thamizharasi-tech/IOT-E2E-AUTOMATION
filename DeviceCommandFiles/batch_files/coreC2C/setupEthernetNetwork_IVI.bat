@echo off
CLS
SETLOCAL enabledelayedexpansion

echo adbSerialNo is %1

IF "%2%"=="Ethernet" goto EthernetNetworkSetup
IF "%2%"=="CubicSIM" goto CubicSIMnetwork

echo invalid argument.
goto Exit


:EthernetNetworkSetup

REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE ETHERNET NETWORK ON TELEMATICS DEVICE ***
echo --------------------------------------------------------------
REM: print new line
cmd /k "adb -s %1 shell QCMAP_CLI set /p input1=1 %input1% sleep 60 set /p input2=2 %input2% sleep 60 set /p input3=1 %input3% set /p input7=7 %input7% set /p input8=3 %input8% set /p input9=1 %input9% timeout /t 5"

pause 5


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


