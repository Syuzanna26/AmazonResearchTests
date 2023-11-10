import time
import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from pages_.loginPage import LoginPage
from pages_.cartPage import CartPage
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver


class ProductDeletion(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field("syuzanna26.12@gmail.com")
        self.loginPageObj.click_on_continue_button()
        self.loginPageObj.fill_password_field("Davit2602")
        time.sleep(7)  # time sleep is done to avoid captcha given by Amazon website
        self.loginPageObj.click_on_signin_button()

    def test_for_empty_cart_page(self):  # Test Case for empty cart validation.
        cartIconOnNavBarObj = NavigationBar(self.driver)
        cartIconOnNavBarObj.click_on_cart_icon()

        cartPageObj = CartPage(self.driver)
        cartCurrentElement = cartPageObj.get_cart_count_element()

        self.assertEqual(cartCurrentElement, 0)

    def test_for_first_product_deletion(self):  # Test case for deleting the first product from a cart.
        cartIconOnNavBarObj = NavigationBar(self.driver)
        cartIconOnNavBarObj.click_on_cart_icon()

        cartPageObj = CartPage(self.driver)
        cartCurrentElement = cartPageObj.get_cart_count_element()
        cartPageObj.delete_first_product_from_cart()
        cartElementAfterDelation = cartPageObj.get_cart_count_element()

        self.assertEqual(cartCurrentElement - 1, cartElementAfterDelation)

    def test_for_deleting_all_products(self):  # Test case for deleting all existing products from a cart.
        cartIconOnNavBarObj = NavigationBar(self.driver)
        cartIconOnNavBarObj.click_on_cart_icon()

        cartPageObj = CartPage(self.driver)
        cartCurrentElement = cartPageObj.get_cart_count_element()
        while cartCurrentElement != 0:
            cartPageObj.delete_first_product_from_cart()
            cartCurrentElement -= 1

    def tearDown(self):
        self.driver.close()
