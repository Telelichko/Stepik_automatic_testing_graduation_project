from selenium.webdriver.common.by import By


class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class CartPageLocators(object):
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_HAVE_PRODUCTS_TO_BUY = (By.CSS_SELECTOR, ".basket-title .col-sm-6.h3")

class LoginPageLocators(object):
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    LOGIN_URL = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form button")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators(object):
    BASKET_BTN = (By.CSS_SELECTOR, ".header.container-fluid a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MSG_PRODUCT = (By.CSS_SELECTOR, "#messages .alert>.alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    SUCCESS_MESSAGE = MSG_PRODUCT


