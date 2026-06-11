@echo off

REM: print new line

IF "%2%"=="C2CServices" goto C2CServices
IF "%2%"=="OTAServices" goto OTAServices
IF "%2%"=="allServices" goto allServices
IF "%2%"=="c2cService" goto c2cService
IF "%2%"=="otaService" goto otaService
IF "%2%"=="sotaService" goto sotaService
IF "%2%"=="mosquitto" goto mosquitto
IF "%2%"=="su" goto su
IF "%2%"=="dmService" goto dmService

:C2CServices
echo Running all the c2c services on ivi device with adb serial no - %1
adb -s %1 shell logcat -c c2clogger
adb -s %1 shell logcat -b all -c
::adb -s %1 shell sh /data/start_IVI_services.sh
::adb -s %1 shell stop dm_service
::adb -s %1 shell stop c2c_hub_service
::adb -s %1 shell stop ota_manager_service
::adb -s %1 shell stop sota_manager_service
adb -s %1 shell start dm_service
adb -s %1 shell start c2c_hub_service
adb -s %1 shell start ota_manager_service
adb -s %1 shell start sota_manager_service

goto Exit

:OTAServices
echo Running all the ota services on ivi device with adb serial no - %1
adb -s %1 root
::adb -s %1 shell killall dm
::adb -s %1 shell export LD_LIBRARY_PATH=./:/vendor/lib64/
::adb -s %1 shell am start -n com.qualcomm.androidotaagent/.ui.MainActivity
::adb -s %1 shell sh /data/start_IVI_OTAservices.sh
adb -s %1 shell stop ota_manager_service
adb -s %1 shell stop sota_manager_service
adb -s %1 shell start ota_manager_service
adb -s %1 shell start sota_manager_service

goto Exit

:allServices
adb -s %1 shell sh /data/start_IVI_services.sh
adb -s %1 shell sh /data/start_IVI_OTAservices.sh

goto Exit

:c2cService
adb -s %1 shell killall c2c_hub
adb -s %1 shell start c2c_hub_service

goto Exit

:su
adb -s %1 shell su

goto Exit

:mosquitto
adb -s %1 shell killall mosquitto
adb -s %1 shell mosquitto &

goto Exit

:sotaService
adb -s %1 shell killall sota_manager
adb -s %1 shell start sota_manager_service

goto Exit

:otaService
adb -s %1 shell killall ota_manager
adb -s %1 shell start ota_manager_service

goto Exit

:dmService
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service

:Exit
