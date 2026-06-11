#!/bin/sh

helpFunction()
{
   echo ""
   echo "Usage: statistics script - used for monitor health of c2c components"
   echo "Use with the following switch/flag"
   echo " -d  Time interval between two read: Example: -d 1 - (DEFAULT=1)"
   echo " -f  Name of the .csv file : Example: -f c2c.csv (DEFAULT=c2c.csv)"
   exit 1 # Exit script after printing help
}

delaytime=2;
filename="c2c.csv"

while getopts "p:d:f:" opt
do
	case "$opt" in
   		d ) delaytime="$OPTARG" ;;
    	f ) filename="$OPTARG" ;;
		? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$delaytime" ]
then
   echo "Inputs needed, Please refer help";
   helpFunction
fi

if pgrep -x "dm" > /dev/null
then
	echo "dm is running"
else
    echo "dm is not running"
    echo -n "Do you want to Continue (y/n)? "
	read answer
	if [ "$answer" != "${answer#[Yy]}" ] ;then 
    	echo "continue without dm"
	else
    	echo "Exit"
    	exit 1
	fi
fi

if pgrep -x "cm_manager" > /dev/null
then
	echo "cm_manager is running"
else
    echo "cm_manager is not running"
    echo -n "Do you want to Continue (y/n)? "
	read answer
	if [ "$answer" != "${answer#[Yy]}" ] ;then 
    	echo "continue without cm_manager"
	else
    	echo "Exit"
    	exit 1
	fi
fi

if pgrep -x "ota_manager" > /dev/null
then
	echo "ota_manager is running"
else
    echo "ota_manager is not running"
    echo -n "Do you want to Continue (y/n)? "
	read answer
	if [ "$answer" != "${answer#[Yy]}" ] ;then 
    	echo "continue without ota_manager"
	else
    	echo "Exit"
    	exit 1
	fi
fi

if pgrep -x "c2c_rule_engine" > /dev/null
then
	echo "c2c_rule_engine is running"
else
    echo "c2c_rule_engine is not running"
    echo -n "Do you want to Continue (y/n)? "
	read answer
	if [ "$answer" != "${answer#[Yy]}" ] ;then 
    	echo "continue without c2c_rule_engine"
	else
    	echo "Exit"
    	exit 1
	fi
fi

if pgrep -x "c2c_hub" > /dev/null
then
	echo "c2c_hub is running"
else
    echo "c2c_hub is not running"    
fi



echo "TIME, HUB_PID, HUB_CPU, HUB_MEM, HUB_ARGS, DM_PID, DM_CPU, DM_MEM, DM_ARGS, CM_PID, CM_CPU, CM_MEM, CM_ARGS,OM_PID, OM_CPU, OM_MEM, OM_ARGS,CRE_PID, CRE_CPU, CRE_MEM, CRE_ARGS"  >> $filename

echo "Hit [CTRL+C] to stop!"
	
while [ 1 ]
do
	
	if pgrep -x "c2c_hub" > /dev/null
	then
		HUB_VAL=$(top -b -n 2 -d 0.5 -p $(pgrep -d',' -f c2c_hub) | tail -1)
		DM_VAL=$(top -b -n 2 -d 0.5 -p $(pgrep -d',' -x dm) | tail -1)
		CM_VAL=$(top -b -n 2 -d 0.5 -p $(pgrep -d',' -f cm_manager) | tail -1)
		OM_VAL=$(top -b -n 2 -d 0.5 -p $(pgrep -d',' -f ota_manager) | tail -1)
		CRE_VAL=$(top -b -n 2 -d 0.5 -p $(pgrep -d',' -f c2c_rule_engine) | tail -1)
		
		HUB_PID=$(echo $HUB_VAL | awk '{print $1}')
		HUB_CPU=$(echo $HUB_VAL | awk '{print $9}')
		HUB_MEM=$(echo $HUB_VAL | awk '{print $10}')
		HUB_ARGS=$(echo $HUB_VAL | awk '{print $12}')
		
		DM_PID=$(echo $DM_VAL | awk '{print $1}')
		DM_CPU=$(echo $DM_VAL | awk '{print $9}')
		DM_MEM=$(echo $DM_VAL | awk '{print $10}')
		DM_ARGS=$(echo $DM_VAL | awk '{print $12}')	
		
		CM_PID=$(echo $CM_VAL | awk '{print $1}')
		CM_CPU=$(echo $CM_VAL | awk '{print $9}')
		CM_MEM=$(echo $CM_VAL | awk '{print $10}')
		CM_ARGS=$(echo $CM_VAL | awk '{print $12}')
		
		OM_PID=$(echo $OM_VAL | awk '{print $1}')
		OM_CPU=$(echo $OM_VAL | awk '{print $9}')
		OM_MEM=$(echo $OM_VAL | awk '{print $10}')
		OM_ARGS=$(echo $OM_VAL | awk '{print $12}')
		
		CRE_PID=$(echo $CRE_VAL | awk '{print $1}')
		CRE_CPU=$(echo $CRE_VAL | awk '{print $9}')
		CRE_MEM=$(echo $CRE_VAL | awk '{print $10}')
		CRE_ARGS=$(echo $CRE_VAL | awk '{print $12}')
		
		
	else		
		HUB_PID=DM_PID=CM_PID=OM_PID=CRE_PID="NOT_RUNNING"
		HUB_CPU=HUB_MEM=HUB_ARGS=DM_CPU=DM_MEM=DM_ARGS=CM_CPU=CM_MEM=CM_ARGS=OM_CPU=OM_MEM=OM_ARGS=CRE_CPU=CRE_MEM=CRE_ARGS=""
	fi

	TIME=$(date +"%d-%m-%y-%T")

 	echo "$TIME, $HUB_PID, $HUB_CPU, $HUB_MEM, $HUB_ARGS, $DM_PID, $DM_CPU, $DM_MEM, $DM_ARGS, $CM_PID, $CM_CPU, $CM_MEM, $CM_ARGS,$OM_PID, $OM_CPU, $OM_MEM, $OM_ARGS,$CRE_PID, $CRE_CPU, $CRE_MEM, $CRE_ARGS"  >> $filename
 	
	sleep $delaytime
done



