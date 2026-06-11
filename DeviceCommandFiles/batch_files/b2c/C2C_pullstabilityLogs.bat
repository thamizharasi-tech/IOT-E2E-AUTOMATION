@echo off

IF "%2%"=="stability_logs" (
REM: print new line
echo %3%
adb -s %1 shell logcat -d > %3%
adb shell logcat -d > %3%
)



