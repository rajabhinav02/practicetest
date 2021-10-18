from Base.SeleniumDriver import SeleniumDrivers


class Confirmation(SeleniumDrivers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __framecard = "//iframe[contains(@title, 'Secure card number')]"
    __framedate = "//iframe[contains(@title, 'Secure expiration date')]"
    __framesecurity = "//iframe[contains(@title, 'Secure CVC')]"
    __Cardlocation = "[placeholder='Card Number']"
    __expirydate = "[placeholder='MM / YY']"
    __SecurityCode = "[placeholder='Security Code']"
    __countryname = "country-list"  # name
    __confirmbutton = "[class*='sp-buy']"
    __finalmessage = "//li[contains(@class, 'card-no')]/span"

    def switchframecard(self):
        self.switchframe(self.__framecard, "xpath")

    def switchframedate(self):
        self.switchframe(self.__framedate, "xpath")

    def switchframesecurity(self):
        self.switchframe(self.__framesecurity, "xpath")

    def switchtodefault(self):
        self.switchdefaultfromframe()

    def sendcarddata(self, cardnumber):
        self.sendData(self.__Cardlocation, cardnumber, "css")

    def senddate(self, dateex):
        self.sendData(self.__expirydate, dateex, "css")

    def sendsecurity(self, code):
        self.sendData(self.__SecurityCode, code, "css")

    def selectcountry(self, country):
        self.selectDropdown(country,self.__countryname, "name")

    def clickconfirm(self):
        self.clickElement(self.__confirmbutton, "css")

    def getmessage(self):
        message = self.getText(self.__finalmessage, "xpath")
        return message

    def scrollview(self):
        self.scrollinview(self.__confirmbutton, "css")

    def payment(self, country, cardnumber="", dateex="", code=""):

        self.scrollview()
        self.switchframecard()
        self.sendcarddata(cardnumber)
        self.switchtodefault()
        self.switchframedate()
        self.senddate(dateex)
        self.switchtodefault()
        self.switchframesecurity()
        self.sendsecurity(code)
        self.switchtodefault()
        self.selectcountry(country)
        self.clickconfirm()

    def waitformessage(self,time):
        self.waitingpresence(self.__finalmessage, time, "xpath")

    def validatetext(self):
        message = self.getmessage()
        if "declined" in message:
            return True
        else:
            return False




