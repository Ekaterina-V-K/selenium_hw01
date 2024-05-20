from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.mainUrl = ("http://localhost/litecart/en/")
        self.wait = WebDriverWait(driver, 10)

    def moveToMainPage(self):
        return self.driver.get(self.mainUrl)

    def moveToProductCart(self, wd, num):
        loc_duck=(By.XPATH,f'//ul[@class="listing-wrapper products"]/li[{num}]/a[@class="link"]')
        wd.find_element(*loc_duck).click()
