REM: print new line
echo.
echo --------------------------------------------------------------
echo *** SETUP/CONFIGURE ETHERNET NETWORK ON TELEMATICS DEVICE ***
echo --------------------------------------------------------------
REM: print new line

cmd /k "adb -s %1 shell QCMAP_CLI set /p name=< input.txt"

pause 2
