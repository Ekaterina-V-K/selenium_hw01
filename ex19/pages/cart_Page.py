from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def moveToCartPage(self):
        loc_cart=(By.XPATH,'//div[@id="cart"]/a[@class="link"]')
        self.driver.find_element(*loc_cart).click()

    def isCartEmpty(self):
        loc_remove_button = (By.XPATH, '//button[@value="Remove"]')
        if len(self.driver.find_elements(*loc_remove_button))>0:
            return False
        else:
            return True

    def removeProduct(self):
        loc_remove_button = (By.XPATH, '//button[@value="Remove"]')
        remove_button = self.driver.find_element(*loc_remove_button)
        remove_button.click()
        WebDriverWait(self.driver, 10).until((EC.staleness_of(remove_button)))