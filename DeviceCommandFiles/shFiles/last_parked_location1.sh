#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it
{
    echo "any2any"
    sleep 1
    echo "cit 0"
    sleep 1
    echo "creg C2C_FETCH_ATTR_APP 0"
    sleep 1
    echo "cap C2C_SSIL_APP 0"
    sleep 1
    #Enter alert
    echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP   {"altitude":214.1,"latitude":28.60886667,"longitude":77.230,"bearing":92.9,"speed":0,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE

#publish location 
# --------------------LOCATION----------------------------
#AL_GPS_STATUS
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988750,\"area\": 0,\"value\":  92.001}]"
sleep 1

#AL_GSM_SIGNAL_STRENGTH
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988751,\"area\": 0,\"value\": 53.001}]"
sleep 1

#AL_NETWORK_OP_NAME
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988752,\"area\": 0,\"value\": 13.89}]"
sleep 1

#AL_TIMESTAMP
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988753,\"area\": 0,\"value\": 73.001}]"
sleep 1

#AL_LAT_DIR
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988754,\"area\": 0,\"value\": 19.19}]"
sleep 1

#AL_LONG_DIR
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988755,\"area\": 0,\"value\": 493}]"
sleep 1

#AL_DELTA_DIST_COVERED
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988759,\"area\": 0,\"value\": 53.001}]"
sleep 1

#AL_PDOP
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988760,\"area\": 0,\"value\": 58.001}]"
sleep 1

#AL_HDOP
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988761,\"area\": 0,\"value\": 58.001}]"
sleep 1

#AL_GPS_FIX
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 559988762,\"area\": 0,\"value\": 60.001}]"
sleep 1

#Ignition off
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 272670739,\"area\": 0,\"value\": 3}]"
sleep 1