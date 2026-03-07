from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.FORMSET),\
            "Корзина должна быть пустой, но в ней есть товар"
    def should_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Отсутствует текст о пустой корзине"