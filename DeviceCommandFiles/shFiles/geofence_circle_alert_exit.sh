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
    # Exit Point A (NE) - moved ~+0.01 deg lat/long (~1.4km) to be clearly outside 500m
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.62370736476138,"Longitude":77.23751858264235,"CoarseOverGround":4.5,"Speed":0.1} 0'
    sleep 2
    # Exit Point B (SW) - moved ~-0.01 deg lat/long (~1.48km) to be clearly outside 500m
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":92.9,"Latitude":28.603700,"Longitude":77.217500,"CoarseOverGround":4.5,"Speed":0.5} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE