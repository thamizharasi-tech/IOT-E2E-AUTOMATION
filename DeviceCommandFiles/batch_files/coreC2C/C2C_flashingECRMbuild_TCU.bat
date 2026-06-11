@echo off

IF "%2%"=="NAD" goto OTA
IF "%2%"=="TCU" goto NON_OTA

echo invalid argument.
goto Exit

:OTA

REM: print new line
echo.
echo -----------------------------------------------------------------------
echo *** FLASHING ECRM IMAGE ON NAD DEVICE with serail no. %1 FOR OTA ***
echo -----------------------------------------------------------------------
REM: print new line

cmd /c "adb -s %1 reboot bootloader & fastboot devices & fastboot -s %1 flash data \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\userfs.ubifs & 
fastboot -s %1 flash system_a \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\system.squash & fastboot -s %1 flash system_b \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\system.squash &
fastboot -s %1 flash telaf_a \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\telaf_ro.squashfs & fastboot -s %1 flash telaf_b \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\telaf_ro.squashfs &
fastboot -s %1 flash boot_a \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\sa515m-boot.img & fastboot -s %1 flash boot_b \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\sa515m-boot.img &
fastboot -s %1 flash abl_a \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\abl.elf & fastboot -s %1 flash abl_b \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\abl.elf & fastboot -s %1 reboot"

goto Exit

:NON_OTA

REM: print new line
echo.
echo ------------------------------------------------------
echo *** FLASHING ECRM IMAGE ON TCU/NAD DEVICE FOR NON_OTA   ***
echo ------------------------------------------------------
REM: print new line

adb -s %1 reboot bootloader 
fastboot devices 
::fastboot -s %1 flash data \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\userfs.ubifs
fastboot -s %1 flash system \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\sysfs.ubi
::fastboot -s %1 flash telaf \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\telaf_ro.squashfs
fastboot -s %1 flash boot \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\boot.img
fastboot -s %1 flash abl \\snowcone\builds692\PROD\LE.UM.7.1.3-20302-sa515m.Int-11\apps_proc\build-qti-distro-tele-debug\tmp-glibc\deploy\images\sa515m\qti-tele-image\abl.elf
fastboot -s %1 reboot

goto Exit

:Exit

::echo. ecrm Image is flashed


