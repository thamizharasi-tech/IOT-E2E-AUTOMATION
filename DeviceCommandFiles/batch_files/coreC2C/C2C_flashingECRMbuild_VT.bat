@echo off

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING ECRM IMAGE ON VT DEVICE ***
echo -------------------------------------------------
REM: print new line

set path = \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl_a \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\abl.elf 
fastboot flash abl_b \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\abl.elf 
fastboot flash boot_a \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-boot.img 
fastboot flash boot_b \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-boot.img 
fastboot flash cache \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-cache.ext4 
fastboot flash persist \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-persist.ext4 
fastboot flash system \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-sysfs.ext4 
fastboot flash systemrw \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-systemrw.ext4 
fastboot flash userdata \\brooks\qces_logs2\C2C\C2C_1.1\TCU\sa2150p\sa2150p-usrfs.ext4
fastboot -s %1 reboot

