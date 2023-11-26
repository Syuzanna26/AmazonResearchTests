from tests_.baseTest import BaseTestWithLogin
from pages_.navigationBarPages_.navigationBar import NavigationBar
from testData_.testData import product1
from pages_.productRelatedPages_.searchResultPage import SearchResultPage
from pages_.productRelatedPages_.productDetailsPage import ProductDetailsPage


class CheckProductDetails(BaseTestWithLogin):

    def test_for_name_and_price_Validation(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_in_search_field(product1)
        navigationBarObj.click_on_search_button()
        searchResultPageObj = SearchResultPage(self.driver)
        name = searchResultPageObj.get_first_Product_name()
        price = searchResultPageObj.get_first_product_price()
        searchResultPageObj.click_on_first_product_from_list()
        productDetailsPage = ProductDetailsPage(self.driver)
        expectedName = productDetailsPage.get_product_name()
        expectedPrice = productDetailsPage.get_product_price()

        self.assertEqual(name, expectedName, "ERROR: Name Does Not Match")
        self.assertEqual(price, expectedPrice, "ERROR: Price Does Not Match")

