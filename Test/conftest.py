import pytest
from selenium import webdriver

from TestData.testdata import Testdata


def pytest_addoption(parser):
    parser.addoption("--browser_name", action= "store", default = "chrome")
    parser.addoption("--channel_name", action = "store", default = "cut")

#def pytest_addoptionagain(parser):
    #parser.addoptionagain("--channel", action = "store", default = "ete")


@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("browser_name")
    channelname= request.config.getoption("channel_name")

    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        if channelname == "ete":
            driver.maximize_window()
            driver.get("https://www.google.com")
        elif channelname == "cut":
            driver.maximize_window()
            driver.get("https://courses.letskodeit.com/")

    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
        if channelname == "ete":
            driver.maximize_window()
            driver.get("https://www.google.com")
        elif channelname == "cut":
            driver.maximize_window()
            driver.get("https://courses.letskodeit.com/")

    #driver.maximize_window()
    #driver.get("https://courses.letskodeit.com/")
    if request.cls is not None:
        request.cls.driver= driver
    yield
    driver.quit()


@pytest.fixture(params= Testdata.dataexcelinput("test_login"))
def testdatainputsignin(request):
    return request.param

@pytest.fixture(params= Testdata.dataexcelinput("test_selectandvalidatecourse"))
def testdatainputcourse(request):
    return request.param

@pytest.fixture(params= Testdata.dataexcelinput("test_Enroll"))
def testcardinput(request):
    return request.param

@pytest.fixture(params=Testdata.testdatavalue)
def testd(request):
    return request.param