from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, f"Expected substring 'login' in URL, but received {self.url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is missing"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG).click()