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
    sleep 1
	
	#RPM 
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 300}]"
    sleep 1 
	
	#Ignition [trip start]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"
    sleep 1
	
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
    sleep 1
	
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
	
	#RPM 
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 600}]"
    sleep 1
	
	#hvac temp current
    LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
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
    sleep 1
	
	#speed	
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 95}]"
	sleep 1

	#Ignition [trip ends]
	LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 1}]"
    sleep 15
	
	# #Ignition [trip start]
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"
    # sleep 1
	
	# #fuel level
    # LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 30}]"
    # sleep 1
    
	# #latitiude
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 17.628162822}]"
    # sleep 1
    
	# #longitude
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 72.816781922}]"
    # sleep 1
	
    # #battery levle
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 400}]"
    # sleep 1
	
    # #alltitude
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 72.22}]"
    # sleep 1
	
    # #bearing
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
    # sleep 1
	
	# #velocity
    # LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
    # sleep 1
	
	# #hvac temp current
    # LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
    # sleep 10	
	

	# #Ignition [trip ends]
	# LD_LIBRARY_PATH=/vendor/lib64/ ./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 1}]"   
	
	
	
done

