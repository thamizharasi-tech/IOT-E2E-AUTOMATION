@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local

IF "%1%"=="IVI" goto SingleIVIdevice
echo invalid argument.
goto Exit

:SingleIVIdevice

REM: print new line
echo.
echo -----------------------------------------
echo *** Sideloaded files are replaced with default files for IVI device***
echo -----------------------------------------
REM: print new line
DEL %folder_path%\c2c\*.*?
adb -s %2 pull /mnt/vendor/persist/data/c2c/dm.conf %folder_path%\c2c\
adb -s %2 pull /mnt/vendor/persist/data/c2c/car2cloud.conf %folder_path%\c2c\
adb -s %2 pull /mnt/vendor/persist/data/c2c/side_loaded.conf %folder_path%\c2c\
adb -s %2 pull /mnt/vendor/persist/data/c2c/c2c_default.conf %folder_path%\c2c\
copy %folder_path%\drimaes_defaultConfNew\c2c_vehicle.json %folder_path%\c2c\ 


:Exit