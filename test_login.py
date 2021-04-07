from .pages.product_page import ProductPage
from .pages.product_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import faker

def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        f=faker.Faker()
        email=f.email()
        password="olegtikhonov"
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.register_new_user(email, password)
        time.sleep(5)
