#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
# echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

#cd /vendor/bin || exit 1

# Start vm_a2a_test in background
#./vm_a2a_test &
#echo "vm_a2a_test started with PID $!"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it
{
    echo 'cm'
    sleep 1
    echo 'hcsi'
    sleep 1
    echo "hcssr vehicle_settings.user_settings.vehicle_mode.vacation_mode {\"enabled\":1} test 1 2"
    sleep 5
	echo "quit"
    sleep 1
    echo ""
} | "$C2C_TEST_CONSOLE"
