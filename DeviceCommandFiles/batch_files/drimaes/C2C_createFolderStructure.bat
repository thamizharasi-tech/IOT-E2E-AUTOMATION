@echo off

:createFolder
adb -s %1 root
adb -s %1 shell mkdir -p /data/vendor/c2c
adb -s %1 shell mkdir -p /data/usr/local/certs

