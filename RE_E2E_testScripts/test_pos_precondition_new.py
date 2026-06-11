import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.e2e_testData import *
from C2CModules.geofence import Geofence_createGeofence, geofence_getGeofence_by_systemId, \
    geofence_map_geofence_to_vehicle, geofence_getGeofence_by_vehicleMappingId, \
    geofence_deleteGeofence_by_vehicleMappingId, geofence_precondition

from C2CModules.commandControl_modules import command_precondition

from C2CModules.vehicle_configurations import vehicleMode_precondition


OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_geofence_precondition1:

    def test_pos_save_geofence_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "geofence_config_update"
        statePreconditions1 = {
            "value": [
                "ON"
            ],
            "operator": "eq",
            "attribute": "ignition"
        }

        statePreconditions2 = {
            "value": [
                "privacy_mode",
                "incognito_mode",
                "remote_diagnostic",
                "NORMAL_MODE"
            ],
            "operator": "in",
            "attribute": "vehicleMode"
        }

        statePreconditions3 = {
            "value": [
                "OFF"
            ],
            "operator": "eq",
            "attribute": "parkMode"
        }
        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Precondition-1: ", statePreconditions1)
        print("Precondition-2: ", statePreconditions2)
        print("Precondition-3: ", statePreconditions3)
        print("----------------------------------------------------------")

        geofence_precondition(self, model, action, statePreconditions1, statePreconditions2, statePreconditions3, "save_precondition")

    def test_pos_update_geofence_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "geofence_config_update"
        statePreconditions1 = {
            "value": [
                "ON"
            ],
            "operator": "eq",
            "attribute": "ignition"
        }

        statePreconditions2 = {
            "value": [
                "privacy_mode",
                "incognito_mode",
                "remote_diagnostic",
                "NORMAL_MODE"
            ],
            "operator": "in",
            "attribute": "vehicleMode"
        }

        statePreconditions3 = {
            "value": [
                "OFF"
            ],
            "operator": "eq",
            "attribute": "parkMode"
        }
        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Precondition-1: ", statePreconditions1)
        print("Precondition-2: ", statePreconditions2)
        print("Precondition-3: ", statePreconditions3)
        print("----------------------------------------------------------")

        geofence_precondition(self, model, action, statePreconditions1, statePreconditions2, statePreconditions3,
                              "update_precondition")

class Test_command_precondition1:

    def test_pos_save_command_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "VEHICLE_LOCK"
        statePreconditions1 = {
            "value": [
                "OFF"
            ],
            "operator": "eq",
            "attribute": "ignition"
        }

        statePreconditions2 = {
            "value": [
                "PRIVACY_MODE",
                "INCOGNITO_MODE",
                "VACATION_MODE",
                "NORMAL_MODE"
            ],
            "operator": "in",
            "attribute": "vehicleMode"
        }

        statePreconditions3 = {
            "value": [
                "ON"
            ],
            "operator": "eq",
            "attribute": "parkMode"
        }
        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Precondition-1: ", statePreconditions1)
        print("Precondition-2: ", statePreconditions2)
        print("Precondition-3: ", statePreconditions3)
        print("----------------------------------------------------------")

        command_precondition(self, model, action, statePreconditions1, statePreconditions2, statePreconditions3, "save_precondition")

class Test_vehicleMode_precondition1:

    def test_pos_save_vacation_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_update_vacation_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE", "PRIVACY_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_privacy_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2,
                                 "save_precondition")

    def test_pos_update_privacy_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE", "VACATION_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_incognito_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2,
                                 "save_precondition")

    def test_pos_update_incognito_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_vacation_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_save_privacy_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_save_incognito_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "currentState", "operator": "eq", "value": ["ACTIVE"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")
