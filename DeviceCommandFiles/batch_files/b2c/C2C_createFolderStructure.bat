@echo off

:createFolder
adb -s %1 root
adb -s %1 shell mkdir -p /mnt/vendor/persist/data/c2c


