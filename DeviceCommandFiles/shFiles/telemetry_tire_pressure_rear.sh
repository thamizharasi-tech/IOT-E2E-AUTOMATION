#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish tire pressure value 
# --------------------Tire Pressure----------------------------
#Battery-SOC
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 392168201,\"area\": 4,\"value\": 5.32}]"
sleep 1
