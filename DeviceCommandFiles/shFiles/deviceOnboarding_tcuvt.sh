#!/bin/sh
cd /data
adb shell mkdir /data/c2c/common/files
adb shell systemctl stop c2c_hub
adb shell systemctl stop c2c_dm
adb shell systemctl stop c2c_softsku_manager
adb shell systemctl stop softsku
adb push /data/c2c/common/files/certs/ /data/usr/local/
adb push /data/c2c/common/files/c2c/c2c_vehicle.json /etc/c2c/
adb push /data/c2c/common/files/c2c/dm.conf /etc/c2c/
adb push /data/c2c/common/files/c2c/side_loaded.conf /etc/c2c/
adb push /data/c2c/common/files/c2c/car2cloud.conf /etc/c2c/
adb push /data/c2c/common/files/c2c/c2c_default.conf /etc/c2c/
adb push /data/c2c/common/files/c2c/cmd_svc.conf /etc/c2c/
adb push /data/c2c/common/files/c2c/tele_service.conf.conf /etc/c2c/
adb push /data/c2c/common/files/certs/ /data/usr/local/certs/
adb shell dos2unix /etc/c2c/**
adb shell dos2unix /data/usr/local/certs/**
adb shell cp /data/usr/local/certs/token_cert /data/qwes/
adb shell rm /persist/data/pfm/licenses/* 
adb shell systemctl start c2c_dm
adb shell systemctl start c2c_softsku_manager
adb shell systemctl start softsku