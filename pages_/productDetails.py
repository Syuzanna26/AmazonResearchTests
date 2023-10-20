from selenium.webdriver.common.by import By

class ProductDetails():
    def __init__(self, driver):
        self.driver = driver

    def click_on_add_to_cart_button(self):
        addToCartButton = self.driver.find_element(By. ID, "add-to-cart-button")
        addToCartButton.click()

