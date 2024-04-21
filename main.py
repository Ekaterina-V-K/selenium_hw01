import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element("name","username").send_keys("admin")
    driver.find_element("name","password").send_keys("admin")
    driver.find_element("name","login").click()
    #WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))
    driver.quit()