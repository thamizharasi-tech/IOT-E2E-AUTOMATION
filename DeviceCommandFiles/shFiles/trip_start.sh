#!/bin/sh


cd /data/
export LD_LIBRARY_PATH=./
su

#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"
sleep 15
	


