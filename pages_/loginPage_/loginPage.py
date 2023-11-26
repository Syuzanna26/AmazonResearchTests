from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")
        self.__incorrectPasswordErrorMessageTextLocator = (By.CLASS_NAME, "a-list-item")
        self.__incorrectEmailErrorMessageTextLocator = (By.CLASS_NAME, "a-list-item")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_on_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_on_signin_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click(signInButtonElement)

    def get_incorrect_password_error_message_text(self):
        incorrectPasswordErrorMessageTextElement = self._find_element(self.__incorrectPasswordErrorMessageTextLocator)
        return self._get_element_text(incorrectPasswordErrorMessageTextElement)

    def get_incorrect_email_error_message_text(self):
        incorrectEmailErrorMessageTextElement = self._find_element(self.__incorrectEmailErrorMessageTextLocator)
        return self._get_element_text(incorrectEmailErrorMessageTextElement)
