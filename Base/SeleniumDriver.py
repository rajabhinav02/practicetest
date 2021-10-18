import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import Utilities.cllogging as cl
import logging

class SeleniumDrivers:
    log = cl.custom_logging(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def getBytype(self, locatortype):
        """
        getting the ByType
        """
        try:
            locatortype = locatortype.lower()
            if locatortype == "id":
                return By.ID
            elif locatortype == "xpath":
                return By.XPATH
            elif locatortype == "css":
                return By.CSS_SELECTOR
            elif locatortype == "class":
                return By.CLASS_NAME
            elif locatortype == "link":
                return By.LINK_TEXT
            elif locatortype == "name":
                return By.NAME
            elif locatortype == "tag":
                return By.TAG_NAME
            elif locatortype == "patiallink":
                return By.PARTIAL_LINK_TEXT

            self.log.info("By type of locator type "+locatortype +" is returned")
        except:
            self.log.error("By type of locator type "+locatortype + " is not returned")

    def getElement(self,locator,locatortype="id"):
        """

        :param locator:
        :param locatortype:
        :return: element
        """
        try:
            locatortype = locatortype.lower()
            byType = self.getBytype(locatortype)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element with locatortype "+locatortype +" and locator "+locator+ " is returned")
            return element
        except:
            self.log.info("Element with locatortype " + locatortype + " and locator " + locator + " is not returned")

    def getElementList(self, locator, locatortype="id"):
        """
        getting the list of elements
        :param locator:
        :param locatortype:
        :return:
        """
        try:
            locatortype = locatortype.lower()
            byType = self.getBytype(locatortype)
            elementlist = self.driver.find_elements(byType,locator)
            self.log.info("Elementlist with locatortype " + locatortype + " and locator " + locator + " is returned")
            return elementlist
        except:
            self.log.info("Elementlist with locatortype " + locatortype + " and locator " + locator + " is not returned")

    def clickElement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locator, locatortype)
            if element is not None:
                element.click()
                self.log.info("Element with locatortype " + locatortype + " and locator " + locator + " is clicked")
            else:
                self.log.error("Element with locatortype " + locatortype + " and locator " + locator + " is not clicked")
        except:
            self.log.error("Element with locatortype " + locatortype + " and locator " + locator + " is not found")

    def sendData(self, locator, data, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locator, locatortype)
            if element is not None:
                element.send_keys(data)
                self.log.info("Data with locatortype " + locatortype + " and locator " + locator + " is send")
            else:
                self.log.error("Data with locatortype " + locatortype + " and locator " + locator + " is not send")
        except:
            self.log.error("Data with locatortype " + locatortype + " and locator " + locator + " is not found")

    def getTitle(self):
        try:
            titlename = self.driver.title
            self.log.info("Title is returned "+titlename)
            return titlename
        except:
            self.log.error("No title is returned")

    def validateEnabled(self,locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locator,locatortype)
            if element.is_enabled():
                self.log.info("element with locator "+locator +" and locatortype "+locatortype+" is enabled")
                return True
            else:
                self.log.info("element with locator " + locator + " and locatortype " + locatortype + " is disabled")
                return False
        except:
            self.log.error("no element with locator "+locator +"and locatortype "+locatortype +" is found ")

    def validatePresence(self, locator, locatortype="id"):

            locatortype = locatortype.lower()
            elementlist = self.getElementList(locator, locatortype)
            if len(elementlist) > 0:
                self.log.info("Element with locator "+locator +" and locatortype "+locatortype +"is present")
                return True
            else:
                self.log.info("Element with locator " + locator + " and locatortype " + locatortype + "is not present")
                return False

    def clickAllRadio(self, locator,locatortype="id"):
        try:
            locatortype = locatortype.lower()
            elementlist = self.getElementList(locator, locatortype)
            for element in elementlist:
                element.click()
                time.sleep(2)
            self.log.info("All elements with locator " +locator +" and locatortype "+locatortype +"is clicked")
        except:
            self.log.error("All elements with locator " + locator + " and locatortype " + locatortype + "is not clicked")

    def selectDropdown(self, value, locator,locatortype="id"):
        try:
            locatortype= locatortype.lower()
            select= Select(self.getElement(locator,locatortype))
            select.select_by_visible_text(value)
            self.log.info("Dropdown with locator "+locator +"and locatortype "+locatortype +" is selected with visible text "+value)
        except:
            self.log.error("Dropdown with locator "+locator +"and locatortype "+locatortype +" is not found")

    def waitingpresence(self,locator, waittime, locatortype="id"):
        try:
            wait = WebDriverWait(self.driver, waittime)
            byType= self.getBytype(locatortype)
            wait.until(expected_conditions.presence_of_element_located((byType,locator)))
            self.log.info("waiting for presence of locator "+locator +" and locatortype"+locatortype)
        except:
            self.log.error("Issue with wait")

    def getScreenshot(self, resultmessage):
        filename = resultmessage+ str(round(time.time()*1000))+ ".png"
        screenshotdirectory= "../Screenshots/"
        relativefilename = screenshotdirectory+filename
        currentdirectory = os.path.dirname(__file__)
        screenshotfilename = os.path.join(currentdirectory, relativefilename)
        destinationdirectory = os.path.join(currentdirectory,screenshotdirectory)

        try:
            if not os.path.exists(destinationdirectory):
                os.makedirs(destinationdirectory)
            self.driver.save_screenshot(screenshotfilename)
            self.log.info("screenshot taken and saved at "+destinationdirectory)
        except:
            self.log.error("no screenshot taken")


    def getText(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element= self.getElement(locator, locatortype)

            elementtext = element.text

            self.log.info("Text returned for element with locator "+locator +" and locatortype "+locatortype +" is "+elementtext)
            return elementtext
        except:
            self.log.error("Text not returned for element with locator "+locator +" and locatortype "+locatortype)


    def webscroll(self, direction ="up"):

        if direction == "up":
            self.driver.execute_script("window.scroll(0,-1000);")
        elif direction == "down":
            self.driver.execute_script("window.scroll(0, 1000);")


    def scrollinview(self, locator, locatortype="id"):
        try:
            locatortype= locatortype.lower()
            element = self.getElement(locator, locatortype)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info("scrolled to element with locator "+locator +" and locatortype "+locatortype)
        except:
            self.log.error("scrolling failed to element with locator " + locator + " and locatortype " + locatortype)

    def switchframe(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locator, locatortype)
            self.driver.switch_to.frame(element)
            self.log.info("switched to frame with locator "+locator +" and locatortype "+locatortype)
        except:
            self.log.error("not switched to frame with locator " + locator + " and locatortype " + locatortype)

    def switchdefaultfromframe(self):
        try:
            self.driver.switch_to.default_content()
            self.log.info("switched to default from frame")
        except:
            self.log.error("not switched to default from frame")








