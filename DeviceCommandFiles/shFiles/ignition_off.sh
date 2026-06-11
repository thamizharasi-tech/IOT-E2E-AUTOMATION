#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

# -------------------IGNITION STATE - OFF---------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557875730,\"area\": 0,\"value\": 0}]"
