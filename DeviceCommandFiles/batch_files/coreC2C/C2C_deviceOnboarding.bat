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
adb -s %1 shell rm -rf /data/c2c_deployment_tcu 
adb -s %1 shell rm /data/c2c_deployment_tcu.zip 
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_tcu.zip /data/ 
adb -s %1 shell chmod +x /data/c2c_deployment_tcu.zip 
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_tcu.sh /data/ 
adb -s %1 shell chmod +x /data/c2c_deployment_tcu.zip 
adb -s %1 shell chmod +x /data/deviceOnboarding_tcu.sh 
adb -s %1 shell sh /data/deviceOnboarding_tcu.sh"

:Exit
