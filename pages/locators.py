from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG = (By.NAME, "registration_submit")

class ProductPageLocators:
    ADD_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages .alertinner strong")
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main p.price_color")

class BasketPageLocators:
    FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p a")