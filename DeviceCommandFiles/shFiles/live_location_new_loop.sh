#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
#echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"

# Define the path to the c2c_test_console
C2C_TEST_CONSOLE="/data/c2c_test_console"

# Function to send location data to c2c_test_console
send_location() {
    local latitude=$1
    local longitude=$2
    local altitude=$3
    local bearing=$4
    local speed=$5
    local horizontalAccuracy=$6
    local verticalAccuracy=$7

    echo "csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {\"altitude\":$altitude,\"latitude\":$latitude,\"longitude\":$longitude,\"bearing\":$bearing,\"speed\":$speed,\"horizontalAccuracy\":$horizontalAccuracy,\"verticalAccuracy\":$verticalAccuracy,\"speedAccuracy\":7.9,\"bearingAccuracy\":9.4} 0"
}

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

    while true; do
        # Update these values to simulate live location tracking
        latitude=28.608861
        longitude=77.2302
        altitude=92.001
        bearing=214.1
        speed=0.0
        horizontalAccuracy=92.0
        verticalAccuracy=0.0

        send_location $latitude $longitude $altitude $bearing $speed $horizontalAccuracy $verticalAccuracy
        sleep 10

        # Update the values for the next location
        latitude=28.608862
        longitude=77.2303
        bearing=214.2
        speed=10.0
        horizontalAccuracy=92.1
        verticalAccuracy=10.0

        send_location $latitude $longitude $altitude $bearing $speed $horizontalAccuracy $verticalAccuracy
        sleep 10

        # Add more updates as needed
    done

    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE