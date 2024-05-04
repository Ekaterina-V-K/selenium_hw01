import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


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
    #в)проверим что обычная цена зачеркнутая и серая (R=G=B)
    # main_price_X=
    # main_price_gray=

    #г)проверим что акционная цена жирная и красная (G=0 AND B=0)
    #д)акционная цена крупнее чем обычная (сравнить размер шрифта)

    main_utka.find_element(By.XPATH, 'a').click()
    time.sleep(3)


    # ___на странице товара:___
    # а)получим название товара
    sub_name_utochka=''
    # б)получим цены товара (обычная и акционная)
    sub_price_utochka=0
    sub_sale_utochka=0
    # в) проверим что обычная цена зачеркнутая и серая (R=G=B)
    # г) проверим что акционная цена жирная и красная (G=0 AND B=0)
    # д) акционная цена крупнее чем обычная (сравнить размер шрифта)

    #общее:
    # а)сравнить цены между страницами
    if main_price_utochka!=sub_price_utochka:
        print("На главной странице и на странице товара не совпадают обычные цены товара")
    if main_sale_utochka!=sub_sale_utochka:
        print("На главной странице и на странице товара не совпадают акционные цены товара")
    # б)сравнить названия между страницами
    if main_name_utochka!=sub_name_utochka:
        print("На главной странице и на странице товара не совпадает текст названия товара")

