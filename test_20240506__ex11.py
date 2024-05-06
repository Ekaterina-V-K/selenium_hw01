import pytest
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link="http://localhost/litecart/en/create_account"

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
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
   #  заполняем поля

   # придумаем логин и пароль
    user_email=generate_unique_email()
    driver.find_element(By.XPATH,'//input[@type="text" and @name="firstname"]').send_keys("Ivan")
    driver.find_element(By.XPATH,'//input[@type="text" and @name="lastname"]').send_keys("Ivanov")
    driver.find_element(By.XPATH,'//input[@type="text" and @name="address1"]').send_keys("1st street")
    driver.find_element(By.XPATH,'//input[@type="text" and @name="postcode"]').send_keys("12345")
    driver.find_element(By.XPATH,'//input[@type="text" and @name="city"]').send_keys("LA")
    # country_el= driver.find_element(By.XPATH,'//select[@name="country_code"]/option[@value="US"]')
    country_el= driver.find_element(By.XPATH,'//select[@name="country_code"]')
    # Создаем объект класса Select, который представляет выпадающий список
    select = Select(country_el)
    # Устанавливаем значение в выпадающем списке по тексту опции
    select.select_by_visible_text("United States")

    driver.find_element(By.XPATH,'//input[@type="email" and @name="email"]').send_keys(user_email)
    driver.find_element(By.XPATH,'//input[@type="tel" and @name="phone"]').send_keys("+12345678999")
    passwd='123456'
    driver.find_element(By.XPATH,'//input[@type="password" and @name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH,'//input[@type="password" and @name="confirmed_password"]').send_keys(passwd)
    time.sleep(3)
    # Жмем на кнопку создать аккаунт
    driver.find_element(By.XPATH, '//button[@name="create_account"]').click()
    time.sleep(3)
    #разлогиниваемся
    driver.find_element(By.XPATH, '//a[text()="Logout"]').click()
    #логинимся на главной странице
    driver.find_element(By.XPATH, '//input[@type="text" and @name="email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH, '//button[@name="login"]').click()
    time.sleep(2)
    #разлогиниваемся
    driver.find_element(By.XPATH, '//a[text()="Logout"]').click()




