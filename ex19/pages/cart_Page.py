from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def moveToCartPage(self, wd):
        loc_cart=(By.XPATH,'//div[@id="cart"]/a[@class="link"]')
        wd.find_element(*loc_cart).click()

    def isCartEmpty(self, wd):
        loc_remove_button = (By.XPATH, '//button[@value="Remove"]')
        if len(wd.find_elements(*loc_remove_button))>0:
            return False
        else:
            return True

    def removeProduct(self, wd):
        loc_remove_button = (By.XPATH, '//button[@value="Remove"]')
        remove_button = wd.find_element(*loc_remove_button)
        remove_button.click()
        WebDriverWait(wd, 10).until((EC.staleness_of(remove_button)))

