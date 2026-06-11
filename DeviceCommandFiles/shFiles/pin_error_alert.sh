#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it
{
    echo "dm"
    sleep 1
	echo "a2a_alerts"
	sleep 1
    echo "alerts_init"
    sleep 1
	echo "send_alerts 1 2"
    sleep 2
} | $C2C_TEST_CONSOLE 