import pytest
from selenium import webdriver
import time as sl

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = Service("D:/chromedriver/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("http://www.rahulshettyacademy.com/angularpractice/")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        pass

    elif browser_name == "IE":
        # driver = webdriver.
        pass

    request.cls.driver = driver
    yield
    driver.close()
    