@echo off

REM: print new line
echo.
echo ---------------------------------------------------------------------------------
echo *** DEPLOYMENT PACKAGE AND REQUIRED FILES PASSED FOR DEVICE ONBOARDING ***
echo ---------------------------------------------------------------------------------
REM: print new line
echo.

IF "%2" == "IVI" goto IVI
echo invalid argument.
goto Exit


:IVI

REM: print new line
echo.
echo -------------------------------------------------
echo *** IVI DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

adb -s %1 root 
adb -s %1 remount 
adb -s %1 shell rm -rf /data/c2c_deployment_ivi_only
adb -s %1 shell rm /data/c2c_deployment_ivi_only.zip
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_ivi_only.zip /data/
adb -s %1 shell chmod +x /data/c2c_deployment_ivi_only.zip
adb -s %1 push %3\shFiles\device_onboarding_ivi_primary.sh /data/
adb -s %1 shell chmod +x /data/c2c_deployment_ivi_only.zip
adb -s %1 shell chmod +x /data/c2c_deployment_ivi_only.sh
adb -s %1 shell sh /data/device_onboarding_ivi_primary.sh

:Exit
