#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish paho command for Tampering alert
# --------------------TAMPERING ALERT----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557895681,\"area\": 0,\"value\": 9}]"