from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_LINK)
        add_to_cart.click()

    def should_message_about_adding(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message == name,f"В сообщение о добавлении указано '{message}', но добавляли товар '{name}'"

    def should_message_about_cart_value(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET).text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert message == price, f"Стоимость корзины '{message}', но добавляли товар стоимостью '{price}'"