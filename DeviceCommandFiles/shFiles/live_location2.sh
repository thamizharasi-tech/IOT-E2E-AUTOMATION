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
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.1,"Latitude":28.608861,"Longitude":77.2302,"CoarseOverGround":92.0,"Speed":0,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
    sleep 30
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.2,"Latitude":28.608862,"Longitude":77.2303,"CoarseOverGround":92.1,"Speed":10,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
    sleep 30
    echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.3,"Latitude":28.608863,"Longitude":77.2304,"CoarseOverGround":92.2,"Speed":20,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
    sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.4,"Latitude":28.608864,"Longitude":77.2305,"CoarseOverGround":92.3,"Speed":30,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.5,"Latitude":28.608865,"Longitude":77.2306,"CoarseOverGround":92.4,"Speed":40,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.6,"Latitude":28.608866,"Longitude":77.2307,"CoarseOverGround":92.5,"Speed":50,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.7,"Latitude":28.608867,"Longitude":77.2308,"CoarseOverGround":92.6,"Speed":60,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.8,"Latitude":28.608868,"Longitude":77.2309,"CoarseOverGround":4.5,"Speed":80,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.9,"Latitude":28.608869,"Longitude":77.2310,"CoarseOverGround":92.7,"Speed":120,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.1,"Latitude":28.608870,"Longitude":77.2311,"CoarseOverGround":92.8,"Speed":90,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.2,"Latitude":28.608871,"Longitude":77.2312,"CoarseOverGround":92.9,"Speed":70,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.2,"Latitude":28.608872,"Longitude":77.2313,"CoarseOverGround":93.0,"Speed":5,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.3,"Latitude":28.608873,"Longitude":77.2314,"CoarseOverGround":93.1,"Speed":15,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.4,"Latitude":28.608874,"Longitude":77.2315,"CoarseOverGround":93.2,"Speed":25,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.5,"Latitude":28.608875,"5Longitude":77.2316,"CoarseOverGround":92.3,"Speed":35,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.6,"Latitude":28.608876,"Longitude":77.2317,"CoarseOverGround":92.4,"Speed":45,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.7,"Latitude":28.608877,"Longitude":77.2318,"CoarseOverGround":92.5,"Speed":55,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.8,"Latitude":28.608878,"8Longitude":77.2319,"CoarseOverGround":92.6,"Speed":65,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.9,"Latitude":28.608879,"Longitude":77.2320,"CoarseOverGround":92.7,"Speed":85,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.0,"Latitude":28.608880,"Longitude":77.2321,"CoarseOverGround":92.8,"Speed":125,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.1,"Latitude":28.608881,"Longitude":77.2322,"CoarseOverGround":92.9,"Speed":95,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.2,"Latitude":28.608882,"Longitude":77.2323,"CoarseOverGround":93.0,"Speed":75,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.3,"Latitude":28.608883,"Longitude":77.2324,"CoarseOverGround":93.1,"Speed":9,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.4,"Latitude":28.608884,"Longitude":77.2325,"CoarseOverGround":93.4,"Speed":11,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.5,"Latitude":28.608885,"Longitude":77.2326,"CoarseOverGround":93.5,"Speed":22,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.6,"Latitude":28.608886,"Longitude":77.2327,"CoarseOverGround":93.6,"Speed":32,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.7,"Latitude":28.608888,"Longitude":77.2328,"CoarseOverGround":93.7,"Speed":42,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.8,"Latitude":28.608889,"Longitude":77.2329,"CoarseOverGround":93.8,"Speed":54,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":216.9,"Latitude":28.608890,"Longitude":77.2330,"CoarseOverGround":93.9,"Speed":64,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.0,"Latitude":28.608891,"Longitude":77.2331,"CoarseOverGround":94.0,"Speed":86,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.1,"Latitude":28.608892,"Longitude":77.2332,"CoarseOverGround":94.1,"Speed":121,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.2,"Latitude":28.608893,"Longitude":77.2333,"CoarseOverGround":94.2,"Speed":91,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.3,"Latitude":28.608894,"Longitude":77.2334,"CoarseOverGround":94.3,"Speed":79,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.4,"Latitude":28.608895,"Longitude":77.2335,"CoarseOverGround":94.4,"Speed":03,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.5,"Latitude":28.608896,"Longitude":77.2336,"CoarseOverGround":94.5,"Speed":13,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.5,"Latitude":28.608897,"Longitude":77.2337,"CoarseOverGround":94.6,"Speed":23,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.6,"Latitude":28.608898,"Longitude":77.2338,"CoarseOverGround":94.7,"Speed":38,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":217.7,"Latitude":28.608899,"Longitude":77.2306,"CoarseOverGround":94.8,"Speed":42,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.6,"Latitude":28.608866,"Longitude":77.2307,"CoarseOverGround":94.9,"Speed":52,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.7,"Latitude":28.608867,"Longitude":77.2308,"CoarseOverGround":92.5,"Speed":66,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.8,"Latitude":28.608868,"Longitude":77.2309,"CoarseOverGround":92.6,"Speed":88,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.9,"Latitude":28.608869,"Longitude":77.2310,"CoarseOverGround":92.7,"Speed":129,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.1,"Latitude":28.608870,"Longitude":77.2311,"CoarseOverGround":92.8,"Speed":96,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":215.2,"Latitude":28.608871,"Longitude":77.2312,"CoarseOverGround":92.9,"Speed":76,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 30
	echo 'csend C2C_INFO_PLATFORM C2C_SSIL_APP {"Altitude":214.7,"Latitude":28.608866,"Longitude":77.2308,"CoarseOverGround":93.0,"Speed":66,"RMCTimestamp":1738842602273,"GPSFix":1,"Date":060225,"Time":115003.00,"LattitudeDirection":"N","LongitudeDirection":"E","GGATimestamp":1738842602273,"SatellitesUsed":12,"HDOP":0.4,"AltitudeUnit":"M","GSATimestamp":1738842602273,"PDOP":0.7,"GpsStatus":"false","SimOperatorName":"airtel","EpochTime":1447594} 0'
	sleep 1
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE