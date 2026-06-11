@echo off

REM: print new line
echo.

echo ComboDeviceOnboarding is set to %1


IF "%1%"=="No" goto Singledevice
IF "%1%"=="Yes" goto Combodevice

echo invalid argument.
goto Exit

:Singledevice

IF "%4%"=="No" (
echo TCU adb serial no is : %2

REM: print new line
echo.
echo -----------------------------------------
echo *** CREATE FOLDER STRUCTURE ON NORMAL TCU DEVICE ***
echo -----------------------------------------
REM: print new line
REM: print new line

:: Set read write permissions
adb -s %2 shell mount -o rw,remount /

:: Set the path for TCU binaries
adb -s %2 shell mkdir -p /data/usr/bin

:: Set the path for TCU certs
adb -s %2 shell mkdir -p /data/usr/local/certs

:: Set the path for TCU sideloaded confs
adb -s %2 shell mkdir -p /etc/c2c

:: Set the path for TCU libraries
adb -s %2 shell mkdir -p /data/usr/lib/

:: Set the path for TCU logs
adb -s %2 shell mkdir -p /data/local/tmp/

echo Required folder structure is created on TCU device
REM: print new line
echo.
)

goto exit



:Combodevice

echo TCU adb serial no is : %2
echo IVI adb serial no is : %3

IF "%4%"=="No" (
REM: print new line
echo.
echo -----------------------------------------
echo *** CREATE FOLDER STRUCTURE ON NORMAL TCU ***
echo -----------------------------------------
REM: print new line

:: Set read write permissions
adb -s %2 shell mount -o rw,remount /

:: Set the path for TCU binaries
adb -s %2 shell mkdir -p /data/usr/local/bin

:: Set the path for TCU certs
adb -s %2 shell mkdir -p /data/usr/local/certs

:: Set the path for TCU sideloaded confs
adb -s %2 shell mkdir -p /usr/local/conf

:: Set the path for TCU libraries
adb -s %2 shell mkdir -p /data/usr/lib/

:: Set the path for TCU logs
adb -s %2 shell mkdir -p /data/local/tmp/

echo Required folder structure is created on TCU device
REM: print new line
)

REM: print new line
echo.
echo -----------------------------------------
echo *** CREATE FOLDER STRUCTURE ON IVI DEVICE ***
echo -----------------------------------------
REM: print new line

:: Set read write permissions
::adb -s %3 root
::adb -s %3 remount

:: Set the path for IVI binaries
adb -s %3 shell mkdir -p /data/usr/local/bin

:: Set the path for IVI sideloaded confs
::adb -s %3 shell mkdir -p /usr/local/conf

:: Set the path for IVI libraries
adb -s %3 shell mkdir -p /data/usr/lib/

:: Set the path for IVI logs
adb -s %3 shell mkdir -p /data/local/tmp/

echo Required folder structure is created on IVI device
REM: print new line

goto exit

:exit