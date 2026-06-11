@echo off

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING ECRM IMAGE ON IVI DEVICE ***
echo -------------------------------------------------
REM: print new line.

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl %2\abl.img
fastboot flash boot_a %2\boot.img
fastboot flash dtbo %2\dtbo.img
fastboot flash metadata %2\metadata.img
fastboot flash persist %2\persist.img
fastboot flash super %2\super.img
fastboot flash userdata %2\userdata.img
fastboot flash vbmeta_a %2\vbmeta.img
fastboot flash vbmeta_system_a %2\vbmeta_system.img
fastboot flash vendor_boot %2\vendor_boot.img
fastboot -s %1 reboot
