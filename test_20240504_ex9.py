import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

loc_countries='//table[@class="dataTable"]/tbody/tr[@class="row"]/td[3]/a'
loc_geo="//table[@class='dataTable']/tbody/tr[ not (@class='header')]/td[3]/select/option[@selected='selected']"
link="http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    time.sleep(1)
    country_rows = driver.find_elements(By.XPATH, loc_countries)
    country_row_l = len(country_rows)
    for indx in range(country_row_l):  # цикл по строкам стран
        country_rows = driver.find_elements(By.XPATH, loc_countries)
        cr = country_rows[indx]
        cr.click()
        time.sleep(2)
        el_geo=driver.find_elements(By.XPATH, loc_geo)
        country_geo=[]

        for el in el_geo:
            country_geo.append(el.get_attribute('text'))
        c_g=country_geo.copy()
        c_g.sort()
        if c_g!=country_geo:
            print(f"Список геозон страны {cr.get_attribute('textContent')} не отсортирован")
        driver.back()
        time.sleep(3)