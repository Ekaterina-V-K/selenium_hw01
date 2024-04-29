import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

loc_lvl0="//ul[@id='box-apps-menu']/li[@id='app-']"
loc_lvl1="//ul[@class='docs']//span[@class='name']"
loc_h1="//h1"
link="http://localhost/litecart/admin/"

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def check_exists_by_loc(drv,loc):
    return bool(drv.find_elements(By.XPATH, loc))

def test_example(driver):
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    elements=driver.find_elements(By.XPATH, loc_lvl0)
    elements_count =len(elements)
    for indx in range(elements_count):
       elements = driver.find_elements(By.XPATH, loc_lvl0)
       el=elements[indx]
       print(el.text)
       el.click()
       time.sleep(0)
       el_h1 = driver.find_element(By.XPATH, loc_h1)  # ищем элемент h1
       assert check_exists_by_loc(driver,loc_h1), f"Не найден заголовок H1 в разделе {el.text}"
       print('H1:', el_h1.text)
       #Обход вложенных элементов
       elements_1 = driver.find_elements(By.XPATH, loc_lvl1)
       elements_1_count = len(elements_1)
       for indx1 in range(elements_1_count):
           elements_1 = driver.find_elements(By.XPATH, loc_lvl1)
           el1 = elements_1[indx1]
           print('>',el1.text)
           el1.click()
           el_h1 = driver.find_element(By.XPATH, loc_h1)  # ищем элемент h1
           assert check_exists_by_loc(driver,loc_h1), f"Не найден заголовок H1 в разделе {el.text}>{el1.text}"
           print('> H1:', el_h1.text)