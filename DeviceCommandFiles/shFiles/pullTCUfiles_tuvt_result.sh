#!/bin/sh
cd /data
adb pull /etc/c2c/ /data/c2c/common/c2c/
adb pull /persist/data/pfm/licenses/ /data/c2c/common/licenses/
#adb shell logcat -d > /data/c2c/common/tcu_c2clogs.txt
