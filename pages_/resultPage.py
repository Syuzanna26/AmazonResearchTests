from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductLocator = (By.XPATH, "//img[@class='s-image'][1]")

    def click_on_first_product_from_list(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click(firstProductElement)
