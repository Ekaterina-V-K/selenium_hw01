import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


loc_lvl0="//ul[@id='box-apps-menu']/li[@id='app-']"
loc_lvl1="//ul[@class='docs']//span[@class='name']"
link="http://localhost/litecart/admin/"


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    #wd = webdriver.Edge()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    time.sleep(2)
    for indx in range(17):
        elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.XPATH,loc_lvl0))
        elements[indx].click()
        print(elements[indx].text)
        time.sleep(1)
