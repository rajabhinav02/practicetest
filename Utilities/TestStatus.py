import logging

from Base.SeleniumDriver import SeleniumDrivers
import Utilities.cllogging as cl


class TestResultStatus(SeleniumDrivers):
    log = cl.custom_logging(logging.DEBUG)

    def __init__(self, driver):
        super(TestResultStatus,self).__init__(driver)
        self.driver=driver
        self.resultlist = []

    def SetTestStatus(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info("##Validation is pass for "+resultmessage)
                else:
                    self.resultlist.append("Fail")
                    self.getScreenshot(resultmessage)
                    self.log.error("##Validation is failed for "+resultmessage)
            else:
                self.resultlist.append("Fail")
                self.getScreenshot(resultmessage)
                self.log.error("##Validation is failed for "+resultmessage)
        except:
            self.resultlist.append("Fail")
            self.getScreenshot(resultmessage)
            self.log.error("##Validation is failed for "+resultmessage)

    def TestStatus(self, result, resultmessage):
        self.SetTestStatus(result,resultmessage)

    def TestStatusFinal(self, result, resultmessage, tcname):
        self.SetTestStatus(result, resultmessage)

        if "Fail" in self.resultlist:
            self.log.error("Test Case "+tcname + " failed")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info("Test Case "+tcname + "passed")
            self.resultlist.clear()
            assert True == True


