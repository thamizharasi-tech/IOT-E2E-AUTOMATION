#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#Ignition OFF
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"

#Vehicle Lock
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 1}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

# Tow Alert location

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608963904243854}, {'id': 559940098, 'area': 0, 'value': 77.22999505359383}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"