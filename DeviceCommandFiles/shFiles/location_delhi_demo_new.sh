#!/bin/sh

# Home Location

sleep 1
#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"

sleep 3
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 1
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 0}]"

sleep 1
#Ignition [trip start]
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 4}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 1}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 2}]"

#new
sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.609059}, {'id': 559940098, 'area': 0, 'value': 77.229717}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 2}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.609046}, {'id': 559940098, 'area': 0, 'value': 77.229783}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 4}]"

# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 5}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.609020}, {'id': 559940098, 'area': 0, 'value': 77.229864}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.609002}, {'id': 559940098, 'area': 0, 'value': 77.229927}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

#need1 lat
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608997}, {'id': 559940098, 'area': 0, 'value': 77.229974}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608971160619618}, {'id': 559940098, 'area': 0, 'value': 77.229970108259352}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25} {\"id\": 291504647,\"area\": 0,\"value\": 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608931718838814}, {'id': 559940098, 'area': 0, 'value': 77.22997681378186}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608905840049882}, {'id': 559940098, 'area': 0, 'value': 77.2300109814177}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608874009563348}, {'id': 559940098, 'area': 0, 'value': 77.2300425157769}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6088751869308}, {'id': 559940098, 'area': 0, 'value': 77.23005726792694}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60887047746091}, {'id': 559940098, 'area': 0, 'value': 77.230175285127299}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885700610538}, {'id': 559940098, 'area': 0, 'value': 77.23023999967462}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608851707950823}, {'id': 559940098, 'area': 0, 'value': 77.23028425612318}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60884935321521}, {'id': 559940098, 'area': 0, 'value': 77.23039623834991}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60000}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608848175847452}, {'id': 559940098, 'area': 0, 'value': 77.2304539058435}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60884464374415}, {'id': 559940098, 'area': 0, 'value': 77.2305182788596}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883344374406}, {'id': 559940098, 'area': 0, 'value': 77.23068726594478}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 18}]"

#sleep 2
#LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608835813485356}, {'id': 559940098, 'area': 0, 'value': 77.23060679175676}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
# Trip - Start Odometer & battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 100}, {\"id\": 559943684,\"area\": 0,\"value\": 25}, {\"id\": 291504647,\"area\": 0,\"value\": 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 96.5}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60896667}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6091}, {'id': 559940098, 'area': 0, 'value': 77.23076667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 341.8}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6091}, {'id': 559940098, 'area': 0, 'value': 77.23076667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 341.8}, {'id': 559942149, 'area': 0, 'value': 20}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60931667}, {'id': 559940098, 'area': 0, 'value': 77.2306}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 26}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60953333}, {'id': 559940098, 'area': 0, 'value': 77.23041667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 26}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60961667}, {'id': 559940098, 'area': 0, 'value': 77.2303}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 309.1}, {'id': 559942149, 'area': 0, 'value': 26}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60961667}, {'id': 559940098, 'area': 0, 'value': 77.2303}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 309.1}, {'id': 559942149, 'area': 0, 'value': 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60971667}, {'id': 559940098, 'area': 0, 'value': 77.23011667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 28}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60983333}, {'id': 559940098, 'area': 0, 'value': 77.22995}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 28}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 27}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60993333}, {'id': 559940098, 'area': 0, 'value': 77.22978333}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 27}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61003333}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 215.1}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 27}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60001}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 24}]"



sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61013333}, {'id': 559940098, 'area': 0, 'value': 77.22945}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 24}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60002}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61013333}, {'id': 559940098, 'area': 0, 'value': 77.22945}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61023333}, {'id': 559940098, 'area': 0, 'value': 77.22928333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60002}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 15}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61033333}, {'id': 559940098, 'area': 0, 'value': 77.22911667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61043333}, {'id': 559940098, 'area': 0, 'value': 77.22893333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.22876667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 15}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60002}, {\"id\": 291504905,\"area\": 0,\"value\": 99}, {\"id\": 559943684,\"area\": 0,\"value\": 24}, {\"id\": 291504647,\"area\": 0,\"value\": 17}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 17}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60002}, {\"id\": 291504905,\"area\": 0,\"value\": 98}, {\"id\": 559943684,\"area\": 0,\"value\": 23}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61075}, {'id': 559940098, 'area': 0, 'value': 77.22843333}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61085}, {'id': 559940098, 'area': 0, 'value': 77.22826667}, {'id': 559940099, 'area': 0, 'value': 216.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61096667}, {'id': 559940098, 'area': 0, 'value': 77.22811667}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 311.5}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60002}, {\"id\": 291504905,\"area\": 0,\"value\": 98}, {\"id\": 559943684,\"area\": 0,\"value\": 22}, {\"id\": 291504647,\"area\": 0,\"value\": 23}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6111}, {'id': 559940098, 'area': 0, 'value': 77.22798333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 23}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61123333}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 23}]"

sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60003}, {\"id\": 291504905,\"area\": 0,\"value\": 98}, {\"id\": 559943684,\"area\": 0,\"value\": 22}, {\"id\": 291504647,\"area\": 0,\"value\": 25}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61123333}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6114}, {'id': 559940098, 'area': 0, 'value': 77.22775}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 332.2}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61156667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 336.3}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61173333}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 345.2}, {'id': 559942149, 'area': 0, 'value': 25}]"

#sleep 2
#LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61191667}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6121}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 25}]"

# sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6121}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 25}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61228333}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 25}]"
sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60003}, {\"id\": 291504905,\"area\": 0,\"value\": 98}, {\"id\": 559943684,\"area\": 0,\"value\": 22}, {\"id\": 291504647,\"area\": 0,\"value\": 50}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61228333}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61263333}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61281667}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.613000000000003}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 50}]"
sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60003}, {\"id\": 291504905,\"area\": 0,\"value\": 97}, {\"id\": 559943684,\"area\": 0,\"value\": 21}, {\"id\": 291504647,\"area\": 0,\"value\": 60}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.613000000000003}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61316667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61335}, {'id': 559940098, 'area': 0, 'value': 77.22768333}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61353333}, {'id': 559940098, 'area': 0, 'value': 77.2277}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61371667}, {'id': 559940098, 'area': 0, 'value': 77.22771667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6139}, {'id': 559940098, 'area': 0, 'value': 77.22773333}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 1
# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 97}, {\"id\": 559943684,\"area\": 0,\"value\": 21}, {\"id\": 291504647,\"area\": 0,\"value\": 80}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6139}, {'id': 559940098, 'area': 0, 'value': 77.22773333}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 80}]"


sleep 2
#hb
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883415,\"area\": 0,\"value\": 1}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61406667}, {'id': 559940098, 'area': 0, 'value': 77.22776667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 10.0}, {'id': 559942149, 'area': 0, 'value': 80}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 97}, {\"id\": 559943684,\"area\": 0,\"value\": 21}, {\"id\": 291504647,\"area\": 0,\"value\": 70}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61425}, {'id': 559940098, 'area': 0, 'value': 77.2278}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 9.1}, {'id': 559942149, 'area': 0, 'value': 70}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61441667}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 14.8}, {'id': 559942149, 'area': 0, 'value': 70}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 97}, {\"id\": 559943684,\"area\": 0,\"value\": 21}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61458333}, {'id': 559940098, 'area': 0, 'value': 77.22793333}, {'id': 559940099, 'area': 0, 'value': 215.0}, {'id': 559940100, 'area': 0, 'value': 23.7}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 97}, {\"id\": 559943684,\"area\": 0,\"value\": 21}, {\"id\": 291504647,\"area\": 0,\"value\": 12}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61458333}, {'id': 559940098, 'area': 0, 'value': 77.22793333}, {'id': 559940099, 'area': 0, 'value': 215.0}, {'id': 559940100, 'area': 0, 'value': 23.7}, {'id': 559942149, 'area': 0, 'value': 12}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 0}]"

sleep 4
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61486667}, {'id': 559940098, 'area': 0, 'value': 77.22818333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 44.6}, {'id': 559942149, 'area': 0, 'value': 0}]"

# Crash Alert

sleep 10
# Crash alert
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891597,\"area\": 0,\"value\": 2}]"
#sleep 5
# Crash alert
#LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557891597,\"area\": 0,\"value\": 3}]"
sleep 10

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 2}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61496667}, {'id': 559940098, 'area': 0, 'value': 77.22835}, {'id': 559940099, 'area': 0, 'value': 217.8}, {'id': 559940100, 'area': 0, 'value': 55.6}, {'id': 559942149, 'area': 0, 'value': 2}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 8}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61505}, {'id': 559940098, 'area': 0, 'value': 77.22853333}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 8}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 14}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.22871667}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 14}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61521667}, {'id': 559940098, 'area': 0, 'value': 77.2289}, {'id': 559940099, 'area': 0, 'value': 217.7}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 20}, {\"id\": 291504647,\"area\": 0,\"value\": 42}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61521667}, {'id': 559940098, 'area': 0, 'value': 77.2289}, {'id': 559940099, 'area': 0, 'value': 217.7}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 42}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 55}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6153}, {'id': 559940098, 'area': 0, 'value': 77.22908333}, {'id': 559940099, 'area': 0, 'value': 217.5}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 67}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 96}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 67}]"


sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61538333}, {'id': 559940098, 'area': 0, 'value': 77.22926667}, {'id': 559940099, 'area': 0, 'value': 217.3}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 67}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60004}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 72}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61546667}, {'id': 559940098, 'area': 0, 'value': 77.22943333}, {'id': 559940099, 'area': 0, 'value': 217.2}, {'id': 559940100, 'area': 0, 'value': 60.3}, {'id': 559942149, 'area': 0, 'value': 72}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 83}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61555}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 83}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 100}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61563333}, {'id': 559940098, 'area': 0, 'value': 77.2298}, {'id': 559940099, 'area': 0, 'value': 217.0}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 100}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 121}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.22998333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 121}]"

sleep 2
#ha
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883414,\"area\": 0,\"value\": 1}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 120}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6158}, {'id': 559940098, 'area': 0, 'value': 77.23016667}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 120}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 117}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61588333}, {'id': 559940098, 'area': 0, 'value': 77.23035}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 117}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 112}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61596667}, {'id': 559940098, 'area': 0, 'value': 77.23053333}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 112}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 95}, {\"id\": 559943684,\"area\": 0,\"value\": 19}, {\"id\": 291504647,\"area\": 0,\"value\": 117}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 117}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 94}, {\"id\": 559943684,\"area\": 0,\"value\": 18}, {\"id\": 291504647,\"area\": 0,\"value\": 104}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 104}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6161}, {'id': 559940098, 'area': 0, 'value': 77.23091667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 69.2}, {'id': 559942149, 'area': 0, 'value': 104}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 94}, {\"id\": 559943684,\"area\": 0,\"value\": 18}, {\"id\": 291504647,\"area\": 0,\"value\": 94}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61616667}, {'id': 559940098, 'area': 0, 'value': 77.2311}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 94}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23131667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 85.0}, {'id': 559942149, 'area': 0, 'value': 94}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60005}, {\"id\": 291504905,\"area\": 0,\"value\": 94}, {\"id\": 559943684,\"area\": 0,\"value\": 18}, {\"id\": 291504647,\"area\": 0,\"value\": 80}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23151667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 90.0}, {'id': 559942149, 'area': 0, 'value': 80}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61611667}, {'id': 559940098, 'area': 0, 'value': 77.23171667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 80}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60006}, {\"id\": 291504905,\"area\": 0,\"value\": 94}, {\"id\": 559943684,\"area\": 0,\"value\": 18}, {\"id\": 291504647,\"area\": 0,\"value\": 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61611667}, {'id': 559940098, 'area': 0, 'value': 77.23171667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23188333}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61593333}, {'id': 559940098, 'area': 0, 'value': 77.23205}, {'id': 559940099, 'area': 0, 'value': 213.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61581667}, {'id': 559940098, 'area': 0, 'value': 77.23221667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 128.6}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.23238333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6157}, {'id': 559940098, 'area': 0, 'value': 77.23243333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 50}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60006}, {\"id\": 291504905,\"area\": 0,\"value\": 94}, {\"id\": 559943684,\"area\": 0,\"value\": 18}, {\"id\": 291504647,\"area\": 0,\"value\": 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6157}, {'id': 559940098, 'area': 0, 'value': 77.23243333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 60}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 60}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60006}, {\"id\": 291504905,\"area\": 0,\"value\": 93}, {\"id\": 559943684,\"area\": 0,\"value\": 17}, {\"id\": 291504647,\"area\": 0,\"value\": 76}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 76}]"

sleep 2
#ha
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883414,\"area\": 0,\"value\": 1}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 76}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 91}, {\"id\": 559943684,\"area\": 0,\"value\": 16}, {\"id\": 291504647,\"area\": 0,\"value\": 82}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 82}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 90}, {\"id\": 559943684,\"area\": 0,\"value\": 16}, {\"id\": 291504647,\"area\": 0,\"value\": 85}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61561667}, {'id': 559940098, 'area': 0, 'value': 77.23255}, {'id': 559940099, 'area': 0, 'value': 213.1}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 85}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 90}, {\"id\": 559943684,\"area\": 0,\"value\": 15}, {\"id\": 291504647,\"area\": 0,\"value\": 92}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61551667}, {'id': 559940098, 'area': 0, 'value': 77.23273333}, {'id': 559940099, 'area': 0, 'value': 212.6}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 92}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61541667}, {'id': 559940098, 'area': 0, 'value': 77.2329}, {'id': 559940099, 'area': 0, 'value': 212.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 92}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61533333}, {'id': 559940098, 'area': 0, 'value': 77.23306667}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 92}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 89}, {\"id\": 559943684,\"area\": 0,\"value\": 14}, {\"id\": 291504647,\"area\": 0,\"value\": 90}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61533333}, {'id': 559940098, 'area': 0, 'value': 77.23306667}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 90}]"

sleep 2
#hb
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883415,\"area\": 0,\"value\": 1}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61523333}, {'id': 559940098, 'area': 0, 'value': 77.23325}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 90}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.23341667}, {'id': 559940099, 'area': 0, 'value': 212.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 90}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61503333}, {'id': 559940098, 'area': 0, 'value': 77.2336}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 90}]"

sleep 2
#ha
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557883414,\"area\": 0,\"value\": 1}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61495}, {'id': 559940098, 'area': 0, 'value': 77.23376667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 90}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61485}, {'id': 559940098, 'area': 0, 'value': 77.23395}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 90}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 89}, {\"id\": 559943684,\"area\": 0,\"value\": 14}, {\"id\": 291504647,\"area\": 0,\"value\": 64}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61485}, {'id': 559940098, 'area': 0, 'value': 77.23395}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 64}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61475}, {'id': 559940098, 'area': 0, 'value': 77.23411667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 64}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61461667}, {'id': 559940098, 'area': 0, 'value': 77.23425}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 64}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 88}, {\"id\": 559943684,\"area\": 0,\"value\": 13}, {\"id\": 291504647,\"area\": 0,\"value\": 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61448333}, {'id': 559940098, 'area': 0, 'value': 77.23438333}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61435}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 50}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61418333}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 156.3}, {'id': 559942149, 'area': 0, 'value': 50}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60007}, {\"id\": 291504905,\"area\": 0,\"value\": 88}, {\"id\": 559943684,\"area\": 0,\"value\": 13}, {\"id\": 291504647,\"area\": 0,\"value\": 56}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61418333}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 156.3}, {'id': 559942149, 'area': 0, 'value': 56}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61401667}, {'id': 559940098, 'area': 0, 'value': 77.23466667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 160.7}, {'id': 559942149, 'area': 0, 'value': 56}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61383333}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 56}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61365}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 56}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61346667}, {'id': 559940098, 'area': 0, 'value': 77.23463333}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 56}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6133}, {'id': 559940098, 'area': 0, 'value': 77.23461667}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 56}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 87}, {\"id\": 559943684,\"area\": 0,\"value\": 14}, {\"id\": 291504647,\"area\": 0,\"value\": 40}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61311667}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 40}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61293333}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 40}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61275}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 40}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61258333}, {'id': 559940098, 'area': 0, 'value': 77.23456667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 40}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6124}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 213.5}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 40}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 87}, {\"id\": 559943684,\"area\": 0,\"value\": 13}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61221667}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 212.5}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61203333}, {'id': 559940098, 'area': 0, 'value': 77.23453333}, {'id': 559940099, 'area': 0, 'value': 211.4}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61185}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 210.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61168333}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6115}, {'id': 559940098, 'area': 0, 'value': 77.2345}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 86}, {\"id\": 559943684,\"area\": 0,\"value\": 13}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61131667}, {'id': 559940098, 'area': 0, 'value': 77.23445}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 193.5}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61115}, {'id': 559940098, 'area': 0, 'value': 77.23441667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 190.0}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61098333}, {'id': 559940098, 'area': 0, 'value': 77.23433333}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 203.7}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61083333}, {'id': 559940098, 'area': 0, 'value': 77.23421667}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 214.3}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61071667}, {'id': 559940098, 'area': 0, 'value': 77.23406667}, {'id': 559940099, 'area': 0, 'value': 209.3}, {'id': 559940100, 'area': 0, 'value': 228.5}, {'id': 559942149, 'area': 0, 'value': 10}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 85}, {\"id\": 559943684,\"area\": 0,\"value\": 12}, {\"id\": 291504647,\"area\": 0,\"value\": 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.23388333}, {'id': 559940099, 'area': 0, 'value': 209.6}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 5]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.2337}, {'id': 559940099, 'area': 0, 'value': 210.1}, {'id': 559940100, 'area': 0, 'value': 238.1}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61046667}, {'id': 559940098, 'area': 0, 'value': 77.23351667}, {'id': 559940099, 'area': 0, 'value': 210.6}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 5}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 83}, {\"id\": 559943684,\"area\": 0,\"value\": 12}, {\"id\": 291504647,\"area\": 0,\"value\": 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61038333}, {'id': 559940098, 'area': 0, 'value': 77.23333333}, {'id': 559940099, 'area': 0, 'value': 211.2}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6103}, {'id': 559940098, 'area': 0, 'value': 77.23315}, {'id': 559940099, 'area': 0, 'value': 212.5}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 5}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 82}, {\"id\": 559943684,\"area\": 0,\"value\": 11}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61021667}, {'id': 559940098, 'area': 0, 'value': 77.23296667}, {'id': 559940099, 'area': 0, 'value': 213.5}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61015}, {'id': 559940098, 'area': 0, 'value': 77.23278333}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 10}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 81}, {\"id\": 559943684,\"area\": 0,\"value\": 11}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61006667}, {'id': 559940098, 'area': 0, 'value': 77.2326}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60998333}, {'id': 559940098, 'area': 0, 'value': 77.23241667}, {'id': 559940099, 'area': 0, 'value': 215.1}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6099}, {'id': 559940098, 'area': 0, 'value': 77.23223333}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 10}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 80}, {\"id\": 559943684,\"area\": 0,\"value\": 10}, {\"id\": 291504647,\"area\": 0,\"value\": 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60983333}, {'id': 559940098, 'area': 0, 'value': 77.23205}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 247.5}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60975}, {'id': 559940098, 'area': 0, 'value': 77.23186667}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60966667}, {'id': 559940098, 'area': 0, 'value': 77.23168333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60958333}, {'id': 559940098, 'area': 0, 'value': 77.2315}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 15}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60948333}, {'id': 559940098, 'area': 0, 'value': 77.23133333}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 235.6}, {'id': 559942149, 'area': 0, 'value': 15}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60008}, {\"id\": 291504905,\"area\": 0,\"value\": 79}, {\"id\": 559943684,\"area\": 0,\"value\": 10}, {\"id\": 291504647,\"area\": 0,\"value\": 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60936667}, {'id': 559940098, 'area': 0, 'value': 77.23118333}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 228.5}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60923333}, {'id': 559940098, 'area': 0, 'value': 77.23105}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 221.3}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906667}, {'id': 559940098, 'area': 0, 'value': 77.23095}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 207.8}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60888333}, {'id': 559940098, 'area': 0, 'value': 77.23093333}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6088}, {'id': 559940098, 'area': 0, 'value': 77.23091667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 190.0}, {'id': 559942149, 'area': 0, 'value': 20}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60009}, {\"id\": 291504905,\"area\": 0,\"value\": 78}, {\"id\": 559943684,\"area\": 0,\"value\": 9}, {\"id\": 291504647,\"area\": 0,\"value\": 10}]"

sleep 1
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60881667}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 280.7}, {'id': 559942149, 'area': 0, 'value': 10}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23041667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 270.0}, {'id': 559942149, 'area': 0, 'value': 10}]"

# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60009}, {\"id\": 291504905,\"area\": 0,\"value\": 77}, {\"id\": 559943684,\"area\": 0,\"value\": 9}, {\"id\": 291504647,\"area\": 0,\"value\": 5}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23021667}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 275.4}, {'id': 559942149, 'area': 0, 'value': 10}]"


# Odometer, battery level & Speed
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504644,\"area\": 0,\"value\": 60009}, {\"id\": 291504905,\"area\": 0,\"value\": 76}, {\"id\": 559943684,\"area\": 0,\"value\": 9}, {\"id\": 291504647,\"area\": 0,\"value\": 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60882732964291}, {'id': 559940098, 'area': 0, 'value': 77.23017476156079}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883321648267}, {'id': 559940098, 'area': 0, 'value': 77.2300996597118}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608870892249232}, {'id': 559940098, 'area': 0, 'value': 77.23006076768286}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608889730127434}, {'id': 559940098, 'area': 0, 'value': 77.23003931001172}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60895566267459}, {'id': 559940098, 'area': 0, 'value': 77.23000980571389}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608963904243854}, {'id': 559940098, 'area': 0, 'value': 77.22999505359383}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608999225231475}, {'id': 559940098, 'area': 0, 'value': 77.22993604499818}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"
sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

#Ignition [trip ends]
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"

#Last parked location
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 1}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

# Tow Alert location

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608963904243854}, {'id': 559940098, 'area': 0, 'value': 77.22999505359383}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 5
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60895566267459}, {'id': 559940098, 'area': 0, 'value': 77.23000980571389}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

#sleep 2
#LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883321648267}, {'id': 559940098, 'area': 0, 'value': 77.2300996597118}, {'id': #559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

# Critical Battery 
sleep 2
# battery level - below 20
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 19}, {\"id\": 559943684,\"area\": 0,\"value\": 8}]"

sleep 2	
#Tampering alert
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557895681,\"area\": 0,\"value\": 5}]"


sleep 2	
# Speed - 0
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504647,\"area\": 0,\"value\": 0}]"

sleep 20
#Disable Tow Away alert & Ignition -2
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 2}]"

sleep 10
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883321648267}, {'id': 559940098, 'area': 0, 'value': 77.2300996597118}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60895566267459}, {'id': 559940098, 'area': 0, 'value': 77.23000980571389}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608963904243854}, {'id': 559940098, 'area': 0, 'value': 77.22999505359383}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"

sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.608999225231475}, {'id': 559940098, 'area': 0, 'value': 77.22993604499818}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"
sleep 2
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60906030812995}, {'id': 559940098, 'area': 0, 'value': 77.22966241433508}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0}]"


#sleep 10
# battery level - greater than 20
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 75}, {\"id\": 559943684,\"area\": 0,\"value\": 9}]"

#sleep 2
# battery level - greater than 20
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 86}, {\"id\": 559943684,\"area\": 0,\"value\": 15}]"

#sleep 2
# battery level - greater than 20
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 92}, {\"id\": 559943684,\"area\": 0,\"value\": 18}]"

sleep 2
# battery level - greater than 100
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 291504905,\"area\": 0,\"value\": 100},{\"id\": 559943684,\"area\": 0,\"value\": 25}]"

