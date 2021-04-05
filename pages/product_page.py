from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .locators import MainPageLocators
from .basket_page import BasketPage


class ProductPage(BasePage):
   def should_be_add_button(self):
       assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"
   def add_product_to_basket(self):
       button=self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
       button.click()
   def should_be_succes_message(self):
       button=self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
       print(button.text)
       assert button.text=="Coders at Work", "Wrong message after adding product to the basket"
   def should_not_be_success_message(self):
       assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), \
       "Success message is presented, but should not be"
   def success_message_should_be_disappeare(self):
       assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), \
       "Success message is not disappeared"

