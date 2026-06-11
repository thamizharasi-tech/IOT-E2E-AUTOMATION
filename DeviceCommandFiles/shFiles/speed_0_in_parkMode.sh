#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish speed value 
# --------------------Battery SOH----------------------------

#Speed
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875288,\"area\": 0,\"value\": 0}]"
sleep 1

#parkMode
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875296,\"area\": 0,\"value\": 12}]"
sleep 1