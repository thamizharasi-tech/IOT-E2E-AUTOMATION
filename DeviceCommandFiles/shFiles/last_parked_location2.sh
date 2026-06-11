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
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"RMCTimestamp":1745564145527,"GPSFix":1,"Date":250425,"Time":65546,"Latitude":28.60886667,"LattitudeDirection":"N","Longitude":77.2302,"LongitudeDirection":"E","Speed":123,"CoarseOverGround":92.9,"GGATimestamp":1745564145527,"SatellitesUsed":12,"HDOP":58.001,"Altitude":214.1,"AltitudeUnit":"M","GSATimestamp":1745564145527,"PDOP":58.001,"GpsStatus":false,"SimOperatorName":"airtel","EpochTime":1745564146291,"CarrierBand":"4G","RSSIDbm":"-78","UploadSpeed":"15000kbps","DownloadSpeed":"30000kbps","SNRValues":[{"Satellite-11":46}]} 0'
    sleep 5
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE

#Ignition off
LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m  "[{\"id\": 557875295,\"area\": 0,\"value\": 3}]"
sleep 1