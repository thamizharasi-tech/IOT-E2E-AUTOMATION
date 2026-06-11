#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish HILL HOLD STATE ALERT
# -------------------- HILL HOLD STATE ALERT----------------------------
# HILL HOLD STATE ALERT
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876054,\"area\": 0,\"value\": 1}]"
sleep 1
