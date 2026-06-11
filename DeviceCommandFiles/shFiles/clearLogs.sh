#!/bin/sh
cd /data/local/tmp/
systemctl stop softsku
systemctl stop c2c_hub
systemctl stop c2c_dm
systemctl stop c2c_softsku_manager
killall dm
killall c2c_hub
killall softsku_manager





