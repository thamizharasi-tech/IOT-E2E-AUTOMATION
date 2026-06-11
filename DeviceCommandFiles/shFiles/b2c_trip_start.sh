#!/bin/sh


cd /data/
export LD_LIBRARY_PATH=./
su

#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"

cansend can0 7F2#2E00  # RPM [ rpm:11776.000000 ]
sleep 1
cansend can0 7FC#20   # Speed [ speed:32.000000 ]
sleep 1
cansend can0 7EE#20    # Fuel level [fuel_level:8192.000000 ]
sleep 1
cansend can0 7FB#80 # Battery level [ ev_battery_level:128.000000 ]
sleep 1
cansend can0 7EC#0000FEEF  # Odo meter [ odo:65263.000000]
sleep 1

cansend can0 7FF#04  # Ignition Start

cansend can0 7F2#2E10  # RPM  [ rpm:11792.000000 ]
sleep 1
cansend can0 7FC#50   # Speed [ speed:80.000000 ]
sleep 1
cansend can0 7EE#15    # Fuel level [fuel_level:5376.000000 ]
sleep 1
cansend can0 7FB#70 # Battery level [ev_battery_level:112.000000]
sleep 1
cansend can0 7EC#0000FFEE  # Odo meter [ odo:65518.000000]
sleep 1




	


