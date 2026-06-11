#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish speed value 
# --------------------Battery SOH----------------------------
#Speed
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 10}]"
sleep 1