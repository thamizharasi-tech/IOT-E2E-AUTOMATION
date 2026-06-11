@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTAfiles

REM: print new line

IF "%2%"=="sota" goto sota
IF "%2%"=="fota" goto fota
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

:fota_userConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/user_consent_subscribe.sh
adb -s %1 shell sh /data/fotaV2Scripts/user_consent_subscribe.sh &

goto Exit

:fota_downloadConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/download_consent_accept.sh
adb -s %1 shell sh /data/fotaV2Scripts/download_consent_accept.sh


goto Exit

:fota_installConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/install_consent_accept.sh
adb -s %1 shell sh /data/fotaV2Scripts/install_consent_accept.sh

goto Exit

:fota_userConsent
adb -s %1 shell chmod +x /data/fotaV2Scripts/reboot_consent_accept.sh
adb -s %1 shell sh /data/fotaV2Scripts/reboot_consent_accept.sh
adb -s %1 reboot

:Exit
