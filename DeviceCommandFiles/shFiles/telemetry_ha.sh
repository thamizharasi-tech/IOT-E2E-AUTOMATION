#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish HA 
# --------------------HA----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883414,\"area\": 0,\"value\": 1}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883414,\"area\": 0,\"value\": 1}]"


./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876191,\"area\": 0,\"value\": 1}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876191,\"area\": 0,\"value\": 1}]"
sleep 1