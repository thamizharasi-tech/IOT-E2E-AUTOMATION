#!/bin/sh


LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 9.333333333333334}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 3}]"

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 8.333333333333334}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.2305}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 93.6}, {'id': 559942149, 'area': 0, 'value': 11.11111111111111}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23065}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 90.0}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 96.5}, {'id': 559942149, 'area': 0, 'value': 16.416666666666668}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60896667}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 14.777777777777779}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6091}, {'id': 559940098, 'area': 0, 'value': 77.23076667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 341.8}, {'id': 559942149, 'area': 0, 'value': 15.555555555555555}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60921667}, {'id': 559940098, 'area': 0, 'value': 77.23068333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 327.9}, {'id': 559942149, 'area': 0, 'value': 15.277777777777777}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60931667}, {'id': 559940098, 'area': 0, 'value': 77.2306}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 13.75}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60943333}, {'id': 559940098, 'area': 0, 'value': 77.2305}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 323.0}, {'id': 559942149, 'area': 0, 'value': 16.22222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60953333}, {'id': 559940098, 'area': 0, 'value': 77.23041667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 13.75}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60961667}, {'id': 559940098, 'area': 0, 'value': 77.2303}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 309.1}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60971667}, {'id': 559940098, 'area': 0, 'value': 77.23011667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60983333}, {'id': 559940098, 'area': 0, 'value': 77.22995}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60993333}, {'id': 559940098, 'area': 0, 'value': 77.22978333}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61003333}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 215.1}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61013333}, {'id': 559940098, 'area': 0, 'value': 77.22945}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61023333}, {'id': 559940098, 'area': 0, 'value': 77.22928333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61033333}, {'id': 559940098, 'area': 0, 'value': 77.22911667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61043333}, {'id': 559940098, 'area': 0, 'value': 77.22893333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.22876667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61075}, {'id': 559940098, 'area': 0, 'value': 77.22843333}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61085}, {'id': 559940098, 'area': 0, 'value': 77.22826667}, {'id': 559940099, 'area': 0, 'value': 216.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61096667}, {'id': 559940098, 'area': 0, 'value': 77.22811667}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 311.5}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6111}, {'id': 559940098, 'area': 0, 'value': 77.22798333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61123333}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6114}, {'id': 559940098, 'area': 0, 'value': 77.22775}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 332.2}, {'id': 559942149, 'area': 0, 'value': 20.88888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61156667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 336.3}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61173333}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 345.2}, {'id': 559942149, 'area': 0, 'value': 19.11111111111111}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61191667}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6121}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61228333}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61245}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 217.2}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61263333}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61281667}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.613000000000003}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61316667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61335}, {'id': 559940098, 'area': 0, 'value': 77.22768333}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61353333}, {'id': 559940098, 'area': 0, 'value': 77.2277}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61371667}, {'id': 559940098, 'area': 0, 'value': 77.22771667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6139}, {'id': 559940098, 'area': 0, 'value': 77.22773333}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61406667}, {'id': 559940098, 'area': 0, 'value': 77.22776667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 10.0}, {'id': 559942149, 'area': 0, 'value': 18.75}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61425}, {'id': 559940098, 'area': 0, 'value': 77.2278}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 9.1}, {'id': 559942149, 'area': 0, 'value': 20.583333333333332}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61441667}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 14.8}, {'id': 559942149, 'area': 0, 'value': 19.11111111111111}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61458333}, {'id': 559940098, 'area': 0, 'value': 77.22793333}, {'id': 559940099, 'area': 0, 'value': 215.0}, {'id': 559940100, 'area': 0, 'value': 23.7}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61473333}, {'id': 559940098, 'area': 0, 'value': 77.22803333}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 30.3}, {'id': 559942149, 'area': 0, 'value': 19.27777777777778}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61486667}, {'id': 559940098, 'area': 0, 'value': 77.22818333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 44.6}, {'id': 559942149, 'area': 0, 'value': 20.833333333333332}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61496667}, {'id': 559940098, 'area': 0, 'value': 77.22835}, {'id': 559940099, 'area': 0, 'value': 217.8}, {'id': 559940100, 'area': 0, 'value': 55.6}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61505}, {'id': 559940098, 'area': 0, 'value': 77.22853333}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.22871667}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61521667}, {'id': 559940098, 'area': 0, 'value': 77.2289}, {'id': 559940099, 'area': 0, 'value': 217.7}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6153}, {'id': 559940098, 'area': 0, 'value': 77.22908333}, {'id': 559940099, 'area': 0, 'value': 217.5}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61538333}, {'id': 559940098, 'area': 0, 'value': 77.22926667}, {'id': 559940099, 'area': 0, 'value': 217.3}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61546667}, {'id': 559940098, 'area': 0, 'value': 77.22943333}, {'id': 559940099, 'area': 0, 'value': 217.2}, {'id': 559940100, 'area': 0, 'value': 60.3}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61555}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61563333}, {'id': 559940098, 'area': 0, 'value': 77.2298}, {'id': 559940099, 'area': 0, 'value': 217.0}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.22998333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6158}, {'id': 559940098, 'area': 0, 'value': 77.23016667}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61588333}, {'id': 559940098, 'area': 0, 'value': 77.23035}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61596667}, {'id': 559940098, 'area': 0, 'value': 77.23053333}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6161}, {'id': 559940098, 'area': 0, 'value': 77.23091667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 69.2}, {'id': 559942149, 'area': 0, 'value': 20.916666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61616667}, {'id': 559940098, 'area': 0, 'value': 77.2311}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23131667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 85.0}, {'id': 559942149, 'area': 0, 'value': 21.277777777777775}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23151667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 90.0}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61611667}, {'id': 559940098, 'area': 0, 'value': 77.23171667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 20.916666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23188333}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61593333}, {'id': 559940098, 'area': 0, 'value': 77.23205}, {'id': 559940099, 'area': 0, 'value': 213.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61581667}, {'id': 559940098, 'area': 0, 'value': 77.23221667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 128.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.23238333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6157}, {'id': 559940098, 'area': 0, 'value': 77.23243333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 5.222222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 4.916666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 4.916666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61561667}, {'id': 559940098, 'area': 0, 'value': 77.23255}, {'id': 559940099, 'area': 0, 'value': 213.1}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 9.86111111111111}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61551667}, {'id': 559940098, 'area': 0, 'value': 77.23273333}, {'id': 559940099, 'area': 0, 'value': 212.6}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61541667}, {'id': 559940098, 'area': 0, 'value': 77.2329}, {'id': 559940099, 'area': 0, 'value': 212.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61533333}, {'id': 559940098, 'area': 0, 'value': 77.23306667}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61523333}, {'id': 559940098, 'area': 0, 'value': 77.23325}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.23341667}, {'id': 559940099, 'area': 0, 'value': 212.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61503333}, {'id': 559940098, 'area': 0, 'value': 77.2336}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61495}, {'id': 559940098, 'area': 0, 'value': 77.23376667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61485}, {'id': 559940098, 'area': 0, 'value': 77.23395}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61475}, {'id': 559940098, 'area': 0, 'value': 77.23411667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61461667}, {'id': 559940098, 'area': 0, 'value': 77.23425}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61448333}, {'id': 559940098, 'area': 0, 'value': 77.23438333}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61435}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61418333}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 156.3}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61401667}, {'id': 559940098, 'area': 0, 'value': 77.23466667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 160.7}, {'id': 559942149, 'area': 0, 'value': 19.583333333333332}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61383333}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61365}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61346667}, {'id': 559940098, 'area': 0, 'value': 77.23463333}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6133}, {'id': 559940098, 'area': 0, 'value': 77.23461667}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 18.555555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61311667}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61293333}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61275}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61258333}, {'id': 559940098, 'area': 0, 'value': 77.23456667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 18.555555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6124}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 213.5}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61221667}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 212.5}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61203333}, {'id': 559940098, 'area': 0, 'value': 77.23453333}, {'id': 559940099, 'area': 0, 'value': 211.4}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61185}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 210.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61168333}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6115}, {'id': 559940098, 'area': 0, 'value': 77.2345}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61131667}, {'id': 559940098, 'area': 0, 'value': 77.23445}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 193.5}, {'id': 559942149, 'area': 0, 'value': 20.88888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61115}, {'id': 559940098, 'area': 0, 'value': 77.23441667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 190.0}, {'id': 559942149, 'area': 0, 'value': 18.75}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61098333}, {'id': 559940098, 'area': 0, 'value': 77.23433333}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 203.7}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61083333}, {'id': 559940098, 'area': 0, 'value': 77.23421667}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 214.3}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61071667}, {'id': 559940098, 'area': 0, 'value': 77.23406667}, {'id': 559940099, 'area': 0, 'value': 209.3}, {'id': 559940100, 'area': 0, 'value': 228.5}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.23388333}, {'id': 559940099, 'area': 0, 'value': 209.6}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.2337}, {'id': 559940099, 'area': 0, 'value': 210.1}, {'id': 559940100, 'area': 0, 'value': 238.1}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61046667}, {'id': 559940098, 'area': 0, 'value': 77.23351667}, {'id': 559940099, 'area': 0, 'value': 210.6}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61038333}, {'id': 559940098, 'area': 0, 'value': 77.23333333}, {'id': 559940099, 'area': 0, 'value': 211.2}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6103}, {'id': 559940098, 'area': 0, 'value': 77.23315}, {'id': 559940099, 'area': 0, 'value': 212.5}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61021667}, {'id': 559940098, 'area': 0, 'value': 77.23296667}, {'id': 559940099, 'area': 0, 'value': 213.5}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61015}, {'id': 559940098, 'area': 0, 'value': 77.23278333}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61006667}, {'id': 559940098, 'area': 0, 'value': 77.2326}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60998333}, {'id': 559940098, 'area': 0, 'value': 77.23241667}, {'id': 559940099, 'area': 0, 'value': 215.1}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6099}, {'id': 559940098, 'area': 0, 'value': 77.23223333}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60983333}, {'id': 559940098, 'area': 0, 'value': 77.23205}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60975}, {'id': 559940098, 'area': 0, 'value': 77.23186667}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60966667}, {'id': 559940098, 'area': 0, 'value': 77.23168333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60958333}, {'id': 559940098, 'area': 0, 'value': 77.2315}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60948333}, {'id': 559940098, 'area': 0, 'value': 77.23133333}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 235.6}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60936667}, {'id': 559940098, 'area': 0, 'value': 77.23118333}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 228.5}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60923333}, {'id': 559940098, 'area': 0, 'value': 77.23105}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 221.3}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906667}, {'id': 559940098, 'area': 0, 'value': 77.23095}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 207.8}, {'id': 559942149, 'area': 0, 'value': 20.88888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60888333}, {'id': 559940098, 'area': 0, 'value': 77.23093333}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6088}, {'id': 559940098, 'area': 0, 'value': 77.23091667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 190.0}, {'id': 559942149, 'area': 0, 'value': 9.388888888888888}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60881667}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 280.7}, {'id': 559942149, 'area': 0, 'value': 9.9444444444441883}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23061667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 19.63888888888889}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23041667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 270.0}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 13.944444444444445}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 8.333333333333334}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 2.7777777777777777}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
   
sleep 1