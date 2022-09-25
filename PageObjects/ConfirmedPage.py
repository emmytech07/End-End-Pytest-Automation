import selenium
from selenium.webdriver.common.by import By
class ConfirmedPage:

    def __init__(self, driver):
        self.driver = driver 

    sendkeys  = (By.XPATH, "//input[@id='country']")
    sendkeys2 = (By.LINK_TEXT, "India")
    checkbox  = (By.CSS_SELECTOR, 'div[class="checkbox checkbox-primary"]')
    clickConfirm = (By.CSS_SELECTOR, 'input[type=submit]')
    successText = (By.CLASS_NAME, "alert-success")

    def sendKeys(self):
        return self.driver.find_element(*ConfirmedPage.sendkeys)

    def sendKeys2(self):
        return self.driver.find_element(*ConfirmedPage.sendkeys2)
    
    def chekBox(self):
        return self.driver.find_element(*ConfirmedPage.checkbox)
    
    def ClickConfirm(self):
        return self.driver.find_element(*ConfirmedPage.clickConfirm)
    
    def successTexT(self):
        return self.driver.find_element(*ConfirmedPage.successText)

    
