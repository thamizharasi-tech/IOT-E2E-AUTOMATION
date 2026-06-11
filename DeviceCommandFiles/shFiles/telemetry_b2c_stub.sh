#!/bin/sh

while true
do

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 0}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 50}]"
  sleep 0.5

  #fuel level
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 30}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60010}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 5}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 100}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60020}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 10}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 150}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60030}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 20}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 200}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60040}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 40}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 250}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60050}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 60}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 300}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60060}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 80}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 350}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60070}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 100}]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 400}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60080}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 119]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 450}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60090}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 120]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 500}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60100}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 121]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 550}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60150}]"
  sleep 0.5

  #speed
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504647, 'area': 0, 'value': 130]"
  sleep 0.5

  #rpm
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504901, 'area': 0, 'value': 600}]"
  sleep 0.5

  #odo meter value
  LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60200}]"
  sleep 0.5

done


