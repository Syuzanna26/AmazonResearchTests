from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class ProductDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonLocator)
        self._click(addToCartButtonElement)
