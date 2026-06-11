#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./


#//EV: Ignition ON and Drive Mode and speed is greater than or equal to 3 km/hr (speed ≥ 3 km/hr).

#publish speed value 

#Ignition
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875730,\"area\": 0,\"value\": 1}]"
sleep 1

#Speed
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875288,\"area\": 0,\"value\": 4}]"
sleep 1

#rideMode-0
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875296,\"area\": 0,\"value\": 0}]"
sleep 1
