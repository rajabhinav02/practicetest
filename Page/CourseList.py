from Base.SeleniumDriver import SeleniumDrivers



class CourseList(SeleniumDrivers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __courseinput = "[name='course']"
    __searchbutton = "[class*='fa-search']"
    __courselinkmain = "//h4[@class='dynamic-heading' and contains(text(),'{0}')]"

    def send_cousename(self, coursename):
        self.sendData(self.__courseinput, coursename, "css")

    def click_search(self):
        self.clickElement(self.__searchbutton, "css")

    def clickcourse(self, coursename):
        __actualcourselink = self.__courselinkmain.format(coursename)
        self.clickElement(__actualcourselink, "xpath")

    def selectclickcourse(self, coursename):
        self.send_cousename(coursename)
        self.click_search()
        self.clickcourse(coursename)



