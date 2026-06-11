#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish Over Speed 
# --------------------Over Speed----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 130}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 130}]"

./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875288,\"area\": 0,\"value\": 130}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875288,\"area\": 0,\"value\": 130}]"