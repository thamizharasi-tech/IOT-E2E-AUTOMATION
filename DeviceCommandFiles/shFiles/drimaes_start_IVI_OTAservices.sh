#!/bin/sh
# run OTA services
adb root
cd /vendor/bin/
killall ota_manager
killall sota_manager
stop ota_manager_service
stop sota_manager_service
start ota_manager_service
start sota_manager_service
#export LD_LIBRARY_PATH=./:/vendor/lib64/
#chmod 777 /vendor/bin/ota_manager
#chmod 777 /vendor/bin/sota_manager
#ota_manager &
#sota_manager &
