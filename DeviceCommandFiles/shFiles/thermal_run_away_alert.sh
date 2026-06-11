#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish THERMAL RUN AWAY ALERT value
# -------------------- THERMAL RUN AWAY ALERT  ----------------------------
# THERMAL RUN AWAY ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875624,\"area\": 0,\"value\": 1}]"
sleep 1
 