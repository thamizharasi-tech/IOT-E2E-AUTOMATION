@echo off
echo adbSerialNo is %1
echo command/function is %2

IF "%2%"=="reboot" goto rebootdevice
IF "%2%"=="root" goto root
IF "%2%"=="createFolder" goto createFolder
IF "%2%"=="remount" goto remountdevice
IF "%2%"=="currentSlot" goto currentSlot
IF "%2%"=="firmwareVer_ivi" goto firmwareVer
IF "%2%"=="firmwareVer" goto firmwareVer
IF "%2%"=="uname-a" goto uname-a
IF "%2%"=="packageList" goto packageList
IF "%2%"=="connectivityCheck_ping" goto connectivityCheck_ping
IF "%2%"=="connectivityCheck_curl" goto connectivityCheck_curl
echo invalid argument.
goto Exit

:rebootdevice
adb -s %1 reboot

goto Exit

:root
::cmd /k "adb -s %1 root"
adb -s %1 root

goto Exit

:createFolder
adb -s %1 shell mkdir /data/vendor/c2c
adb -s %1 shell mkdir /data/usr/local/certs

goto Exit

:remountdevice
cmd /k "adb -s %1 remount"

goto Exit

:firmwareVer
cmd /k "adb -s %1 root & adb -s %1 shell cat /vendor/firmware_mnt/verinfo/ver_info.txt & adb -s %1 pull /vendor/firmware_mnt/verinfo/ver_info.txt C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\"

goto Exit

:uname-a
cmd /k "adb -s %1 shell uname -a"

goto Exit

:currentSlot
cmd /k "adb -s %1 shell bootctl get-current-slot"

goto Exit

:packageList
cmd /k "adb -s %1 shell pm list packages"

goto Exit

:connectivityCheck_ping
cmd /k "adb -s %1 shell ping -c 3 8.8.8.8"

:connectivityCheck_curl
cmd /k "adb -s %1 shell curl www.google.com"

:Exit

