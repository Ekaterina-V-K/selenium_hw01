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
    #wd = webdriver.Firefox()
    #wd = webdriver.Edge()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def check_exists_by_loc(drv,loc):
    # try:
    #     drv.find_elements(By.XPATH, loc)
    # except NoSuchElementException:
    #     return False
    # return True
    return bool(drv.find_elements(By.XPATH, loc))

def test_example(driver):
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    elements=driver.find_elements(By.XPATH, loc_lvl0)
    elements_count =len(elements)
    assert check_exists_by_loc(driver,loc_h1), "Не найден заголовок H1 в корне сайта"

    for indx in range(elements_count):
       elements = driver.find_elements(By.XPATH, loc_lvl0)
       el=elements[indx]
       print(el.text)
       el.click()
       time.sleep(0)
       #el_h1 = driver.find_element(By.XPATH, loc_h1)  # ищем элемент h1
       el_h1 = driver.find_elements(By.XPATH, loc_h1)  # ищем элемент h1
       assert len(el_h1), "Не найден заголовок H1"
       print('H1:', el_h1[0].text)
       #Обход вложенных элементов
       elements_1 = driver.find_elements(By.XPATH, loc_lvl1)
       elements_1_count = len(elements_1)
       for indx1 in range(elements_1_count):
           elements_1 = driver.find_elements(By.XPATH, loc_lvl1)
           el1 = elements_1[indx1]
           print('>',el1.text)
           el1.click()
           el_h1 = driver.find_elements(By.XPATH, loc_h1)  # ищем элемент h1
           assert len(el_h1), "Не найден заголовок H1"
           print('>H1:', el_h1[0].text)
           time.sleep(0)


       #print(el_h1)
       #assert  el_h1!=None,   'Элемент H1 на вкладке не найден'
       #перебираем внутренние элементы
       #time.sleep(0)