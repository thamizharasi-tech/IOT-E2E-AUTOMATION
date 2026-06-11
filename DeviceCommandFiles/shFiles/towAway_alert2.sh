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
    echo "creg C2C_INFO_PLATFORM 0"
    sleep 1
    echo "cap C2C_SSIL_APP 0"
	sleep 1
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.612632751464844,"Longitude":77.227653503417969,"CoarseOverGround":4.5,"Speed":0.5} 0'
	sleep 5
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.612642751464844,"Longitude":77.227663503417969,"CoarseOverGround":4.5,"Speed":0.9} 0'
	sleep 1
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.612652751464844,"Longitude":77.227673503417969,"CoarseOverGround":4.5,"Speed":1.9} 0'
	sleep 1
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.612652751464844,"Longitude":77.227673503417969,"CoarseOverGround":4.5,"Speed":2.9} 0'
	sleep 1
	echo "quit"
	sleep 1
	echo ""
} | $C2C_TEST_CONSOLE

LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{\"id\": 557895681,\"area\": 0,\"value\": 0}]"