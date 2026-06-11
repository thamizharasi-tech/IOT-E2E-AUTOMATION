#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Start the c2c_test_console and interact with it
if [ "$1" = "digital_pin_generate" ]; then
{
    echo "dp"
    sleep 1
    echo "dp_init"
    sleep 1
    echo "dp_send 105 0"
    sleep 1
    echo "quit"
} | $C2C_TEST_CONSOLE
elif [ "$1" = "digital_pin_vehicle_lock" ]; then
{
    echo "dp"
    sleep 1
    echo "dp_init"
    sleep 1
    echo "dp_send 104 pin_2"
    sleep 1
    echo "quit"
} | $C2C_TEST_CONSOLE
elif [ "$1" = "digital_pin_expiry" ]; then
{
    echo "dp"
    sleep 1
    echo "dp_init"
    sleep 1
    echo "dp_send 109 pin_1"
    sleep 1
    echo "quit"
} | $C2C_TEST_CONSOLE
else
  echo "Invalid input"
fi