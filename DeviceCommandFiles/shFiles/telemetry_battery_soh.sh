#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish battery soc value 
# --------------------Battery SOC----------------------------
#Battery-SOC
#LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559943684,\"area\": 0,\"value\": 25}]"
#sleep 1

#publish battery soh value 
# --------------------Battery SOH----------------------------
#Battery-SOC
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559943685,\"area\": 0,\"value\": 15}]"
sleep 1