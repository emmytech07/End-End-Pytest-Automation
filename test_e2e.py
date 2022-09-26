

from selenium import webdriver
import time as sl
import pytest

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.CheckOut import CheckOutPage
from PageObjects.HomePage import HomePage

from PageObjects.ConfirmedPage import ConfirmedPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # self.driver.find_element(By.XPATH, value='//a[text()="Shop"]').click()

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckOutPage(self.driver)
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            # print(cardText)
            if cardText== 'iphone X':
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getCheckOne().click()
        checkOutPage.getCheckTwo().click()


        confirmPage = ConfirmedPage(self.driver)
        confirmPage.sendKeys().send_keys('ind')
        #Run explicit
        self.varifyLinkPresence("India")

        confirmPage.sendKeys2().click()
        confirmPage.chekBox().click()
        confirmPage.ClickConfirm().click()

        self.driver.implicitly_wait(5)
        successText = confirmPage.successTexT().text
        sl.sleep(5)
        assert "Success! Thank you!" in successText 
        self.driver.quit()