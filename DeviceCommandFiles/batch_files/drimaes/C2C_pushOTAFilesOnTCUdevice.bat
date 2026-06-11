@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTAfiles

REM: print new line

IF "%2%"=="sota" goto sota
IF "%2%"=="fota" goto fota
IF "%2%"=="fota_userConsentFiles" goto fota_userConsentFiles
IF "%2%"=="fota_userConsent" goto fota_userConsent
IF "%2%"=="fota_downloadConsent" goto fota_downloadConsent
IF "%2%"=="fota_installConsent" goto fota_installConsent
IF "%2%"=="fota_rebootConsent" goto fota_rebootConsent

:sota
cmd /k "adb -s %1 push %folder_path%\master.conf /data/ & adb -s %1 push %folder_path%\softsku.conf /data/etc/ & adb -s %1 push %folder_path%\image_version.txt /data/etc & adb -s %1 push %folder_path%\sota_session.json /etc/c2c/ & adb -s %1 shell dos2unix /data/master.conf & adb -s %1 shell dos2unix /data/etc/softsku.conf & adb -s %1 shell dos2unix /data/etc/image_version.txt & adb -s %1 shell dos2unix /etc/c2c/sota_session.json"

goto Exit

:fota
cmd /k "adb -s %1 push %folder_path%\master.conf /data/ & adb -s %1 push %folder_path%\softsku.conf /data/etc/ & adb -s %1 push %folder_path%\image_version.txt /data/etc & adb -s %1 push %folder_path%\ota_session.json /etc/c2c/ & adb -s %1 shell dos2unix /data/master.conf & adb -s %1 shell dos2unix /data/etc/softsku.conf & adb -s %1 shell dos2unix /data/etc/image_version.txt & adb -s %1 shell dos2unix /etc/c2c/ota_session.json & adb -s %1 push %folder_path%\fotaV2Scripts /data/ & adb -s %1 shell chmod +x /data/fotaV2Scripts/*"

goto Exit

:fota_userConsentFiles
adb -s %1 push %folder_path%\fotaV2Scripts /data/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\fota_userConsent.sh /data/fotaV2Scripts/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\fota_downloadConsent.sh /data/fotaV2Scripts/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\fota_installConsent.sh /data/fotaV2Scripts/
adb -s %1 push C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\shFiles\fota_rebootConsent.sh /data/fotaV2Scripts/
adb -s %1 shell chmod +x /data/fotaV2Scripts/*

goto Exit

:fota_userConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/fota_userConsent.sh
adb -s %1 shell sh /data/fotaV2Scripts/fota_userConsent.sh

goto Exit

:fota_downloadConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/fota_downloadConsent.sh
adb -s %1 shell sh /data/fotaV2Scripts/fota_downloadConsent.sh


goto Exit

:fota_installConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/fota_installConsent.sh
adb -s %1 shell sh /data/fotaV2Scripts/fota_installConsent.sh

goto Exit

:fota_rebootConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/fota_rebootConsent.sh
adb -s %1 shell sh /data/fotaV2Scripts/fota_rebootConsent.sh

:Exit
