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
    echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.1,"latitude":28.608861,"longitude":77.2302,"bearing":92.0,"speed":0,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
    sleep 30
    echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.2,"latitude":28.608862,"longitude":77.2303,"bearing":92.1,"speed":10,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
    sleep 30
    echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.3,"latitude":28.608863,"longitude":77.2304,"bearing":92.2,"speed":20,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
    sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.4,"latitude":28.608864,"longitude":77.2305,"bearing":92.3,"speed":30,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.5,"latitude":28.608865,"longitude":77.2306,"bearing":92.4,"speed":40,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.6,"latitude":28.608866,"longitude":77.2307,"bearing":92.5,"speed":50,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.7,"latitude":28.608867,"longitude":77.2308,"bearing":92.6,"speed":60,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.8,"latitude":28.608868,"longitude":77.2309,"bearing":4.5,"speed":80,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.9,"latitude":28.608869,"longitude":77.2310,"bearing":92.7,"speed":120,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.1,"latitude":28.608870,"longitude":77.2311,"bearing":92.8,"speed":90,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.2,"latitude":28.608871,"longitude":77.2312,"bearing":92.9,"speed":70,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.2,"latitude":28.608872,"longitude":77.2313,"bearing":93.0,"speed":5,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.3,"latitude":28.608873,"longitude":77.2314,"bearing":93.1,"speed":15,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.4,"latitude":28.608874,"longitude":77.2315,"bearing":93.2,"speed":25,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.5,"latitude":28.608875,"5longitude":77.2316,"bearing":92.3,"speed":35,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.6,"latitude":28.608876,"longitude":77.2317,"bearing":92.4,"speed":45,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.7,"latitude":28.608877,"longitude":77.2318,"bearing":92.5,"speed":55,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.8,"latitude":28.608878,"8longitude":77.2319,"bearing":92.6,"speed":65,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.9,"latitude":28.608879,"longitude":77.2320,"bearing":92.7,"speed":85,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.0,"latitude":28.608880,"longitude":77.2321,"bearing":92.8,"speed":125,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.1,"latitude":28.608881,"longitude":77.2322,"bearing":92.9,"speed":95,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.2,"latitude":28.608882,"longitude":77.2323,"bearing":93.0,"speed":75,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.3,"latitude":28.608883,"longitude":77.2324,"bearing":93.1,"speed":9,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.4,"latitude":28.608884,"longitude":77.2325,"bearing":93.4,"speed":11,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.5,"latitude":28.608885,"longitude":77.2326,"bearing":93.5,"speed":22,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.6,"latitude":28.608886,"longitude":77.2327,"bearing":93.6,"speed":32,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.7,"latitude":28.608888,"longitude":77.2328,"bearing":93.7,"speed":42,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.8,"latitude":28.608889,"longitude":77.2329,"bearing":93.8,"speed":54,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":216.9,"latitude":28.608890,"longitude":77.2330,"bearing":93.9,"speed":64,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.0,"latitude":28.608891,"longitude":77.2331,"bearing":94.0,"speed":86,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.1,"latitude":28.608892,"longitude":77.2332,"bearing":94.1,"speed":121,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.2,"latitude":28.608893,"longitude":77.2333,"bearing":94.2,"speed":91,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.3,"latitude":28.608894,"longitude":77.2334,"bearing":94.3,"speed":79,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.4,"latitude":28.608895,"longitude":77.2335,"bearing":94.4,"speed":03,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.5,"latitude":28.608896,"longitude":77.2336,"bearing":94.5,"speed":13,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.5,"latitude":28.608897,"longitude":77.2337,"bearing":94.6,"speed":23,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.6,"latitude":28.608898,"longitude":77.2338,"bearing":94.7,"speed":38,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":217.7,"latitude":28.608899,"longitude":77.2306,"bearing":94.8,"speed":42,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.6,"latitude":28.608866,"longitude":77.2307,"bearing":94.9,"speed":52,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.7,"latitude":28.608867,"longitude":77.2308,"bearing":92.5,"speed":66,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.8,"latitude":28.608868,"longitude":77.2309,"bearing":92.6,"speed":88,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.9,"latitude":28.608869,"longitude":77.2310,"bearing":92.7,"speed":129,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.1,"latitude":28.608870,"longitude":77.2311,"bearing":92.8,"speed":96,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":215.2,"latitude":28.608871,"longitude":77.2312,"bearing":92.9,"speed":76,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 30
	echo 'csend C2C_FETCH_ATTR_APP C2C_SSIL_APP {"altitude":214.7,"latitude":28.608866,"longitude":77.2308,"bearing":93.0,"speed":66,"horizontalAccuracy":1.2,"verticalAccuracy":3.5,"speedAccuracy":7.9,"bearingAccuracy":9.4} 0'
	sleep 1
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE