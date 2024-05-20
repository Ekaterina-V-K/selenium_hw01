import pytest
from ex19.app.application import Application
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    application = Application(driver)
    application.addProductsToCart(driver)
    application.removeProduct(driver)


