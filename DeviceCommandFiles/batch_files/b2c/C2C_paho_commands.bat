@echo off

if %2%==telemetry_location goto telemetry_location

if %2%==telemetry_can_odo goto telemetry_can_odo
if %2%==telemetry_can_speed goto telemetry_can_speed
if %2%==telemetry_can_fuel goto telemetry_can_fuel
if %2%==telemetry_can_battery_level goto telemetry_can_battery_level
if %2%==telemetry_can_range_remaining goto telemetry_can_range_remaining
if %2%==telemetry_can_remaining_battery_charge goto remaining_battery_charge
if %2%==telemetry_can_sideStand_ON goto telemetry_can_sideStand_ON
if %2%==telemetry_can_sideStand_OFF goto telemetry_can_sideStand_OFF
if %2%==telemetry_can_front_tire_pressure goto telemetry_can_front_tire_pressure
if %2%==telemetry_can_rear_tire_pressure goto telemetry_can_rear_tire_pressure
if %2%==telemetry_can_headlight_ON goto telemetry_can_headlight_ON
if %2%==telemetry_can_headlight_OFF goto telemetry_can_headlight_OFF
if %2%==telemetry_can_taillight_ON goto telemetry_can_taillight_ON
if %2%==telemetry_can_taillight_OFF goto telemetry_can_taillight_OFF
if %2%==telemetry_can_indicator_0 goto telemetry_can_indicator_0
if %2%==telemetry_can_indicator_1 goto telemetry_can_indicator_1
if %2%==telemetry_can_indicator_2 goto telemetry_can_indicator_2
if %2%==telemetry_can_indicator_3 goto telemetry_can_indicator_3
if %2%==telemetry_can_gear_position_2 goto telemetry_can_gear_position_2
if %2%==telemetry_can_gear_position_4 goto telemetry_can_gear_position_4
if %2%==telemetry_can_gear_position_8 goto telemetry_can_gear_position_8
if %2%==telemetry_can_high_beam_ON goto telemetry_can_high_beam_ON
if %2%==telemetry_can_high_beam_OFF goto telemetry_can_high_beam_OFF
if %2%==telemetry_can_hazard_light_ON goto telemetry_can_hazard_light_ON
if %2%==telemetry_can_hazard_light_OFF goto telemetry_can_hazard_light_OFF
if %2%==telemetry_can_SOS_ON goto telemetry_can_SOS_ON
if %2%==telemetry_can_SOS_OFF goto telemetry_can_SOS_OFF
if %2%==telemetry_can_rpm goto telemetry_can_rpm
if %2%==telemetry_can_ride_mode_normal goto telemetry_can_ride_mode_normal
if %2%==telemetry_can_ride_mode_economy goto telemetry_can_ride_mode_economy
if %2%==telemetry_can_ride_mode_vendorSpecific goto telemetry_can_ride_mode_vendorSpecific
if %2%==telemetry_can_speed_notification goto telemetry_can_speed_notification
if %2%==telemetry_can_normal_battery_temp goto telemetry_can_normal_battery_temp
if %2%==telemetry_can_warning_battery_temp goto telemetry_can_warning_battery_temp
if %2%==telemetry_can_critical_battery_temp goto telemetry_can_critical_battery_temp
if %2%==telemetry_can_mobilize goto telemetry_can_mobilize
if %2%==telemetry_can_immobilize goto telemetry_can_immobilize

if %2%==trip_start goto trip_start
if %2%==trip_start_v3 goto trip_start_v3
if %2%==trip_stop goto trip_stop
if %2%==location_geofence goto location_geofence
if %2%==location_liveTracking goto location_liveTracking
if %2%==telemetry_b2c_stub goto telemetry_b2c_stub
if %2%==trip_summary_stub goto trip_summary_stub
if %2%==trip_summary_stub1 goto trip_summary_stub1
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


if %2%==trip_start goto trip_start
if %2%==trip_stop goto trip_stop
if %2%==location_geofence goto location_geofence
if %2%==switch_to_hybrid_stub goto switch_to_hybrid_stub
if %2%==switch_to_origin goto switch_to_origin
if %2%==switch_to_can_stub goto switch_to_can_stub
if %2%==switch_to_paho_stub goto switch_to_paho_stub



if %2%==ignition_off goto ignition_off
if %2%==ignition_on goto ignition_on
if %2%==live_location goto live_location
if %2%==last_parked_location goto last_parked_location
if %2%==gps_speed goto gps_speed
if %2%==critical_battery goto critical_battery
if %2%==tampering_alert goto tampering_alert
if %2%==towAway_alert goto towAway_alert
if %2%==crash_alert goto crash_alert
if %2%==trip_stub goto trip_stub
if %2%==commandControl_precondition_speedZero goto commandControl_precondition_speedZero
if %2%==ignition_on_alert goto ignition_on_alert
if %2%==batteryHeatCold_alert goto batteryHeatCold_alert
if %2%==geofence_alert goto geofence_alert

if %2%==telemetry_ha goto telemetry_ha
if %2%==telemetry_hb goto telemetry_hb
if %2%==telemetry_overspeed goto telemetry_overspeed
if %2%==telemetry_odo goto telemetry_odo

if %2%==trip_stub_without_stop goto trip_stub_without_stop

if %2%==telemetry_battery_soc goto telemetry_battery_soc
if %2%==telemetry_battery_soh goto telemetry_battery_soh
if %2%==telemetry_battery_soc_exceed_limit goto telemetry_battery_soc_exceed_limit
if %2%==telemetry_battery_soh_exceed_limit goto telemetry_battery_soh_exceed_limit

if %2%==digital_pin_generate goto digital_pin_generate
if %2%==digital_pin_vehicle_unlock_admin goto digital_pin_vehicle_unlock_admin
if %2%==digital_pin_vehicle_unlock_primary goto digital_pin_vehicle_unlock_primary
if %2%==digital_pin_vehicle_unlock_secondary goto digital_pin_vehicle_unlock_secondary
if %2%==digital_pin_expiry_admin goto digital_pin_expiry_admin
if %2%==digital_pin_expiry_primary goto digital_pin_expiry_primary
if %2%==digital_pin_expiry_secondary goto digital_pin_expiry_secondary
if %2%==geofence_alert1 goto geofence_alert1
if %2%==towAway_alert1 goto towAway_alert1
if %2%==geofence_alert_polygon goto geofence_alert_polygon
if %2%==live_location1 goto live_location1
if %2%==last_parked_location1 goto last_parked_location1
if %2%==gps_speed1 goto gps_speed1
if %2%==live_location2 goto live_location2
if %2%==gps_speed2 goto gps_speed2
if %2%==geofence_alert2 goto geofence_alert2
if %2%==towAway_alert2 goto towAway_alert2
if %2%==towAway_alert3 goto towAway_alert3
if %2%==geofence_alert_polygon1 goto geofence_alert_polygon1
if %2%==dtc goto dtc
if %2%==speed_running_state goto speed_running_state
if %2%==speed_halt_state goto speed_halt_state
if %2%==speed_0_ignition_off goto speed_0_ignition_off
if %2%==speed_3km_ignition_on goto speed_3km_ignition_on
if %2%==speed_valid_ignition_off goto speed_valid_ignition_off
if %2%==speed_less3km_ignition_on goto speed_less3km_ignition_on
if %2%==crash_alert_ddl goto crash_alert_ddl
if %2%==telemetry_speed goto telemetry_speed
if %2%==attestation_stub goto attestation_stub
if %2%==last_parked_location2 goto last_parked_location2
if %2%==vehicle_mode_test goto vehicle_mode_test
if %2%==trip_stub1 goto trip_stub1
if %2%==diagnostic_event goto diagnostic_event
if %2%==sos_alert goto sos_alert
if %2%==sos_alert1 goto sos_alert1
if %2%==telemetry_odo_exceed_limit goto telemetry_odo_exceed_limit
if %2%==telemetry_ignition_on goto telemetry_ignition_on
if %2%==telemetry_ignition_off goto telemetry_ignition_off
if %2%==vehicle_mode_precondition goto vehicle_mode_precondition
if %2%==remoteLockAlert_simulation goto remoteLockAlert_simulation
if %2%==remoteUnlockAlert_simulation goto remoteUnlockAlert_simulation
if %2%==plugInAlert_simulation goto plugInAlert_simulation
if %2%==plugOutAlert_simulation goto plugOutAlert_simulation
if %2%==ignitionOn_simulation goto ignitionOn_simulation
if %2%==ignitionOff_simulation goto ignitionOff_simulation
if %2%==batteryHeatAlert_simulation goto batteryHeatAlert_simulation
if %2%==batteryColdAlert_simulation goto batteryColdAlert_simulation
if %2%==vehicleState_rideMode_sna goto vehicleState_rideMode_sna
if %2%==vehicleState_rideMode_sleep goto vehicleState_rideMode_sleep
if %2%==vehicleState_rideMode_deep_sleep goto vehicleState_rideMode_deep_sleep
if %2%==vehicleState_rideMode_vacation goto vehicleState_rideMode_vacation
if %2%==vehicleState_rideMode_shut_off goto vehicleState_rideMode_shut_off
if %2%==vehicleState_rideMode_forced_ota goto vehicleState_rideMode_forced_ota
if %2%==vehicleState_rideMode_power_up goto vehicleState_rideMode_power_up
if %2%==vehicleState_rideMode_boot_up goto vehicleState_rideMode_boot_up
if %2%==vehicleState_rideMode_diagnostics goto vehicleState_rideMode_diagnostics
if %2%==vehicleState_rideMode_charge_idle goto vehicleState_rideMode_charge_idle
if %2%==vehicleState_rideMode_charge_fault goto vehicleState_rideMode_charge_fault
if %2%==vehicleState_rideMode_ota goto vehicleState_rideMode_ota
if %2%==vehicleState_rideMode_park goto vehicleState_rideMode_park
if %2%==vehicleState_rideMode_slow_mode goto vehicleState_rideMode_slow_mode
if %2%==vehicleState_rideMode_riding goto vehicleState_rideMode_riding
if %2%==vehicleState_rideMode_onboard_fast goto vehicleState_rideMode_onboard_fast
if %2%==vehicleState_rideMode_onboard_slow goto vehicleState_rideMode_onboard_slow
if %2%==vehicleState_rideMode_alarm goto vehicleState_rideMode_alarm
if %2%==speed_valid_in_parkMode goto speed_valid_in_parkMode
if %2%==speed_0_in_parkMode goto speed_0_in_parkMode
if %2%==speed_0_not_in_parkMode goto speed_0_not_in_parkMode
if %2%==speed_3km_not_in_parkMode goto speed_3km_not_in_parkMode
if %2%==speed_less3km_not_in_parkMode goto speed_less3km_not_in_parkMode
if %2%==speed_running_state_v2 goto speed_running_state_v2
if %2%==speed_halt_state_v2 goto speed_halt_state_v2
if %2%==command_precondition_ignition_lvl1 goto command_precondition_ignition_lvl1
if %2%==geofence_circle_alert_entry goto geofence_circle_alert_entry
if %2%==geofence_circle_alert_exit goto geofence_circle_alert_exit
if %2%==geofence_polygon_alert_entry goto geofence_polygon_alert_entry
if %2%==geofence_polygon_alert_exit goto geofence_polygon_alert_exit
if %2%==sos_alert2 goto sos_alert2
if %2%==diagnostic_event1 goto diagnostic_event1
if %2%==onboarding_vin_stub goto onboarding_vin_stub
if %2%==c2c_health goto c2c_health
if %2%==transaction_control_indicator_alert goto transaction_control_indicator_alert
if %2%==cruise_control_state_alert goto cruise_control_state_alert
if %2%==harsh_acceleration_notification goto harsh_acceleration_notification
if %2%==harsh_breaking_notification goto harsh_breaking_notification
if %2%==limp_mode_alert goto limp_mode_alert
if %2%==motor_temp_warn_alert goto motor_temp_warn_alert
if %2%==hill_hold_state_alert goto hill_hold_state_alert
if %2%==bike_charge_state_alert goto bike_charge_state_alert
if %2%==vehicle_fully_charged_alert goto vehicle_fully_charged_alert
if %2%==vehicle_not_charge_alert goto vehicle_not_charge_alert
if %2%==low_battery_state_1_alert goto low_battery_state_1_alert
if %2%==low_battery_state_2_alert goto low_battery_state_2_alert
if %2%==battery_health_alert goto battery_health_alert
if %2%==battery_high_temp_alert goto battery_high_temp_alert
if %2%==motor_health_alert goto motor_health_alert
if %2%==mcu_high_temp_alert goto mcu_high_temp_alert
if %2%==thermal_run_away_alert goto thermal_run_away_alert
if %2%==brake_control_fail_alert goto brake_control_fail_alert
if %2%==handlebar_controls_fail_alert goto handlebar_controls_fail_alert
if %2%==bms_communication_fail_alert goto bms_communication_fail_alert
if %2%==mcu_communication_fail_alert goto mcu_communication_fail_alert
if %2%==obc_communication_fail_alert goto obc_communication_fail_alert
if %2%==flat_tire_error_for_front_alert goto flat_tire_error_for_front_alert
if %2%==flat_tire_error_for_rear_alert goto flat_tire_error_for_rear_alert
if %2%==low_pressure_for_rear_alert goto low_pressure_for_rear_alert
if %2%==low_pressure_for_front_alert goto low_pressure_for_front_alert
if %2%==high_pressure_for_rear_alert goto high_pressure_for_rear_alert
if %2%==high_pressure_for_front_alert goto high_pressure_for_front_alert
if %2%==pin_error_alert goto pin_error_alert
if %2%==ddl_file_conversion_stub goto ddl_file_conversion_stub
if %2%==vacation_mode_disable goto vacation_mode_disable
if %2%==remote_diagnostic_mode_precondition goto remote_diagnostic_mode_precondition
if %2%==trip_stub2 goto trip_stub2
if %2%==vacation_mode_enable goto vacation_mode_enable
if %2%==privacy_mode_enable goto privacy_mode_enable
if %2%==privacy_mode_disable goto privacy_mode_disable
if %2%==incognito_mode_enable goto incognito_mode_enable
if %2%==incognito_mode_disable goto incognito_mode_disable
if %2%==remote_diagnostic_mode_enable goto remote_diagnostic_mode_enable
if %2%==remote_diagnostic_mode_disable goto remote_diagnostic_mode_disable
if %2%==service_mode_enable goto service_mode_enable
if %2%==service_mode_disable goto service_mode_disable
if %2%==add_new_feature_from_cluster goto add_new_feature_from_cluster
if %2%==edit_feature_from_cluster goto edit_feature_from_cluster
if %2%==delete_feature_from_cluster goto delete_feature_from_cluster
if %2%==dtc_v2 goto dtc_v2
if %2%==ota_init goto ota_init
if %2%==towAway_alert4 goto towAway_alert4
if %2%==service_mode_rdm_enable goto service_mode_rdm_enable
if %2%==service_mode_rdm_disable goto service_mode_rdm_disable
if %2%==speed_valid_in_parkMode_v2 goto speed_valid_in_parkMode_v2
if %2%==speed_0_in_parkMode_v2 goto speed_0_in_parkMode_v2
if %2%==speed_0_not_in_parkMode_v2 goto speed_0_not_in_parkMode_v2
if %2%==speed_3km_not_in_parkMode_v2 goto speed_3km_not_in_parkMode_v2
if %2%==speed_state_idle goto speed_state_idle
if %2%==speed_running_state_v3 goto speed_running_state_v3
if %2%==speed_halt_state_v3 goto speed_halt_state_v3
if %2%==trip_stub3 goto trip_stub3
if %2%==vm_delta_change goto vm_delta_change
if %2%==remoteLockAlert2_simulation goto remoteLockAlert2_simulation
if %2%==remoteUnlockAlert2_simulation goto remoteUnlockAlert2_simulation
if %2%==device_authentication_flag goto device_authentication_flag
if %2%==trip_stub4 goto trip_stub4
if %2%==switching_normal_mode_from_cluster goto switching_normal_mode_from_cluster
if %2%==rideState_atRest_speed_0 goto rideState_atRest_speed_0
if %2%==rideState_inMotion_speed_10 goto rideState_inMotion_speed_10
if %2%==dtc_dstub goto dtc_dstub

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** RUN CAN COMMANDS ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

:telemetry_location
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_stub.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\vhal_stub.so /vendor/lib64/
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell mkdir /data/scripts
adb -s %1 push %3\shFiles\location_delhi.sh /data/scripts/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 shell sh /data/scripts/location_delhi.sh

goto Exit

:telemetry_can_odo

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 push %3\shFiles\can_odo.sh /data/
adb -s %1 shell dos2unix /data/can_odo.sh
adb -s %1 shell chmod +x /data/can_odo.sh
adb -s %1 shell sh /data/can_odo.sh
adb shell cansend can0 7EC#0000FFFF
adb -s %1 shell cansend can0 7EC#0000FFFF  :: Odo = 12031.000000

goto Exit

:telemetry_can_speed

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 push %3\shFiles\can_speed.sh /data/
adb -s %1 shell dos2unix /data/can_speed.sh
adb -s %1 shell chmod +x /data/can_speed.sh
adb -s %1 shell sh /data/can_speed.sh
adb shell cansend can0 7FC#20
adb -s %1 shell cansend can0 7FC#20  :: speed = 32.000000

goto Exit

:telemetry_can_fuel

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 push %3\shFiles\loc_fuel.sh /data/
adb -s %1 shell dos2unix /data/loc_fuel.sh
adb -s %1 shell chmod +x /data/loc_fuel.sh
adb -s %1 shell sh /data/loc_fuel.sh
adb shell cansend can0 7EE#20  :: Fuel = 8192 ml
adb -s %1 shell cansend can0 7EE#20  :: Fuel = 8192 ml

goto Exit

:telemetry_can_battery_level

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7FB#80  :: EV_Battery_Level = 128 wh
adb -s %1 shell cansend can0 7FB#80  


goto Exit

:telemetry_can_range_remaining

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
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
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
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
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 shell cansend can0 7FE#00
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
:: adb -s %1 pull /vendor/lib64/libssil.so libssil_orig.so
:: adb -s %1 pull /vendor/bin/dm dm-orig
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb -s %1 shell cansend can0 7FE#01
adb -s %1 shell cansend can0 7FC#00

goto Exit

:chargingNotification_can_charge_port_connected

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AC#01
adb -s %1 shell cansend can0 7AC#01 :: Charge Port Connected - ev_charge_port_connected:1

goto Exit

:chargingNotification_can_charge_port_connected_and_isCharging

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AD#00EC
adb -s %1 shell cansend can0 7AD#00EC :: Charge Port Connected and is charging - inst_charge_rate:236.000000 MW

goto Exit

:chargingNotification_can_charge_port_disconnected

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AC#00
adb -s %1 shell cansend can0 7AC#00 :: Charge Port Disconnected - ev_charge_port_connected:0

goto Exit

:chargingNotification_can_charge_port_connected_and_notCharging

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AD#0000
adb -s %1 shell cansend can0 7AD#0000 :: Charge Port Connected and is not charging - inst_charge_rate:0.000000

goto Exit

:chargingNotification_can_charge_port_open

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AB#01
adb -s %1 shell cansend can0 7AB#00 :: Charge Port Open - ev_charge_port_open:1

goto Exit

:chargingNotification_can_charge_port_close

adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
:: adb -s %1 push %3\paho_files\libssil_orig.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell stop dm_service
:: adb -s %1 shell start dm_service
adb shell cansend can0 7AB#00
adb -s %1 shell cansend can0 7AB#00 :: Charge Port Close - ev_charge_port_open:0

goto Exit

:trip_start
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/*
adb -s %1 push %3\shFiles\b2c_trip_start.sh /data/
adb -s %1 shell dos2unix /data/b2c_trip_start.sh
adb -s %1 shell chmod +x /data/b2c_trip_start.sh
adb -s %1 shell sh /data/b2c_trip_start.sh
adb -s %1 shell cansend can0 7FF#04  :: Ignition start


goto Exit

:trip_start_v3
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/*
adb -s %1 push %3\shFiles\b2c_trip_start_v3.sh /data/
adb -s %1 shell dos2unix /data/b2c_trip_start_v3.sh
adb -s %1 shell chmod +x /data/b2c_trip_start_v3.sh
adb -s %1 shell sh /data/b2c_trip_start_v3.sh
adb -s %1 shell cansend can0 7FF#04  :: Ignition start


goto Exit

:trip_stop
:: adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\b2c_trip_stop.sh /data/
adb -s %1 shell dos2unix /data/b2c_trip_stop.sh
adb -s %1 shell chmod +x /data/b2c_trip_stop.sh
adb -s %1 shell sh /data/b2c_trip_stop.sh
::adb -s %1 shell cansend can0 7FF#03  :: Ignition stop

goto Exit

:location_geofence
adb -s %1 root
adb -s %1 remount
:: adb -s %1 shell stop dm_service
:: adb -s %1 push %3\paho_files\b2c\libssil_stub.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\b2c\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell sync
:: adb -s %1 shell start dm_service
:: adb -s %1 shell start dm_service
adb -s %1 push %3\shFiles\location_delhi.sh /data/
adb -s %1 shell dos2unix /data/location_delhi.sh
adb -s %1 shell chmod +x /data/location_delhi.sh
adb -s %1 shell sh /data/location_delhi.sh

goto Exit

:location_liveTracking
adb -s %1 root
adb -s %1 remount
:: adb -s %1 shell stop dm_service
:: adb -s %1 push %3\paho_files\b2c\libssil_stub.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\b2c\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell sync
:: adb -s %1 shell start dm_service
:: adb -s %1 shell start dm_service
adb -s %1 push %3\shFiles\location_delhi_new.sh /data/
adb -s %1 shell dos2unix /data/location_delhi_new.sh
adb -s %1 shell chmod +x /data/location_delhi_new.sh
adb -s %1 shell sh /data/location_delhi_new.sh

goto Exit


:telemetry_b2c_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\telemetry_b2c_stub.sh /data/
adb -s %1 shell dos2unix /data/telemetry_b2c_stub.sh
adb -s %1 shell chmod +x /data/telemetry_b2c_stub.sh
adb -s %1 shell sh /data/telemetry_b2c_stub.sh


:telemetry_accelerometer_data
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\accelerometer_data.sh /data/
adb -s %1 shell dos2unix /data/accelerometer_data.sh
adb -s %1 shell chmod +x /data/accelerometer_data.sh
adb -s %1 shell sh /data/accelerometer_data.sh

goto Exit

:telemetry_gyro_data
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\gyro.sh /data/
adb -s %1 shell dos2unix /data/gyro.sh
adb -s %1 shell chmod +x /data/gyro.sh
adb -s %1 shell sh /data/gyro.sh

goto Exit


:trip_summary_stub1
adb -s %1 root
adb -s %1 remount
:: adb -s %1 push %3\paho_files\libssil_stub.so /vendor/lib64/libssil.so
:: adb -s %1 push %3\paho_files\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/**
adb -s %1 shell sync
adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\b2c_telemetry_stub_trip.sh /data/
adb -s %1 shell dos2unix /data/b2c_telemetry_stub_trip.sh
adb -s %1 shell chmod +x /data/b2c_telemetry_stub_trip.sh
adb -s %1 shell sh /data/b2c_telemetry_stub_trip.sh

goto Exit

:trip_summary_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
#adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/**
adb -s %1 shell sync
adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\b2c_telemetry_stub_trip2.sh /data/
adb -s %1 shell dos2unix /data/b2c_telemetry_stub_trip2.sh
adb -s %1 shell chmod +x /data/b2c_telemetry_stub_trip2.sh
adb -s %1 shell sh /data/b2c_telemetry_stub_trip2.sh

goto Exit

:trip_summary_log:
adb -s %1 pull /mnt/vendor/persist/data/c2c/Trip_waypoints/ C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs/
adb -s %1 pull /mnt/vendor/persist/data/c2c/Trip_waypoints/
adb -s %1 shell cp -r /mnt/vendor/persist/data/c2c/Trip_waypoints/ /data/
adb -s %1 shell logcat [C2CLOGGER] -t 90000000000 > C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\log.txt

goto Exit

:telemetry_can_sideStand_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7FE#01       #[side_stand:1]
adb -s %1 shell cansend can0 7FE#01 #[side_stand:1]
goto Exit

:telemetry_can_sideStand_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7FE#00       #[side_stand:0]
adb -s %1 shell cansend can0 7FE#00 #[side_stand:0]
goto Exit

:telemetry_can_front_tire_pressure
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A9#01DC  	#front_tire_pressure:220.000000
adb -s %1 shell cansend can0 7A9#01DC  	#front_tire_pressure:220.000000
goto Exit

:telemetry_can_rear_tire_pressure
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A9#04E1 	#rear_tire_pressure:225.000000
adb -s %1 shell cansend can0 7A9#04E1 	#rear_tire_pressure:225.000000
goto Exit

:telemetry_can_SOS_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7FD#01 		 	 #sos_status:1
adb -s %1 shell cansend can0 7FD#01 	 #sos_status:1
goto Exit

:telemetry_can_SOS_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7FD#00 		 	 #sos_status:0
adb -s %1 shell cansend can0 7FD#00 	 #sos_status:0
goto Exit

:telemetry_can_headlight_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F4#01        #headlights:1
adb -s %1 shell cansend can0 7F4#01  #headlights:1
goto Exit

:telemetry_can_headlight_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F4#00        #headlights:0
adb -s %1 shell cansend can0 7F4#00  #headlights:0
goto Exit

:telemetry_can_normal_battery_temp #currentBatteryTemp <65
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7EA#30       #currentBatteryTemp = 48.0  BATTERY_TEMP:48.000000
adb -s %1 shell cansend can0 7EA#30
goto Exit

:telemetry_can_warning_battery_temp #currentBatteryTemp 65 to 75
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7EA#42       #currentBatteryTemp = 66.0  BATTERY_TEMP:66.000000
adb -s %1 shell cansend can0 7EA#42
goto Exit

:telemetry_can_critical_battery_temp #currentBatteryTemp >75
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7EA#65       #currentBatteryTemp = 101.0  BATTERY_TEMP:101.000000
adb -s %1 shell cansend can0 7EA#65
goto Exit

:telemetry_can_speed_notification
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7FC#80
adb -s %1 shell cansend can0 7FC#80  :: speed = 128.000000
goto Exit

:telemetry_can_taillight_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7B2#01        #taillights:1
adb -s %1 shell cansend can0 7B2#01  #taillights:1
goto Exit

:telemetry_can_taillight_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7B2#00        #taillights:0
adb -s %1 shell cansend can0 7B2#00  #taillights:0
goto Exit

:telemetry_can_indicator_1
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F9#01        #turn_signal:1
adb -s %1 shell cansend can0 7F9#01  #turn_signal:1
goto Exit

:telemetry_can_indicator_2
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F9#02        #turn_signal:2
adb -s %1 shell cansend can0 7F9#02  #turn_signal:2
goto Exit

:telemetry_can_indicator_3
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F9#03        #turn_signal:3
adb -s %1 shell cansend can0 7F9#03  #turn_signal:3
goto Exit

:telemetry_can_indicator_0
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F9#00        #turn_signal:0
adb -s %1 shell cansend can0 7F9#00  #turn_signal:0
goto Exit

:telemetry_can_gear_position_2
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F8#02        #gear_position:2
adb -s %1 shell cansend can0 7F8#02  #gear_position:2
goto Exit

:telemetry_can_gear_position_4
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F8#04        #gear_position:4
adb -s %1 shell cansend can0 7F8#04  #gear_position:4
goto Exit

:telemetry_can_gear_position_8
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F8#08        #gear_position:8
adb -s %1 shell cansend can0 7F8#08  #gear_position:8
goto Exit

:telemetry_can_high_beam_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F3#01        # high_beam_state:1
adb -s %1 shell cansend can0 7F3#01  # high_beam_state:1
goto Exit

:telemetry_can_high_beam_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F3#00        # high_beam_state:0
adb -s %1 shell cansend can0 7F3#00  # high_beam_state:0
goto Exit

:telemetry_can_hazard_light_ON
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A6#01        # hazard_lights_state:1
adb -s %1 shell cansend can0 7A6#01  # hazard_lights_state:1
goto Exit

:telemetry_can_hazard_light_OFF
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A6#00        # hazard_lights_state:0
adb -s %1 shell cansend can0 7A6#00  # hazard_lights_state:0
goto Exit

:telemetry_can_rpm
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F2#2E00        # rpm:11776.000000
adb -s %1 shell cansend can0 7F2#2E00  # rpm:11776.000000
goto Exit

:telemetry_can_mobilize
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A3#01        #immobilize_state:1
adb -s %1 shell cansend can0 7A3#01
goto Exit

:telemetry_can_immobilize
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7A3#00        #immobilize_state:0
adb -s %1 shell cansend can0 7A3#00
goto Exit


:telemetry_can_ride_mode_normal
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F7#00
adb -s %1 shell cansend can0 7F7#00  :: ride_mode:0
goto Exit


:telemetry_can_ride_mode_economy
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F7#01
adb -s %1 shell cansend can0 7F7#01  :: ride_mode:1
goto Exit

:telemetry_can_ride_mode_vendorSpecific
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F7#02
adb -s %1 shell cansend can0 7F7#02  :: ride_mode:2
goto Exit

:remaining_battery_charge
adb -s %1 root
adb -s %1 remount
adb -s %1 shell logcat -c
adb shell cansend can0 7F5#01FF
adb -s %1 shell cansend can0 7F5#01FF  :: 100%

goto Exit

:switch_to_hybrid_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 shell cp /vendor/lib64/libssil.so /vendor/lib64/libssil1.so
adb -s %1 shell cp /vendor/lib64/vhal_stub.so /vendor/lib64/vhal_stub1.so
adb -s %1 push %3\paho_files\b2c\gnss_only_hybrid_stub\libssil.so /vendor/lib64/libssil.so
adb -s %1 push %3\paho_files\b2c\gnss_only_hybrid_stub\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell dos2unix /vendor/bin/paho_cs_pub
adb -s %1 shell chmod +x /vendor/bin/paho_cs_pub
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/block_data_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/data_holder_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/event_array_reg.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/cmd_registry.bin
adb -s %1 shell sync
adb -s %1 shell start dm_service

goto Exit

:switch_to_paho_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 shell cp /vendor/lib64/libssil.so /vendor/lib64/libssil1.so
adb -s %1 push %3\paho_files\b2c\phao_stub\libssil.so /vendor/lib64/libssil.so
adb -s %1 shell cp /vendor/lib64/vhal_stub.so /vendor/lib64/vhal_stub1.so
adb -s %1 push %3\paho_files\b2c\paho_stub\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell dos2unix /vendor/bin/paho_cs_pub
adb -s %1 shell chmod +x /vendor/bin/paho_cs_pub
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/block_data_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/data_holder_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/event_array_reg.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/cmd_registry.bin
adb -s %1 shell sync
adb -s %1 shell start dm_service

goto Exit

:switch_to_can_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 shell cp /vendor/lib64/libssil.so /vendor/lib64/libssil1.so
adb -s %1 push %3\paho_files\b2c\can_stub\libssil.so /vendor/lib64/libssil.so
adb -s %1 shell cp /vendor/lib64/vhal_stub.so /vendor/lib64/vhal_stub1.so
adb -s %1 push %3\paho_files\b2c\can_stub\vhal_stub.so /vendor/lib64/
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 shell dos2unix /vendor/bin/paho_cs_pub
adb -s %1 shell chmod +x /vendor/bin/paho_cs_pub
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/block_data_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/data_holder_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/event_array_reg.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/cmd_registry.bin
adb -s %1 shell sync
adb -s %1 shell start dm_service

goto Exit

:switch_to_origin
adb -s %1 root
adb -s %1 remount
adb -s %1 shell stop dm_service
adb -s %1 shell cp /vendor/lib64/libssil1.so /vendor/lib64/libssil.so
adb -s %1 shell cp /vendor/lib64/vhal_stub1.so /vendor/lib64/vhal_stub.so
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/block_data_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/data_holder_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/event_array_reg.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/cmd_registry.bin
adb -s %1 shell sync
adb -s %1 shell start dm_service

goto Exit

:: ####################################################################
:: RE Paho Commands
:: ####################################################################


:ignition_off
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell sync
adb -s %1 push %3\shFiles\ignition_off.sh /data/
adb push %3\shFiles\ignition_off.sh /data/
adb -s %1 push %3\shFiles\ignition_off.sh /data/
adb -s %1 shell dos2unix /data/ignition_off.sh
adb -s %1 shell chmod +x /data/ignition_off.sh
adb -s %1 shell sh /data/ignition_off.sh

goto Exit

:ignition_on
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell sync
adb -s %1 push %3\shFiles\ignition_on.sh /data/
adb push %3\shFiles\ignition_on.sh /data/
adb -s %1 push %3\shFiles\ignition_on.sh /data/
adb -s %1 shell dos2unix /data/ignition_on.sh
adb -s %1 shell chmod +x /data/ignition_on.sh
adb -s %1 shell sh /data/ignition_on.sh

goto Exit


:last_parked_location
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
::adb -s %1 push %3\shFiles\last_parked_location.sh /vendor/bin/
::adb -s %1 shell dos2unix /data/last_parked_location.sh
::adb -s %1 shell chmod +x /data/last_parked_location.sh
::adb -s %1 shell sh /data/last_parked_location.sh

adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\last_parked_location.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/last_parked_location.sh
adb -s %1 shell chmod +x /data/last_parked_location.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/last_parked_location.sh

::adb -s %1 push %3\shFiles\last_parked_location.sh /data/
::adb push %3\shFiles\last_parked_location.sh /data/
::adb -s %1 shell dos2unix /data/last_parked_location.sh
::adb -s %1 shell chmod +x /data/last_parked_location.sh
::adb -s %1 shell sh /data/last_parked_location.sh

goto Exit

:gps_speed
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\gps_speed.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/gps_speed.sh
adb -s %1 shell chmod +x /data/gps_speed.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/gps_speed.sh

goto Exit

:live_location
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\live_location.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/live_location.sh
adb -s %1 shell chmod +x /data/live_location.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/live_location.sh

goto Exit

:tampering_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\tampering_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/tampering_alert.sh
adb -s %1 shell chmod +x /data/tampering_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/tampering_alert.sh

goto Exit

:towAway_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\towAway_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/towAway_alert.sh
adb -s %1 shell chmod +x /data/towAway_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/towAway_alert.sh

goto Exit

:crash_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\crash_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/crash_alert.sh
adb -s %1 shell chmod +x /data/crash_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/crash_alert.sh

goto Exit

:trip_stub
:: adb -s %1 root
:: adb -s %1 remount
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/**
:: adb -s %1 shell sync
:: adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\trip_stub.sh /data/
adb -s %1 shell dos2unix /data/trip_stub.sh
adb -s %1 shell chmod +x /data/trip_stub.sh
adb -s %1 shell sh /data/trip_stub.sh

goto Exit

:commandControl_precondition_speedZero
adb -s %1 push %3\shFiles\command_speed_zero.sh /data/
adb -s %1 shell dos2unix /data/command_speed_zero.sh
adb -s %1 shell chmod +x /data/command_speed_zero.sh
adb -s %1 shell sh /data/command_speed_zero.sh

goto Exit

:critical_battery
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\critical_battery.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/critical_battery.sh
adb -s %1 shell chmod +x /data/critical_battery.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/critical_battery.sh

goto Exit

:batteryHeatCold_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\batteryHeatCold_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/batteryHeatCold_alert.sh
adb -s %1 shell chmod +x /data/batteryHeatCold_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/batteryHeatCold_alert.sh

goto Exit

:ignition_on_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\ignition_on_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/ignition_on_alert.sh
adb -s %1 shell chmod +x /data/ignition_on_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/ignition_on_alert.sh

goto Exit

:geofence_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/geofence_alert.sh
adb -s %1 shell chmod +x /data/geofence_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_alert.sh

goto Exit

:telemetry_ha
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_ha.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_ha.sh
adb -s %1 shell chmod +x /data/telemetry_ha.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_ha.sh

goto Exit

:telemetry_hb
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_hb.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_hb.sh
adb -s %1 shell chmod +x /data/telemetry_hb.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_hb.sh

goto Exit

:telemetry_overspeed
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_overspeed.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_overspeed.sh
adb -s %1 shell chmod +x /data/telemetry_overspeed.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_overspeed.sh

goto Exit

:telemetry_odo
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_odo.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_odo.sh
adb -s %1 shell chmod +x /data/telemetry_odo.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_odo.sh

goto Exit

:trip_stub_without_stop
:: adb -s %1 root
:: adb -s %1 remount
:: adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
:: adb -s %1 shell rm /mnt/vendor/persist/data/c2c/Trip_waypoints/**
:: adb -s %1 shell sync
:: adb -s %1 shell logcat -c
adb -s %1 push %3\shFiles\trip_stub_without_stop.sh /data/
adb -s %1 shell dos2unix /data/trip_stub_without_stop.sh
adb -s %1 shell chmod +x /data/trip_stub_without_stop.sh
adb -s %1 shell sh /data/trip_stub_without_stop.sh

goto Exit

:telemetry_battery_soc
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_battery_soc.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_battery_soc.sh
adb -s %1 shell chmod +x /data/telemetry_battery_soc.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_battery_soc.sh

goto Exit

:telemetry_battery_soh
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_battery_soh.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_battery_soh.sh
adb -s %1 shell chmod +x /data/telemetry_battery_soh.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_battery_soh.sh

goto Exit

:telemetry_battery_soc_exceed_limit
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_battery_soc_exceed_limit.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_battery_soc_exceed_limit.sh
adb -s %1 shell chmod +x /data/telemetry_battery_soc_exceed_limit.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_battery_soc_exceed_limit.sh

goto Exit

:telemetry_battery_soh_exceed_limit
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_battery_soh_exceed_limit.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_battery_soh_exceed_limit.sh
adb -s %1 shell chmod +x /data/telemetry_battery_soh_exceed_limit.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_battery_soh_exceed_limit.sh

goto Exit

:digital_pin_generate
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin.sh
adb -s %1 shell chmod +x /data/digital_pin.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin.sh

goto Exit

:digital_pin_vehicle_unlock_admin
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_vehicle_unlock_admin.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_vehicle_unlock_admin.sh
adb -s %1 shell chmod +x /data/digital_pin_vehicle_unlock_admin.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_vehicle_unlock_admin.sh

goto Exit

:digital_pin_vehicle_unlock_primary
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_vehicle_unlock_primary.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_vehicle_unlock_primary.sh
adb -s %1 shell chmod +x /data/digital_pin_vehicle_unlock_primary.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_vehicle_unlock_primary.sh

goto Exit

:digital_pin_vehicle_unlock_secondary
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_vehicle_unlock_secondary.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_vehicle_unlock_secondary.sh
adb -s %1 shell chmod +x /data/digital_pin_vehicle_unlock_secondary.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_vehicle_unlock_secondary.sh

goto Exit

:digital_pin_expiry_admin
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_expiry_admin.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_expiry_admin.sh
adb -s %1 shell chmod +x /data/digital_pin_expiry_admin.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_expiry_admin.sh

goto Exit

:digital_pin_expiry_primary
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_expiry_primary.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_expiry_primary.sh
adb -s %1 shell chmod +x /data/digital_pin_expiry_primary.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_expiry_primary.sh

goto Exit

:digital_pin_expiry_secondary
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\digital_pin_expiry_secondary.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/digital_pin_expiry_secondary.sh
adb -s %1 shell chmod +x /data/digital_pin_expiry_secondary.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/digital_pin_expiry_secondary.sh

goto Exit

:geofence_alert1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\geofence_alert1.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_alert1.sh
adb -s %1 shell chmod +x /data/geofence_alert1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_alert1.sh

goto Exit

:towAway_alert1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\towAway_alert1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/towAway_alert1.sh
adb -s %1 shell chmod +x /data/towAway_alert1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/towAway_alert1.sh

goto Exit

:geofence_alert_polygon
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_alert_polygon.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_alert_polygon.sh
adb -s %1 shell chmod +x /data/geofence_alert_polygon.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_alert_polygon.sh

goto Exit

:live_location1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\live_location1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/live_location1.sh
adb -s %1 shell chmod +x /data/live_location1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/live_location1.sh

goto Exit

:last_parked_location1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\last_parked_location1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/last_parked_location1.sh
adb -s %1 shell chmod +x /data/last_parked_location1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/last_parked_location1.sh

goto Exit

:gps_speed1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\gps_speed1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/gps_speed1.sh
adb -s %1 shell chmod +x /data/gps_speed1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/gps_speed1.sh

goto Exit

:live_location2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\live_location2.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/live_location2.sh
adb -s %1 shell chmod +x /data/live_location2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/live_location2.sh

goto Exit

:gps_speed2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\gps_speed2.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/gps_speed2.sh
adb -s %1 shell chmod +x /data/gps_speed2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/gps_speed2.sh

goto Exit

:geofence_alert2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\geofence_alert2.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_alert2.sh
adb -s %1 shell chmod +x /data/geofence_alert2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_alert2.sh

goto Exit

:towAway_alert2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\towAway_alert2.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/towAway_alert2.sh
adb -s %1 shell chmod +x /data/towAway_alert2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/towAway_alert2.sh

goto Exit

:towAway_alert3
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\towAway_alert3.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/towAway_alert3.sh
adb -s %1 shell chmod +x /data/towAway_alert3.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/towAway_alert3.sh

goto Exit

:towAway_alert4
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
::adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\towAway_alert4.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
::adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/towAway_alert4.sh
adb -s %1 shell chmod +x /data/towAway_alert4.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/towAway_alert4.sh

goto Exit

:geofence_alert_polygon1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_alert_polygon1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_alert_polygon1.sh
adb -s %1 shell chmod +x /data/geofence_alert_polygon1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_alert_polygon1.sh

goto Exit

:last_parked_location2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\last_parked_location2.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/last_parked_location2.sh
adb -s %1 shell chmod +x /data/last_parked_location2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/last_parked_location2.sh

goto Exit

:dtc
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\dtc.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/dtc.sh
adb -s %1 shell chmod +x /data/dtc.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/dtc.sh

goto Exit

:speed_running_state
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_running_state.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_running_state.sh
adb -s %1 shell chmod +x /data/speed_running_state.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_running_state.sh

goto Exit

:speed_halt_state
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_halt_state.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_halt_state.sh
adb -s %1 shell chmod +x /data/speed_halt_state.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_halt_state.sh

goto Exit

:speed_0_ignition_off
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_0_ignition_off.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_0_ignition_off.sh
adb -s %1 shell chmod +x /data/speed_0_ignition_off.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_0_ignition_off.sh

goto Exit

:speed_3km_ignition_on
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_3km_ignition_on.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_3km_ignition_on.sh
adb -s %1 shell chmod +x /data/speed_3km_ignition_on.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_3km_ignition_on.sh

goto Exit

:speed_valid_ignition_off
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_valid_ignition_off.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_valid_ignition_off.sh
adb -s %1 shell chmod +x /data/speed_valid_ignition_off.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_valid_ignition_off.sh

goto Exit

:speed_less3km_ignition_on
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_less3km_ignition_on.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_less3km_ignition_on.sh
adb -s %1 shell chmod +x /data/speed_less3km_ignition_on.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_less3km_ignition_on.sh

goto Exit

:crash_alert_ddl
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\crash_alert_ddl.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/crash_alert_ddl.sh
adb -s %1 shell chmod +x /data/crash_alert_ddl.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/crash_alert_ddl.sh

goto Exit

:telemetry_speed
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_speed.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_speed.sh
adb -s %1 shell chmod +x /data/telemetry_speed.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_speed.sh

goto Exit

:attestation_stub
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\attestation_stub.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/attestation_stub.sh
adb -s %1 shell chmod +x /data/attestation_stub.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/attestation_stub.sh

goto Exit

:vehicle_mode_test
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicle_mode_test.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicle_mode_test.sh
adb -s %1 shell chmod +x /data/vehicle_mode_test.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicle_mode_test.sh

goto Exit

:trip_stub1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\trip_stub1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/trip_stub1.sh
adb -s %1 shell chmod +x /data/trip_stub1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/trip_stub1.sh

goto Exit

:diagnostic_event
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\diagnostic_event.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/diagnostic_event.sh
adb -s %1 shell chmod +x /data/diagnostic_event.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/diagnostic_event.sh

goto Exit

:sos_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\sos_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/sos_alert.sh
adb -s %1 shell chmod +x /data/sos_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/sos_alert.sh

goto Exit

:sos_alert1
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\sos_alert1.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/sos_alert1.sh
adb -s %1 shell chmod +x /data/sos_alert1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/sos_alert1.sh

goto Exit

:telemetry_odo_exceed_limit
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_odo_exceed_limit.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_odo_exceed_limit.sh
adb -s %1 shell chmod +x /data/telemetry_odo_exceed_limit.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_odo_exceed_limit.sh

goto Exit

:telemetry_ignition_on
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_ignition_on.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_ignition_on.sh
adb -s %1 shell chmod +x /data/telemetry_ignition_on.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_ignition_on.sh

goto Exit

:telemetry_ignition_off
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\telemetry_ignition_off.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/telemetry_ignition_off.sh
adb -s %1 shell chmod +x /data/telemetry_ignition_off.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/telemetry_ignition_off.sh

goto Exit

:vehicle_mode_precondition
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicle_mode_precondition.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicle_mode_precondition.sh
adb -s %1 shell chmod +x /data/vehicle_mode_precondition.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicle_mode_precondition.sh

goto Exit

:ignitionOn_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\ignitionOn_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/ignitionOn_simulation.sh
adb -s %1 shell chmod +x /data/ignitionOn_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/ignitionOn_simulation.sh

goto Exit

:ignitionOff_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\ignitionOff_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/ignitionOff_simulation.sh
adb -s %1 shell chmod +x /data/ignitionOff_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/ignitionOff_simulation.sh

goto Exit

:batteryHeatAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\batteryHeatAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/batteryHeatAlert_simulation.sh
adb -s %1 shell chmod +x /data/batteryHeatAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/batteryHeatAlert_simulation.sh

goto Exit

:batteryColdAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\batteryColdAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/batteryColdAlert_simulation.sh
adb -s %1 shell chmod +x /data/batteryColdAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/batteryColdAlert_simulation.sh

goto Exit

:remoteLockAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\remoteLockAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/remoteLockAlert_simulation.sh
adb -s %1 shell chmod +x /data/remoteLockAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remoteLockAlert_simulation.sh

goto Exit

:remoteUnlockAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\remoteUnlockAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/remoteUnlockAlert_simulation.sh
adb -s %1 shell chmod +x /data/remoteUnlockAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remoteUnlockAlert_simulation.sh

goto Exit

:plugInAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\plugInAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/plugInAlert_simulation.sh
adb -s %1 shell chmod +x /data/plugInAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/plugInAlert_simulation.sh

goto Exit

:plugOutAlert_simulation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\plugOutAlert_simulation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/plugOutAlert_simulation.sh
adb -s %1 shell chmod +x /data/plugOutAlert_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/plugOutAlert_simulation.sh

goto Exit

:vehicleState_rideMode_sna
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_sna.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_sna.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_sna.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_sna.sh

goto Exit

:vehicleState_rideMode_sleep
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_sleep.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_sleep.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_sleep.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_sleep.sh

goto Exit

:vehicleState_rideMode_deep_sleep
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_deep_sleep.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_deep_sleep.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_deep_sleep.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_deep_sleep.sh

goto Exit

:vehicleState_rideMode_vacation
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_vacation.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_vacation.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_vacation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_vacation.sh

goto Exit

:vehicleState_rideMode_shut_off
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_shut_off.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_shut_off.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_shut_off.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_shut_off.sh

goto Exit

:vehicleState_rideMode_forced_ota
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_forced_ota.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_forced_ota.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_forced_ota.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_forced_ota.sh

goto Exit

:vehicleState_rideMode_power_up
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_power_up.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_power_up.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_power_up.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_power_up.sh

goto Exit

:vehicleState_rideMode_boot_up
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_boot_up.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_boot_up.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_boot_up.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_boot_up.sh

goto Exit

:vehicleState_rideMode_diagnostics
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_diagnostics.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_diagnostics.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_diagnostics.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_diagnostics.sh

goto Exit

:vehicleState_rideMode_charge_idle
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_charge_idle.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_charge_idle.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_charge_idle.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_charge_idle.sh

goto Exit

:vehicleState_rideMode_charge_fault
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_charge_fault.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_charge_fault.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_charge_fault.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_charge_fault.sh

goto Exit

:vehicleState_rideMode_ota
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_ota.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_ota.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_ota.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_ota.sh

goto Exit

:vehicleState_rideMode_park
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_park.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_park.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_park.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_park.sh

goto Exit

:vehicleState_rideMode_slow_mode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_slow_mode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_slow_mode.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_slow_mode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_slow_mode.sh

goto Exit

:vehicleState_rideMode_riding
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_riding.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_riding.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_riding.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_riding.sh

goto Exit

:vehicleState_rideMode_onboard_fast
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_onboard_fast.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_onboard_fast.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_onboard_fast.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_onboard_fast.sh

goto Exit

:vehicleState_rideMode_onboard_slow
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_onboard_slow.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_onboard_slow.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_onboard_slow.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_onboard_slow.sh

goto Exit

:vehicleState_rideMode_alarm
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicleState_rideMode_alarm.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicleState_rideMode_alarm.sh
adb -s %1 shell chmod +x /data/vehicleState_rideMode_alarm.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicleState_rideMode_alarm.sh

goto Exit

:speed_valid_in_parkMode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_valid_in_parkMode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_valid_in_parkMode.sh
adb -s %1 shell chmod +x /data/speed_valid_in_parkMode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_valid_in_parkMode.sh

goto Exit

:speed_0_in_parkMode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_0_in_parkMode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_0_in_parkMode.sh
adb -s %1 shell chmod +x /data/speed_0_in_parkMode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_0_in_parkMode.sh

goto Exit

:speed_0_not_in_parkMode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_0_not_in_parkMode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_0_not_in_parkMode.sh
adb -s %1 shell chmod +x /data/speed_0_not_in_parkMode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_0_not_in_parkMode.sh

goto Exit

:speed_3km_not_in_parkMode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_3km_not_in_parkMode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_3km_not_in_parkMode.sh
adb -s %1 shell chmod +x /data/speed_3km_not_in_parkMode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_3km_not_in_parkMode.sh

goto Exit

:speed_halt_state_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_halt_state_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_halt_state_v2.sh
adb -s %1 shell chmod +x /data/speed_halt_state_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_halt_state_v2.sh

goto Exit

:speed_less3km_not_in_parkMode
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_less3km_not_in_parkMode.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_less3km_not_in_parkMode.sh
adb -s %1 shell chmod +x /data/speed_less3km_not_in_parkMode.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_less3km_not_in_parkMode.sh

goto Exit

:speed_running_state_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_running_state_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_running_state_v2.sh
adb -s %1 shell chmod +x /data/speed_running_state_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_running_state_v2.sh

goto Exit

:command_precondition_ignition_lvl1
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\command_precondition_ignition_lvl1.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/command_precondition_ignition_lvl1.sh
adb -s %1 shell chmod +x /data/command_precondition_ignition_lvl1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/command_precondition_ignition_lvl1.sh

goto Exit

:geofence_circle_alert_entry
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_circle_alert_entry.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_circle_alert_entry.sh
adb -s %1 shell chmod +x /data/geofence_circle_alert_entry.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_circle_alert_entry.sh

goto Exit

:geofence_circle_alert_exit
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_circle_alert_exit.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_circle_alert_exit.sh
adb -s %1 shell chmod +x /data/geofence_circle_alert_exit.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_circle_alert_exit.sh

goto Exit

:geofence_polygon_alert_entry
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_polygon_alert_entry.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_polygon_alert_entry.sh
adb -s %1 shell chmod +x /data/geofence_polygon_alert_entry.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_polygon_alert_entry.sh

goto Exit

:geofence_polygon_alert_exit
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\geofence_polygon_alert_exit.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/geofence_polygon_alert_exit.sh
adb -s %1 shell chmod +x /data/geofence_polygon_alert_exit.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/geofence_polygon_alert_exit.sh

goto Exit

:sos_alert2
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\sos_alert2.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/sos_alert2.sh
adb -s %1 shell chmod +x /data/sos_alert2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/sos_alert2.sh

goto Exit

:diagnostic_event1
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\diagnostic_event1.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/diagnostic_event1.sh
adb -s %1 shell chmod +x /data/diagnostic_event1.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/diagnostic_event1.sh

goto Exit

:onboarding_vin_stub
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\onboarding_vin_stub.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/onboarding_vin_stub.sh
adb -s %1 shell chmod +x /data/onboarding_vin_stub.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/onboarding_vin_stub.sh

goto Exit

:c2c_health
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\shFiles\c2c_health.sh /data/
adb -s %1 shell dos2unix /data/c2c_health.sh
adb -s %1 shell chmod +x /data/c2c_health.sh
adb -s %1 push %3\shFiles\c2c.csv /data/
adb -s %1 shell dos2unix /data/c2c.csv
adb -s %1 shell chmod +x /data/c2c.csv
adb -s %1 shell sync
adb -s %1 shell sh /data/c2c_health.sh


goto Exit


:transaction_control_indicator_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\transaction_control_indicator_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/transaction_control_indicator_alert.sh
adb -s %1 shell chmod +x /data/transaction_control_indicator_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/transaction_control_indicator_alert.sh

goto Exit

:cruise_control_state_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\cruise_control_state_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/cruise_control_state_alert.sh
adb -s %1 shell chmod +x /data/cruise_control_state_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/cruise_control_state_alert.sh

goto Exit

:harsh_acceleration_notification 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\harsh_acceleration_notification.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/harsh_acceleration_notification.sh
adb -s %1 shell chmod +x /data/harsh_acceleration_notification.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/harsh_acceleration_notification.sh

goto Exit


:harsh_breaking_notification 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\harsh_breaking_notification.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/harsh_breaking_notification.sh
adb -s %1 shell chmod +x /data/harsh_breaking_notification.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/harsh_breaking_notification.sh

goto Exit

:limp_mode_alert 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\limp_mode_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/limp_mode_alert.sh
adb -s %1 shell chmod +x /data/limp_mode_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/limp_mode_alert.sh

goto Exit

:motor_temp_warn_alert 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\motor_temp_warn_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/motor_temp_warn_alert.sh
adb -s %1 shell chmod +x /data/motor_temp_warn_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/motor_temp_warn_alert.sh
adb -s %1 shell sh /data/motor_temp_warn_alert.sh

goto Exit

:hill_hold_state_alert 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\hill_hold_state_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/hill_hold_state_alert.sh
adb -s %1 shell chmod +x /data/hill_hold_state_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/hill_hold_state_alert.sh

goto Exit


:bike_charge_state_alert 
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\bike_charge_state_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/bike_charge_state_alert.sh
adb -s %1 shell chmod +x /data/bike_charge_state_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/bike_charge_state_alert.sh

goto Exit

:vehicle_fully_charged_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicle_fully_charged_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicle_fully_charged_alert.sh
adb -s %1 shell chmod +x /data/vehicle_fully_charged_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicle_fully_charged_alert.sh

goto Exit

:vehicle_not_charge_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vehicle_not_charge_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/vehicle_not_charge_alert.sh
adb -s %1 shell chmod +x /data/vehicle_not_charge_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vehicle_not_charge_alert.sh

goto Exit

:low_battery_state_1_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\low_battery_state_1_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/low_battery_state_1_alert.sh
adb -s %1 shell chmod +x /data/low_battery_state_1_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/low_battery_state_1_alert.sh

goto Exit

:low_battery_state_2_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\low_battery_state_2_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/low_battery_state_2_alert.sh
adb -s %1 shell chmod +x /data/low_battery_state_2_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/low_battery_state_2_alert.sh

goto Exit

:battery_health_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\battery_health_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/battery_health_alert.sh
adb -s %1 shell chmod +x /data/battery_health_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/battery_health_alert.sh

goto Exit

:battery_high_temp_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\battery_high_temp_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/battery_high_temp_alert.sh
adb -s %1 shell chmod +x /data/battery_high_temp_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/battery_high_temp_alert.sh

goto Exit


:motor_health_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\motor_health_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/motor_health_alert.sh
adb -s %1 shell chmod +x /data/motor_health_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/motor_health_alert.sh


goto Exit

:mcu_high_temp_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\mcu_high_temp_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/mcu_high_temp_alert.sh
adb -s %1 shell chmod +x /data/mcu_high_temp_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/mcu_high_temp_alert.sh

goto Exit

:thermal_run_away_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\thermal_run_away_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/thermal_run_away_alert.sh
adb -s %1 shell chmod +x /data/thermal_run_away_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/thermal_run_away_alert.sh

goto Exit

:brake_control_fail_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\brake_control_fail_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/brake_control_fail_alert.sh
adb -s %1 shell chmod +x /data/brake_control_fail_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/brake_control_fail_alert.sh

goto Exit

:handlebar_controls_fail_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\handlebar_controls_fail_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/handlebar_controls_fail_alert.sh
adb -s %1 shell chmod +x /data/handlebar_controls_fail_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/handlebar_controls_fail_alert.sh

goto Exit

:bms_communication_fail_alert
adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\bms_communication_fail_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/bms_communication_fail_alert.sh
adb -s %1 shell chmod +x /data/bms_communication_fail_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/bms_communication_fail_alert.sh

goto Exit

:mcu_communication_fail_alert

adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\mcu_communication_fail_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/mcu_communication_fail_alert.sh
adb -s %1 shell chmod +x /data/mcu_communication_fail_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/mcu_communication_fail_alert.sh

goto Exit


:obc_communication_fail_alert

adb -s %1 root
adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\obc_communication_fail_alert.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/obc_communication_fail_alert.sh
adb -s %1 shell chmod +x /data/obc_communication_fail_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/obc_communication_fail_alert.sh

goto Exit

:flat_tire_error_for_front_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\flat_tire_error_for_front_alert.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/flat_tire_error_for_front_alert.sh
adb -s %1 shell chmod +x /data/flat_tire_error_for_front_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/flat_tire_error_for_front_alert.sh

goto Exit


:flat_tire_error_for_rear_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\flat_tire_error_for_rear_alert.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/flat_tire_error_for_rear_alert.sh
adb -s %1 shell chmod +x /data/flat_tire_error_for_rear_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/flat_tire_error_for_rear_alert.sh

goto Exit

:low_pressure_for_rear_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\low_pressure_for_rear_alert.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/low_pressure_for_rear_alert.sh
adb -s %1 shell chmod +x /data/low_pressure_for_rear_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/low_pressure_for_rear_alert.sh

goto Exit

:low_pressure_for_front_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
::adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\low_pressure_for_front_alert.sh /data/
::adb -s %1 push %3\paho_files\libssil.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
::adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/low_pressure_for_front_alert.sh
adb -s %1 shell chmod +x /data/low_pressure_for_front_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/low_pressure_for_front_alert.sh

goto Exit

:high_pressure_for_rear_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\high_pressure_for_rear_alert.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/high_pressure_for_rear_alert.sh
adb -s %1 shell chmod +x /data/high_pressure_for_rear_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/high_pressure_for_rear_alert.sh

goto Exit

:high_pressure_for_front_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\high_pressure_for_front_alert.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/high_pressure_for_front_alert.sh
adb -s %1 shell chmod +x /data/high_pressure_for_front_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/high_pressure_for_front_alert.sh

goto Exit

:pin_error_alert
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\pin_error_alert.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/pin_error_alert.sh
adb -s %1 shell chmod +x /data/pin_error_alert.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/pin_error_alert.sh

goto Exit

:ddl_file_conversion_stub
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\ddl_file_conversion_stub.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/ddl_file_conversion_stub.sh
adb -s %1 shell chmod +x /data/ddl_file_conversion_stub.sh
adb -s %1 shell sync
::adb -s %1 shell sh /data/pin_error_alert.sh

goto Exit

:vacation_mode_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\vacation_mode_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/vacation_mode_disable.sh
adb -s %1 shell chmod +x /data/vacation_mode_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vacation_mode_disable.sh

goto Exit

:remote_diagnostic_mode_precondition
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\remote_diagnostic_mode_precondition.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/remote_diagnostic_mode_precondition.sh
adb -s %1 shell chmod +x /data/remote_diagnostic_mode_precondition.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remote_diagnostic_mode_precondition.sh

goto Exit

:trip_stub2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\trip_stub2.sh /data/
adb -s %1 push %3\paho_files\libssi2.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/trip_stub2.sh
adb -s %1 shell chmod +x /data/trip_stub2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/trip_stub2.sh

goto Exit

:vacation_mode_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\vacation_mode_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/vacation_mode_enable.sh
adb -s %1 shell chmod +x /data/vacation_mode_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vacation_mode_enable.sh

goto Exit

:privacy_mode_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\privacy_mode_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/privacy_mode_enable.sh
adb -s %1 shell chmod +x /data/privacy_mode_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/privacy_mode_enable.sh

goto Exit

:privacy_mode_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\privacy_mode_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/privacy_mode_disable.sh
adb -s %1 shell chmod +x /data/privacy_mode_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/privacy_mode_disable.sh

goto Exit

:incognito_mode_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\incognito_mode_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/incognito_mode_enable.sh
adb -s %1 shell chmod +x /data/incognito_mode_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/incognito_mode_enable.sh

goto Exit

:incognito_mode_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\incognito_mode_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/incognito_mode_disable.sh
adb -s %1 shell chmod +x /data/incognito_mode_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/incognito_mode_disable.sh

goto Exit

:remote_diagnostic_mode_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\remote_diagnostic_mode_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/remote_diagnostic_mode_enable.sh
adb -s %1 shell chmod +x /data/remote_diagnostic_mode_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remote_diagnostic_mode_enable.sh

goto Exit

:remote_diagnostic_mode_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\remote_diagnostic_mode_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/remote_diagnostic_mode_disable.sh
adb -s %1 shell chmod +x /data/remote_diagnostic_mode_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remote_diagnostic_mode_disable.sh

goto Exit

:service_mode_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\service_mode_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/service_mode_enable.sh
adb -s %1 shell chmod +x /data/service_mode_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/service_mode_enable.sh

goto Exit

:service_mode_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\service_mode_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/service_mode_disable.sh
adb -s %1 shell chmod +x /data/service_mode_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/service_mode_disable.sh

goto Exit

:add_new_feature_from_cluster
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\add_new_feature_from_cluster.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/add_new_feature_from_cluster.sh
adb -s %1 shell chmod +x /data/add_new_feature_from_cluster.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/add_new_feature_from_cluster.sh

goto Exit

:edit_feature_from_cluster
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\edit_feature_from_cluster.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/edit_feature_from_cluster.sh
adb -s %1 shell chmod +x /data/edit_feature_from_cluster.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/edit_feature_from_cluster.sh

goto Exit

:delete_feature_from_cluster
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\delete_feature_from_cluster.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/delete_feature_from_cluster.sh
adb -s %1 shell chmod +x /data/delete_feature_from_cluster.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/delete_feature_from_cluster.sh

goto Exit


:dtc_v2
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\dtc_v2.sh /data/
adb -s %1 push %3\paho_files\libssil.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/dtc_v2.sh
adb -s %1 shell chmod +x /data/dtc_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/dtc_v2.sh

goto Exit

:ota_init
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\ota_init.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/ota_init.sh
adb -s %1 shell chmod +x /data/ota_init.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/ota_init.sh

goto Exit

:service_mode_rdm_enable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\service_mode_rdm_enable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/service_mode_rdm_enable.sh
adb -s %1 shell chmod +x /data/service_mode_rdm_enable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/service_mode_rdm_enable.sh

goto Exit

:service_mode_rdm_disable
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\shFiles\service_mode_rdm_disable.sh /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/service_mode_rdm_disable.sh
adb -s %1 shell chmod +x /data/service_mode_rdm_disable.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/service_mode_rdm_disable.sh

goto Exit

:speed_valid_in_parkMode_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_valid_in_parkMode_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_valid_in_parkMode_v2.sh
adb -s %1 shell chmod +x /data/speed_valid_in_parkMode_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_valid_in_parkMode_v2.sh

goto Exit

:speed_0_in_parkMode_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_0_in_parkMode_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_0_in_parkMode_v2.sh
adb -s %1 shell chmod +x /data/speed_0_in_parkMode_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_0_in_parkMode_v2.sh

goto Exit

:speed_0_not_in_parkMode_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_0_not_in_parkMode_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_0_not_in_parkMode_v2.sh
adb -s %1 shell chmod +x /data/speed_0_not_in_parkMode_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_0_not_in_parkMode_v2.sh

goto Exit

:speed_3km_not_in_parkMode_v2
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_3km_not_in_parkMode_v2.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_3km_not_in_parkMode_v2.sh
adb -s %1 shell chmod +x /data/speed_3km_not_in_parkMode_v2.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_3km_not_in_parkMode_v2.sh

goto Exit

:speed_halt_state_v3
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_halt_state_v3.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_halt_state_v3.sh
adb -s %1 shell chmod +x /data/speed_halt_state_v3.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_halt_state_v3.sh

goto Exit

:speed_state_idle
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_state_idle.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_state_idle.sh
adb -s %1 shell chmod +x /data/speed_state_idle.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_state_idle.sh

goto Exit

:speed_running_state_v3
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\speed_running_state_v3.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/speed_running_state_v3.sh
adb -s %1 shell chmod +x /data/speed_running_state_v3.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/speed_running_state_v3.sh

goto Exit

:trip_stub3
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\trip_stub3.sh /data/
adb -s %1 push %3\paho_files\libssi2.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/trip_stub3.sh
adb -s %1 shell chmod +x /data/trip_stub3.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/trip_stub3.sh

goto Exit


:vm_delta_change
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
::adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\vm_delta_change.sh /data/
::adb -s %1 push %3\paho_files\libssi2.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
::adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/vm_delta_change.sh
adb -s %1 shell chmod +x /data/vm_delta_change.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/vm_delta_change.sh

goto Exit

:remoteLockAlert2_simulation
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
::adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\remoteLockAlert2_simulation.sh /data/
::adb -s %1 push %3\paho_files\libssi2.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
::adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/remoteLockAlert2_simulation.sh
adb -s %1 shell chmod +x /data/remoteLockAlert2_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remoteLockAlert2_simulation.sh

goto Exit

:remoteUnlockAlert2_simulation
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
::adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\remoteUnlockAlert2_simulation.sh /data/
::adb -s %1 push %3\paho_files\libssi2.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
::adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/remoteUnlockAlert2_simulation.sh
adb -s %1 shell chmod +x /data/remoteUnlockAlert2_simulation.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/remoteUnlockAlert2_simulation.sh

goto Exit

:device_authentication_flag
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\device_authentication_flag.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/device_authentication_flag.sh
adb -s %1 shell chmod +x /data/device_authentication_flag.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/device_authentication_flag.sh

goto Exit

:trip_stub4
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\trip_stub4.sh /data/
adb -s %1 push %3\paho_files\libssi2.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/trip_stub4.sh
adb -s %1 shell chmod +x /data/trip_stub4.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/trip_stub4.sh

goto Exit

:switching_normal_mode_from_cluster
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\switching_normal_mode_from_cluster.sh /data/
adb -s %1 push %3\paho_files\libssi2.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/switching_normal_mode_from_cluster.sh
adb -s %1 shell chmod +x /data/switching_normal_mode_from_cluster.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/switching_normal_mode_from_cluster.sh

goto Exit

:rideState_atRest_speed_0
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\rideState_atRest_speed_0.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/rideState_atRest_speed_0.sh
adb -s %1 shell chmod +x /data/rideState_atRest_speed_0.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/rideState_atRest_speed_0.sh

goto Exit

:rideState_inMotion_speed_10
adb -s %1 root
adb -s %1 remount
adb -s %1 push %3\paho_files\paho_cs_pub /vendor/bin/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\rideState_inMotion_speed_10.sh /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3c.so /data/
adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell dos2unix /data/rideState_inMotion_speed_10.sh
adb -s %1 shell chmod +x /data/rideState_inMotion_speed_10.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/rideState_inMotion_speed_10.sh

goto Exit

:dtc_dstub
adb -s %1 root
adb -s %1 remount
::adb -s %1 push %3\paho_files\c2c_test_console /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c_test_console\c2c_test_console /data/
adb -s %1 push %3\paho_files\paho_cs_pub /data/
adb -s %1 push %3\shFiles\dtc_dstub.sh /data/
::adb -s %1 push %3\paho_files\libssi2.so /data/
::adb -s %1 push %3\paho_files\libpaho-mqtt3cs.so /data/
::adb -s %1 shell chmod +x /data/paho_cs_pub /data/
adb -s %1 shell chmod +x /data/c2c_test_console /data/
adb -s %1 shell dos2unix /data/dtc_dstub.sh
adb -s %1 shell chmod +x /data/dtc_dstub.sh
adb -s %1 shell sync
adb -s %1 shell sh /data/dtc_dstub.sh

goto Exit

:Exit


