import time
from pages_.navigationBarPages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin
from pages_.loginPage_.loginPage import LoginPage


class SigningOut(BaseTestWithLogin):

    def test_for_sign_out(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.move_mouse_to_account_and_lists_container()
        time.sleep(5)
        navigationBarObj.click_on_sign_out_button()
        time.sleep(5)
        loginPageObj = LoginPage(self.driver)

        self.assertEqual("Sign-In", loginPageObj._get_title())

