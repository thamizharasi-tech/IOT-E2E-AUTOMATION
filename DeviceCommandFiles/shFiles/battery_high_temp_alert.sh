#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish BATTERY HIGH TEMP ALERT value
# -------------------- BATTERY HIGH TEMP ALERT ----------------------------
# BATTERY HIGH TEMP ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875615,\"area\": 0,\"value\": 1}]"
sleep 1
