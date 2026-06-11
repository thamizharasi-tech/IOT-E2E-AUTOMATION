@echo off

if %2%==push_tel_files goto push_tel_files
if %2%==paho_trip_start goto paho_trip_start
if %2%==paho_trip_stop goto paho_trip_stop
if %2%==paho_trip_waypoint goto paho_trip_waypoint
if %2%==paho_telemetry_stub_trip goto paho_telemetry_stub_trip
if %2%==paho_telemetry_stubLoop goto paho_telemetry_stubLoop
if %2%==paho_telemetry_stub goto paho_telemetry_stub
if %2%==paho_telemetry_stubtel goto paho_telemetry_stubtel
if %2%==paho_telemetry_stub1 goto paho_telemetry_stub1


:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path=/mnt/vendor/persist/data/c2c/

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PAHO COMMANDS ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

:paho_telemetry_stubLoop
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stubLoop.sh /data/ 
adb -s %1 shell dos2unix /data/telemetry_stubLoop.sh
adb -s %1 shell sh /data/telemetry_stubLoop.sh

goto Exit

:paho_telemetry_stub_trip
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stub_trip.sh /data/ 
adb -s %1 shell dos2unix /data/telemetry_stub_trip.sh
adb -s %1 shell sh /data/telemetry_stub_trip.sh

goto Exit

:paho_trip_waypoint
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stub_trip_waypoint.sh /data/ 
adb -s %1 shell dos2unix /data/telemetry_stub_trip_waypoint.sh
adb -s %1 shell sh /data/telemetry_stub_trip_waypoint.sh

goto Exit

:push_tel_files
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so

goto Exit


:paho_trip_start
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell killall trip_start.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\trip_start.sh /data/
adb -s %1 shell dos2unix /data/trip_start.sh
adb -s %1 shell chmod +x /data/trip_start.sh
adb -s %1 shell sh /data/trip_start.sh

goto Exit

:paho_trip_stop
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell killall trip_stop.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\trip_stop.sh /data/
adb -s %1 shell dos2unix /data/trip_stop.sh
adb -s %1 shell chmod +x /data/trip_stop.sh
adb -s %1 shell sh /data/trip_stop.sh

goto Exit

:paho_telemetry_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell telemetry_stub.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stub.sh /data/ 
adb -s %1 shell dos2unix /data/telemetry_stub.sh
adb -s %1 shell sh /data/telemetry_stub.sh

goto Exit

:paho_telemetry_stubtel
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell telemetry_stubtel.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stubtel.sh /data/ 
adb -s %1 shell dos2unix /data/telemetry_stubtel.sh
adb -s %1 shell sh /data/telemetry_stubtel.sh

goto Exit

:paho_telemetry_stub1
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell killall paho_telemetry_stub.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\paho_telemetry_stub.sh /data/ 
adb -s %1 shell dos2unix /data/paho_telemetry_stub.sh
adb -s %1 shell sh /data/paho_telemetry_stub.sh

goto Exit


:paho_trip
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libmosquitto.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell chmod 777 /data/libmosquitto.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3c.so
adb -s %1 shell chmod 777 /data/libpaho-mqtt3cs.so
adb -s %1 shell killall trip_start.sh
adb -s %1 shell logcat -c
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\trip_start.sh /data/paho_files/
adb -s %1 shell dos2unix /data/paho_files/trip_start.sh
adb -s %1 shell sh /data/paho_files/trip_start.sh

goto Exit

:Exit


