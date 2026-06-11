#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish MOTOR TEMP WARN ALERT 
# -------------------- MOTOR TEMP WARN ALERT----------------------------
# MOTOR TEMP WARN ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876073,\"area\": 0,\"value\": 1}]"
sleep 1
