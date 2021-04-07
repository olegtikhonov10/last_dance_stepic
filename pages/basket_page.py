from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Basket is not empty"
def basket_is_empty_text_is_displayed(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Basket is not emty' text is not shown"
