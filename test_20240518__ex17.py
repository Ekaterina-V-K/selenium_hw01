import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


link = "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1"

#@pytest.fixture(params=['chrome','edge','firefox'])
@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param.lower() == 'chrome':
        wd = webdriver.Chrome()
    elif request.param.lower() == 'firefox':
        wd = webdriver.Firefox()
    elif request.param.lower() == 'edge':
        wd = webdriver.Edge()
    else:
        print("Неподдерживаемый браузер!")
        return
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    loc = (By.XPATH, '//table[@class="dataTable"]/tbody/tr[@class="row"]/td[3]/a[contains(@href,"product_id=")]')
    el_products = driver.find_elements(*loc)
    el_product_l = len(el_products)
    for indx in range(el_product_l):  # цикл по строкам стран
        el_products = driver.find_elements(*loc)
        el = el_products[indx]
        el.click()
        driver.back()
    for l in driver.get_log("browser"):
        print(l)


