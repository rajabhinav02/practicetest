from Base.SeleniumDriver import SeleniumDrivers



class Homepage(SeleniumDrivers):

    def __init__(self,driver):
        super(Homepage,self).__init__(driver)
        self.driver = driver


    __sign_in = "//a[@class='dynamic-link' and (text()= 'Sign In')]"
    __email = "//div[@class='form-group']//input[@placeholder='Email Address']"
    __password = "#password"
    __login_button = "//input[@value='Login']"
    __login_image = "//img[@class='zl-navbar-rhs-img ']"


    def click_signin(self):
        self.clickElement(self.__sign_in, "xpath")

    def send_email(self,email):
        self.sendData(self.__email, email, "xpath")

    def send_pwd(self, password):
        self.sendData(self.__password, password, "css")

    def click_login(self):
        self.clickElement(self.__login_button, "xpath")

    def login(self,email, password):
        #self.click_signin()
        self.send_email(email)
        self.send_pwd(password)
        self.click_login()





    def validate_signin(self):
        presence=self.validatePresence(self.__email, "xpath")
        if presence == True:
            return True
        else:
            return False

    def validate_login(self):
        presence = self.validatePresence(self.__login_image, "xpath")
        if presence == True:
            return True
        else:
            return False






