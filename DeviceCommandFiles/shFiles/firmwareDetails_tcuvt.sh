#!/bin/sh
adb shell date --s $1
adb pull /firmware/image/Ver_Info.txt /data/c2c/common