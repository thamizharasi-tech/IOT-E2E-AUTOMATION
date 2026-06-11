@echo off

REM: print new line
echo.
echo ---------------------------------------------------------------------------------
echo *** DEPLOYMENT PACKAGE AND REQUIRED FILES PASSED FOR DEVICE ONBOARDING ***
echo ---------------------------------------------------------------------------------
REM: print new line
echo.

IF "%2" == "TCU" goto TCU
IF "%2" == "NAD" goto NAD
IF "%2" == "IVI" goto IVI
IF "%2" == "VT" goto VT


echo invalid argument.
goto Exit


:TCU

REM: print new line
echo.
echo -------------------------------------------------
echo *** TCU DEVICE ***
echo -------------------------------------------------
REM: print new line

adb -s %1 shell rm c2c_deployment_tcu/c2c_device_tcu.zip 
adb -s %1 shell sh /data/c2c_deployment_tcu/c2c_tcu_install.sh

goto Exit

:NAD

REM: print new line
echo.
echo -------------------------------------------------
echo *** NAD DEVICE ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 shell sh /data/deviceOnboarding_tcu_nad.sh"

goto Exit

:IVI

REM: print new line
echo.
echo -------------------------------------------------
echo *** IVI DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

adb -s %1 shell sh /data/deviceOnboarding_ivi.sh

goto Exit

:VT

REM: print new line
echo.
echo -------------------------------------------------
echo *** VT DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

adb -s %1 shell sh /data/deviceOnboarding_vt.sh

:Exit
