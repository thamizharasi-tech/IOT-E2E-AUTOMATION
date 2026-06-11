#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish BATTERY LOW TEMP ALERT value
# -------------------- BATTERY LOW TEMP ALERT ----------------------------
# BATTERY LOW TEMP ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876173,\"area\": 0,\"value\": 30}]"
sleep 1
