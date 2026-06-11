#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish ridemode value 
# --------------------Ridemode SNA----------------------------
#ridemode
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875296,\"area\": 0,\"value\": 3}]"
sleep 1
