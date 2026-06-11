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
    echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP   {"altitude":2.2,"latitude":28.6087,"longitude":77.2300,"bearing":2.5,"speed":32,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE