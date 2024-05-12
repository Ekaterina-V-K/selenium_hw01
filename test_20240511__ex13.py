import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


link = "http://localhost/litecart/en/"

# @pytest.fixture(params=['chrome','edge','firefox'])
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


def add_prods_to_cart(drv):
    wait = WebDriverWait(drv, 5)
    for _ in range(3):
        # 2) открыть первый товар из списка
        loc_first_duck=(By.XPATH,'//ul[@class="listing-wrapper products"]/li/a[@class="link"]')
        # loc_first_duck = (By.XPATH, '//a[@title="Yellow Duck"]')  # проверка на желтой утке с размером
        drv.find_element(*loc_first_duck).click()
        # 2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
        # size Если есть размер - его нужно указать
        loc_size=(By.XPATH,'//select[@name="options[Size]"]')
        try:
            # Находим элемент size
            el_size = drv.find_element(*loc_size)
            drv.execute_script(f"arguments[0].selectedIndex={1}; arguments[0].dispatchEvent(new Event('change'))",
                                  el_size)
        except NoSuchElementException:
            print("Элемент изменения размера не найден у товара")
        loc_cart_counter = (By.XPATH, '//span[@class="quantity"]')
        current_cart_items=drv.find_element(*loc_cart_counter).get_attribute("textContent")
        loc_button=(By.XPATH,'//button[@value="Add To Cart"]')
        drv.find_element(*loc_button).click()
        # 3) подождать, пока счётчик товаров в корзине обновится
        NewTextCounter=str(int(current_cart_items)+1)
        wait.until(EC.text_to_be_present_in_element(loc_cart_counter, NewTextCounter))
        # 4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
        drv.back()

def test_ex13(driver):
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 30)
    # 1) открыть главную страницу
    driver.get(link)
    # 2-4)
    add_prods_to_cart(driver)
    # 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
    loc_cart=(By.XPATH,'//a[@href="http://localhost/litecart/en/checkout" and @class="link"]')
    element = wait.until(EC.presence_of_element_located(loc_cart))
    element.click()
    # 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
    loc_remove_button=(By.XPATH, '//button[@value="Remove"]')
    remove_buttons=driver.find_elements(*loc_remove_button)
    count_remove_buttons=len(remove_buttons)
    for i in range( count_remove_buttons):
        button=wait.until(EC.visibility_of_element_located(loc_remove_button))
        button.click()

    time.sleep(5)
