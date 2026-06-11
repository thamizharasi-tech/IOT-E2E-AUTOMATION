@echo off

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING HLOS IMAGE ON IVI DEVICE ***
echo -------------------------------------------------
REM: print new line.

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\abl.elf
fastboot flash boot_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\boot.img
fastboot flash dtbo \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\dtbo.img
fastboot flash metadata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\metadata.img
fastboot flash persist \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\persist.img
fastboot flash super \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\super.img
fastboot flash userdata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\userdata.img
fastboot flash vbmeta_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\vbmeta.img
fastboot flash vbmeta_system_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\vbmeta_system.img
fastboot flash vendor_boot \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.4_Sprin2_Bug_fix\vendor_boot.img
fastboot -s %1 reboot
