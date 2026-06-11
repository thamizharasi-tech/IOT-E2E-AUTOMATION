import pytest
from C2CModules.token_generation import *


class Test_tokenGen:

    # Registration-RequestToken
    @pytest.mark.Smoke
    def test1_positive_Registration_RequestToken(self):
        token_gen_reus_mod(self, "API_Data", "Registration-RequestToken")
        setup_Registration_testdata(self)

    # Registration-RequestToken_GETmethod
    @pytest.mark.Smoke
    def test2_positive_Registration_RequestToken_GETmethod(self):
        token_gen_reus_mod(self, "API_Data", "Registration-RequestToken_GETmethod")
        setup_Registration_status_testdata(self)

    # Telemetry_AuthToken
    @pytest.mark.Smoke
    def test3_positive_Telemetry_AuthToken(self):
        token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
        setup_Telemtery_testdata(self)

    # CommandControl_AuthToken
    @pytest.mark.Smoke
    def test4_positive_CommandControl_AuthToken(self):
        token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
        setup_commandControl_testdata(self)

    # Notification-AuthToken
    @pytest.mark.Smoke
    def test5_positive_Notification_AuthToken(self):
        token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
        setup_notify_testdata(self)

    # Vehicle-AuthToken
    @pytest.mark.Smoke
    def test6_positive_Vehicle_AuthToken(self):
        token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
        setup_vehicle_testdata(self)

    # AssetManagement_trip_AuthToken
    @pytest.mark.Smoke
    def test7_positive_AssetManagement_trip_AuthToken(self):
        token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
        setup_asset_testdata(self)

    # SOTA-getToken
    @pytest.mark.Smoke
    def test8_positive_SOTA_getToken(self):
        token_gen_reus_mod(self, "API_Data", "SOTA-getToken")
        setup_SOTA_testdata(self)

    # FOTA-getToken
    @pytest.mark.Smoke
    def test9_positive_FOTA_GetToken(self):
        token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
        setup_FOTA_testdata(self)

    # Statistics_getToken
    @pytest.mark.Smoke
    def test9_positive_TelemetryPublisher_GetToken(self):
        token_gen_reus_mod(self, "API_Data", "TelemetryPublisher_getToken")
        setup_statistics_testdata(self)

    # Statistics_getToken
    @pytest.mark.Smoke
    def test9_positive_Statistics_GetToken(self):
        token_gen_reus_mod(self, "API_Data", "Statistics_getToken")
        setup_telPublisher_testdata(self)

    # Log Manager_getToken
    @pytest.mark.Smoke
    def test10_positive_LogManager_GetToken(self):
        logManager_token_generation(self)
        time.sleep(5)
        setup_logManager_testdata(self)
        # setup_userManagementService_testdata(self)

    # User Management Service_getToken
    @pytest.mark.Smoke
    def test10_positive_LogManager_GetToken(self):
        logManager_token_generation(self)
        time.sleep(5)
        setup_userManagementService_testdata(self)

