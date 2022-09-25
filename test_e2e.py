from selenium import webdriver
import time as sl
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testone:

    def test_e2e(self):

        service_obj = Service("D:/chromedriver/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)

        driver.maximize_window()
        driver.get("http://www.rahulshettyacademy.com/angularpractice/")

        driver.find_element(By.XPATH, value='//a[text()="Shop"]').click()
        products = driver.find_elements(by='xpath', value='//div[@class="card h-100"]')
        for product in products:

            productName = product.find_element(By.XPATH, value='./div/h4/a').text
            
            if productName== 'iphone X':
                product.find_element(By.XPATH, value='./div/button').click()
            
        driver.find_element(By.XPATH, value="//a[@class='nav-link btn btn-primary']").click()
        driver.find_element(By.CSS_SELECTOR, value="button[class='btn btn-success']").click()
        driver.find_element(By.XPATH, value="//input[@id='country']").send_keys('ind')
        wait =WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT,"India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.CSS_SELECTOR, value='div[class="checkbox checkbox-primary"]').click()
        driver.find_element(By.CSS_SELECTOR, value='input[type=submit]').click()
        driver.implicitly_wait(5)
        successText = driver.find_element(By.CLASS_NAME, "alert-success").text
        sl.sleep(5)
        assert "Success! Thank you!" in successText 
        driver.quit()