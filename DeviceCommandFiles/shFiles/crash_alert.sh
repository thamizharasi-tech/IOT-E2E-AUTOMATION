#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish paho command for crash alert
# --------------------CRASH ALERT----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891597,\"area\": 0,\"value\": 5}]"