import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

loc_countries = '//tr[@class="row"]//td/a[text()]'
link = "http://localhost/litecart/admin/?app=countries&doc=countries"
#link_country_zone = 'http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code='
loc_country_row='//tr[@class="row"]'


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_8_check_countries(driver):  # Проверка списка стран на сортировку
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    time.sleep(1)
    countries = driver.find_elements(By.XPATH, loc_countries)
    name_countries = []
    for country in countries:  # цикл по странам
        name_countries.append(country.get_attribute('text'))
    sort_c=name_countries.copy()
    sort_c.sort()
    if sort_c != name_countries:
        print("Список стран не отсортирован по алфавиту")

def test_8_check_geo(driver):  # Проверка списка стран на сортировку
    driver.get(link)
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    time.sleep(1)
    country_rows = driver.find_elements(By.XPATH, loc_country_row)
    #name_countries = []
    country_row_l=len(country_rows)
    for indx in range(country_row_l):  # цикл по строкам стран
        country_rows = driver.find_elements(By.XPATH, loc_country_row)
        cr=country_rows[indx]
        count_zones=int(cr.find_element(By.XPATH,'td[6]').get_attribute('textContent'))
        if count_zones>0:
            print(cr.find_element(By.XPATH,'td[5]').get_attribute('textContent'), count_zones)

            link_geo=cr.find_element(By.XPATH,'td[5]/a').get_attribute('href')
            driver.get(link_geo)
            #Собрать массив геозон
            loc_geo_name='//table[@class="dataTable"]/tbody/tr[ not(@class="header")]/td[3]'
            geo_names=driver.find_elements(By.XPATH,loc_geo_name)
            names=[]
            for zone_name in geo_names:
                names.append(zone_name.get_attribute('textContent'))
            sort_names=names.copy()
            sort_names.sort()
            if sort_names!=names:
                print(f"Список геозон страны {cr.find_element(By.XPATH,'td[5]').get_attribute('textContent')} не отсортирован по алфавиту")
            #Вернемся на страницу с списком стран
            time.sleep(2)
            driver.back()


