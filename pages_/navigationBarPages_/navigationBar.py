from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import logger


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = (By.ID, "nav-cart")
        self.__languageChangingFlagLocator = (By. XPATH, "//a[@id='icp-nav-flyout']/span/span[2]/div")
        self.__languageChangingButtonLocator = (By.CLASS_NAME, "icp-nav-link-inner")
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__accountAndListsContainerLocator = (By.ID, "nav-link-accountList")
        self.__signOutButtonLocator = (By.ID, "nav-item-signout")

    def fill_in_search_field(self, text):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_on_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_on_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def get_cart_count_element(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_element_text(cartCountElement))

    def validate_emptiness_of_cart_by_its_quantity(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        if int(self._get_element_text(cartCountElement)) == 0:
            logger("INFO", "The Cart Is Empty.")
        else:
            logger("ERROR", "The Cart Is Not Empty")
            exit(4)

    def click_on_language_changing_button(self):
        languageChangingButtonElement = self._find_element(self.__languageChangingButtonLocator)
        self._click(languageChangingButtonElement)

    def get_language_changing_flag_icon_text(self):
        languageChangingFlagIconElement = self._find_element(self.__languageChangingFlagLocator)
        return self._get_element_text(languageChangingFlagIconElement)

    def move_mouse_to_account_and_lists_container(self):
        accountAndListsContainerElement = self._find_element(self.__accountAndListsContainerLocator)
        self._mouse_move(accountAndListsContainerElement)

    def click_on_sign_out_button(self):
        signOutButtonElement = self._find_element(self.__signOutButtonLocator)
        self._click(signOutButtonElement)


