#!/bin/sh
cd /data/
rm -rf /data/c2c_deployment_tcu_nad/
killall dm
killall softsku_manager
killall c2c_hub
systemctl stop softsku
systemctl stop c2c_hub
systemctl stop c2c_dm
systemctl stop c2c_softsku_manager
systemctl stop c2c_ota_manager
systemctl stop c2c_sota_manager
unzip /data/c2c_deployment_tcu_nad.zip
cd /data/c2c_deployment_tcu_nad/
chmod +x *
/data/c2c_deployment_tcu_nad/c2c_tcu_install.sh