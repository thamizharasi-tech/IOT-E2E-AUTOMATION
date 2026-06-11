#!/bin/sh

#Geofence

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61370736476138}, {'id': 559940098, 'area': 0, 'value': 77.22751858264235}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 4}]"

#Geofence Exit

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.612632751464844}, {'id': 559940098, 'area': 0, 'value': 77.227653503417969}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.614967346191406}, {'id': 559940098, 'area': 0, 'value': 77.228347778320312}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

#GEOFENCE ENTER

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.614250183105469}, {'id': 559940098, 'area': 0, 'value': 77.227798461914062}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.613349914550781}, {'id': 559940098, 'area': 0, 'value': 77.227684020996094}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
#Ignition [trip stop]
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"