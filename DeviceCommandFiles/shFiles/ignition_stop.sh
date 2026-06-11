#!/bin/sh


cd /data/
export LD_LIBRARY_PATH=./


#ignition_off
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875328,\"area\": 0,\"value\": 3}]"

sleep 1
