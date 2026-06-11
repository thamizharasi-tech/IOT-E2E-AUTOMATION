@echo off

IF "%2%"=="TCU" goto TCUServices
IF "%2%"=="IVI" goto IVIServices
IF "%2%"=="VT" goto VTServices
IF "%2%"=="PRIMARY_IVI" goto IVIServices_PRIMARY
IF "%2%"=="OTA" goto OTAServices

:TCUServices

echo.
echo ----------------------------------------------------
echo *** STOP SERVICE ON TCU DEVICE ***
echo ----------------------------------------------------
REM: print new line
echo.
if "%3%"=="c2c_dm" (
cmd /k "adb -s %1 shell systemctl stop c2c_dm"
REM: print new line
echo c2c_dm service is stopped on TCU device
)
if "%3%"=="c2c_softsku_manager" (
cmd /k "adb -s %1 shell systemctl stop c2c_softsku_manager"
REM: print new line
echo c2c_softsku_manager service is stopped on TCU device
)
if "%3%"=="softsku" (
cmd /k "adb -s %1 shell systemctl stop softsku"
REM: print new line
echo softsku service is stopped on TCU device
)
if "%3%"=="mosquitto" (
cmd /k "adb -s %1 shell systemctl stop mosquitto"
REM: print new line
echo mosquitto service is stopped on TCU device
)
if "%3%"=="c2c_hub" (
cmd /k "adb -s %1 shell systemctl stop c2c_hub"
REM: print new line
echo c2c_hub service is stopped on TCU device
)
if "%3%"=="c2c_ota_manager" (
cmd /k "adb -s %1 shell systemctl stop c2c_ota_manager"
REM: print new line
echo c2c_dm service is stopped on TCU device
)
if "%3%"=="c2c_sota_manager" (
cmd /k "adb -s %1 shell systemctl stop c2c_sota_manager"
REM: print new line
echo softsku service is stopped on TCU device
)

goto Exit

:IVIServices

echo.
echo ----------------------------------------------------
echo *** STOP SERVICE ON IVI DEVICE ***
echo ----------------------------------------------------
REM: print new line
echo.
if "%3%"=="c2c_dm" (
cmd /k "adb -s %1 shell killall c2c_dm"
REM: print new line
echo c2c_dm service is stopped on IVI device
)

if "%3%"=="softsku" (
cmd /k "adb -s %1 shell killall softsku"
REM: print new line
echo softsku service is stopped on IVI device
)
goto Exit

:VTServices

echo.
echo ----------------------------------------------------
echo *** STOP SERVICE ON VT DEVICE ***
echo ----------------------------------------------------
REM: print new line
echo.
if "%3%"=="c2c_dm" (
cmd /k "adb -s %1 shell systemctl stop c2c_dm"
REM: print new line
echo c2c_dm service is stopped on VT device
)

if "%3%"=="softsku" (
cmd /k "adb -s %1 shell systemctl stop softsku"
REM: print new line
echo softsku service is stopped on VT device
)
goto Exit

:IVIServices_PRIMARY

echo.
echo ----------------------------------------------------
echo *** STOP SERVICE ON IVI DEVICE ***
echo ----------------------------------------------------
REM: print new line
echo.
if "%3%"=="c2c_dm" (
cmd /k "adb -s %1 shell killall c2c_dm"
REM: print new line
echo c2c_dm service is stopped on IVI device
)

if "%3%"=="softsku" (
cmd /k "adb -s %1 shell killall c2c_hub"
REM: print new line
echo softsku service is stopped on IVI device
)

:Exit



