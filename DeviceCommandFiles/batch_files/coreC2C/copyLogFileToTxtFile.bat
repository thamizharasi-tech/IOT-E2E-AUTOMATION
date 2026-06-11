@echo off
echo adbSerialNo is %1
cmd /k "adb -s %1 shell logcat -f /data/local/tmp/c2c_hub_log_file.txt"
