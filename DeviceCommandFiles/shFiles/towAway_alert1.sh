#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

#publish paho command for Tampering alert
# --------------------TAMPERING ALERT----------------------------
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557895681,\"area\": 0,\"value\": 1}]"
sleep 1


# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it to set the GPS_SPEED > 0.83
{
    echo "any2any"
    sleep 1
    echo "cit 0"
    sleep 1
    echo "creg C2C_FETCH_ATTR_APP 0"
    sleep 1
    echo "cap C2C_SSIL_APP 0"
	sleep 1
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":92.9,"latitude":28.612632751464844,"longitude":77.227653503417969,"bearing":4.5,"speed":0.5,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 5
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":92.9,"latitude":28.612642751464844,"longitude":77.227663503417969,"bearing":4.5,"speed":0.9,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 1
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":92.9,"latitude":28.612652751464844,"longitude":77.227673503417969,"bearing":4.5,"speed":1.9,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 1
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":92.9,"latitude":28.612652751464844,"longitude":77.227673503417969,"bearing":4.5,"speed":2.9,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 1
	echo "quit"
	sleep 1
	echo ""
} | $C2C_TEST_CONSOLE

LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557895681,\"area\": 0,\"value\": 0}]"