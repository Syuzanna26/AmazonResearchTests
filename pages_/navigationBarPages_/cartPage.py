from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__deleteFirstProductButtonLocator = (By.XPATH, "//input[@value='Delete'][1]")
        self.__cartEmptinessValidatingMessageLocator = (By. CLASS_NAME, "a-spacing-mini.a-spacing-top-base")

    def delete_first_product_from_cart(self):
        deleteFirstProductButtonElement = self._find_element(self.__deleteFirstProductButtonLocator)
        self._click(deleteFirstProductButtonElement)

    def delete_all_products_from_cart(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        cartQuantityNumberElement = int(self._get_element_text(cartCountElement))
        while cartQuantityNumberElement != 0:
            self.delete_first_product_from_cart()
            cartQuantityNumberElement -= 1

    def get_cart_emptiness_validating_message_text(self):
        cartEmptinessValidatingMessageElement = self._find_element(self.__cartEmptinessValidatingMessageLocator)
        return self._get_element_text(cartEmptinessValidatingMessageElement)



