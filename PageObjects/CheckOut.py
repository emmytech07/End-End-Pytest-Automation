import selenium
from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self, driver ):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOne  =  (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkTwo  = (By.CSS_SELECTOR,"button[class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCheckOne(self):
        return self.driver.find_element(*CheckOutPage.checkOne)
    
    def getCheckTwo(self):
        return self.driver.find_element(*CheckOutPage.checkTwo)
    
    