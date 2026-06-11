#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish VEHICLE FULLY CHARGED NOTIFICATION ALERT ALERT
# -------------------- VEHICLE FULLY CHARGED NOTIFICATION----------------------------
# VEHICLE FULLY CHARGED NOTIFICATION
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 559972569,\"area\": 0,\"value\": 100}]"
sleep 1
