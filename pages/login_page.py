from pages.base_page import BasePage            # Импорт базового класса BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password, password_confirm):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        login_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password.send_keys(password_confirm)
        register_btn.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert str(self.browser.current_url) == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
