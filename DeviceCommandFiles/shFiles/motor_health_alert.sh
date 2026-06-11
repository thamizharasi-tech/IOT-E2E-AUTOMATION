#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish MOTOR HEALTH ALERT value
# -------------------- MOTOR HEALTH ALERT  ----------------------------
# MOTOR HEALTH ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876073,\"area\": 0,\"value\": 11}]"
sleep 1
