from lib2to3.pgen2 import driver
import selenium
from selenium.webdriver.common.by import By

class HomePage:

    shop = (By.XPATH, '//a[text()="Shop"]')

    def shopItems(self):
        driver.find_element(*HomePage.shop)
