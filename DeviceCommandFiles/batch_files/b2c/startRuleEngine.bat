adb -s 1a6ffea7 shell stop dm_service
adb -s 1a6ffea7 push libssil_stub.so /vendor/lib64/libssil.so
adb -s 1a6ffea7 shell sync
adb -s 1a6ffea7 shell start dm_service



