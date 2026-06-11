#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish paho command for Battery Heat Cold alert
# --------------------Battery Heat Cold ALERT----------------------------

paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891601,\"area\": 0,\"value\": 36}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891601,\"area\": 0,\"value\": 76}]"

#publish paho command for the Battery Heat Cold ALERT change using PAHO command
# --------------------Battery Heat Cold ALERT----------------------------
# ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891601,\"area\": 0,\"value\": 76}]"