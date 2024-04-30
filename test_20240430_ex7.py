import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

loc_prod="//div[@class='image-wrapper']"
loc_stick="div.sticker"
link="http://localhost/litecart/en/"


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get(link)
    time.sleep(1)
    products=driver.find_elements(By.XPATH, loc_prod)
    for prod in products: #цикл по товарам
       print(prod.find_element(By.XPATH,"//div[@class='image-wrapper']/img").get_attribute('alt'), \
              'имеет стикер', prod.find_elements(By.CSS_SELECTOR, loc_stick)[0].get_attribute('Title') )
       assert  len(prod.find_elements(By.CSS_SELECTOR, loc_stick))==1, "Стикер не один"
