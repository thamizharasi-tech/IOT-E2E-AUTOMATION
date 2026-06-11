@echo off

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING ECRM IMAGE ON Fusion TCU DEVICE ***
echo -------------------------------------------------
REM: print new line

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa515m\sa515m\abl.elf
fastboot flash boot \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa515m\sa515m\sa515m-boot.img
fastboot flash system \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa515m\sa515m\sa515m-sysfs.ubi
fastboot -s %1 reboot

