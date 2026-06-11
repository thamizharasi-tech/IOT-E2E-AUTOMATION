@echo off

if %2%==telemetry_location goto telemetry_location

if %2%==telemetry_can_odo goto telemetry_can_odo
if %2%==telemetry_can_speed goto telemetry_can_speed
if %2%==telemetry_can_fuel goto telemetry_can_fuel
if %2%==telemetry_can_battery_level goto telemetry_can_battery_level
if %2%==telemetry_can_range_remaining goto telemetry_can_range_remaining
if %2%==trip_start goto trip_start
if %2%==trip_stop goto trip_stop
if %2%==location_geofence goto location_geofence
if %2%==telemetry_b2c_stub goto telemetry_b2c_stub
if %2%==trip_summary_stub goto trip_summary_stub
if %2%==trip_summary_log goto trip_summary_log
if %2%==switch_to_stub goto switch_to_stub
if %2%==switch_to_orig goto switch_to_orig
if %2%==telemetry_accelerometer_data goto telemetry_accelerometer_data
if %2%==telemetry_gyro_data goto telemetry_gyro_data

if %2%==commandControl_precondition1 goto commandControl_precondition1
if %2%==commandControl_precondition2 goto commandControl_precondition2
if %2%==commandControl_precondition3 goto commandControl_precondition3

if %2%==chargingNotification_can_charge_port_connected goto chargingNotification_can_charge_port_connected
if %2%==chargingNotification_can_charge_port_connected_and_isCharging goto chargingNotification_can_charge_port_connected_and_isCharging
if %2%==chargingNotification_can_charge_port_disconnected goto chargingNotification_can_charge_port_disconnected
if %2%==chargingNotification_can_charge_port_connected_and_notCharging goto chargingNotification_can_charge_port_connected_and_notCharging
if %2%==chargingNotification_can_charge_port_open goto chargingNotification_can_charge_port_open
if %2%==chargingNotification_can_charge_port_close goto chargingNotification_can_charge_port_close

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** CAN COMMANDS ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

:telemetry_location
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
::adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
::adb -s %1 pull /vendor/bin/dm dm-orig
adb -s %1 push %3\paho_files\libssil_stub.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell mkdir /data/scripts
adb -s %1 push %3\shFiles\location_delhi.sh /data/scripts/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb -s %1 shell sh /data/scripts/location_delhi.sh

goto Exit

:telemetry_can_odo

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
::adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7EC#0000FFFF
adb -s %1 shell cansend can0 7EC#0000FFFF  :: Odo = 65535 km

goto Exit

:telemetry_can_speed

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
::adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
::adb -s %1 pull /vendor/bin/dm dm-orig
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7FC#20
adb -s %1 shell cansend can0 7FC#20  :: speed = 32.000000

goto Exit

:telemetry_can_fuel

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7EE#20
adb -s %1 shell cansend can0 7EE#20  :: Fuel = 8192 ml

goto Exit

:telemetry_can_battery_level

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7FB#80
adb -s %1 shell cansend can0 7FB#80  :: EV_Battery_Level = 128 wh

goto Exit

:chargingNotification_can_charge_port_connected

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AC#01
adb -s %1 shell cansend can0 7AC#01 :: Charge Port Connected - ev_charge_port_connected:1

goto Exit

:chargingNotification_can_charge_port_connected_and_isCharging

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AD#00EC
adb -s %1 shell cansend can0 7AD#00EC :: Charge Port Connected and is charging - inst_charge_rate:236.000000 MW

goto Exit

:chargingNotification_can_charge_port_disconnected

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AC#00
adb -s %1 shell cansend can0 7AC#00 :: Charge Port Disconnected - ev_charge_port_connected:0

goto Exit

:chargingNotification_can_charge_port_connected_and_notCharging

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AD#0000
adb -s %1 shell cansend can0 7AD#0000 :: Charge Port Connected and is not charging - inst_charge_rate:0.000000

goto Exit

:chargingNotification_can_charge_port_open

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AB#01
adb -s %1 shell cansend can0 7AC#00 :: Charge Port Open - ev_charge_port_open:1

goto Exit

:chargingNotification_can_charge_port_close

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7AB#00
adb -s %1 shell cansend can0 7AC#00 :: Charge Port Close - ev_charge_port_open:0

goto Exit

:telemetry_can_range_remaining

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7F5#02FF
adb -s %1 shell cansend can0 7F5#02FF  :: Rage Remaining = 511 km

goto Exit

:: Ignition OFF or Acc / Immobilize / SOS:
:commandControl_precondition1
echo ---------------------
echo Preconditions:
echo speed should be 0
echo ---------------------

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7FC#00
adb -s %1 shell cansend can0 7FC#00

goto Exit

:: UnLock / Ignition ON:

:commandControl_precondition2
echo Preconditions:
echo - speed should be 0
echo - side stand should be OFF

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb shell cansend can0 7FE#00
adb -s %1 shell cansend can0 7FC#00

goto Exit


:: Lock / Mobilize / Buzz Bike / play sound:

:commandControl_precondition3
echo Preconditions:
echo - speed should be 0
echo - side stand should be ON

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb -s %1 shell cansend can0 7FE#01
adb -s %1 shell cansend can0 7FC#00

goto Exit

:trip_start
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell stop dm_service
adb -s %1 shell start dm_service
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\trip_start.sh /data/
adb -s %1 shell dos2unix /data/trip_start.sh
adb -s %1 shell chmod +x /data/trip_start.sh
adb -s %1 shell sh /data/trip_start.sh
adb -s %1
adb -s %1 shell cansend can0 7FF#04  :: Ignition start


goto Exit

:trip_stop
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\trip_stop.sh /data/
adb -s %1 shell dos2unix /data/trip_stop.sh
adb -s %1 shell chmod +x /data/trip_stop.sh
adb -s %1 shell sh /data/trip_stop.sh
adb -s %1 shell cansend can0 7FF#03  :: Ignition start

goto Exit

:location_geofence
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\libssil_stub.so /vendor/lib64/libssil.so
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell sync
adb -s %1 shell start dm_service
adb -s %1 shell start dm_service
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\location_delhi.sh /data/
adb -s %1 shell dos2unix /data/location_delhi.sh
adb -s %1 shell chmod +x /data/location_delhi.sh
adb -s %1 shell sh /data/location_delhi.sh
goto Exit

:telemetry_b2c_stub
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\telemetry_b2c_stub.sh /data/
adb -s %1 shell dos2unix /data/telemetry_b2c_stub.sh
adb -s %1 shell chmod +x /data/telemetry_b2c_stub.sh
adb -s %1 shell sh /data/telemetry_b2c_stub.sh


:telemetry_accelerometer_data
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\accelerometer_data.sh /data/
adb -s %1 shell dos2unix /data/accelerometer_data.sh
adb -s %1 shell chmod +x /data/accelerometer_data.sh
adb -s %1 shell sh /data/accelerometer_data.sh


:telemetry_gyro_data
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\gyro.sh /data/
adb -s %1 shell dos2unix /data/gyro.sh
adb -s %1 shell chmod +x /data/gyro.sh
adb -s %1 shell sh /data/gyro.sh


:telemetry_b2c_stub
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\telemetry_b2c_stub.sh /data/
adb -s %1 shell dos2unix /data/telemetry_b2c_stub.sh
adb -s %1 shell chmod +x /data/telemetry_b2c_stub.sh
adb -s %1 shell sh /data/telemetry_b2c_stub.sh

goto Exit

:trip_summary_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 shell rm /data/ivi_c2clogs.txt
adb -s %1 shell sync
adb -s %1 shell start dm_service
adb -s %1 shell start dm_service
adb -s %1 push C:\Users\suttarak\PycharmProjects\Car2CloudE2ETesting2\DeviceCommandFiles\shFiles\b2c_telemetry_stub_trip.sh /data/
adb -s %1 shell dos2unix /data/b2c_telemetry_stub_trip.sh
adb -s %1 shell chmod +x /data/b2c_telemetry_stub_trip.sh
adb -s %1 shell sh /data/b2c_telemetry_stub_trip.sh
goto Exit

:trip_summary_log:
adb -s %1 pull /data/ivi_c2clogs.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs
adb -s %1 shell logcat [C2CLOGGER] -t 10000 > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\log.txt

:switch_to_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 push %3\paho_files\libssil_stub.so /vendor/lib64/libssil.so
adb -s %1 shell dos2unix /vendor/lib64/libssil_stub.so
adb -s %1 shell chmod+x /vendor/lib64/libssil_stub.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell sync
adb -s %1 shell start dm_service

goto Exit

:switch_to_orig
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
adb -s %1 shell dos2unix /vendor/lib64/libssil_orig.so
adb -s %1 shell chmod+x /vendor/lib64/libssil_orig.so
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell sync
adb -s %1 shell reboot


:Exit
