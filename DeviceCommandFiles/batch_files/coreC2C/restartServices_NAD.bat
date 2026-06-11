@echo off
echo adbSerialNo is %1
cmd /k "adb -s %1 shell systemctl restart softsku & adb -s %1 shell systemctl restart c2c_dm & adb -s %1 shell systemctl restart c2c_softsku_manager & adb -s %1 shell systemctl restart c2c_hub"
