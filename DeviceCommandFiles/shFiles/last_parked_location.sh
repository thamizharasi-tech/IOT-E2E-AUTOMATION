#!/bin/sh

cd /data/
export LD_LIBRARY_PATH=./

#publish location 
# --------------------LOCATION----------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559988750, 'area': 0, 'value': 92.001},
{'id': 559988751, 'area': 0, 'value': 53.001},
{'id': 559988752, 'area': 0, 'value': 13.89},
{'id': 559988753, 'area': 0, 'value': 73.001},
{'id': 559988754, 'area': 0, 'value': 19.19},
{'id': 559988755, 'area': 0, 'value': 493},
{'id': 559988759, 'area': 0, 'value': 53.001},
{'id': 559988760, 'area': 0, 'value': 58.001},
{'id': 559988761, 'area': 0, 'value': 58.001},
{'id': 559988762, 'area': 0, 'value': 60.001},
{'id': 559940097, 'area': 0, 'value': 28.60886667},
{'id': 559940098, 'area': 0, 'value': 77.230},
{'id': 559940099, 'area': 0, 'value': 214.1},
{'id': 559940100, 'area': 0, 'value': 92.9},
{'id': 559942149, 'area': 0, 'value': 0}, {'id': 289408009, 'area': 0, 'value': 3}]"

#publish ignition state
# -------------------IGNITION STATE - OFF---------------------------
./paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 3}]"
