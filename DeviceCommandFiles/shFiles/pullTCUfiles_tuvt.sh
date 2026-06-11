#!/bin/sh
cd /data
adb shell systemctl stop c2c_hub
adb shell systemctl stop c2c_dm
adb shell systemctl stop c2c_softsku_manager
adb shell systemctl stop softsku
adb pull /etc/c2c/c2c_vehicle.json /data/c2c/common/tcuFiles/
adb pull /etc/c2c/dm.conf /data/c2c/common/tcuFiles/
adb pull /etc/c2c/side_loaded.conf /data/c2c/common/tcuFiles/
adb pull /etc/c2c/car2cloud.conf /data/c2c/common/tcuFiles/
adb pull /etc/c2c/c2c_default.conf /data/c2c/common/tcuFiles/
adb pull /etc/c2c/cmd_svc.conf /data/c2c/common/tcuFiles/
adb pull /etc/c2c/tele_service.conf /data/c2c/common/tcuFiles/
adb shell ifconfig eth0 > /data/c2c/common/tcuFiles/ipAddressTCU.txt
adb shell ifconfig eth0 > /data/c2c/common/ipAddressTCU.txt

