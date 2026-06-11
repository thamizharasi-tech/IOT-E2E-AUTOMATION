#!/bin/sh
cd /data/
killall dm
killall softsku
stop dm_service
stop c2c_hub
chmod +x /data/c2c_deployment_ivi_only.zip
chmod 777 /data/c2c_deployment_ivi_only.zip
unzip /data/c2c_deployment_ivi_only.zip
cd /data/c2c_deployment_ivi_only/
chmod +x /data/c2c_deployment_ivi_only/*
sh /data/c2c_deployment_ivi_only/c2c_ivi_only_install.sh

