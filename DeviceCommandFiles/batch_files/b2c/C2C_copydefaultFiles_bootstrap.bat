@echo off

:SingleDevice


echo.
echo -----------------------------------------------------------------------
echo *** Sideloaded files are replaced with default files for IVI device***
echo -----------------------------------------------------------------------


copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\conf_files\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\

echo %1%
if %1%==QC-QA goto QC-QA
if %1%==QC-INTG goto QC-INTG
if %1%==B2C-DEMO goto B2C-DEMO
if %1%==GCP-QA goto GCP-QA
if %1%==GCP-DEV goto GCP-DEV
if %1%==GCP-REP goto GCP-REP
if %1%==RE-DEV goto RE-DEV
if %1%==RE-PERF goto RE-PERF
if %1%==GCP-PEN goto GCP-PEN
if %1%==GCP-QA2 goto GCP-QA2
if %1%==GCP-DEMO2 goto GCP-DEMO2
if %1%==GCP-QA3 goto GCP-QA3
if %1%==GCP-QA4 goto GCP-QA4
if %1%==GCP-QA5 goto GCP-QA5
if %1%==GCP-PERF2 goto GCP-PERF2
if %1%==RE-UAT goto RE-UAT
if %1%==RE-DM1 goto RE-DM1
if %1%==PRE-PROD goto PRE-PROD
if %1%==GCP-QA8 goto GCP-QA8



:QC-QA:
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-qa_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-qa_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\
:: copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-qa_default-certs\clientcert.pem.crt C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\clientcert.pem.crt
:: copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-qa_default-certs\private.pem.key C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\private.pem.key
:: copy C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-qa_default-certs\cacert.pem C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\cacert.pem

goto exit

:QC-INTG
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-intg_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\qc-intg_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:B2C-DEMO
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\b2c-demo_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\b2c-demo_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-DEV
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-dev_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-dev_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-REP
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-rep_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-rep_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:RE-DEV
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-dev_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-dev_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:RE-PERF
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-perf_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-perf_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-PEN
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-pen_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-pen_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA2
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-DEMO2
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-demo2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-demo2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA3
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa3_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa3_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA4
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa4_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa4_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA5
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa5_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa5_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-QA8
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa8_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-qa8_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:GCP-PERF2   
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-perf2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\gcp-perf2_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:RE-UAT
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-uat_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-uat_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:RE-DM1
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-dm1_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-dm1_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:PRE-PROD
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-pre_prod_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\c2c\
copy /y C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re-pre_prod_default-certs\* C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\certs\

goto exit

:exit





