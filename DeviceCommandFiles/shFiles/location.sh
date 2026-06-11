#!/bin/sh

counter=0
speed=0
battery_level=0
sos=0
power_state=0
side_stand=0

sleep_time=1

ip link set can0 up type can bitrate 50000

## EV type set 
cansend can0 7F1#0A
# start fake location
am broadcast -a android.intent.action.CUSTOM_LOCATION --ez EXTRA_ENABLED "true"
## set battery capacity to 240
cansend can0 7EF#0240


cmd_cansend_speed()
{
  speed=$1
  #speed_can=`echo "obase=16; $speed" | bc`
  speed_can=`printf "%02x" $speed`
  speed_can=`echo "7FC""#""$speed_can"`
  cansend can0 $speed_can
}

cmd_cansend_battery()
{
    battery_level_input=$1
	battery_level=battery_level_input
	range_battery_level_multiple=240
	range_battery_level_div=100
    battery_level=$(( (battery_level_input * range_battery_level_multiple) / (range_battery_level_div)))
	#paho battery_level
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504905, 'area': 0, 'value': $battery_level}]"
	battery_can=`printf "%02x" $battery_level`
    battery_can=`echo "7FB""#""$battery_can"`
    cansend can0 $battery_can
	range_multiple=2
    range_level=$((battery_level_input * range_multiple))
	#paho range_level
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 291504904, 'area': 0, 'value': $range_level}]"
    range_can=`printf "%04x" $range_level`
    range_can=`echo "7F5""#""$range_can"`
    cansend can0 $range_can
}

cmd_cansend_fuel_level_low()
{
    fuel_level_low=$1
    fuel_level_low_can=`printf "%02x" $fuel_level_low`
    fuel_level_low_can=`echo "7ED""#""$fuel_level_low_can"`
    cansend can0 $fuel_level_low_can
	#paho fuel_level_low
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 287310853, 'area': 0, 'value': $fuel_level_low_can}]"
}

cmd_cansend_sos()
{
    sos=$1
	#sos_can=`echo "obase=16; $sos" | bc`
	sos_can=`printf "%02x" $sos`
	sos_can=`echo "7FD""#""$sos_can"`
	cansend can0 $sos_can
	#paho sos
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 555749181, 'area': 0, 'value': $sos_can}]"
}

cmd_cansend_ignition()
{
    power_state=$1
	#power_can=`echo "obase=16; $power_state" | bc`
	power_can=`printf "%02x" $power_state`
	power_can=`echo "7E9""#""$power_can"`
	cansend can0 $power_can
	#paho ignition
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 289408009, 'area': 0, 'value': $power_can}]"
}

cmd_cansend_sidestand()
{
    side_stand=$1
	#side_stand_can=`echo "obase=16; $side_stand" | bc`
	side_stand_can=`printf "%02x" $side_stand`
	side_stand_can=`echo "7FE#""$side_stand_can"`
	cansend can0 $side_stand_can
	#paho sidestand
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/VEHICLE" -m "[{'id': 555749179, 'area': 0, 'value': $side_stand_can}]"
}

cmd_cansend_location()
{
    latitude=$1
	longitude=$1
	altitude=$1
	bearing=$1
	velocity=$1
	
	#paho sidestand
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 0.0}]"
}


while true
do

	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#1	0	0	0	0	80
	cmd_cansend_ignition 0
	cmd_cansend_sidestand 1
	cmd_cansend_fuel_level_low 0
	cmd_cansend_battery 50
	cmd_cansend_speed 0
	cmd_cansend_sos 0

	sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#2	0	0	0	0	80
	sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#4	1	0	0	0	80
	sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#5	1	0	0	0	80
	sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#6	1	0	0	0	80
	sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#7	1	0	0	30	79
	
	## START OF CES SCRIPT WITH LOCATION #####
	
	## LAS VEGAS
  
	cmd_cansend_speed 0
	cmd_cansend_battery 50
	cmd_cansend_sidestand 0
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133, 'longitude':-115.160033333, 'altitude':2055.2, 'bearing':289.9, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 50	
	cmd_cansend_ignition 1
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133, 'longitude':-115.160033333, 'altitude':2055.2, 'bearing':289.9, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13305, 'longitude':-115.160133333, 'altitude':2055.3, 'bearing':301.8, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133083333, 'longitude':-115.160233333, 'altitude':2055.5, 'bearing':292.4, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1331, 'longitude':-115.160333333, 'altitude':2055.7, 'bearing':281.7, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133083333, 'longitude':-115.16035, 'altitude':2055.8, 'bearing':218.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133066667, 'longitude':-115.160333333, 'altitude':2055.8, 'bearing':141.1, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133033333, 'longitude':-115.1603, 'altitude':2055.8, 'bearing':141.1, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.160283333, 'altitude':2056.1, 'bearing':172.3, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13285, 'longitude':-115.160283333, 'altitude':2056.2, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132766667, 'longitude':-115.160283333, 'altitude':2056.3, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132666667, 'longitude':-115.160266667, 'altitude':2056.4, 'bearing':172.3, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132583333, 'longitude':-115.160266667, 'altitude':2056.5, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132483333, 'longitude':-115.160266667, 'altitude':2056.6, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1324, 'longitude':-115.160266667, 'altitude':2056.7, 'bearing':180, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.160266667, 'altitude':2056.7, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 49	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160283333, 'altitude':2056.8, 'bearing':218.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160316667, 'altitude':2056.9, 'bearing':270, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160366667, 'altitude':2057.1, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160483333, 'altitude':2057.3, 'bearing':270, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.1607, 'altitude':2057.2, 'bearing':270, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160916667, 'altitude':2057, 'bearing':270, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.16115, 'altitude':2057.6, 'bearing':270, 'velocity':55}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.161366667, 'altitude':2058.3, 'bearing':270, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 48	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.161583333, 'altitude':2058.7, 'bearing':270, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 47	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.161816667, 'altitude':2058.3, 'bearing':270, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 35
	cmd_cansend_battery 47	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.162033333, 'altitude':2061, 'bearing':270, 'velocity':35}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 47	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.16215, 'altitude':2061.2, 'bearing':270, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 47	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.16225, 'altitude':2060.6, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 47	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162316667, 'altitude':2060.1, 'bearing':287.2, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 46	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.16235, 'altitude':2059.9, 'bearing':270, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46
	cmd_cansend_sidestand 1	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46
	cmd_cansend_sos 1	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46
	cmd_cansend_sos 0	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 46
	cmd_cansend_sidestand 0
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162366667, 'altitude':2059.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 45	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.1624, 'altitude':2059.9, 'bearing':270, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 45	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.16245, 'altitude':2060, 'bearing':270, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 45	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.162566667, 'altitude':2060.3, 'bearing':270, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 44	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.1628, 'altitude':2061, 'bearing':270, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 44	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.163016667, 'altitude':2061.6, 'bearing':270, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 43	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.163233333, 'altitude':2062.1, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 43	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13235, 'longitude':-115.163466667, 'altitude':2062.3, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 42	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132383333, 'longitude':-115.163683333, 'altitude':2063.1, 'bearing':280.8, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 42	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1324, 'longitude':-115.1639, 'altitude':2064, 'bearing':275.4, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 41	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132416667, 'longitude':-115.164116667, 'altitude':2064.8, 'bearing':275.4, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 41	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1325, 'longitude':-115.164316667, 'altitude':2065.5, 'bearing':297.3, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 41	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132516667, 'longitude':-115.164433333, 'altitude':2066, 'bearing':280, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 40	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13255, 'longitude':-115.164466667, 'altitude':2066.3, 'bearing':321.1, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 40	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132583333, 'longitude':-115.164516667, 'altitude':2066.5, 'bearing':309.5, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 39	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132616667, 'longitude':-115.164483333, 'altitude':2066.5, 'bearing':38.9, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 39	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1327, 'longitude':-115.164433333, 'altitude':2066.3, 'bearing':25.9, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 38	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132783333, 'longitude':-115.164383333, 'altitude':2066.1, 'bearing':25.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 38	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.164283333, 'altitude':2065.9, 'bearing':28.3, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 37	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1331, 'longitude':-115.164183333, 'altitude':2065.6, 'bearing':25.9, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 37	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13325, 'longitude':-115.164066667, 'altitude':2065.1, 'bearing':32.1, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 36	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133483333, 'longitude':-115.163916667, 'altitude':2065.1, 'bearing':27.4, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 36	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133733333, 'longitude':-115.16375, 'altitude':2064.3, 'bearing':28.3, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 36	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133966667, 'longitude':-115.1636, 'altitude':2064.2, 'bearing':27.4, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 53
	cmd_cansend_battery 35	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1342, 'longitude':-115.16345, 'altitude':2064.3, 'bearing':27.4, 'velocity':53}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 35	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13445, 'longitude':-115.163283333, 'altitude':2063.6, 'bearing':28.3, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 34	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.134683333, 'longitude':-115.163133333, 'altitude':2062.7, 'bearing':27.4, 'velocity':55}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 34	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.134916667, 'longitude':-115.162983333, 'altitude':2062.3, 'bearing':27.4, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 52
	cmd_cansend_battery 33	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135166667, 'longitude':-115.162816667, 'altitude':2062.5, 'bearing':28.3, 'velocity':52}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 32	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1354, 'longitude':-115.162666667, 'altitude':2061.4, 'bearing':27.4, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 32	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135633333, 'longitude':-115.1625, 'altitude':2061.1, 'bearing':30, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 35
	cmd_cansend_battery 31	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135866667, 'longitude':-115.16235, 'altitude':2060.8, 'bearing':27.4, 'velocity':35}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 31	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136116667, 'longitude':-115.1622, 'altitude':2060.1, 'bearing':25.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 31	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1362, 'longitude':-115.16215, 'altitude':2059.7, 'bearing':25.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 30	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136233333, 'longitude':-115.162116667, 'altitude':2059.5, 'bearing':38.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 30	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136266667, 'longitude':-115.162083333, 'altitude':2059.4, 'bearing':38.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 30	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136266667, 'longitude':-115.162016667, 'altitude':2059.3, 'bearing':90, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 29	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136266667, 'longitude':-115.161916667, 'altitude':2059.2, 'bearing':90, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 29	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136266667, 'longitude':-115.161683333, 'altitude':2058.7, 'bearing':90, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 28	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136266667, 'longitude':-115.161466667, 'altitude':2058.3, 'bearing':90, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 28	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13625, 'longitude':-115.161233333, 'altitude':2058, 'bearing':95.1, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 27	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13625, 'longitude':-115.161016667, 'altitude':2057.5, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 27	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13625, 'longitude':-115.1608, 'altitude':2056.8, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 26	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13625, 'longitude':-115.160566667, 'altitude':2056.1, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 26	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136233333, 'longitude':-115.16035, 'altitude':2055.5, 'bearing':95.4, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 25	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136233333, 'longitude':-115.160133333, 'altitude':2055.1, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 25	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136233333, 'longitude':-115.1599, 'altitude':2054.6, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 25	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136233333, 'longitude':-115.159683333, 'altitude':2054.3, 'bearing':90, 'velocity':55}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 24	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136216667, 'longitude':-115.159466667, 'altitude':2054.1, 'bearing':95.4, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 24	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136216667, 'longitude':-115.159233333, 'altitude':2053.8, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 54
	cmd_cansend_battery 23	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136216667, 'longitude':-115.1589, 'altitude':2053.1, 'bearing':90, 'velocity':54}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 23	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1362, 'longitude':-115.158566667, 'altitude':2052.5, 'bearing':93.5, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 22	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1362, 'longitude':-115.158233333, 'altitude':2051.6, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 53
	cmd_cansend_battery 22	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1362, 'longitude':-115.1579, 'altitude':2051.1, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 21	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136183333, 'longitude':-115.157566667, 'altitude':2050.5, 'bearing':93.5, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 21	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136183333, 'longitude':-115.157233333, 'altitude':2050.1, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 20
	cmd_cansend_fuel_level_low 1 # Fuel low when 20	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136183333, 'longitude':-115.1569, 'altitude':2048.5, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 52
	cmd_cansend_battery 20	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136166667, 'longitude':-115.156566667, 'altitude':2047.3, 'bearing':93.5, 'velocity':52}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 19	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136166667, 'longitude':-115.156233333, 'altitude':2046.3, 'bearing':90, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 19	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13615, 'longitude':-115.1559, 'altitude':2045.3, 'bearing':93.5, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 19	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13615, 'longitude':-115.155683333, 'altitude':2044.5, 'bearing':90, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 18	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13615, 'longitude':-115.15545, 'altitude':2043.8, 'bearing':90, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 17	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136133333, 'longitude':-115.155233333, 'altitude':2043, 'bearing':95.4, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 16	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136133333, 'longitude':-115.155116667, 'altitude':2042.5, 'bearing':90, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 15	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136133333, 'longitude':-115.155, 'altitude':2041.9, 'bearing':90, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 14	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136083333, 'longitude':-115.1549, 'altitude':2041.6, 'bearing':121.8, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 13	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.136, 'longitude':-115.1549, 'altitude':2041.8, 'bearing':180, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 12
	cmd_cansend_sidestand 1	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 15	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 20	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_fuel_level_low 0
	cmd_cansend_battery 50	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 90	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 100	
	cmd_cansend_sidestand 0
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13595, 'longitude':-115.1549, 'altitude':2041.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 100	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135866667, 'longitude':-115.1549, 'altitude':2042.2, 'bearing':180, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 100	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135683333, 'longitude':-115.1549, 'altitude':2042.9, 'bearing':180, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 99	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.135416667, 'longitude':-115.1549, 'altitude':2043.4, 'bearing':180, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 99	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13515, 'longitude':-115.1549, 'altitude':2043.5, 'bearing':180, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 98	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.134883333, 'longitude':-115.1549, 'altitude':2043.8, 'bearing':180, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 98	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1346, 'longitude':-115.154916667, 'altitude':2044, 'bearing':182.7, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 97	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.134333333, 'longitude':-115.154916667, 'altitude':2044.4, 'bearing':180, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 45
	cmd_cansend_battery 97	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.134066667, 'longitude':-115.154916667, 'altitude':2044.5, 'bearing':180, 'velocity':45}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 96	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1338, 'longitude':-115.154916667, 'altitude':2044.3, 'bearing':180, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 96	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.133533333, 'longitude':-115.154916667, 'altitude':2044.4, 'bearing':180, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 95	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13325, 'longitude':-115.154916667, 'altitude':2044.2, 'bearing':180, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 95	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132983333, 'longitude':-115.154916667, 'altitude':2044, 'bearing':180, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 94
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132716667, 'longitude':-115.154916667, 'altitude':2043.9, 'bearing':180, 'velocity':0}"
    cmd_cansend_sidestand 1		
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 94
	cmd_cansend_sos 1	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132716667, 'longitude':-115.154916667, 'altitude':2043.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 94	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132716667, 'longitude':-115.154916667, 'altitude':2043.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 94
	cmd_cansend_sos 0
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132716667, 'longitude':-115.154916667, 'altitude':2043.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 94
	cmd_cansend_sidestand 0		
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132716667, 'longitude':-115.154916667, 'altitude':2043.9, 'bearing':180, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 94	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132533333, 'longitude':-115.154933333, 'altitude':2043.7, 'bearing':184.2, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 93	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132366667, 'longitude':-115.154933333, 'altitude':2043.4, 'bearing':180, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 93	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.154933333, 'altitude':2043.4, 'bearing':180, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 93	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.154983333, 'altitude':2043.4, 'bearing':230.5, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 92	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.155033333, 'altitude':2043.3, 'bearing':270, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 92	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.155083333, 'altitude':2043.2, 'bearing':270, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 90	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.1552, 'altitude':2043.1, 'bearing':270, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 89	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.155416667, 'altitude':2043, 'bearing':270, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 88	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132283333, 'longitude':-115.15575, 'altitude':2043.5, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 35
	cmd_cansend_battery 87	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.156083333, 'altitude':2044.2, 'bearing':273.5, 'velocity':35}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 86	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.156416667, 'altitude':2044.7, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 34
	cmd_cansend_battery 85	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.15675, 'altitude':2045.5, 'bearing':270, 'velocity':34}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 84	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.1571, 'altitude':2046.5, 'bearing':270, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 83	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.157433333, 'altitude':2047, 'bearing':270, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 45
	cmd_cansend_battery 82	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.157766667, 'altitude':2047.3, 'bearing':270, 'velocity':45}"
    sleep $sleep_time

	cmd_cansend_speed 48
	cmd_cansend_battery 81	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1323, 'longitude':-115.1581, 'altitude':2047.8, 'bearing':270, 'velocity':48}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 80	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.158433333, 'altitude':2048.5, 'bearing':273.5, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 52
	cmd_cansend_battery 79	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.158766667, 'altitude':2049.7, 'bearing':270, 'velocity':52}"
    sleep $sleep_time

	cmd_cansend_speed 53
	cmd_cansend_battery 78	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.1591, 'altitude':2051.1, 'bearing':270, 'velocity':53}"
    sleep $sleep_time

	cmd_cansend_speed 60
	cmd_cansend_battery 77	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.159433333, 'altitude':2052.7, 'bearing':270, 'velocity':60}"
    sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 76	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.159766667, 'altitude':2054.3, 'bearing':270, 'velocity':55}"
    sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 75	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.159983333, 'altitude':2055.4, 'bearing':270, 'velocity':50}"
    sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 74	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132316667, 'longitude':-115.160216667, 'altitude':2056.6, 'bearing':270, 'velocity':40}"
    sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 73	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132333333, 'longitude':-115.160266667, 'altitude':2056.8, 'bearing':292.4, 'velocity':30}"
    sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 72	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132383333, 'longitude':-115.16025, 'altitude':2056.7, 'bearing':15.1, 'velocity':25}"
    sleep $sleep_time

	cmd_cansend_speed 23
	cmd_cansend_battery 71	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132466667, 'longitude':-115.16025, 'altitude':2056.6, 'bearing':0, 'velocity':23}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 70	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132516667, 'longitude':-115.16025, 'altitude':2056.5, 'bearing':0, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 69	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13255, 'longitude':-115.160216667, 'altitude':2056.4, 'bearing':38.9, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 68	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132583333, 'longitude':-115.160116667, 'altitude':2056.1, 'bearing':67.6, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 67	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.13265, 'longitude':-115.1599, 'altitude':2055.5, 'bearing':69.1, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 66	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1327, 'longitude':-115.15975, 'altitude':2055.4, 'bearing':67.6, 'velocity':15}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 65	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132833333, 'longitude':-115.1597, 'altitude':2055.4, 'bearing':16.9, 'velocity':20}"
    sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 64	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.1329, 'longitude':-115.159766667, 'altitude':2055.1, 'bearing':321.1, 'velocity':20}"
	
    sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 63	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132916667, 'longitude':-115.159816667, 'altitude':2054.9, 'bearing':292.4, 'velocity':10}"
    sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 62	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.15985, 'altitude':2054.8, 'bearing':301.8, 'velocity':5}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 62	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.159866667, 'altitude':2054.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 62
	cmd_cansend_sidestand 1
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.159866667, 'altitude':2054.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 62
	cmd_cansend_ignition 0	
	paho_c_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':36.132933333, 'longitude':-115.159866667, 'altitude':2054.8, 'bearing':270, 'velocity':0}"
    sleep $sleep_time
    
done
