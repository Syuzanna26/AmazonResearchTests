from pages_.navigationBar import NavigationBar
from pages_.searchResultPage import SearchResultPage
from pages_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogin
from testData_.testData import product1


# Test case for product searching and adding it successfully in cart.
class ProductSearching(BaseTestWithLogin):

    def test_for_product_searching_adding_in_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_in_search_field(product1)
        navigationBarObj.click_on_search_button()

        searchResultPageObj = SearchResultPage(self.driver)
        searchResultPageObj.click_on_sort_by_button()
        searchResultPageObj.click_on_best_sellers_button()
        searchResultPageObj.click_on_first_product_from_list()

        navigationBarObj = NavigationBar(self.driver)
        cartQuantityBeforeAddingproduct = navigationBarObj.get_cart_count_element()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_on_add_to_cart_button()
        cartQuantityAfterAddingProduct = navigationBarObj.get_cart_count_element()

        self.assertEqual(cartQuantityBeforeAddingproduct + 1, cartQuantityAfterAddingProduct)
