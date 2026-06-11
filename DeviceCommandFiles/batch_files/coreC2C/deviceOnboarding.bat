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
IF "%2" == "TCUVT_fusion" goto TCUVT_fusion

echo invalid argument.
goto Exit


:TCU

REM: print new line
echo.
echo -------------------------------------------------
echo *** TCU DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 root & adb -s %1 remount & adb -s %1 shell rm -rf /data/c2c_deployment_tcu & adb -s %1 shell rm /data/c2c_deployment_tcu.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_tcu.zip /data/ & adb -s %1 shell chmod 777 /data/c2c_deployment_tcu.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_tcu.sh /data/ & adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* & adb -s %1 shell chmod +x /data/c2c_deployment_tcu.zip & adb -s %1 shell chmod +x /data/deviceOnboarding_tcu.sh & adb -s %1 shell sh /data/deviceOnboarding_tcu.sh"

goto Exit

:NAD

REM: print new line
echo.
echo -------------------------------------------------
echo *** TCU- NAD DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 root & adb -s %1 remount & adb -s %1 shell rm -rf /data/c2c_deployment_tcu_nad & adb -s %1 shell rm /data/c2c_deployment_tcu_nad.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_tcu_nad.zip /data/ & adb -s %1 shell chmod +x /data/c2c_deployment_tcu_nad.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_nad.sh /data/ & adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* & adb -s %1 shell chmod +x /data/deviceOnboarding_nad.sh & adb -s %1 shell dos2unix /data/deviceOnboarding_nad.sh & adb -s %1 shell sh /data/deviceOnboarding_nad.sh"

goto Exit

:IVI

REM: print new line
echo.
echo -------------------------------------------------
echo *** IVI DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 root & adb -s %1 shell rm /data/c2c_deployment_ivi.zip & adb -s %1 shell rm -rf /data/c2c_deployment_ivi & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_ivi.zip /data/ & adb -s %1 shell chmod +x /data/c2c_deployment_ivi.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_ivi.sh /data/ & adb -s %1 shell chmod +x /data/c2c_deployment_ivi.zip & adb -s %1 shell chmod +x /data/deviceOnboarding_ivi.sh & adb -s %1 shell sh /data/deviceOnboarding_ivi.sh set /p name=< C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\C2Cbat\iviInput.txt"

goto Exit

:VT

REM: print new line
echo.
echo -------------------------------------------------
echo *** VT DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 root & adb -s %1 remount & adb -s %1 shell mount -o remount, rw / & adb -s %1 shell rm -rf /c2c_deployment_vt & adb -s %1 shell rm /data/c2c_deployment_vt.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_vt.zip /data/ & adb -s %1 shell chmod 777 /data/c2c_deployment_vt.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_vt.sh /data/ & adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* & adb -s %1 shell chmod +x /data/c2c_deployment_vt.zip & adb -s %1 shell chmod +x /data/deviceOnboarding_vt.sh & adb -s %1 shell sh /data/deviceOnboarding_vt.sh"

goto Exit

:TCUVT_fusion

REM: print new line
echo.
echo -------------------------------------------------
echo *** VT DEVICE SETUP ***
echo -------------------------------------------------
REM: print new line

cmd /k "adb -s %1 shell rm /c2c_deployment_vt.zip & adb -s %1 shell rm /data/c2c/common/files/certs/c2c_deployment_tcu.zip & adb -s %1 shell rm -rf /c2c_deployment_vt & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_vt.zip / & adb -s %1 shell chmod +x /c2c_deployment_vt.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_vt.sh / & adb -s %1 shell chmod +x /c2c_deployment_vt.zip & adb -s %1 shell dos2unix /deviceOnboarding_vt.sh & adb -s %1 shell sh /deviceOnboarding_vt.sh & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\deploymentPackages\c2c_deployment_tcu.zip /data/c2c/common/files/certs/ & adb -s %1 shell chmod +x /data/c2c/common/files/certs/c2c_deployment_tcu.zip & adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\deviceOnboarding_tcuvt_depPack.sh /data/c2c/common/files/certs/ & adb -s %1 shell chmod +x /data/c2c/common/files/certs/deviceOnboarding_tcuvt_depPack.sh & adb -s %1 shell dos2unix /data/c2c/common/files/certs/deviceOnboarding_tcuvt_depPack.sh & adb -s %1 shell rm /persist/data/pfm/licenses/[0-9]* & adb -s %1 shell sh /data/c2c/common/files/certs/deviceOnboarding_tcuvt_depPack.sh"

:Exit
