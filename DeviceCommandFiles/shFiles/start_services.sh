#!/bin/sh
systemctl stop c2c_dm
systemctl disable c2c_dm
systemctl stop c2c_softsku_managere
systemctl disable c2c_softsku_manager
systemctl stop c2c_hub
systemctl disable c2c_hub
systemctl stop softsku
cd /data/usr/local/bin
systemctl start softsku
/data/usr/local/bin/softsku_manager &
/data/usr/local/bin/dm &
/data/usr/local/bin/c2c_hub &




