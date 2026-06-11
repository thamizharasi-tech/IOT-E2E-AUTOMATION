@echo off

set hlos_image_path=\\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos

REM: print new line
echo.
echo -------------------------------------------------
echo *** FLASHING HLOS IMAGE ON IVI DEVICE ***
echo -------------------------------------------------
REM: print new line.

adb -s %1 reboot bootloader 
fastboot devices
fastboot flash abl \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\abl.elf
fastboot flash boot_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\boot.img
fastboot flash dtbo \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\dtbo.img
fastboot flash metadata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\metadata.img
fastboot flash persist \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\persist.img
fastboot flash super \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\super.img
fastboot flash userdata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\userdata.img
fastboot flash vbmeta_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\vbmeta.img
fastboot flash vbmeta_system_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\vbmeta_system.img
fastboot flash vendor_boot \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint3\hlos\vendor_boot.img
fastboot -s %1 reboot

REM adb -s %1 reboot bootloader 
REM fastboot devices
REM fastboot flash abl \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\abl.elf
REM fastboot flash boot_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\boot.img
REM fastboot flash dtbo \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\dtbo.img
REM fastboot flash metadata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\metadata.img
REM fastboot flash persist \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\persist.img
REM fastboot flash super \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\super.img
REM fastboot flash userdata \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\userdata.img
REM fastboot flash vbmeta_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\vbmeta.img
REM fastboot flash vbmeta_system_a \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\vbmeta_system.img
REM fastboot flash vendor_boot \\brooks\qces_logs2\C2C\C2C_1.4\Drimaes\Release_1.5_Sprint4\hlos\vendor_boot.img
REM fastboot -s %1 reboot
