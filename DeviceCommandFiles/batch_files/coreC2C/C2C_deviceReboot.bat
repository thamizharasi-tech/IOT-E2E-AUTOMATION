@echo off

IF "%2%"=="reboot" goto rebootdevice
IF "%2%"=="remount" goto remountdevice
echo invalid argument.
goto Exit

:rebootdevice
cmd /k "adb -s %1 root"

goto Exit

:remountdevice
cmd /k "adb -s %1 remount"

:Exit

