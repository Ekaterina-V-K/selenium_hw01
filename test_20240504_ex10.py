import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import ast

link="http://localhost/litecart/en/"
utochka="//div[@id='box-campaigns']/div[@class='content']/ul[@class='listing-wrapper products']/li"
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_ex10(driver):
    # открыть главную страницу
    driver.get(link)
    main_utka=driver.find_element(By.XPATH,utochka)

    #Найдем первый товар в блоке Campaigns
    #___на главной странице:___
    #а)получим название товара
    main_name_utochka=main_utka.find_element(By.XPATH, "a[@class='link']").get_attribute("title")
    #б)получим цены товара (обычная и акционная)
    main_price_utochka=main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/s[@class="regular-price"]').get_attribute("textContent")
    main_sale_utochka=main_utka.find_element(By.XPATH, 'a/div[@class="price-wrapper"]/strong[@class="campaign-price"]').get_attribute("textContent")
    #в)проверим что обычная цена зачеркнутая
    main_price_X=(main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/s[@class="regular-price"]').value_of_css_property('text-decoration-line')=='line-through')
    if not main_price_X:
        print("Шрифт основной цены на главной странице не перечеркнутый")
    #  и серая (R=G=B)
    main_price_color=main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/s[@class="regular-price"]').value_of_css_property('color')
    r, g, b, alpha = ast.literal_eval(main_price_color.strip("rgba"))
    if not (r==g==b):
        print("Цвет основной цены на главной странице не серый")

    #г)проверим что акционная цена жирная
    main_sale_is_bold=int(main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/strong[@class="campaign-price"]').value_of_css_property('font-weight'))>400
    if not main_sale_is_bold:
        print("Шрифта акционной цены на главной странице не жирный")
    #  и красная (G=0 AND B=0)
    main_sale_color=main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/strong[@class="campaign-price"]').value_of_css_property('color')
    r, g, b, alpha = ast.literal_eval(main_sale_color.strip("rgba"))
    if not (g==0 and b==0):
        print("Цвет шрифта акционной цены на главной странице не красный")

    #д)акционная цена крупнее чем обычная (сравнить размер шрифта)
    main_price_font_size=main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/s[@class="regular-price"]').value_of_css_property('font-size')
    main_sale_font_size=main_utka.find_element(By.XPATH, 'a/div[@class ="price-wrapper"]/strong[@class="campaign-price"]').value_of_css_property('font-size')
    # удаляем "px" в конце и преобразуем в целое число
    main_price_font_size=float(main_price_font_size[:-2])
    main_sale_font_size = float(main_sale_font_size[:-2])
    if main_sale_font_size<=main_price_font_size:
        print("Размер шрифта акционной цены на главной странице не крупнее, чем размер шрифта обычной цены")

    main_utka.find_element(By.XPATH, 'a').click()
    time.sleep(3)

    # ___на странице товара:___
    # а)получим название товара
    sub_utka_el=driver.find_element(By.XPATH, "//div[@id='box-product']")
    sub_name_utochka=sub_utka_el.find_element(By.XPATH, "div[@style]/h1[@class='title']").get_attribute("textContent")
    # б)получим цены товара (обычная и акционная)
    sub_price_utochka=driver.find_element(By.XPATH,"//s[@class='regular-price']").get_attribute('textContent')
    sub_sale_utochka=driver.find_element(By.XPATH,"//strong[@class='campaign-price']").get_attribute('textContent')
    # в)проверим что обычная цена зачеркнутая
    sub_price_X = (driver.find_element(By.XPATH,"//s[@class='regular-price']").value_of_css_property('text-decoration-line') == 'line-through')
    if not sub_price_X:
        print("Шрифт основной цены на странице товара не перечеркнутый")
    #  и серая (R=G=B)
    sub_price_color = driver.find_element(By.XPATH,"//s[@class='regular-price']").value_of_css_property('color')
    r, g, b, alpha = ast.literal_eval(sub_price_color.strip("rgba"))
    if not (r == g == b):
        print("Цвет основной цены на странице товара не серый")
    # г)проверим что акционная цена жирная
    sub_sale_is_bold = int(driver.find_element(By.XPATH,"//strong[@class='campaign-price']").value_of_css_property('font-weight')) > 400
    if not sub_sale_is_bold:
        print("Шрифта акционной цены на странице товара не жирный")
    #  и красная (G=0 AND B=0)
    sub_sale_color = driver.find_element(By.XPATH,"//strong[@class='campaign-price']").value_of_css_property('color')
    r, g, b, alpha = ast.literal_eval(sub_sale_color.strip("rgba"))
    if g != 0 and b != 0:
        print("Цвет шрифта акционной цены на странице товара не красный")
    # д)акционная цена крупнее чем обычная (сравнить размер шрифта)
    sub_price_font_size = driver.find_element(By.XPATH,"//s[@class='regular-price']").value_of_css_property('font-size')
    sub_sale_font_size = driver.find_element(By.XPATH,"//strong[@class='campaign-price']").value_of_css_property('font-size')
    # удаляем "px" в конце и преобразуем в целое число
    sub_price_font_size = float(sub_price_font_size[:-2])
    sub_sale_font_size = float(sub_sale_font_size[:-2])
    if sub_sale_font_size <= sub_price_font_size:
        print("Размер шрифта акционной цены на странице товара не крупнее, чем размер шрифта обычной цены")
    # ---------------

    #общее:
    # а)сравнить цены между страницами
    if main_price_utochka!=sub_price_utochka:
        print("На главной странице и на странице товара не совпадают обычные цены товара")
    if main_sale_utochka!=sub_sale_utochka:
        print("На главной странице и на странице товара не совпадают акционные цены товара")
    # б)сравнить названия между страницами
    if main_name_utochka!=sub_name_utochka:
        print("На главной странице и на странице товара не совпадает текст названия товара")

