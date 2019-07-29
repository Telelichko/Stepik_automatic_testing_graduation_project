from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest
import time


@pytest.mark.login
class TestLoginFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.should_be_login_link()

@pytest.mark.guest_add_to_cart
class TestGuestAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    def test_guest_cant_see_success_message_after_adding_product_to_cart(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.add_product_to_cart()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.add_product_to_cart()
        page.get_product_name_in_msg_success()

@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "User_password"
        password_confirm = password
        login_page.register_new_user(email, password, password_confirm)
        login_page.should_be_authorized_user()
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.add_product_to_cart()
        page.get_product_name_in_msg_success()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    page = CartPage(browser, browser.current_url)
    page.open()
    page.should_not_be_products_in_the_basket()
    page.should_not_be_products_in_the_basket_msg()

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_be_disappeared_success_message()

