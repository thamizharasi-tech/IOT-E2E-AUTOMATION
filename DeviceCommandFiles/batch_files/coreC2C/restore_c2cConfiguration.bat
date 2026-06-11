:: Usage
::%1 - adb serial id
::%2 - local network tcu_path_lib
:: %3 TCU/IVI
::sample TCU input   .\restore_c2cConfiguration.bat ef3148a9 C:\Sri\build1 TCU
::sample IVI input   .\restore_c2cConfiguration.bat 1234567 C:\Sri\build1 IVI

@echo off
:: Set the path for TCU libraries and binaries
set tcu_path_lib=/data/usr/temp
::Set path for TCU certs and config
set tcu_path_certs=/usr/local/temp
::Set path for IVI path
set ivi_path=/usr/local/temp
if %3%==TCU (
adb -s %1 root
adb -s %1 remount
adb -s %1 shell chmod 777 /usr/local/temp

::---------To push the certificates onto the TCU ----------------
adb -s %1 shell mkdir -p %tcu_path_certs%/certs
adb -s %1 push %2\TCU\certs\cacert.pem %tcu_path_certs%/certs/
adb -s %1 push %2\TCU\certs\clientcert.pem.crt %tcu_path_certs%/certs/
adb -s %1 push %2\TCU\certs\private.pem.key %tcu_path_certs%/certs/
::---------To push the config files onto the TCU ------------
adb -s %1 shell mkdir -p %tcu_path_certs%/conf
adb -s %1 push %2\TCU\conf\c2c.conf %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\c2c_vehicle.json %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\dm.conf %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\dm_chipset.conf %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\mosquitto.conf %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\softsku.conf %tcu_path_certs%/conf/
adb -s %1 push %2\TCU\conf\side_loaded.conf %tcu_path_certs%/conf/
::-----------------Push TCU binaries------------------------
adb -s %1 shell mkdir -p %tcu_path_lib%/bin
adb -s %1 push %2\TCU\bin\mosquitto %tcu_path_lib%/bin/
adb -s %1 push %2\TCU\bin\SoftSKU_Manager %tcu_path_lib%/bin/
adb -s %1 push %2\TCU\bin\DM %tcu_path_lib%/bin/
adb -s %1 push %2\TCU\bin\C2C_hub %tcu_path_lib%/bin/
::-----------------Push TCU library------------------------
adb -s %1 shell mkdir -p %tcu_path_lib%/lib
adb -s %1 push %2\TCU\lib\libpaho-mqtt3c.so %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libpaho-mqtt3c.so.1 %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libpaho-mqtt3c.so.1.3 %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libpaho-mqtt3cs.so %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libpaho-mqtt3cs.so.1 %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libpaho-mqtt3cs.so.1.3 %tcu_path_lib%/lib/ 
adb -s %1 push %2\TCU\lib\libjson-c.so %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libjson-c.so.5 %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libjson-c.so.5.1.0 %tcu_path_lib%/lib/  
adb -s %1 push %2\TCU\lib\libsoa.so %tcu_path_lib%/lib/
adb -s %1 push %2\TCU\lib\libc2cutils.so %tcu_path_lib%/lib/
echo ------------- Display the TCU files in directories---------------
adb -s %1 shell ls -ltr %tcu_path_certs%/certs
adb -s %1 shell ls -ltr %tcu_path_certs%/conf
adb -s %1 shell ls -ltr %tcu_path_lib%/lib
adb -s %1 shell ls -ltr %tcu_path_lib%/bin
) else if %3%==IVI (
echo IVI
adb -s %1 root
adb -s %1 remount
adb -s %1 shell chmod 777 /usr/local/temp
::-------------To push the binaries onto the IVI ------------------
adb -s %1 shell mkdir -p %ivi_path%/bin
adb -s %1 push %2\IVI\bin\DM %ivi_path%/bin/
::-------------To push the config files onto the IVI---------------
adb -s %1 shell mkdir -p %ivi_path%/lib
adb -s %1 push %2\IVI\lib\libsoa.so %ivi_path%/lib
adb -s %1 push %2\IVI\lib\libc2cutils.so %ivi_path%/lib
adb -s %1 push %2\IVI\lib\libpaho-mqtt3c.so %ivi_path%/lib
adb -s %1 push %2\IVI\lib\libpaho-mqtt3cs.so %ivi_path%/lib
adb -s %1 push %2\IVI\lib\libjson.so %ivi_path%/lib  
::---------------To push the config files onto the IVI------------
adb -s %1 shell mkdir -p %ivi_path%/conf
adb -s %1 push %2\IVI\conf\dm.conf %ivi_path%/conf/
adb -s %1 push %2\IVI\conf\dm_chipset.conf %ivi_path%/conf/
echo ------------- Display the IVI files  in directories--------------
adb -s %1 shell ls -ltr %ivi_path%/conf
adb -s %1 shell ls -ltr %ivi_path%/bin
adb -s %1 shell ls -ltr %ivi_path%/lib
) else (
echo "Wrong Input!! Enter either TCU or IVI as third parameter"
)