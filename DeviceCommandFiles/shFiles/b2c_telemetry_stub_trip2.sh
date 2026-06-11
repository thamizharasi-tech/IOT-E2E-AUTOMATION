#!/bin/sh

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6000}]"
sleep 1

#RPM
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 400}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 60}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97100}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59100}]"
sleep 1

#battery level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 400}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 920}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
sleep 1

#speed
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 75}]"
sleep 1

paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6000}]"
sleep 1

#RPM
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 300}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 60}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97100}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59100}]"
sleep 1

#battery level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 400}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 920}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
sleep 1

#speed
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 75}]"
sleep 1

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6010}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 55}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97105}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59105}]"
sleep 1

#battery levle
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 350}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 920}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 16}]"
sleep 1

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6050}]"
sleep 1

#RPM
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 200}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 50}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97110}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.49110}]"
sleep 1

#battery levle
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 350}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 930}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 15}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 40}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97120}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59120}]"
sleep 1

#battery level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 300}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 900}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
sleep 1

#speed
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 105}]"
sleep 1

#Ignition [trip ends]
#paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 1}]"
sleep 10

#Ignition [trip start]
#paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 4}]"
sleep 1

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6100}]"
sleep 1

#RPM
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504901,\"area\": 0,\"value\": 600}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 30}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97130}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59130}]"
sleep 1

#battery levle
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 400}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 800}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 15}]"
sleep 1

#odo meter value
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 6150}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 20}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97140}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59140}]"
sleep 1

#battery levle
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 250}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 72.22}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
sleep 1

#fuel level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504903,\"area\": 0,\"value\": 15}]"
sleep 1

#latitiude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940097,\"area\": 0,\"value\": 12.97150}]"
sleep 1

#longitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940098,\"area\": 0,\"value\": 77.59150}]"
sleep 1

#battery level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 200}]"
sleep 1

#alltitude
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559940099,\"area\": 0,\"value\": 750}]"
sleep 1

#bearing
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559940100,\"area\": 0,\"value\":  186.22}]"
sleep 1

#velocity
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 559942149,\"area\": 0,\"value\": 85.22}]"
sleep 1

#hvac temp current
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{\"id\": 358614274,\"area\": 0,\"value\": 12}]"
sleep 1

#speed
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 55}]"
sleep 1

#battery level
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 200}]"
sleep 1

#accerleration
#paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[1.29]}]"
#sleep 1

#accerleration
#paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[10.1]}]"
#sleep 1

#accerleration
#paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[1.1]}]"
#sleep 1

#gyroscope
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.465011,0.610000,-0.333224]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.175426,0.705438,0.333280]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.836176,0.80876,-0.609051]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.069319,0.96313,-0.563651]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.121440,0.61748,-2.175378]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.276402,0.77182,-0.616900]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.687211,0.62614,0.871585]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.352158,0.78043,-0.489030]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.479941,0.93468,1.828066]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.556444,0.848891,-0.344533]}]"
sleep 0.05

paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.465011,0.610000,-0.333224]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.175426,0.705438,0.333280]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.836176,0.80876,-0.609051]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.069319,0.96313,-0.563651]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.121440,0.61748,-2.175378]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.276402,0.77182,-0.616900]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-0.687211,0.62614,0.871585]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.352158,0.78043,-0.489030]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-2.479941,0.93468,1.828066]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.556444,0.848891,-0.344533]}]"
sleep 0.05
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560054278, \"area\": 0, \"value\":[-1.556444,0.448891,-0.344533]}]"
sleep 0.05

#accerleration - HA

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.83,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.92,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.98,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.04,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.96,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.83,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.92,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.98,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.04,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.96,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.76,0]}]"


sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.83,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.92,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.98,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.04,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.96,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.76,0]}]"


sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.83,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.92,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.98,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.04,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.02,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.96,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,3.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,4.76,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,1.76,0]}]"

#accerlation HB

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.47,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.58,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.16,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.43,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.69,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.93,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.15,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-6.35,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.54,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.47,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.58,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.16,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.43,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.69,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.93,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.15,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-6.35,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.54,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.47,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.58,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.16,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.43,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.69,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.93,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.15,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-6.35,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.54,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.47,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.58,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.88,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-5.16,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.43,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.69,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.93,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.15,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-6.35,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.54,0]}]"

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-1.54,0]}]"

#accerlation HB

sleep .2
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 560050177, \"area\": 0, \"value\":[0,-4.47,0]}]"


#Ignition [trip ends]
# paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 3}]"
paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 289408009,\"area\": 0,\"value\": 1}]"
sleep 0.50