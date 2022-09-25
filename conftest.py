import pytest
from selenium import webdriver
import time as sl

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("D:/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://www.rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
    