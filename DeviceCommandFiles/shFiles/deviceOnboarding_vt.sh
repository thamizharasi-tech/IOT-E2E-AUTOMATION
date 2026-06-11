#!/bin/sh
killall dm
killall softsku
systemctl stop softsku
systemctl stop c2c_dm
unzip /c2c_deployment_vt.zip
cd /c2c_deployment_vt/
chmod +x *
/c2c_deployment_vt/c2c_vt_install.sh