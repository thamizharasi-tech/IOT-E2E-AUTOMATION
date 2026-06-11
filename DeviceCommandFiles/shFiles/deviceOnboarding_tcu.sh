#!/bin/sh
cd /data/
killall dm
killall softsku_manager
killall c2c_hub
rm -rf /data/c2c_deployment_tcu
systemctl stop softsku
systemctl stop c2c_hub
systemctl stop c2c_dm
systemctl stop c2c_softsku_manager
systemctl stop c2c_ota_manager
systemctl stop c2c_sota_manager
unzip /data/c2c_deployment_tcu.zip
cd /data/c2c_deployment_tcu/
chmod +x /data/c2c_deployment_tcu/c2c_tcu_install.sh
/data/c2c_deployment_tcu/c2c_tcu_install.sh