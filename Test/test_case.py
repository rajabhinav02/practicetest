import time

import pytest

from Page.Confirm import Confirmation
from Page.CourseList import CourseList
from Page.Enroll import EnrollCourse
from Page.Homepage import Homepage
from Utilities.TestStatus import TestResultStatus


@pytest.mark.usefixtures("setup")
class TestCourse:

    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.hm = Homepage(self.driver)
        self.co= CourseList(self.driver)
        self.en = EnrollCourse(self.driver)
        self.ts = TestResultStatus(self.driver)
        self.conf = Confirmation(self.driver)

    def test_signin(self):
        self.hm.click_signin()
        signinb = self.hm.validate_signin()
        self.ts.TestStatusFinal(signinb, "sign-in", "test_signin")

    def test_login(self, testd): #testdatainputsignin):
        self.hm.login(testd["Username"], testd["Password"])
        loginb = self.hm.validate_login()
        self.ts.TestStatusFinal(loginb, "Login Test", "test_login")


    def test_selectandvalidatecourse(self, testdatainputcourse):
        self.co.selectclickcourse(testdatainputcourse["Course_Name"])
        selectcourse=self.en.validateCoursename(testdatainputcourse["Course_Name"])
        self.ts.TestStatusFinal(selectcourse,"Selected Course", "test_selectandvalidatecourse")

    def test_Enroll(self, testd):#testcardinput):
        self.en.clickEnroll()
        self.conf.payment(testd["Country"], testd["Card_Number"], testd["Expiry_Date"], testd["CVV"])
        self.conf.waitformessage(5)
        finaltext = self.conf.validatetext()
        self.ts.TestStatusFinal(finaltext, "Enroll and Payment", "test_Enroll")

    """
    def test_payment(self):
        text= self.conf.validatetext()
        self.ts.TestStatusFinal(text,"Enroll and Payment", "test_payment")
    """






