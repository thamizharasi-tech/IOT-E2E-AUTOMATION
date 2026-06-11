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
    echo "creg C2C_INFO_PLATFORM 0"
    sleep 1
    echo "cap C2C_SSIL_APP 0"
    sleep 1
    #Enter alert
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP   {"Altitude":2.2,"Latitude":28.6087,"Longitude":77.2300,"CoarseOverGround":2.5,"Speed":0.1} 0'
    sleep 5
	#Exit alert
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP   {"Altitude":2.2,"Latitude":28.6080,"Longitude":80.0014,"CoarseOverGround":2.5,"Speed":0.1} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE