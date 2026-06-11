#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./
su

while true
do		
	#odo meter value
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 600000}]"
    sleep 1
	
	#fuel level
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 30}]"
    sleep 1
    
	#latitiude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 17.628162822}]"
    sleep 1
    
	#longitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 72.816781922}]"
    sleep 1
	
    #battery levle
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 400}]"
    sleep 1
	
    #alltitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 72.22}]"
    sleep 1
	
    #bearing
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
    sleep 1
	
	#velocity
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
    sleep 1
	
	#hvac temp current
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
    sleep 10
	
	#hvac temp current
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
    sleep 10
	
done

