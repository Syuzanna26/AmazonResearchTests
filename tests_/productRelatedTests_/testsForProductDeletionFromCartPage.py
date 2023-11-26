from pages_.navigationBarPages_.navigationBar import NavigationBar
from pages_.navigationBarPages_.cartPage import CartPage
from pages_.productRelatedPages_.searchResultPage import SearchResultPage
from pages_.productRelatedPages_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogin
from testData_.testData import product1


class ProductDeletion(BaseTestWithLogin):

    def test_for_empty_cart_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_cart_button()
        navigationBarObj.get_cart_count_element()
        navigationBarObj.validate_emptiness_of_cart_by_its_quantity()

        cartPagrObj = CartPage(self.driver)

        self.assertEqual("Your Amazon Cart is empty.", cartPagrObj.get_cart_emptiness_validating_message_text())

    def test_for_first_product_deletion(self):
        navigatinBarObj = NavigationBar(self.driver)
        navigatinBarObj.click_on_cart_button()
        cartQuantityBeforeProductDeletion = navigatinBarObj.get_cart_count_element()
        if cartQuantityBeforeProductDeletion == 0:
            navigatinBarObj.fill_in_search_field(product1)
            navigatinBarObj.click_on_search_button()
            searchResultPageObj = SearchResultPage(self.driver)
            searchResultPageObj.click_on_first_product_from_list()
            productDetailsPageObj = ProductDetailsPage(self.driver)
            productDetailsPageObj.click_on_add_to_cart_button()
            navigatinBarObj.click_on_cart_button()
        cartPageObj = CartPage(self.driver)
        cartPageObj.delete_first_product_from_cart()
        cartQuantityAfterProductDeletion = navigatinBarObj.get_cart_count_element()

        self.assertEqual(cartQuantityBeforeProductDeletion - 1, cartQuantityAfterProductDeletion)

    def test_for_deleting_all_products(self):
        navigatinBarObj = NavigationBar(self.driver)
        navigatinBarObj.click_on_cart_button()

        cartPageObj = CartPage(self.driver)
        cartPageObj.delete_all_products_from_cart()

        self.assertEqual(0, navigatinBarObj.get_cart_count_element())

