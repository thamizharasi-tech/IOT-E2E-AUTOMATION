#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish MCU HIGH TEMP ALERT value
# -------------------- MCU HIGH TEMP ALERT  ----------------------------
# MCU HIGH TEMP ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875356,\"area\": 0,\"value\": 1}]"
sleep 1
 