#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#publish   MCU Communication Fail Alert value
# -------------------- MCU Communication Fail Alert  ----------------------------
# MCU Communication Fail Alert
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875738,\"area\": 0,\"value\": 1}]"
sleep 1
 