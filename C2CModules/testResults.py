# =========================================
# Test Results
# =========================================

def testResult(self, TC, subResultTC, resultNote):
    try:
        # if TC == "passed":
        #     subresult = self.result.get_or_create_subresult(subResultTC)
        #     subresult.set_result(TestResults.passed)
        #     subresult.add_note(resultNote)
        #     self.result.set_result(TestResults.passed)
        #     self.result.add_note(resultNote)
        #     assert True
        #
        # elif TC == "failed":
        #     subresult = self.result.get_or_create_subresult(subResultTC)
        #     subresult.set_result(TestResults.failed)
        #     subresult.add_note(resultNote)
        #     self.result.set_result(TestResults.failed)
        #     self.result.add_note(resultNote)
        #     assert False
        #
        # elif TC == "verificationFailed":
        #     subresult = self.result.get_or_create_subresult(subResultTC)
        #     subresult.set_result(TestResults.failed)
        #     subresult.add_note(resultNote)
        #     print("\n")
        if TC == "passed":
            print("Expected behaviour : => ", subResultTC)
            print("Actual behaviour : => ", resultNote)
            print("\n")
            assert True

        elif TC == "failed":
            print("Expected behaviour : => ", subResultTC)
            print("Actual behaviour : => ", resultNote)
            print("\n")
            assert False
        elif TC == "verificationFailed":
            print("Expected behaviour : => ", subResultTC)
            print("Actual behaviour : => ", resultNote)
            print("\n")
            # assert False
        elif TC == "verificationPassed":
            print("Expected behaviour : => ", subResultTC)
            print("Actual behaviour : => ", resultNote)
            print("\n")
    except AttributeError:
        print("Test Case Status", TC)
        print("Expected behaviour : => ", subResultTC)
        print("Actual behaviour : => ", resultNote)
        if TC == "failed":
            assert False