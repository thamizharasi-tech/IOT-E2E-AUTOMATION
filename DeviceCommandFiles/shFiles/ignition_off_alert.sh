#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish IGNITION OFF request
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"