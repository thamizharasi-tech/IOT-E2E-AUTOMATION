#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish BIKE CHARGE STATE ALERT ALERT
# -------------------- BIKE CHARGE STATE ALERT----------------------------
# BIKE CHARGE STATE ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875425,\"area\": 0,\"value\": 1}]"
sleep 1
