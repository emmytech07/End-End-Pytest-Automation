
from selenium import webdriver
import time as sl
import pytest

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage 

class TestHomePage(BaseClass): 
    def test_formSubmission(self):
        homepage = HomePage(self.driver)
        homepage.getname().send_keys("Ilesanmi Emmanuel")
        homepage.getmail().send_keys("Ile07@gmail.com")
        homepage.getcheckbox().click() 
        homepage.getsubmit().click()

        alertText =homepage.getSuccess().text
        assert ('Success' in alertText)