import json
import time
from datetime import timezone
import random

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.vehicle_state import *


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_vehConf_normalMode:

    def test_telemetry_conf_normal(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemetry_push_frequency_update(self, onboardingType, chipsetType, "normal_mode")

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 15000
        time.sleep(120)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)




