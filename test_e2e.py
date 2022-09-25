
from lib2to3.pgen2 import driver
from selenium import webdriver
import time as sl
import pytest

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # self.driver.find_element(By.XPATH, value='//a[text()="Shop"]').click()

        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        products = self.driver.find_elements(by='xpath', value='//div[@class="card h-100"]')
        for product in products:

            productName = product.find_element(By.XPATH, value='./div/h4/a').text
            
            if productName== 'iphone X':
                product.find_element(By.XPATH, value='./div/button').click()
            
        self.driver.find_element(By.XPATH, value="//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, value="button[class='btn btn-success']").click()
        self.driver.find_element(By.XPATH, value="//input[@id='country']").send_keys('ind')
        wait =WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT,"India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, value='div[class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, value='input[type=submit]').click()
        self.driver.implicitly_wait(5)
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        sl.sleep(5)
        assert "Success! Thank you!" in successText 
        self.driver.quit()