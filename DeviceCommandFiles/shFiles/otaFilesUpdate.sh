#!/bin/sh
VINno = $1
sed -n '/vin= /p' coleridge.txt/data/etc/softsku.conf 
sed -i "/vin=/c\vin=%VINno%" ~/data/etc/softsku.conf 
systemctl restart c2c_sota_manager


