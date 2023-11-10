from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_.customLogger import *


class MyListener(AbstractEventListener):
    # def before_navigate_to(self, url, driver):
    #     print("Before navigating to ", url)

    def after_navigate_to(self, url, driver):
        logger("INFO", f"After navigating to {url}")

    # def before_navigate_back(self, driver):
    #     print("before navigating back ", driver.current_url)

    def after_navigate_back(self, driver):
        logger("INFO", f"After navigating back {driver.current_url}")

    # def before_navigate_forward(self, driver):
    #     logger("INFO", f"Before navigating forward ", driver.current_url)

    def after_navigate_forward(self, driver):
        logger("INFO", f"After navigating forward {driver.current_url}")

    # def before_find(self, by, value, driver):
    #     print("before find")

    def after_find(self, by, value, driver):
        logger("INFO", "After Finding")

    # def before_click(self, element, driver):
    #     print("before_click")

    def after_click(self, element, driver):
        logger("INFO", "After clicking")

    # def before_change_value_of(self, element, driver):
    #     print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        logger("INFO", "The value of element is changed")

    # def before_execute_script(self, script, driver):
    #     print("before_execute_script")

    def after_execute_script(self, script, driver):
        logger("INFO", "after_execute_script")

    # def before_close(self, driver):
    #     print("before_close")

    def after_close(self, driver):
        logger("INFO", "After closing")

    # def before_quit(self, driver):
    #     print("before_quit")

    def after_quit(self, driver):
        logger("INFO", "After quiting")

    def on_exception(self, exception, driver):
        logger("WARNING", "on_exception")
