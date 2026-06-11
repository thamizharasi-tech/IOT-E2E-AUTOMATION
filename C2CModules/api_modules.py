# --------------------------
# API reusable Modules
# --------------------------

def pageNo_pageSize_update(complete_url, tc):
    if "page" in tc:
        if "pageNo" in complete_url and "pageSize" in complete_url:
            print("page No and PageSize parameters are present in the endpoint")
        else:
            print("Adding page no & page size parameters in the endpoint")
            complete_url = complete_url + "?pageNo=1&pageSize=10"

        if tc == "pageSize_0":
            complete_url = complete_url.replace("?pageNo=1&pageSize=10", "?pageNo=1&pageSize=0")
        elif tc == "pageSize_1001":
            complete_url = complete_url.replace("?pageNo=1&pageSize=10", "?pageNo=1&pageSize=1001")
        elif tc == "pageNo_0":
            complete_url = complete_url.replace("?pageNo=1&pageSize=10", "?pageNo=0&pageSize=10")
        elif tc == "pageNo_1001":
            complete_url = complete_url.replace("?pageNo=1&pageSize=10", "?pageNo=1001&pageSize=10")

    print(complete_url)
    return complete_url


def header_update(header_x, tc):
    if "invalid_apiKey" == tc:
        header_x["api-key"] = 'xyz'
    elif "null_apiKey" == tc:
        header_x["api-key"] = 'NULL'
    elif "empty_apiKey" in tc:
        header_x["api-key"] = ''
    elif "no_apiKey" in tc:
        del header_x["api-key"]
    elif "invalid_x-requestor" in tc:
        header_x["x-requestor"] = '@#$'
    elif "empty_x-requestor" in tc:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in tc:
        del header_x["x-requestor"]
    elif "no_x-requestor_and_no_apiKey" in tc:
        del header_x["x-requestor"]
        del header_x["api-key"]
    elif "empty_x-requestor_and_empty_apiKey" in tc:
        header_x["api-key"] = ''
        header_x["x-requestor"] = ''
    elif "empty_x-requestor_and_invalid_apiKey" in tc:
        header_x["api-key"] = 'xyz'
        header_x["x-requestor"] = ''
    elif "empty_x-requestor_and_no_apiKey" in tc:
        del header_x["api-key"]
        header_x["x-requestor"] = ''
    elif "no_x-requestor_and_invalid_apiKey" in tc:
        del header_x["x-requestor"]
        header_x["api-key"] = 'xyz'
    elif "no_x-requestor_and_empty_apiKey" in tc:
        del header_x["x-requestor"]
        header_x["api-key"] = ''
    return header_x


def verify_api_response(response, option):
    if response.status_code == 202 and option == "invalid_apiKey":
        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # assert (response_body["message"] == "api keys are not matching. Please provide valid key")
        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False

    elif response.status_code == 403 and option == "invalid_apiKey":
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")


    elif response.status_code == 202 and option == "empty_apiKey":
        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False

    elif response.status_code == 403 and option == "empty_apiKey":
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")


    elif response.status_code == 202 and option == "no_apiKey":

        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # assert (response_body["message"] == "Required authentication headers are missing..!!!!")
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            assert True
        elif "Required authentication headers are missing" in response_body["message"]:
            assert True
        else:
            assert False

    elif response.status_code == 403 and option == "no_apiKey":
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0


    elif response.status_code == 202 and option == "empty_x-requestor":

        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

    elif response.status_code == 403 and option == "empty_x-requestor":
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "x-requestor header cannot be blank")

    elif response.status_code == 202 and option == "no_x-requestor":
        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # assert (response_body["message"] == "Required authentication headers are missing")
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            assert True
        elif "Required authentication headers are missing" in response_body["message"]:
            assert True
        else:
            assert False

    elif response.status_code == 403 and option == "no_x-requestor":
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")


def verify_api_response_for_invalid_header(response, tc):
    assert (
            response.status_code == 403 or response.status_code == 400), "Status code is not 403/400. Rather found : " + str(
        response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if tc == "invalid_apiKey" or tc == "empty_apiKey" or tc == "empty_x-requestor_and_empty_apiKey" or  tc == "no_x-requestor_and_empty_apiKey":
        assert (response_body["message"] == "API keys are not matching. Please provide valid key" or response_body["message"] == "api keys are not matching. Please provide valid key")
    elif tc == "no_apiKey" or tc == "no_x-requestor" or tc == "no_x-requestor_and_no_apiKey" or tc == "empty_x-requestor_and_no_apiKey" or tc == "no_x-requestor_and_invalid_apiKey":
        assert (response_body["message"] == "Required authentication headers are missing")
    elif tc == "empty_x-requestor" or tc == "empty_x-requestor_and_invalid_apiKey":
        assert (response_body["message"] == "x-requestor header cannot be blank")
    else:
        assert False
    return
