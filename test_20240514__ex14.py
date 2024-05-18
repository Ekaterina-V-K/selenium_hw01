import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


link = "http://localhost/litecart/admin/?app=countries&doc=countries"

@pytest.fixture(params=['chrome','edge','firefox'])
# @pytest.fixture(params=['chrome'])
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
    # ОТКРЫТЬ на редактирование страну (откроем первую в списке)
    driver.find_element(By.XPATH, '//table[@class="dataTable"]/tbody/tr[@class="row"]/td[5]/a').click()
    main_tab = driver.current_window_handle
    # найти элементы - ссылки с иконкой в виде квадратика со стрелкой
    elements=driver.find_elements(By.XPATH,'//i[@class="fa fa-external-link"]/parent::*')  # элементы - ссылки
    for el in elements:
    # -кликнуть по элементу
        el.click()
        # -дождаться пока откроется новое окно
        wait.until(EC.number_of_windows_to_be(2))
        list_of_tabs = driver.window_handles
        # -переключиться в новое окно
        for window_handle in driver.window_handles:
            if window_handle != main_tab:
                driver.switch_to.window(window_handle)
                break
        # -закрыть новое окно
        driver.close()
        # -переключиться на основное окно (редактирование страны)
        driver.switch_to.window(main_tab)

    time.sleep(3)