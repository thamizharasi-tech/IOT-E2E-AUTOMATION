@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

REM: print new line

IF "%2%"=="TCU" goto TCUServices
IF "%2%"=="TCUrestart" goto TCUServicesRestart
IF "%2%"=="IVI" goto IVIServices
IF "%2%"=="IVIrestart" goto IVIServicesRestart
IF "%2%"=="VT" goto VTServices
IF "%2%"=="VTrestart" goto VTServicesRestart
IF "%2%"=="PRIMARY_IVI" goto IVIServices_PRIMARY
IF "%2%"=="OTA" goto OTAServices
IF "%2%"=="startC2CServices_bin" goto startC2CServices_bin
IF "%2%"=="TCUVT_fusion" goto TCUVT_fusion

echo Running all the c2c services on tcu device with adb serial no - %1

:TCUServices
::adb -s %1 shell logcat -c c2clogger
::adb -s %1 shell systemctl restart mosquitto
adb -s %1 shell systemctl restart softsku
adb -s %1 shell systemctl restart c2c_dm
adb -s %1 shell systemctl restart c2c_softsku_manager
adb -s %1 shell systemctl restart c2c_hub

goto Exit

:TCUServicesRestart
adb -s %1 shell systemctl restart softsku 
adb -s %1 shell systemctl restart c2c_dm 
adb -s %1 shell systemctl restart c2c_softsku_manager 


goto Exit

:IVIServices
adb -s %1 shell logcat -c c2clogger
echo Running all the c2c services on ivi device with adb serial no - %1
cmd /c "adb -s %1 shell sh /vendor/bin/start_IVI_services.sh"

goto Exit

:IVIServices_PRIMARY
echo Running all the c2c services on ivi device with adb serial no - %1
cmd /c "adb -s %1 shell sh /vendor/bin/start_IVI_services_primary.sh"

goto Exit

:IVIServicesRestart
echo Running all the c2c services on ivi device with adb serial no - %1
cmd /c "adb -s %1 root & adb -s %1 shell killall dm & adb -s %1 shell killall softsku & adb -s %1 shell sh /vendor/bin/start_IVI_services.sh"

goto Exit

:VTServices
adb -s %1 shell logcat -c c2clogger
echo Running all the c2c services on vt device with adb serial no - %1
cmd /k "adb -s %1 shell systemctl restart softsku & adb -s %1 shell systemctl restart c2c_dm"

goto Exit

:VTServicesRestart
adb -s %1 shell logcat -c c2clogger
cmd /k "adb -s %1 shell systemctl restart softsku & adb -s %1 shell systemctl restart c2c_dm"

goto Exit

:OTAServices
echo Running all the c2c services on nad device with adb serial no - %1
cmd /k "adb -s %1 shell systemctl stop c2c_dm & adb -s %1 shell systemctl restart c2c_ota_manager  & adb -s %1 shell systemctl restart c2c_sota_manager"

goto Exit

:TCUVT_fusion
echo Running all the c2c services on nad device with adb serial no - %1
cmd /k "adb -s %1 push %folder_path%\shFiles\start_TCUVT_services.sh /data/c2c/common/ & adb -s %1 shell chmod +x /data/c2c/common/start_TCUVT_services.sh & adb -s %1 shell sh /data/c2c/common/start_TCUVT_services.sh"

goto Exit

:startC2CServices_bin
echo Running all the c2c services on nad device with adb serial no - %1
cmd /k "adb -s %1 push %folder_path%\binLibFiles\bin /data/usr/local/ & adb -s %1 push %folder_path%\shFiles\start_services.sh /data/usr/bin & adb -s %1 shell dos2unix /data/usr/bin/start_services.sh & adb -s %1 shell chmod +x /data/usr/bin/start_services.sh & adb -s %1 shell sh /data/usr/bin/start_services.sh"

:Exit
