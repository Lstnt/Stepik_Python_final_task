from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_LINK)
        add_to_cart.click()

    def