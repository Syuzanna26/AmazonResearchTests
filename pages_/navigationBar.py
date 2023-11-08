from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartIconLocator = (By.ID, "nav-cart")

    def fill_in_search_field(self, text):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_on_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_on_cart_icon(self):
        cartIconElement = self._find_element(self.__cartIconLocator)
        self._click(cartIconElement)
