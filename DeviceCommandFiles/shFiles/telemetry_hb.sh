#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish HB 
# --------------------HB----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883415,\"area\": 0,\"value\": 1}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883415,\"area\": 0,\"value\": 1}]"

./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876189,\"area\": 0,\"value\": 1}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557876189,\"area\": 0,\"value\": 1}]"