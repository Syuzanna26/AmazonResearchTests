from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__sortByButtonLocator = (By.CLASS_NAME, "a-dropdown-prompt")
        self.__bestSellersButtonLocator = (By.ID, "s-result-sort-select_5")
        self.__firstProductLocator = (By.XPATH, "//img[@class='s-image'][1]")

    def click_on_sort_by_button(self):
        sortByButtonElement = self._find_element(self.__sortByButtonLocator)
        self._click(sortByButtonElement)

    def click_on_best_sellers_button(self):
        bestSellersButtonElement = self._find_element(self.__bestSellersButtonLocator)
        self._click(bestSellersButtonElement)

    def click_on_first_product_from_list(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click(firstProductElement)
