
import email
import selenium
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver ):
        self.driver = driver

    shop = (By.XPATH, '//a[text()="Shop"]')
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CSS_SELECTOR, '[class*="alert-success"]')

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getmail(self):
        return self.driver.find_element(*HomePage.email)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)
