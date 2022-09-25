import selenium
from selenium.webdriver.common.by import By
class ConfirmedPage:

    def __init__(self, driver):
        self.driver = driver 

    sendkeys  = (By.XPATH, "//input[@id='country']")
    
    def sendKeys(self):
        return self.driver.find_element(*ConfirmedPage.sendkeys)
    
