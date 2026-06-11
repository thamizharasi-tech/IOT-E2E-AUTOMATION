@echo off

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING ECRM IMAGE ON IVI DEVICE ***
echo -------------------------------------------------
REM: print new line.

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\abl.img
fastboot flash boot_a \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\boot.img
fastboot flash dtbo \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\dtbo.img
fastboot flash metadata \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\metadata.img
fastboot flash persist \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\persist.img
fastboot flash super \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\super.img
fastboot flash userdata \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\userdata.img
fastboot flash vbmeta_a \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\vbmeta.img
fastboot flash vbmeta_system_a \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\vbmeta_system.img
fastboot flash vendor_boot \\brooks\qces_logs2\C2C\R1.4\Client\ivi_test_images\vendor_boot.img
fastboot -s %1 reboot
