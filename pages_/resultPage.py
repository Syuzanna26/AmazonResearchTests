from selenium.webdriver.common.by import By

class ResultPage():
    def __init__(self, driver):
        self.driver = driver

    def click_on_first_product_from_list(self):
        firstProductElement = self.driver.find_element(By. XPATH, "//img[@class='s-image'][1]")
        firstProductElement.click()


