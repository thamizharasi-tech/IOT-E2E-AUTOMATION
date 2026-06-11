@echo off

REM: print new line

IF "%2%"=="TCU" goto TCUServices
IF "%2%"=="IVI" goto IVIServices
IF "%2%"=="VT" goto VTServices
IF "%2%"=="PRIMARY_IVI" goto IVIServices_PRIMARY
IF "%2%"=="OTA" goto OTAServices

:TCUServices
echo Stopping  all the c2c services on tcu device with adb serial no - %1
adb -s %1 shell systemctl stop softsku 
adb -s %1 shell systemctl stop c2c_dm 
adb -s %1 shell systemctl stop c2c_softsku_manager 
adb -s %1 shell systemctl stop c2c_sota_manager 
adb -s %1 shell systemctl stop c2c_ota_manager 
adb -s %1 shell systemctl stop c2c_hub
adb -s %1 shell logcat -c c2clogger

goto Exit

:IVIServices
echo Stopping all the c2c services on ivi device with adb serial no - %1
cmd /c "adb -s %1 shell killall dm & adb -s %1 shell killall softsku & adb -s %1 push ..\..\..\PycharmProjects\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\clearLogsivi.sh /data/local/tmp/ & adb -s %1 shell chmod +x /data/local/tmp/clearLogsivi.sh & adb -s %1 shell sh /data/local/tmp/clearLogsivi.sh"

goto Exit

:IVIServices_PRIMARY
echo Stopping  all the c2c services on ivi device with adb serial no - %1
cmd /c "adb -s %1 shell killall dm & adb -s %1 shell killall c2c_hub"

goto Exit

:VTServices
echo Stopping  all the c2c services on vt device with adb serial no - %1
cmd /k "adb -s %1 shell systemctl stop softsku & adb -s %1 shell systemctl stop c2c_dm"

goto Exit

:OTAServices
echo Stopping  all the c2c services on nad device with adb serial no - %1
cmd /k "adb -s %1 shell systemctl stop c2c_ota_manager  & adb -s %1 shell systemctl stop c2c_sota_manager"

:Exit
