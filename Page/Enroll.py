from Base.SeleniumDriver import SeleniumDrivers
from Page.Homepage import Homepage


class EnrollCourse(SeleniumDrivers):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    __coursetext= "//h1[contains(@class, 'dynamic-heading')]"
    __enrollbutton = "//button[contains(@class, 'dynamic-button')]"

    def validateCoursename(self, coursename):
        selectedcouretext=self.getText(self.__coursetext, "xpath")
        if coursename in selectedcouretext:
            return True
        else:
            return False

    def clickEnroll(self):
        self.clickElement(self.__enrollbutton, "xpath")





