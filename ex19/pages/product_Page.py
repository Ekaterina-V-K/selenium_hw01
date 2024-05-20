from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def isFindedElementSize(self, wd):
        loc_size = (By.XPATH, '//select[@name="options[Size]"]')
        try:
            # Находим элемент size
            el_size = wd.find_element(*loc_size)
            return True
        except NoSuchElementException:
            return False

    def selectSizeDucks(self, wd):
        loc_size = (By.XPATH, '//select[@name="options[Size]"]')
        el_size = wd.find_element(*loc_size)
        wd.execute_script(f"arguments[0].selectedIndex={1}; arguments[0].dispatchEvent(new Event('change'))",el_size)

    def addProduct(self, wd):
        loc_button = (By.XPATH, '//button[@value="Add To Cart"]')
        wd.find_element(*loc_button).click()

    def waitAddedToCart(self, wd, i):
        loc_cart_counter = (By.XPATH, '//span[@class="quantity"]')
        WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element(loc_cart_counter, str(i)))
        loc_back_to_main=(By.XPATH,'//div[@id="logotype-wrapper"]')
        wd.find_element(*loc_back_to_main).click()
