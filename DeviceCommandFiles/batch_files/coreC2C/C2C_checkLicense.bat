@echo off
::echo adbSerialNo is %1
adb -s %1 shell ls -lart /persist/data/pfm/licenses/ 
::adb -s %1 shell cat /persist/data/pfm/licenses/*
