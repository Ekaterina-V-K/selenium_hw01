import pytest
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

link = "http://localhost/litecart/en/create_account"


@pytest.fixture(params=['chrome','edge','firefox'])
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


def generate_unique_email():
    # Получаем текущую дату и время
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Формируем уникальный адрес электронной почты
    unique_email = f"test_{current_time}@example.com"
    return unique_email


def test_ex11(driver):
    # открываем страницу регистрации нового пользователя
    driver.get(link)
    # заполняем поля
    # придумаем логин и пароль
    user_email = generate_unique_email()
    driver.find_element(By.XPATH, '//input[@type="text" and @name="firstname"]').send_keys("Ivan")
    driver.find_element(By.XPATH, '//input[@type="text" and @name="lastname"]').send_keys("Ivanov")
    driver.find_element(By.XPATH, '//input[@type="text" and @name="address1"]').send_keys("1st street")
    driver.find_element(By.XPATH, '//input[@type="text" and @name="postcode"]').send_keys("12345")
    driver.find_element(By.XPATH, '//input[@type="text" and @name="city"]').send_keys("LA")

    sel_country=Select(driver.find_element(By.XPATH, '//select[@name="country_code"]'))
    # Задаем значение, по которому будем искать индекс
    value_to_find = "United States"
    # Находим индекс элемента по его значению
    index = -1
    for option in sel_country.options:
        index += 1
        if option.text == value_to_find:
            indx_US=index
            break
    dropdown = driver.find_element(By.XPATH, '//select[@name="country_code"]')
    driver.execute_script(f"arguments[0].selectedIndex={indx_US}; arguments[0].dispatchEvent(new Event('change'))", dropdown)
    driver.find_element(By.XPATH, '//input[@type="email" and @name="email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//input[@type="tel" and @name="phone"]').send_keys("+12345678999")
    passwd = '123456'
    driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH, '//input[@type="password" and @name="confirmed_password"]').send_keys(passwd)
    time.sleep(3)
    # Жмем на кнопку создать аккаунт
    driver.find_element(By.XPATH, '//button[@name="create_account"]').click()
    time.sleep(3)
    # разлогиниваемся
    driver.find_element(By.XPATH, '//a[text()="Logout"]').click()
    # логинимся на главной странице
    driver.find_element(By.XPATH, '//input[@type="text" and @name="email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH, '//button[@name="login"]').click()
    time.sleep(2)
    # разлогиниваемся
    driver.find_element(By.XPATH, '//a[text()="Logout"]').click()
