@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH VEHICLE CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

::if "%3%"=="vehicle_conf_file_path1" goto vehicle_conf_file_path1
::if "%3%"=="vehicle_conf_file_path2" goto vehicle_conf_file_path2

::vehicle_conf_file_path1
::set conf_dest_path=/mnt/vendor/persist/data/c2c
::goto continue

::vehicle_conf_file_path2
::set conf_dest_path=/mnt/vendor/persist/c2c
::goto continue

REM: Check if the third argument (%3%) is provided
if "%3%"=="" (
    echo Error: Destination path not provided.
    goto Exit
)

REM: Dynamically set the destination path from the third argument
set conf_dest_path=%3%
echo Destination path dynamically set to: %conf_dest_path%

:continue
if "%2%"=="vehicle_conf_all" goto vehicle_conf_all
if "%2%"=="master_conf" goto master_conf
if "%2%"=="telemetry_conf" goto telemetry_conf
if "%2%"=="command_conf" goto command_conf
if "%2%"=="alert_conf" goto alert_conf
if "%2%"=="restart_ruleEngine_service" goto restart_ruleEngine_service

:vehicle_conf_all
adb -s %1 root
adb -s %1 push %folder_path%\. %conf_dest_path%
::adb -s %1 push %folder_path%\vehicleConfiguration\ %conf_dest_path1%
adb -s %1 shell chmod +x %conf_dest_path%/master_conf.json
adb -s %1 shell chmod +x %conf_dest_path%/alert_conf.json
adb -s %1 shell chmod +x %conf_dest_path%/command_conf.json
adb -s %1 shell chmod +x %conf_dest_path%/telemetry_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/master_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/alert_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/command_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/telemetry_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/master_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/alert_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/command_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/telemetry_conf.json
goto restart_cm_manager_service

goto Exit

:master_conf
adb -s %1 root
adb -s %1 push %folder_path%\master_conf.json %conf_dest_path%
::adb -s %1 push %folder_path%\vehicleConfiguration\ %conf_dest_path1%
adb -s %1 shell chmod +x %conf_dest_path%/master_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/master_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/master_conf.json
goto restart_cm_manager_service

goto Exit

:telemetry_conf
adb -s %1 root
adb -s %1 push %folder_path%\telemetry_conf.json %conf_dest_path%
adb -s %1 shell chmod +x %conf_dest_path%/telemetry_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/telemetry_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/telemetry_conf.json
goto restart_cm_manager_service

goto Exit

:command_conf
adb -s %1 root
adb -s %1 push %folder_path%\command_conf.json %conf_dest_path%
adb -s %1 shell chmod +x %conf_dest_path%/command_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/command_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/command_conf.json
goto restart_cm_manager_service

goto Exit

:alert_conf
adb -s %1 root
adb -s %1 push %folder_path%\alert_conf.json %conf_dest_path%
adb -s %1 shell chmod +x %conf_dest_path%/alert_conf.json
adb -s %1 shell dos2unix %conf_dest_path%/alert_conf.json
adb -s %1 shell chown system:system %conf_dest_path%/alert_conf.json
goto restart_cm_manager_service

goto Exit

:restart_cm_manager_service
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** RESTART CM_MANAGER_SERVICE ***
echo ------------------------------------------------------------
adb -s %1 shell stop cm_manager_service
adb -s %1 shell killall cm_manager
adb -s %1 shell start cm_manager_service

goto Exit

:restart_ruleEngine_service
REM: print new line
echo.
echo ------------------------------------------------------------
echo *** RESTART C2C_RULE_ENGINE_SERVICE ***
echo ------------------------------------------------------------
adb -s %1 shell stop rule_engine_service
adb -s %1 shell /vendor/bin/killall c2c_rule_engine
adb -s %1 shell /vendor/bin/start rule_engine_service

goto Exit

:Exit