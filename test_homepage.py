
from lib2to3.pgen2 import driver
from selenium import webdriver
import time as sl
import pytest

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage 
from test_data.HomePageData import HomePageData

class TestHomePage(BaseClass): 
    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        log = self.getLogger()
        log.info("First Name is "+getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        log.info("Last Name is "+getData["lastname"])
        homepage.getmail().send_keys(getData["lastname"])
        homepage.getcheckbox().click() 
        homepage.getsubmit().click()
        log.info("Submitted successfully")

        alertText =homepage.getSuccess().text
        assert ('Success' in alertText)
        self.driver.refresh()
  
    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self,request):
        return request.param