#!/bin/sh


cd /data/
export LD_LIBRARY_PATH=./
su

#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"

cansend can0 7F2#2E00  # RPM
sleep 1
cansend can0 7FC#20   # Speed
sleep 1
cansend can0 7EE#20    # Fuel level
sleep 1
cansend can0 7FB#80 # Battery level
sleep 1
cansend can0 7EC#0000FFFF  # Odo meter
sleep 1

cansend can0 7F2#2E10  # RPM
sleep 1
cansend can0 7FC#50   # Speed
sleep 1
cansend can0 7EE#10    # Fuel level
sleep 1
cansend can0 7FB#50 # Battery level
sleep 1
cansend can0 7EC#0000FFEE  # Odo meter
sleep 1

sleep 15
	


