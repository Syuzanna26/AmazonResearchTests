from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartIconLocator = (By.ID, "nav-cart")
        self.__languageChangingButtonLocator = (By.CLASS_NAME, "icp-nav-link-inner")
        self.__languageIconTextLocator = (By.XPATH, "//a[@id='icp-nav-flyout']/span/span[2]/div")

    def fill_in_search_field(self, text):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_on_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_on_cart_icon(self):
        cartIconElement = self._find_element(self.__cartIconLocator)
        self._click(cartIconElement)

    def click_on_language_changing_button(self):
        languageChangingButtonElement = self._find_element(self.__languageChangingButtonLocator)
        self._click(languageChangingButtonElement)

    def validate_language_icon_text(self):
        languageIconTextElement = self._find_element(self.__languageIconTextLocator)
        if self._get_element_text(languageIconTextElement) != "ES":
            print("Error: The Language Is Not Changed")
            exit(3)
