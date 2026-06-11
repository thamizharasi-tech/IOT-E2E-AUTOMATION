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
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.1,"Latitude":28.608861,"Longitude":77.2302,"CoarseOverGround":92.0,"Speed":32,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE