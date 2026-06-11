#!/bin/sh
cd /data/
killall dm
killall softsku
unzip /data/c2c_deployment_ivi.zip
cd /data/c2c_deployment_ivi/
chmod +x /data/c2c_deployment_ivi/*
/data/c2c_deployment_ivi/c2c_ivi_install.sh
