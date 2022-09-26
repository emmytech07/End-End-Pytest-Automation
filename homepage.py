from optparse import Option
import pytest
from selenium import webdriver
import time as sl

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("D:/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ilesanmi Emmanuel")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("Iles@gmail.com")
# driver.find_element(By.ID, '#exampleInputPassword1').send_keys('Password')
driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
# driver.find_element(By.ID, '#exampleFormControlSelect1').click()
sl.sleep(5)
# driver.find_element(By.XPATH, "//option[contains(text(),'Male')]").click()
# driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

alertText = driver.find_element(By.CSS_SELECTOR, '[class*="alert-success"]').text
assert ('Success' in alertText)
