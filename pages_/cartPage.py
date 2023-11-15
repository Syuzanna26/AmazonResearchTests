from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__deleteFirstProductButtonLocator = (By.XPATH, "//input[@value='Delete'][1]")

    def get_cart_count_element(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_element_text(cartCountElement))

    def delete_first_product_from_cart(self):
        deleteFirstProductButtonElement = self._find_element(self.__deleteFirstProductButtonLocator)
        self._click(deleteFirstProductButtonElement)

    def validate_emptiness_of_cart(self):
        cartCounElement = self._find_element(self.__cartCountLocator)
        if int(self._get_element_text(cartCounElement)) == 0:
            print("Warning! The Cart Is Empty")



