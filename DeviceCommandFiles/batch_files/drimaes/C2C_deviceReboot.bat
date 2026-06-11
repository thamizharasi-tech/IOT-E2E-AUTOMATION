@echo off
echo adbSerialNo is %1
echo command is %2

IF "%2%"=="reboot" goto rebootdevice
IF "%2%"=="remount" goto remountdevice
IF "%2%"=="root" goto rootUser
IF "%2%"=="enableVerity" goto enableVerity
echo invalid argument.
goto Exit

:rebootdevice
cmd /k "adb -s %1 reboot"

goto Exit

:rootUser
cmd /k "adb -s %1 root"

:enableVerity
cmd /k "adb -s %1 shell enable-verity"

goto Exit 

:remountdevice
cmd /k "adb -s %1 remount"

:Exit

