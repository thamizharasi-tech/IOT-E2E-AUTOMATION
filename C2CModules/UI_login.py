def factoryConfiguration(self, model, version):

    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("Create Factory Configuration via Vehicle configuration API : ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    print("==============1.Vehicle Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "vehicle_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be saved successfully for this model",
                           "Factory Conf - Vehicle configuration is saved successfully for this model")
            assert True
            # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0]["message"] == "Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Vehicle configuration should be saved successfully for this model",
                       "Factory Conf - Vehicle configuration already exist for this model")
            # self.result.set_result(TestResults.failed)
            assert True

            #Update vehicle conf with latest configuration

            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

            # Parse API response into JSON
            response_body = response.json()

            # Validate response status code
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Vehicle configuration should be updated successfully for this model",
                               "Factory Conf - Vehicle configuration is updated successfully for this model")
                    assert True
                    # self.result.set_result(TestResults.passed)
            else:
                print("Something went wrong. Please check api response for more details", response.status_code,
                      response_body)
                assert False
    else:
        print("Something went wrong. Please check api response for more details", response.status_code, response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============2.Telemetry Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "telemetry_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Telemetry configuration should be saved successfully for this model",
                       "Factory Conf - Telemetry configuration is saved successfully for this model")
            assert True
            # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Telemetry configuration should be saved successfully for this model",
                       "Factory Conf - Telemetry configuration already exist for this model")
            # self.result.set_result(TestResults.failed)
            assert True

            # Update vehicle conf with latest configuration

            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "telemetry_conf")

            # Parse API response into JSON
            response_body = response.json()

            # Validate response status code
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Telemetry configuration should be updated successfully for this model",
                               "Factory Conf - Telemetry configuration is updated successfully for this model")
                    assert True
                    # self.result.set_result(TestResults.passed)
            else:
                print("Something went wrong. Please check api response for more details", response.status_code,
                      response_body)
                assert False
    else:
        print("Something went wrong. Please check api response for more details", response.status_code, response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============3.Command Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "command_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Command configuration should be saved successfully for this model",
                       "Factory Conf - Command configuration is saved successfully for this model")
            assert True
            # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Command configuration should be saved successfully for this model",
                       "Factory Conf - Command configuration already exist for this model")
            # self.result.set_result(TestResults.failed)
            assert True

            # Update vehicle conf with latest configuration

            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "command_conf")

            # Parse API response into JSON
            response_body = response.json()

            # Validate response status code
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Command configuration should be updated successfully for this model",
                               "Factory Conf - Command configuration is updated successfully for this model")
                    assert True
                    # self.result.set_result(TestResults.passed)
            else:
                print("Something went wrong. Please check api response for more details", response.status_code,
                      response_body)
                assert False
    else:
        print("Something went wrong. Please check api response for more details", response.status_code, response_body)
        assert False

    print("----------------------------------------------------------")

    print("==============4.Alert Conf==============")
    response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "alert_conf")

    # Parse API response into JSON
    response_body = response.json()

    # Validate response status code
    if response.status_code == 200:
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "Factory Conf - Alert configuration should be saved successfully for this model",
                       "Factory Conf - Alert configuration is saved successfully for this model")
            assert True
            # self.result.set_result(TestResults.passed)
    elif response.status_code == 400:
        if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
            "message"] == "Factory Config version already exist for this model":
            testResult(self, "passed",
                       "Factory Conf - Alert configuration should be saved successfully for this model",
                       "Factory Conf - Alert configuration already exist for this model")
            # self.result.set_result(TestResults.failed)
            assert True

            # Update vehicle conf with latest configuration

            response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "alert_conf")

            # Parse API response into JSON
            response_body = response.json()

            # Validate response status code
            if response.status_code == 200:
                if response_body["message"] == "Success":
                    testResult(self, "passed",
                               "Factory Conf - Alert configuration should be updated successfully for this model",
                               "Factory Conf - Alert configuration is updated successfully for this model")
                    assert True
                    # self.result.set_result(TestResults.passed)
            else:
                print("Something went wrong. Please check api response for more details", response.status_code,
                      response_body)
                assert False
    else:
        print("Something went wrong. Please check api response for more details", response.status_code, response_body)
        assert False

    print("----------------------------------------------------------")