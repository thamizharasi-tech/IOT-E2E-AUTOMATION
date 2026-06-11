#!/bin/sh

counter=0
speed=0
battery_level=0
sos=0
power_state=0
side_stand=0
odo=0

sleep_time=1

ip link set can0 up type can bitrate 50000

## EV type set 
cansend can0 7F1#0A
# start fake location
am broadcast -a android.intent.action.CUSTOM_LOCATION --ez EXTRA_ENABLED "true"


cmd_cansend_speed()
{
  speed=$1
  #speed_can=`echo "obase=16; $speed" | bc`
  speed_can=`printf "%02x" $speed`
  speed_can=`echo "7FC""#""$speed_can"`
  cansend can0 $speed_can
}

cmd_cansend_odometer()
{
  odo=$1
  #speed_can=`echo "obase=16; $speed" | bc`
  speed_can=`printf "%02x" $odo`
  speed_can=`echo "7EC""#""$odo_can"`
  cansend can0 $odo_can
}

cmd_cansend_battery()
{
    battery_level_input=$1
	battery_level=battery_level_input
	range_battery_level_multiple=240
	range_battery_level_div=100
    battery_level=$(( (battery_level_input * range_battery_level_multiple) / (range_battery_level_div)))
    battery_can=`printf "%02x" $battery_level`
    battery_can=`echo "7FB""#""$battery_can"`
    cansend can0 $battery_can
	range_multiple=2
    range_level=$((battery_level_input * range_multiple))
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
}

cmd_cansend_sos()
{
    sos=$1
	#sos_can=`echo "obase=16; $sos" | bc`
	sos_can=`printf "%02x" $sos`
	sos_can=`echo "7FD""#""$sos_can"`
	cansend can0 $sos_can
}

cmd_cansend_ignition()
{
    power_state=$1
	#power_can=`echo "obase=16; $power_state" | bc`
	power_can=`printf "%02x" $power_state`
	power_can=`echo "7E9""#""$power_can"`
	cansend can0 $power_can
}

cmd_cansend_sidestand()
{
    side_stand=$1
	#side_stand_can=`echo "obase=16; $side_stand" | bc`
	side_stand_can=`printf "%02x" $side_stand`
	side_stand_can=`echo "7FE#""$side_stand_can"`
	cansend can0 $side_stand_can
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
	cmd_cansend_odometer 0

	#sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#2	0	0	0	0	80
	#sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#4	1	0	0	0	80
	#sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#5	1	0	0	0	80
	#sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#6	1	0	0	0	80
	#sleep $sleep_time
	#	ignition	sos_status	side_stand	can_speed	b_charge_status
	#7	1	0	0	30	79

	## START OF NEW SCRIPT WITH LOCATION #####

	cmd_cansend_speed 0
	cmd_cansend_battery 50
	cmd_cansend_sidestand 0
	cmd_cansend_odometer 10
	cmd_cansend_ignition 0
	cansend can0 7A9#01DC
	cansend can0 7EC#0000AFFF
	cansend can0 7F4#01
	cansend can0 7EA#30
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 9.333333333333334}]"
	sleep $sleep_time


	# Starting from building
	cmd_cansend_speed 0
	cmd_cansend_battery 90
	cmd_cansend_ignition 1
	cmd_cansend_odometer 11
	cmd_cansend_sidestand 1
	cansend can0 7EC#001010
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 9.333333333333334}]"
	sleep $sleep_time

	# Starting from building
	cmd_cansend_speed 0
	cmd_cansend_battery 90
	cmd_cansend_ignition 1
	cmd_cansend_odometer 11
	cmd_cansend_sidestand 0
	cansend can0 7EC#001010
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 9.333333333333334}]"
	sleep $sleep_time


	cmd_cansend_sidestand 0
	cmd_cansend_speed 5
	cmd_cansend_battery 90
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60886667}, {'id': 559940098, 'area': 0, 'value': 77.2302}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 92.9}, {'id': 559942149, 'area': 0, 'value': 5}]"
	sleep $sleep_time

	cmd_cansend_speed 7
	cmd_cansend_battery 90
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.2305}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 93.6}, {'id': 559942149, 'area': 0, 'value': 10}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 87
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885}, {'id': 559940098, 'area': 0, 'value': 77.23065}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 90.0}, {'id': 559942149, 'area': 0, 'value': 20}]"
	sleep $sleep_time

	cmd_cansend_speed 12
	cmd_cansend_battery 87
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60883333}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 96.5}, {'id': 559942149, 'area': 0, 'value': 25}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 85
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60885555}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 96.5}, {'id': 559942149, 'area': 0, 'value': 30}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 85
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60896667}, {'id': 559940098, 'area': 0, 'value': 77.23081667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 45}]"
	sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 80
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6091}, {'id': 559940098, 'area': 0, 'value': 77.23076667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 341.8}, {'id': 559942149, 'area': 0, 'value': 50}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 80
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60921667}, {'id': 559940098, 'area': 0, 'value': 77.23068333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 327.9}, {'id': 559942149, 'area': 0, 'value': 55}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 80
	cansend can0 7EC#0000EFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60931667}, {'id': 559940098, 'area': 0, 'value': 77.2306}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 60}]"
	sleep $sleep_time

	cmd_cansend_speed 17
	cmd_cansend_battery 75
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60943333}, {'id': 559940098, 'area': 0, 'value': 77.2305}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 323.0}, {'id': 559942149, 'area': 0, 'value': 65}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 70
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60953333}, {'id': 559940098, 'area': 0, 'value': 77.23041667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 323.8}, {'id': 559942149, 'area': 0, 'value': 67}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 65
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60961667}, {'id': 559940098, 'area': 0, 'value': 77.2303}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 309.1}, {'id': 559942149, 'area': 0, 'value': 60}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 60
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60971667}, {'id': 559940098, 'area': 0, 'value': 77.23011667}, {'id': 559940099, 'area': 0, 'value': 215.8}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 50
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':12.974083333, 'longitude':77.718016667, 'altitude':891.5, 'bearing':198, 'velocity':40}"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 40
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60983333}, {'id': 559940098, 'area': 0, 'value': 77.22995}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 40
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.60993333}, {'id': 559940098, 'area': 0, 'value': 77.22978333}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 39
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61003333}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 215.1}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 35
	cmd_cansend_battery 39
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61013333}, {'id': 559940098, 'area': 0, 'value': 77.22945}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 38
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61023333}, {'id': 559940098, 'area': 0, 'value': 77.22928333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 21
	cmd_cansend_battery 38
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61033333}, {'id': 559940098, 'area': 0, 'value': 77.22911667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 37
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61043333}, {'id': 559940098, 'area': 0, 'value': 77.22893333}, {'id': 559940099, 'area': 0, 'value': 213.6}, {'id': 559940100, 'area': 0, 'value': 301.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 37
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.22876667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 36
	cmd_cansend_sidestand 1
	cmd_cansend_ignition 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 36
	cmd_cansend_sos 1
	cmd_cansend_sidestand 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 36
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 36
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 36
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 35
	cmd_cansend_sos 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 35
	cmd_cansend_sidestand 0
	cmd_cansend_ignition 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.2286}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time


	cmd_cansend_speed 5
	cmd_cansend_battery 35
	cmd_cansend_sidestand 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61075}, {'id': 559940098, 'area': 0, 'value': 77.22843333}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 308.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 34
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61085}, {'id': 559940098, 'area': 0, 'value': 77.22826667}, {'id': 559940099, 'area': 0, 'value': 216.7}, {'id': 559940100, 'area': 0, 'value': 304.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 34
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61096667}, {'id': 559940098, 'area': 0, 'value': 77.22811667}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 311.5}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 34
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6111}, {'id': 559940098, 'area': 0, 'value': 77.22798333}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 34
	cansend can0 7F4#00
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61123333}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 318.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 34
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6114}, {'id': 559940098, 'area': 0, 'value': 77.22775}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 332.2}, {'id': 559942149, 'area': 0, 'value': 20.88888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 33
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61156667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 215.2}, {'id': 559940100, 'area': 0, 'value': 336.3}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 33
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61173333}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 345.2}, {'id': 559942149, 'area': 0, 'value': 19.11111111111111}]"
	sleep $sleep_time

	cmd_cansend_speed 28
	cmd_cansend_battery 32
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61191667}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 32
	cmd_cansend_battery 32
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6121}, {'id': 559940098, 'area': 0, 'value': 77.22761667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 35
	cmd_cansend_battery 31
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61228333}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 31
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61245}, {'id': 559940098, 'area': 0, 'value': 77.22763333}, {'id': 559940099, 'area': 0, 'value': 217.2}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 42
	cmd_cansend_battery 30
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61263333}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 45
	cmd_cansend_battery 30
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61281667}, {'id': 559940098, 'area': 0, 'value': 77.22765}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 30
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.613000000000003}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 29
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61316667}, {'id': 559940098, 'area': 0, 'value': 77.22766667}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 0.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 65
	cmd_cansend_battery 29
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61335}, {'id': 559940098, 'area': 0, 'value': 77.22768333}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 72
	cmd_cansend_battery 28
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61353333}, {'id': 559940098, 'area': 0, 'value': 77.2277}, {'id': 559940099, 'area': 0, 'value': 215.5}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 80
	cmd_cansend_battery 28
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61371667}, {'id': 559940098, 'area': 0, 'value': 77.22771667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 120
	cmd_cansend_battery 27
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6139}, {'id': 559940098, 'area': 0, 'value': 77.22773333}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 4.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 121
	cmd_cansend_battery 27
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61406667}, {'id': 559940098, 'area': 0, 'value': 77.22776667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 10.0}, {'id': 559942149, 'area': 0, 'value': 18.75}]"
	sleep $sleep_time

	cmd_cansend_speed 110
	cmd_cansend_battery 26
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61425}, {'id': 559940098, 'area': 0, 'value': 77.2278}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 9.1}, {'id': 559942149, 'area': 0, 'value': 20.583333333333332}]"
	sleep $sleep_time

	cmd_cansend_speed 125
	cmd_cansend_battery 26
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61441667}, {'id': 559940098, 'area': 0, 'value': 77.22785}, {'id': 559940099, 'area': 0, 'value': 214.2}, {'id': 559940100, 'area': 0, 'value': 14.8}, {'id': 559942149, 'area': 0, 'value': 19.11111111111111}]"
	sleep $sleep_time

	cmd_cansend_speed 120
	cmd_cansend_battery 25
	cansend can0 7EC#0000BFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61458333}, {'id': 559940098, 'area': 0, 'value': 77.22793333}, {'id': 559940099, 'area': 0, 'value': 215.0}, {'id': 559940100, 'area': 0, 'value': 23.7}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 100
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61473333}, {'id': 559940098, 'area': 0, 'value': 77.22803333}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 30.3}, {'id': 559942149, 'area': 0, 'value': 19.27777777777778}]"
	sleep $sleep_time

	cmd_cansend_speed 92
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61486667}, {'id': 559940098, 'area': 0, 'value': 77.22818333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 44.6}, {'id': 559942149, 'area': 0, 'value': 20.833333333333332}]"
	sleep $sleep_time

	cmd_cansend_speed 85
	cmd_cansend_battery 24
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61496667}, {'id': 559940098, 'area': 0, 'value': 77.22835}, {'id': 559940099, 'area': 0, 'value': 217.8}, {'id': 559940100, 'area': 0, 'value': 55.6}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 80
	cmd_cansend_battery 24
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61505}, {'id': 559940098, 'area': 0, 'value': 77.22853333}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 75
	cmd_cansend_battery 23
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.22871667}, {'id': 559940099, 'area': 0, 'value': 217.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 70
	cmd_cansend_battery 23
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61521667}, {'id': 559940098, 'area': 0, 'value': 77.2289}, {'id': 559940099, 'area': 0, 'value': 217.7}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 65
	cmd_cansend_battery 22
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6153}, {'id': 559940098, 'area': 0, 'value': 77.22908333}, {'id': 559940099, 'area': 0, 'value': 217.5}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 60
	cmd_cansend_battery 22
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61538333}, {'id': 559940098, 'area': 0, 'value': 77.22926667}, {'id': 559940099, 'area': 0, 'value': 217.3}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 21
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61546667}, {'id': 559940098, 'area': 0, 'value': 77.22943333}, {'id': 559940099, 'area': 0, 'value': 217.2}, {'id': 559940100, 'area': 0, 'value': 60.3}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"
	sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 21
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61555}, {'id': 559940098, 'area': 0, 'value': 77.22961667}, {'id': 559940099, 'area': 0, 'value': 217.1}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 45
	cmd_cansend_battery 20
	cmd_cansend_fuel_level_low 1 # Fuel low when 20
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61563333}, {'id': 559940098, 'area': 0, 'value': 77.2298}, {'id': 559940099, 'area': 0, 'value': 217.0}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 20
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.22998333}, {'id': 559940099, 'area': 0, 'value': 216.9}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 19
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6158}, {'id': 559940098, 'area': 0, 'value': 77.23016667}, {'id': 559940099, 'area': 0, 'value': 216.8}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 19
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61588333}, {'id': 559940098, 'area': 0, 'value': 77.23035}, {'id': 559940099, 'area': 0, 'value': 216.6}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 19
	cmd_cansend_sidestand 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61596667}, {'id': 559940098, 'area': 0, 'value': 77.23053333}, {'id': 559940099, 'area': 0, 'value': 216.4}, {'id': 559940100, 'area': 0, 'value': 62.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 18
	cmd_cansend_sidestand 1
	cmd_cansend_ignition 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 25
	cmd_cansend_fuel_level_low 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23071667}, {'id': 559940099, 'area': 0, 'value': 216.2}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_sidestand 0
	cmd_cansend_ignition 1
	cmd_cansend_speed 5
	cmd_cansend_battery 25
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6161}, {'id': 559940098, 'area': 0, 'value': 77.23091667}, {'id': 559940099, 'area': 0, 'value': 215.9}, {'id': 559940100, 'area': 0, 'value': 69.2}, {'id': 559942149, 'area': 0, 'value': 20.916666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 50
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61616667}, {'id': 559940098, 'area': 0, 'value': 77.2311}, {'id': 559940099, 'area': 0, 'value': 215.7}, {'id': 559940100, 'area': 0, 'value': 67.5}, {'id': 559942149, 'area': 0, 'value': 19.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 75
	cansend can0 7EA#42
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23131667}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 85.0}, {'id': 559942149, 'area': 0, 'value': 21.277777777777775}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 90
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61618333}, {'id': 559940098, 'area': 0, 'value': 77.23151667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 90.0}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 100
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61611667}, {'id': 559940098, 'area': 0, 'value': 77.23171667}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 20.916666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 100
	cansend can0 7EA#65
	cmd_cansend_sidestand 0
	cmd_cansend_ignition 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61603333}, {'id': 559940098, 'area': 0, 'value': 77.23188333}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"
	sleep $sleep_time

	cmd_cansend_speed 10
	cmd_cansend_battery 99
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61593333}, {'id': 559940098, 'area': 0, 'value': 77.23205}, {'id': 559940099, 'area': 0, 'value': 213.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 99
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61581667}, {'id': 559940098, 'area': 0, 'value': 77.23221667}, {'id': 559940099, 'area': 0, 'value': 213.4}, {'id': 559940100, 'area': 0, 'value': 128.6}, {'id': 559942149, 'area': 0, 'value': 20.805555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 20
	cmd_cansend_battery 98
	paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "{'latitude':12.97265, 'longitude':77.721383333, 'altitude':891.5, 'bearing':0, 'velocity':20}"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 98
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61571667}, {'id': 559940098, 'area': 0, 'value': 77.23238333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 97
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6157}, {'id': 559940098, 'area': 0, 'value': 77.23243333}, {'id': 559940099, 'area': 0, 'value': 213.3}, {'id': 559940100, 'area': 0, 'value': 110.8}, {'id': 559942149, 'area': 0, 'value': 5.222222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 70
	cmd_cansend_battery 96
	cansend can0 7EC#0000CFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 4.916666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 75
	cmd_cansend_battery 95
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 78
	cmd_cansend_battery 94
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 80
	cmd_cansend_battery 93
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 81
	cmd_cansend_battery 92
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 82
	cmd_cansend_battery 91
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 84
	cmd_cansend_battery 90
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 85
	cmd_cansend_battery 89
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 90
	cmd_cansend_battery 88
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 83
	cmd_cansend_battery 87
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 78
	cmd_cansend_battery 86
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 68
	cmd_cansend_battery 85
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 60
	cmd_cansend_battery 84
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 53
	cmd_cansend_battery 83
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 82
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 14.666666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 15
	cmd_cansend_battery 81
	cansend can0 7EC#0000DFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61566667}, {'id': 559940098, 'area': 0, 'value': 77.23246667}, {'id': 559940099, 'area': 0, 'value': 213.2}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 4.916666666666666}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 80
	cmd_cansend_ignition 0
	cmd_cansend_sidestand 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61561667}, {'id': 559940098, 'area': 0, 'value': 77.23255}, {'id': 559940099, 'area': 0, 'value': 213.1}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 9.86111111111111}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 80
	cmd_cansend_sos 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61551667}, {'id': 559940098, 'area': 0, 'value': 77.23273333}, {'id': 559940099, 'area': 0, 'value': 212.6}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 80
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61541667}, {'id': 559940098, 'area': 0, 'value': 77.2329}, {'id': 559940099, 'area': 0, 'value': 212.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 80
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61533333}, {'id': 559940098, 'area': 0, 'value': 77.23306667}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 79
	cmd_cansend_sos 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61523333}, {'id': 559940098, 'area': 0, 'value': 77.23325}, {'id': 559940099, 'area': 0, 'value': 212.1}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 79
	cmd_cansend_sidestand 0
	cmd_cansend_ignition 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61513333}, {'id': 559940098, 'area': 0, 'value': 77.23341667}, {'id': 559940099, 'area': 0, 'value': 212.8}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_ignition 1
	cmd_cansend_sidestand 0
	cmd_cansend_speed 13
	cmd_cansend_battery 78
	cansend can0 7EC#0000EFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61503333}, {'id': 559940098, 'area': 0, 'value': 77.2336}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 28
	cmd_cansend_battery 77
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61495}, {'id': 559940098, 'area': 0, 'value': 77.23376667}, {'id': 559940099, 'area': 0, 'value': 215.4}, {'id': 559940100, 'area': 0, 'value': 119.7}, {'id': 559942149, 'area': 0, 'value': 18.722222222222225}]"
	sleep $sleep_time

	cmd_cansend_speed 40
	cmd_cansend_battery 76
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61485}, {'id': 559940098, 'area': 0, 'value': 77.23395}, {'id': 559940099, 'area': 0, 'value': 216.0}, {'id': 559940100, 'area': 0, 'value': 121.9}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"
	sleep $sleep_time

	cmd_cansend_speed 53
	cmd_cansend_battery 75
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61475}, {'id': 559940098, 'area': 0, 'value': 77.23411667}, {'id': 559940099, 'area': 0, 'value': 216.3}, {'id': 559940100, 'area': 0, 'value': 124.4}, {'id': 559942149, 'area': 0, 'value': 19.72222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 64
	cmd_cansend_battery 74
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61461667}, {'id': 559940098, 'area': 0, 'value': 77.23425}, {'id': 559940099, 'area': 0, 'value': 215.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 77
	cmd_cansend_battery 73
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61448333}, {'id': 559940098, 'area': 0, 'value': 77.23438333}, {'id': 559940099, 'area': 0, 'value': 214.9}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 90
	cmd_cansend_battery 72
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61435}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 138.7}, {'id': 559942149, 'area': 0, 'value': 19.694444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 92
	cmd_cansend_battery 71
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61418333}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 156.3}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 81
	cmd_cansend_battery 70
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61401667}, {'id': 559940098, 'area': 0, 'value': 77.23466667}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 160.7}, {'id': 559942149, 'area': 0, 'value': 19.583333333333332}]"
	sleep $sleep_time

	cmd_cansend_speed 77
	cmd_cansend_battery 69
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61383333}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 65
	cmd_cansend_battery 68
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61365}, {'id': 559940098, 'area': 0, 'value': 77.23465}, {'id': 559940099, 'area': 0, 'value': 214.8}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 50
	cmd_cansend_battery 67
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61346667}, {'id': 559940098, 'area': 0, 'value': 77.23463333}, {'id': 559940099, 'area': 0, 'value': 214.6}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 66
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6133}, {'id': 559940098, 'area': 0, 'value': 77.23461667}, {'id': 559940099, 'area': 0, 'value': 214.4}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 18.555555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 25
	cmd_cansend_battery 65
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61311667}, {'id': 559940098, 'area': 0, 'value': 77.2346}, {'id': 559940099, 'area': 0, 'value': 214.1}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 21
	cmd_cansend_battery 64
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61293333}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 33
	cmd_cansend_battery 63
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61275}, {'id': 559940098, 'area': 0, 'value': 77.23458333}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 41
	cmd_cansend_battery 62
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61258333}, {'id': 559940098, 'area': 0, 'value': 77.23456667}, {'id': 559940099, 'area': 0, 'value': 214.0}, {'id': 559940100, 'area': 0, 'value': 185.0}, {'id': 559942149, 'area': 0, 'value': 18.555555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 55
	cmd_cansend_battery 61
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6124}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 213.5}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 77
	cmd_cansend_battery 60
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61221667}, {'id': 559940098, 'area': 0, 'value': 77.23455}, {'id': 559940099, 'area': 0, 'value': 212.5}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 20.305555555555554}]"
	sleep $sleep_time

	cmd_cansend_speed 82
	cmd_cansend_battery 59
	cansend can0 7EC#0000FFFF
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61203333}, {'id': 559940098, 'area': 0, 'value': 77.23453333}, {'id': 559940099, 'area': 0, 'value': 211.4}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 75
	cmd_cansend_battery 58
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61185}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 210.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 62
	cmd_cansend_battery 57
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61168333}, {'id': 559940098, 'area': 0, 'value': 77.23451667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 180.0}, {'id': 559942149, 'area': 0, 'value': 18.47222222222222}]"
	sleep $sleep_time

	cmd_cansend_speed 49
	cmd_cansend_battery 56
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.6115}, {'id': 559940098, 'area': 0, 'value': 77.2345}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 184.6}, {'id': 559942149, 'area': 0, 'value': 20.38888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 30
	cmd_cansend_battery 55
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61131667}, {'id': 559940098, 'area': 0, 'value': 77.23445}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 193.5}, {'id': 559942149, 'area': 0, 'value': 20.88888888888889}]"
	sleep $sleep_time

	cmd_cansend_speed 19
	cmd_cansend_battery 54
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61115}, {'id': 559940098, 'area': 0, 'value': 77.23441667}, {'id': 559940099, 'area': 0, 'value': 209.2}, {'id': 559940100, 'area': 0, 'value': 190.0}, {'id': 559942149, 'area': 0, 'value': 18.75}]"
	sleep $sleep_time

	cmd_cansend_speed 14
	cmd_cansend_battery 53
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61098333}, {'id': 559940098, 'area': 0, 'value': 77.23433333}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 203.7}, {'id': 559942149, 'area': 0, 'value': 20.194444444444446}]"
	sleep $sleep_time

	cmd_cansend_speed 12
	cmd_cansend_battery 52
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61083333}, {'id': 559940098, 'area': 0, 'value': 77.23421667}, {'id': 559940099, 'area': 0, 'value': 209.1}, {'id': 559940100, 'area': 0, 'value': 214.3}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 5
	cmd_cansend_battery 51
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61071667}, {'id': 559940098, 'area': 0, 'value': 77.23406667}, {'id': 559940099, 'area': 0, 'value': 209.3}, {'id': 559940100, 'area': 0, 'value': 228.5}, {'id': 559942149, 'area': 0, 'value': 19.555555555555557}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 50
	cmd_cansend_ignition 0
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61063333}, {'id': 559940098, 'area': 0, 'value': 77.23388333}, {'id': 559940099, 'area': 0, 'value': 209.6}, {'id': 559940100, 'area': 0, 'value': 242.6}, {'id': 559942149, 'area': 0, 'value': 20.166666666666664}]"
	sleep $sleep_time

	cmd_cansend_speed 0
	cmd_cansend_battery 50
	cmd_cansend_sidestand 1
	LD_LIBRARY_PATH=/vendor/lib64/ paho_cs_pub -h localhost -p 1883 -t "VHAL_STUB/RECV/LOCATION" -m  "[{'id': 559940097, 'area': 0, 'value': 28.61053333}, {'id': 559940098, 'area': 0, 'value': 77.2337}, {'id': 559940099, 'area': 0, 'value': 210.1}, {'id': 559940100, 'area': 0, 'value': 238.1}, {'id': 559942149, 'area': 0, 'value': 21.083333333333336}]"

  sleep $sleep_time


done
