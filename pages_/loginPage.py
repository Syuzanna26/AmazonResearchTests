from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        pass
    def fill_usernamname_field(self, username):
        userNameFieldElement = self.driver.find_element(By. ID, "ap_email")
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(username)

    def click_on_continu_button(self):
        continuButtonElement = self.driver.find_element(By.ID, "continue")
        continuButtonElement.click()

    def fill_password_field(self, password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)

    def click_on_signin_button(self):
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
    
