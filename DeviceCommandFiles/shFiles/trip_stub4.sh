#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64

C2C_TEST_CONSOLE="/data/c2c_test_console"

send_location(){ 
{
    echo "any2any"
    sleep 1
    echo "cit 0"
    sleep 1
    echo "creg C2C_INFO_PLATFORM 0"
    sleep 1
    echo "cap C2C_SSIL_APP 0"
    sleep 1
	echo "csend C2C_INFO_PLATFORM C2C_SSIL_APP  $1 0"
    sleep 1
    echo "quit"
    sleep 1
    echo ""
} | $C2C_TEST_CONSOLE
}

publish_vehicle_data() {
    LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "$1"
}


#odo meter value[ new odo propertyId]
publish_vehicle_data '[{"id": 559972924,"area": 0,"value": 6000}]'
sleep 1

#location data
send_location '{"Altitude":214.1,"Latitude":28.60906030812995,"Longitude":77.22966241433508,"CoarseOverGround":92.9,"Speed":0}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 400}]'
sleep 1


#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 75}]'
sleep 1

#Ignition [trip start]
publish_vehicle_data '[{"id": 557875729,"area": 0,"value": 1}]'
sleep 1


#odo meter value[ new odo propertyId]
publish_vehicle_data '[{"id": 559972924,"area": 0,"value": 6000.2}]'
sleep 1

#location data
send_location '{"Altitude":214.1,"Latitude":28.609020,"Longitude":77.229864,"CoarseOverGround":92.9,"Speed":5}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 350}]'
sleep 1

#odo meter value[ new odo propertyId]
publish_vehicle_data '[{"id": 559972924,"area": 0,"value": 6000.4}]'
sleep 1

#location data
send_location '{"Altitude":214.1,"Latitude":28.608971160619618,"Longitude":77.229970108259352,"CoarseOverGround":92.9,"Speed":10}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 350}]'
sleep 1

#fuel level
publish_vehicle_data '[{"id": 291504903,"area": 0,"value": 40}]'
sleep 1

#latitiude
send_location '{"Altitude":214.1,"Latitude":28.608905840049882,"Longitude":77.2300109814177,"CoarseOverGround":92.9,"Speed":15}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 300}]'
sleep 1

#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 121}]'
sleep 1

#odo meter value[ new odo propertyId]
publish_vehicle_data '[{"id": 559972924,"area": 0,"value": 6000.6}]'
sleep 1

#location data
send_location '{"Altitude":214.1,"Latitude":28.608851707950823,"Longitude":77.23028425612318,"CoarseOverGround":92.9,"Speed":10}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 400}]'
sleep 1

#odo meter value[ new odo propertyId]
publish_vehicle_data '[{"id": 559972924,"area": 0,"value": 6000.8}]'
sleep 1

#location data
send_location '{Altitude:214.1,"Latitude":28.60884464374415,"Longitude":77.2305182788596,"CoarseOverGround":92.9,"Speed":28}'
sleep 1

#battery level
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 250}]'
sleep 1

#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 0}]'
sleep 1

#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 0}]'
sleep 1

#location data
send_location '{"Altitude":0,"Latitude":28.60896667,"Longitude":77.23081667,"CoarseOverGround":0,"Speed":25}'
sleep 1

#battery levle
publish_vehicle_data '[{"id": 291504905,"area": 0,"value": 200}]'
sleep 1


#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 20}]'
sleep 1


#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 85}]'
sleep 1


#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 120}]'
sleep 1


#ha-new
publish_vehicle_data '[{"id": 557876191,"area": 0,"value": 1}]'
sleep 1

#hb-new
publish_vehicle_data '[{"id": 557876189,"area": 0,"value": 1}]'
sleep 1


#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 55}]'
sleep 1

#speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875288,"area": 0,"value": 0}]'
sleep 1

#max speed value
publish_vehicle_data '[{"id": 557875767,"area": 0,"value": 121}]'
sleep 1

#Average speed [ new propertyId ]	
publish_vehicle_data '[{"id": 557875768,"area": 0,"value": 52.9}]'
sleep 1

#Battery Consumed[ new propertyId]
publish_vehicle_data '[{"id": 559972922,"area": 0,"value": 200.0}]'
sleep 1

#Battery Efficiency[ new propertyId]
publish_vehicle_data '[{"id": 559972921,"area": 0,"value": 1.25}]'
sleep 1

#Trip duration in hrs[ new propertyId]
publish_vehicle_data '[{"id": 557875765,"area": 0,"value": 0]'
sleep 1

#Trip duration in mins[ new propertyId]
publish_vehicle_data '[{"id": 557875766,"area": 0,"value": 0.0375}]'
sleep 1

#Ignition [trip stop]
publish_vehicle_data '[{"id": 557875729,"area": 0,"value": 0}]'
sleep 1