#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it
{
    echo "dp"
    sleep 1
    echo "dp_init"
    sleep 1
	echo "dp_send 105 0"
    sleep 1
    echo "dp_send 104 pin_4"
    sleep 1
    echo "quit"
	sleep 1
	echo ""
} | $C2C_TEST_CONSOLE