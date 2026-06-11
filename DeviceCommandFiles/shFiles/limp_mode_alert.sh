#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish  LIMP MODE NOTIFICATIONT value 
# -------------------- LIMP MODE NOTIFICATION----------------------------
# LIMP MODE NOTIFICATION
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876073,\"area\": 0,\"value\": 10}]"
sleep 1
