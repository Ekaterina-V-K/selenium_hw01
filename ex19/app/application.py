from ex19.pages.cart_Page import CartPage
from ex19.pages.main_Page import MainPage
from ex19.pages.product_Page import ProductPage

class Application:

    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.productPage=ProductPage(driver)
        self.cartPage = CartPage(driver)

    def addProductsToCart(self, NumOfProducts):
        self.mainPage.moveToMainPage()
        for i in range(1, NumOfProducts):
            self.mainPage.moveToProductCart(i)
            if self.productPage.isFindedElementSize():
                self.productPage.selectSizeDucks()
            self.productPage.addProduct()
            self.productPage.waitAddedToCart(i)

    def removeProduct(self):
        self.cartPage.moveToCartPage()
        while not self.cartPage.isCartEmpty():
            self.cartPage.removeProduct()