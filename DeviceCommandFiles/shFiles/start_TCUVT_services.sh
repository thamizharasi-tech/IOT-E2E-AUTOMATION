#!/bin/sh
cd /data/
systemctl restart softsku
systemctl restart c2c_dm
adb shell systemctl restart softsku
adb shell systemctl restart c2c_softsku_manager
adb shell systemctl restart c2c_dm
adb shell systemctl restart c2c_hub






