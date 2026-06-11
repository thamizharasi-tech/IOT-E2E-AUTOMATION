@echo off

IF "%2%"=="c2clogger" (
REM: print new line
echo.
adb -s %1 shell logcat c2clogger -f /data/vendor/c2c/c2c_c2clogger.txt
)
IF "%2%"=="aota" (
REM: print new line
echo.
adb -s %1 shell logcat aota -f /data/vendor/c2c/c2c_aota.txt
)