@echo off

echo.
echo ----------------------------------------------------
echo *** REMOVE/PUSH CORRUPT FILE(S) ON TCU DEVICE ***
echo ----------------------------------------------------
REM: print new line
echo.
if "%2%"=="remRootCert" (
cmd /k "adb -s %1 shell rm /data/usr/local/certs/cacert.pem"
REM: print new line
echo Root certificate is deleted/removed on TCU device
)
if "%2%"=="remx509Cert" (
cmd /k "adb -s %1 shell rm /data/usr/local/certs/clientcert.pem.crt"
REM: print new line
echo X509 certificate is deleted/removed on TCU device
)
if "%2%"=="remPriKey" (
cmd /k "adb -s %1 shell rm /data/usr/local/certs/private.pem.key"
REM: print new line
echo Private Key file is deleted/removed on TCU device
)
if "%2%"=="corruptRootCert" (
cmd /k "adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\corruptFiles\cacert.pem /data/usr/local/certs/"
REM: print new line
echo Corrupt root certificate is pushed on TCU device
)
if "%2%"=="corruptX509Cert" (
cmd /k "adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\corruptFiles\clientcert.pem.crt /data/usr/local/certs/"
REM: print new line
echo Corrupt x509 certificate is pushed on TCU device
)
if "%2%"=="corruptPrivKey" (
cmd /k "adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\corruptFiles\private.pem.key /data/usr/local/certs/"
REM: print new line
echo Corrupt private key file is pushed on TCU device
)
