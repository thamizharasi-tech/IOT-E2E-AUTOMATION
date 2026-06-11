@echo off

echo adbSerialNo is %1

IF "%2%"=="OTA" goto OTA
IF "%2%"=="NON_OTA" goto NON_OTA

echo invalid argument.
goto Exit

:OTA

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING ECRM IMAGE ON NAD DEVICE FOR OTA ***
echo -------------------------------------------------
REM: print new line

cmd /c "adb -s %1 reboot bootloader & fastboot devices & fastboot -s %1 flash data \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\sa515m-usrfs.ubifs & 
fastboot -s %1 flash system_a \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\system.squash & fastboot -s %1 flash system_b \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images2\system.squash &
fastboot -s %1 flash telaf_a \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\telaf_ro.squashfs & fastboot -s %1 flash telaf_b \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\telaf_ro.squashfs &
fastboot -s %1 flash boot_a \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\sa515m-boot.img & fastboot -s %1 flash boot_b \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\sa515m-boot.img &
fastboot -s %1 flash abl_a \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\abl.elf & fastboot -s %1 flash abl_b \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\abl.elf & fastboot -s %1 reboot"

goto Exit

:NON_OTA

REM: print new line
echo.
echo ------------------------------------------------------
echo *** FLASHING ECRM IMAGE ON TCU/NAD DEVICE FOR NON_OTA   ***
echo ------------------------------------------------------
REM: print new line

cmd /c "adb -s %1 reboot bootloader & fastboot devices & fastboot -s %1 flash data \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\sa515m-usrfs.ubifs &
fastboot -s %1 flash system \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\system.squash &
fastboot -s %1 flash telaf \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\telaf_ro.squashfs &
fastboot -s %1 flash boot \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\sa515m-boot.img &
fastboot -s %1 flash abl \\brooks\qces_logs2\C2C\R1.4\Client\edgehub_components\AutomationBinLib\ecrm_Images\abl.elf & fastboot -s %1 reboot"

goto Exit

:Exit


