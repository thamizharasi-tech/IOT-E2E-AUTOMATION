@echo off

:: Set the source folder path for conf & sh files
set folder_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local
set report_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup
set fu_report_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\FeatureUpdateByGroup
set su_report_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\SKUupdateByVIN
set sug_report_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\SKUupdateByGroup
set ota_report_path=C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\OTA
set ota_file_path=C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTAfiles\

IF "%2%"=="DeviceOnboarding" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %report_path%\tcu_files\ 
adb -s %1 pull /data/usr/local/certs %report_path%\tcu_files\ 
adb -s %1 pull /etc/c2c/ %report_path%\tcu_files\
adb -s %1 shell logcat -d > %report_path%\tcu_files\tcu_c2clogs.txt
adb -s %1 pull /persist/data/pfm/licenses/ %fu_report_path%\tcu_files\
)


IF "%2%"=="SKUupdateByVIN" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %su_report_path%\tcu_files\ 
adb -s %1 pull /data/usr/local/certs %su_report_path%\tcu_files 
adb -s %1 pull /etc/c2c/ %su_report_path%\tcu_files 
adb -s %1 shell logcat -d > %su_report_path%\tcu_files\tcu_c2clogs.txt
)


IF "%2%"=="SKUupdateByGroup" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %sug_report_path%\tcu_files\ 
adb -s %1 pull /data/usr/local/certs %sug_report_path%\tcu_files 
adb -s %1 pull /etc/c2c/ %sug_report_path%\tcu_files 
adb -s %1 pull /etc/c2c/ %su_report_path%\tcu_files 
adb -s %1 shell logcat -d > %sug_report_path%\tcu_files\tcu_c2clogs.txt
)


IF "%2%"=="FeatureUpdateByGroup" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %fu_report_path%\tcu_files\
adb -s %1 pull /data/usr/local/certs %fu_report_path%\tcu_files
adb -s %1 pull /etc/c2c/ %fu_report_path%\tcu_files
adb -s %1 shell logcat -d > %fu_report_path%\tcu_files\tcu_c2clogs.txt
)


IF "%2%"=="SKUupdateByVIN_vt" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %su_report_path%\vt_files\ 
adb -s %1 pull /data/usr/local/certs %su_report_path%\vt_files 
adb -s %1 pull /etc/c2c/ %su_report_path%\vt_files 
adb -s %1 shell logcat -d > %su_report_path%\vt_files\vt_c2clogs.txt
)


IF "%2%"=="SKUupdateByGroup_vt" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %sug_report_path%\vt_files\ 
adb -s %1 pull /data/usr/local/certs %sug_report_path%\vt_files 
adb -s %1 pull /etc/c2c/ %sug_report_path%\vt_files 
adb -s %1 shell logcat -d > %sug_report_path%\vt_files\vt_c2clogs.txt
)


IF "%2%"=="FeatureUpdateByGroup_vt" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %fu_report_path%\vt_files\ 
adb -s %1 pull /data/usr/local/certs %fu_report_path%\vt_files 
adb -s %1 pull /etc/c2c/ %fu_report_path%\vt_files 
adb -s %1 shell logcat -d > %fu_report_path%\vt_files\vt_c2clogs.txt
)


IF "%2%"=="OTA" (
REM: print new line
echo.
adb -s %1 pull /etc/c2c/ %ota_report_path%\tcu_files\ 
adb -s %1 pull /data/usr/local/certs %ota_report_path%\tcu_files\ 
adb -s %1 pull /etc/c2c/ota_session.json %ota_report_path%\tcu_files\ 
adb -s %1 shell logcat -d > %ota_report_path%\tcu_files\tcu_c2clogs.txt 
adb -s %1 shell logread tafUpdate > %ota_report_path%\tcu_files\tcu_tafUpdatelogs_ota.txt
)


IF "%2%"=="SOTA" (
REM: print new line
echo.
adb -s %1 pull /etc/c2c/ %ota_report_path%\tcu_files\ 
adb -s %1 pull /data/usr/local/certs %ota_report_path%\tcu_files\ 
adb -s %1 pull /etc/c2c/sota_session.json %ota_report_path%\tcu_files\ 
adb -s %1 shell logcat -d > %ota_report_path%\tcu_files\tcu_c2clogs.txt 
adb -s %1 shell logread tafUpdate > %ota_report_path%\tcu_files\tcu_tafUpdatelogs_sota.txt
)

IF "%2%"=="DeviceOnboarding_IVI" (
REM: print new line
echo.
adb -s %1 pull /vendor/c2c/ C:\Users\suttarak\PycharmProjects\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files
)

IF "%2%"=="OTAfiles" (
REM: print new line
echo.
adb -s %1 pull /data/master.conf %ota_file_path% 
adb -s %1 pull /data/etc/softsku.conf %ota_file_path% 
adb -s %1 pull /data/etc/image_version.txt %ota_file_path%
)

IF "%2%"=="OTA_firmwareVer_before" (
REM: print new line
echo.
adb -s %1 pull /firmware/image/Ver_Info.txt %ota_report_path%\beforeOTA\
)

IF "%2%"=="OTA_firmwareVer_after" (
REM: print new line
echo.
adb -s %1 pull /firmware/image/Ver_Info.txt %ota_report_path%\afterOTA\
)

IF "%2%"=="DeviceOnboarding_tcuvt_fusion" (
REM: print new line
echo.
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/licenses
adb -s %1 push %folder_path%\shFiles\pullTCUfiles_tuvt_result.sh /data/c2c/common/
adb -s %1 shell chmod +x /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 shell sh /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 pull /persist/data/pfm/licenses/ %report_path%\vt_files\
adb -s %1 pull /etc/c2c/ %report_path%\vt_files\
adb -s %1 pull /data/c2c/common/c2c/ %report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/licenses/ %report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/tcu_c2clogs.txt %report_path%\tcu_files\
adb -s %1 shell logcat -d > %report_path%\vt_files\vt_c2clogs.txt
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell rm -rf /data/c2c/common/licenses
adb -s %1 shell rm -rf /data/c2c/common/files
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/*
)

IF "%2%"=="DeviceOnboarding_tcuvt_fusion_skuVIN" (
REM: print new line
echo.
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/licenses
adb -s %1 push %folder_path%\shFiles\pullTCUfiles_tuvt_result.sh /data/c2c/common/
adb -s %1 shell chmod +x /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 shell sh /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 pull /persist/data/pfm/licenses/ %su_report_path%\vt_files\
adb -s %1 pull /etc/c2c/ %su_report_path%\vt_files\
adb -s %1 pull /data/c2c/common/c2c/ %su_report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/licenses/ %su_report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/tcu_c2clogs.txt %su_report_path%\tcu_files\
adb -s %1 shell logcat -d > %su_report_path%\vt_files\vt_c2clogs.txt
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell rm -rf /data/c2c/common/licenses
adb -s %1 shell rm -rf /data/c2c/common/files
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/*
)

IF "%2%"=="DeviceOnboarding_tcuvt_fusion_skuGrp" (
REM: print new line
echo.
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/licenses
adb -s %1 push %folder_path%\shFiles\pullTCUfiles_tuvt_result.sh /data/c2c/common/
adb -s %1 shell chmod +x /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 shell sh /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 pull /persist/data/pfm/licenses/ %sug_report_path%\vt_files\
adb -s %1 pull /etc/c2c/ %sug_report_path%\vt_files\
adb -s %1 pull /data/c2c/common/c2c/ %sug_report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/licenses/ %sug_report_path%%\tcu_files\
adb -s %1 pull /data/c2c/common/tcu_c2clogs.txt %sug_report_path%%\tcu_files\
adb -s %1 shell logcat -d > %sug_report_path%\vt_files\vt_c2clogs.txt
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell rm -rf /data/c2c/common/licenses
adb -s %1 shell rm -rf /data/c2c/common/files
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/*
)


IF "%2%"=="DeviceOnboarding_tcuvt_fusion_FeatUp" (
REM: print new line
echo.
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/c2c
adb -s %1 shell mkdir /data/c2c/common/licenses
adb -s %1 push %folder_path%\shFiles\pullTCUfiles_tuvt_result.sh /data/c2c/common/
adb -s %1 shell chmod +x /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 shell sh /data/c2c/common/pullTCUfiles_tuvt_result.sh
adb -s %1 pull /data/c2c/common/c2c/ %fu_report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/licenses/ %fu_report_path%\tcu_files\
adb -s %1 pull /data/c2c/common/tcu_c2clogs.txt %fu_report_path%\tcu_files\
adb -s %1 shell rm -rf /data/c2c/common/c2c
adb -s %1 shell rm -rf /data/c2c/common/licenses
adb -s %1 shell rm -rf /data/c2c/common/files
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/c2c
adb -s %1 shell rm -rf /data/c2c/common/certs/*
)

IF "%2%"=="DeviceOnboarding_tcuvt" (
REM: print new line
echo.
adb -s %1 pull /persist/data/pfm/licenses/ %report_path%\vt_files\
adb -s %1 pull /etc/c2c/ %report_path%\vt_files\
adb -s %1 shell logcat -d > %report_path%\vt_files\vt_c2clogs.txt
)