#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish BATTERY HEALTH ALERT value
# -------------------- BATTERY HEALTH ALERT ----------------------------
# BATTERY HEALTH ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559972670,\"area\": 0,\"value\": 73}]"
sleep 1
