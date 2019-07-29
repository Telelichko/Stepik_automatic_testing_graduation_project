from pages.locators import ProductPageLocators    # Импорт класса, описывающего главную страницу
from pages.base_page import BasePage            # Импорт базового класса BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def get_msg_product(self):
        msg_product = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT).text
        print(msg_product)
        return msg_product

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_name_in_msg_success(self):
        msg_product = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT).text
        product_name = self.get_product_name()
        assert product_name in msg_product, "Message does not contain product name"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(product_price)
        return product_price

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't  presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"





