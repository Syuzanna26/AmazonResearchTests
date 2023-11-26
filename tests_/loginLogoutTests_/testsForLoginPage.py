import time
from pages_.loginLogoutPages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidPassword,userWithInvalidUsername, signInPageUrl
from tests_.baseTest import BaseTestWithoutLogin


class Login(BaseTestWithoutLogin):

    def test_positive_login(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(validUser.username)
        loginPageObj.click_on_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(7)  # time sleep is done to avoid captcha given by Amazon website
        loginPageObj.click_on_signin_button()

        self.assertEqual("Amazon.com. Spend less. Smile more.", loginPageObj._get_title())

    def test_negative_login_with_invalid_password(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidPassword.username)
        loginPageObj.click_on_continue_button()
        loginPageObj.fill_password_field(userWithInvalidPassword.password)
        time.sleep(7)  # time sleep is done to avoid captcha given by Amazon website
        loginPageObj.click_on_signin_button()

        self.assertEqual("Your password is incorrect", loginPageObj.get_incorrect_password_error_message_text())

    def test_negative_login_with_invalid_email(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidUsername.username)
        loginPageObj.click_on_continue_button()

        self.assertEqual("We cannot find an account with that email address", loginPageObj.get_incorrect_email_error_message_text())

