#!/bin/sh
cd /data
adb shell QCMAP_CLI set /p name=< /data/c2c/common/input.txt
adb shell ifconfig eth0 > /data/c2c/common/ipConfigTCU.txt