import time
import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from pages_.loginPage import LoginPage
from pages_.resultPage import ResultPage
from pages_.productDetails import ProductDetails
from pages_.cartPage import CartPage
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver


# Test case for product searching and adding it successfully in a cart.
class ProductSearching(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
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

    def test_for_product_searching_adding_in_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_in_search_field("Monster truck")
        navigationBarObj.click_on_search_button()

        resultPageObj = ResultPage(self.driver)
        resultPageObj.click_on_first_product_from_list()

        productDetailsObj = ProductDetails(self.driver)
        cartPageObj = CartPage(self.driver)
        cartPreviousElement = cartPageObj.get_cart_count_element()  # for looking previous quantity of cart
        productDetailsObj.click_on_add_to_cart_button()
        cartCurrentElement = cartPageObj.get_cart_count_element()

        self.assertEqual(cartPreviousElement + 1, cartCurrentElement)

    def tearDown(self):
        self.driver.close()
