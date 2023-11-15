import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.languageSettingsPage import LanguageSettings
from pages_.navigationBar import NavigationBar
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LanguageSet(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("syuzanna26.12@gmail.com")
        loginPageObj.click_on_continue_button()
        loginPageObj.fill_password_field("Davit2602")
        time.sleep(7)  # time sleep is done to avoid captcha given by Amazon website
        loginPageObj.click_on_signin_button()

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_language_changing_button()

    def test_for_changing_language_to_spanish(self):
        languageSettingsObj = LanguageSettings(self.driver)
        languageSettingsObj.select_spanish_language_button()
        languageSettingsObj.click_on_save_changes_button()

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.validate_language_icon_text()