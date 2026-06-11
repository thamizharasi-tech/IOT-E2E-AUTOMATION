#!/bin/sh
cd /data
killall dm
killall softsku
systemctl stop softsku
systemctl stop c2c_dm
mount -o remount, rw /
rm -rf /c2c_deployment_vt
rm -rf /data/c2c_deployment_vt
unzip /data/c2c_deployment_vt.zip
cd c2c_deployment_vt/
mount -o remount, rw /
chmod +x /c2c_deployment_vt/*
chmod +x /data/c2c_deployment_vt/*
mount -o remount, rw /
/c2c_deployment_vt/c2c_vt_install.sh
cd /data/c2c_deployment_vt
/bin/sh /data/c2c_deployment_vt/c2c_vt_install.sh
adb shell rm -rf /data/c2c_deployment_tcu
adb shell rm -rf /c2c_deployment_tcu
adb shell rm /data/c2c_deployment_tcu.zip
adb shell rm /c2c_deployment_tcu.zip
adb push /data/c2c_deployment_tcu.zip /data/
adb shell chmod +x /data/c2c_deployment_tcu.zip 
adb push /data/deviceOnboarding_tcu.sh /data/ 
adb push /deviceOnboarding_tcu.sh /data/ 
adb shell chmod +x /data/c2c_deployment_tcu.zip
adb shell chmod +x /data/deviceOnboarding_tcu.sh
adb shell rm /persist/data/pfm/licenses/*
adb shell rm /persist/data/pfm/licenses/[0-9]*  
adb shell sh /data/deviceOnboarding_tcu.sh
