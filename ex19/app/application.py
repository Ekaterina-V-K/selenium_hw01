from selenium import webdriver
from ex19.pages.cart_Page import CartPage
from ex19.pages.main_Page import MainPage
from ex19.pages.product_Page import ProductPage

class Application:

    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.productPage=ProductPage(driver)
        self.cartPage = CartPage(driver)

    def addProductsToCart(self, driver):
        self.mainPage.moveToMainPage()
        for i in range(1, 4):
            self.mainPage.moveToProductCart(driver, i)
            if self.productPage.isFindedElementSize(driver):
                self.productPage.selectSizeDucks(driver)
            self.productPage.addProduct(driver)
            self.productPage.waitAddedToCart(driver, i)

    def removeProduct(self, driver):
        self.cartPage.moveToCartPage(driver)
        while not self.cartPage.isCartEmpty(driver):
            self.cartPage.removeProduct(driver)


