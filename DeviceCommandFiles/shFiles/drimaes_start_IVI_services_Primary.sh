#!/bin/sh
# kill running services
su
#killall dm
#killall c2c_hub
#killall ota_manager
#killall sota_manager
cd /vendor/bin/
stop c2c_hub_service
stop dm_service
start c2c_hub_service
start dm_service
start c2c_hub_service
#Run services
#cd /data
#export LD_LIBRARY_PATH=./:/vendor/lib64/
#cd /vendor/bin
#mosquitto &
#dm &
#c2c_hub &
#sota_manager &
#ota_manager &
#setenforce 0
