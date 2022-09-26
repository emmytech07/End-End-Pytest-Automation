
from lib2to3.pgen2 import driver
from selenium import webdriver
import time as sl
import pytest

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage 

class TestHomePage(BaseClass): 
    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getData[0])
        homepage.getmail().send_keys(getData[1])
        homepage.getcheckbox().click() 
        homepage.getsubmit().click()

        alertText =homepage.getSuccess().text
        assert ('Success' in alertText)
        self.driver.refresh()
  
    @pytest.fixture(params=[("ilesanmi", "Emmanuel"),("John wesley", 'Faith')  ])
    def getData(self,request):
        return request.param