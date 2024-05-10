import pytest
import os
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

link = "http://localhost/litecart/admin/?app=catalog&doc=catalog"


@pytest.fixture(params=['chrome','edge','firefox'])
# @pytest.fixture(params=['firefox'])
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

def generate_unique_DuckCode():
    # Получаем текущую дату и время
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Формируем уникальный адрес электронной почты
    unique_DuckCode = f"{current_time}"
    return unique_DuckCode

def SetDatepicker(driver, XPATH_Selector, datestr):
    date_element=driver.find_element(By.XPATH,XPATH_Selector)
    driver.execute_script(f"arguments[0].value = '{datestr}';", date_element)

def test_ex12(driver):
    # открыть ссылку http://localhost/litecart/admin/?app=catalog&doc=catalog под администратором
    driver.get(link)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()
    time.sleep(1)
    # нажать на кнопку "Add New Product"
    driver.find_element(By.XPATH, '//a[@class="button"][text()=" Add New Product"]').click()
    time.sleep(1)
    # ------заполнить данные на вкладке General-------
    # Status
    loc='//input[@type="radio" and @name="status" and @value="1"]/parent::*'
    driver.find_element(By.XPATH, loc).click()
    Code=generate_unique_DuckCode()
    # Name
    Name="TestDuck"+Code
    driver.find_element(By.XPATH, '//input[@type="text" and @name="name[en]"]').send_keys(Name)
    # Code
    driver.find_element(By.XPATH, '//input[@type="text" and @name="code"]').send_keys(Code)
    # Categories
    loc='//input[@type="checkbox" and @data-name="Rubber Ducks"]'
    driver.find_element(By.XPATH, loc).click()
    # Product Groups
    loc='//input[@type="checkbox" and @name="product_groups[]" and @value="1-3"]'
    driver.find_element(By.XPATH, loc).click()
    # Quantity
    driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
    driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys("10")
    # Sold Out Status
    dropdown = driver.find_element(By.XPATH, '//select[@name="sold_out_status_id"]')
    driver.execute_script(f"arguments[0].selectedIndex={2}; arguments[0].dispatchEvent(new Event('change'))",dropdown)
    # DateValidFrom
    SetDatepicker(driver,'//input[@type="date" and @name="date_valid_from"]','2025-05-10')
    # DateValidTo
    SetDatepicker(driver,'//input[@type="date" and @name="date_valid_to"]','2025-05-10')
    # загрузить картинку!!!!!
    upload_file_field = driver.find_element(By.XPATH, '//input[@type="file" and @name="new_images[]"]')
    Image_path=f"{os.getcwd()}\\ex12\\test_duck.jpg"
    # Загружаем картинку
    upload_file_field.send_keys(Image_path)
    time.sleep(1)
    # -----заполнить данные на вкладке Information-------
    driver.find_element(By.XPATH, '//a[@href][text()="Information"]').click()
    # Manufacturer
    loc="//select[@name='manufacturer_id']"
    dropdown = driver.find_element(By.XPATH, loc)
    driver.execute_script(f"arguments[0].selectedIndex={1}; arguments[0].dispatchEvent(new Event('change'))", dropdown)
    # Short Description
    driver.find_element(By.XPATH, '//input[@type="text" and @name="short_description[en]"]').send_keys("Лучшая уточка")
    # Description
    driver.find_element(By.XPATH, '//div[@class="trumbowyg-editor"]').send_keys("Самая лучшая тестовая уточка")
    time.sleep(3)
    # -------заполнить данные на вкладке Prices---------
    driver.find_element(By.XPATH, '//a[@href][text()="Prices"]').click()
    # Purchase Price
    driver.find_element(By.XPATH, "//input[@name='purchase_price']").clear()
    driver.find_element(By.XPATH, "//input[@name='purchase_price']").send_keys("10")
    # currency (Валюта)
    loc='//select[@name="purchase_price_currency_code"]'
    dropdown = driver.find_element(By.XPATH, loc)
    driver.execute_script(f"arguments[0].selectedIndex={1}; arguments[0].dispatchEvent(new Event('change'))", dropdown)
    # Price USD
    driver.find_element(By.XPATH, "//input[@name='prices[USD]']").send_keys("10")
    time.sleep(1)
    # ------Сохранить товар---------
    driver.find_element(By.XPATH, '//button[@name="save"]').click()
    time.sleep(1)
    # перейти по ссылке http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=0
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=0")
    # проверить наличие добавленного товара в списке
    loc_new_duck=f"//a[text()='{Name}']"
    try:
        driver.find_element(By.XPATH,loc_new_duck)
        print("Новый продукт добавлен на сайт.")
    except NoSuchElementException:
        print("Новый продукт не добавлен на сайт.")
    time.sleep(5)