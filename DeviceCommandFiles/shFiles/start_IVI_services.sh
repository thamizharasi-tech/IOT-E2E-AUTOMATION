#!/bin/sh
# Calling the modules
killall dm
killall softsku
#update_car2cloud
cd /vendor/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/usr/lib/:/vendor/lib64/
chmod 755 /vendor/bin/dm
chmod 755 /vendor/bin/softsku
/vendor/bin/dm &
/vendor/bin/softsku &