from selenium.webdriver.common.by import By


class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def fill_in_search_field(self, text):
        searchFieldElement = self.driver.find_element(By. ID, "twotabsearchtextbox")
        searchFieldElement.send_keys(text)

    def click_on_search_button(self):
        searchButtonElement = self.driver.find_element(By. ID, "nav-search-submit-button")
        searchButtonElement.click()

    def click_on_cart_button(self):
        cartButtonElement = self.driver.find_element(By. ID, "nav-cart")
        cartButtonElement.click()

    def click_on_returns_orders_button(self):
        returnsOrdersButton = self.driver.find_element(By. ID, "nav-orders")
        returnsOrdersButton.click()