#!/bin/sh


cd /data/
export LD_LIBRARY_PATH=./
su

while true
do	
	
	#Ignition [trip start]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 5}]"
    sleep 1
	
	#odo meter value
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 400000}]"
    sleep 1
	
	#fuel level
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 10}]"
    sleep 1
    
	#latitiude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 17.628162819}]"
    sleep 1
    
	#longitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 72.816781910}]"
    sleep 1
	
    #battery levle
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 200}]"
    sleep 1
	
    #alltitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 72.75}]"
    sleep 1
	
    #bearing
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.75}]"
    sleep 1
	
	#velocity
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 86.75}]"
    sleep 1 

	#Ignition [trip ends]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 2}]"
    sleep 1  
	
	#Ignition [trip start]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"
    sleep 1
	
	#odo meter value
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 500000}]"
    sleep 1
	
	#fuel level
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 0}]"
    sleep 1
    
	#latitiude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 17.628162819}]"
    sleep 1
    
	#longitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 72.816781910}]"
    sleep 1
	
    #battery levle
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 200}]"
    sleep 1
	
    #alltitude
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 72.75}]"
    sleep 1
	
    #bearing
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.75}]"
    sleep 1
	
	#velocity
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 86.75}]"
    sleep 1 

	#Ignition [trip ends]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 1}]"   
	
	sleep 15	
	
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 1800000}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 350000}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 17.62816781}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 72.791899392}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 130000}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 132.962}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  252.822}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 152.150}]"
    sleep 1
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 400000}]"
    sleep 1
	
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 2}]"
    sleep 1	
	
done

