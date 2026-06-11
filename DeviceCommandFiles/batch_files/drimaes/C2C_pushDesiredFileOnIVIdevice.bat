@echo off

if %2%==dm_conf goto dm_conf
if %2%==dm_conf_CmdCtrl goto dm_conf_CmdCtrl
if %2%==c2cDefault_conf goto c2cDefault_conf
if %2%==paho_files goto paho_files

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

:: Set the destination folder path for conf & sh files
set conf_dest_path=/mnt/vendor/persist/data/c2c/

REM: print new line
echo.
echo ------------------------------------------------------------
echo *** PUSH UPDATED CONF FILES ON IVI DEVICE ***
echo ------------------------------------------------------------
REM: print new line
echo.

:dm_conf
adb -s %1 root
::adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\dm.conf %conf_dest_path%
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/block_data_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/event_array_reg.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/cmd_registry.bin
adb -s %1 shell rm /mnt/vendor/persist/data/c2c/data_holder_registry.bin
adb shell sed -i 's/telemetry_log=n/telemetry_log=y/' /mnt/vendor/persist/data/c2c/dm.conf
adb shell sed -i 's/telemetry_capability=n/telemetry_capability=y/' /mnt/vendor/persist/data/c2c/dm.conf
adb shell stop dm_service
adb shell start dm_service
::adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/dm.conf

goto Exit

:dm_conf_CmdCtrl
adb -s %1 root
::adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\dm.conf %conf_dest_path%
adb shell sed -i 's/telemetry_log=y/telemetry_log=n/' /mnt/vendor/persist/data/c2c/dm.conf
adb shell sed -i 's/telemetry_capability=y/telemetry_capability=n/' /mnt/vendor/persist/data/c2c/dm.conf
adb shell stop dm_service
adb -s %1 shell killall dm
adb shell start dm_service
::adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/dm.conf

goto Exit

:c2cDefault_conf
::adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\c2c_default.conf %conf_dest_path% 
adb -s %1 shell sed -i 's/telemetry_log=n/telemetry_log=y/' /mnt/vendor/persist/data/c2c/c2c_default.conf
adb -s %1 shell killall dm
::adb -s %1 shell chown system:system /mnt/vendor/persist/data/c2c/c2c_default.conf 

goto Exit


:paho_files
::adb -s %1 root
::adb -s %1 remount
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\paho_files\paho_cs_pub /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\telemetry_stub.sh /data/ 
adb -s %1 shell chmod 777 /data/paho_cs_pub
adb -s %1 shell dosunix /data/telemetry_stub.sh

goto Exit

:Exit


