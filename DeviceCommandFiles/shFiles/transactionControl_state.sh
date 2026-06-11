#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish TRACTION_CONTROL_INDICATOR_ALERT value 
# --------------------TRACTION_CONTROL_INDICATOR_ALERT ----------------------------
#TRACTION_CONTROL_INDICATOR_ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876104,\"area\": 0,\"value\": 1}]"
sleep 1
