from pages.locators import CartPageLocators    # Импорт класса, описывающего главную страницу
from pages.base_page import BasePage            # Импорт базового класса BasePage

class CartPage(BasePage):
    def should_be_products_in_the_basket(self):
        assert self.is_element_present(*CartPageLocators.BASKET_HAVE_PRODUCTS_TO_BUY), \
        "Products in basket are not presented, but should be"

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_HAVE_PRODUCTS_TO_BUY), \
        "Products in basket are presented, but should not be"

    def should_be_products_in_the_basket_msg(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_EMPTY_MSG), \
        "Products in basket are not presented, but should be"

    def should_not_be_products_in_the_basket_msg(self):
        assert self.is_element_present(*CartPageLocators.BASKET_EMPTY_MSG), \
        "Products in basket are presented, but should not be"





