#!/bin/sh
 
export LD_LIBRARY_PATH=/vendor/lib64
 
# Read VIN from local file and strip newline/carriage return characters
VIN=$(cat /data/VinNo.txt | tr -d '\r' | tr -d '\n')
 
# Debug info
echo "Raw VIN file content: '$(cat /data/VinNo.txt)'"
echo "Processed VIN: '$VIN'"
echo "VIN length: ${#VIN}"
 
# Check if VIN is empty
if [ -z "$VIN" ]; then
    echo "ERROR: VIN not found or empty. Check /data/VinNo.txt"
    exit 1
fi
 
# Define the test console path
C2C_TEST_CONSOLE="/data/c2c_test_console"
 
# Start test console and send commands
{
    echo "any2any"
    sleep 1
    echo "vinstub"
    sleep 1
    echo "vinstub $VIN"
	sleep 1
} | $C2C_TEST_CONSOLE