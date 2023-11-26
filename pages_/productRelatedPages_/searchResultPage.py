from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__sortByButtonLocator = (By.CLASS_NAME, "a-dropdown-prompt")
        self.__bestSellersButtonLocator = (By.ID, "s-result-sort-select_5")
        self.__firstProductLocator = (By.XPATH, "//img[@class='s-image'][1]")
        self.__firstProductNameLocator = (By. XPATH, "(//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4'])[1]")
        self.__firstProductPriceLocator = (By. XPATH, "(//span[@class='a-price'])[1]")

    def click_on_sort_by_button(self):
        sortByButtonElement = self._find_element(self.__sortByButtonLocator)
        self._click(sortByButtonElement)

    def click_on_best_sellers_button(self):
        bestSellersButtonElement = self._find_element(self.__bestSellersButtonLocator)
        self._click(bestSellersButtonElement)

    def click_on_first_product_from_list(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click(firstProductElement)

    def get_first_Product_name(self):
        firstProductNameElement = self._find_element(self.__firstProductNameLocator)
        return self._get_element_text(firstProductNameElement)

    def get_first_product_price(self):
        firstProductPriceElement = self._find_element(self.__firstProductPriceLocator)
        return self._get_element_text(firstProductPriceElement)
