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
    #Enter alert-India Gate
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.61370736476138,"Longitude":77.22751858264235,"CoarseOverGround":4.5,"Speed":0.1} 0'
    sleep 5
	#Rajpath Entry
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.61270736476138,"Longitude":77.22651858264235,"CoarseOverGround":4.5,"Speed":0.1} 0'
    sleep 2
	#North Lawn Entry
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.615000,"Longitude":77.229000,"CoarseOverGround":4.5,"Speed":0.5} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE