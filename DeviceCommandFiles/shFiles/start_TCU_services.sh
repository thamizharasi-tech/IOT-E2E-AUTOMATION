#!/bin/sh
cd /data/usr/local/bin/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/usr/lib/
cd /data/usr/local/bin/
./mosquitto -c /usr/local/conf/mosquitto.conf &
./softsku_manager &
./softsku &
./dm &
./c2c_hub &





