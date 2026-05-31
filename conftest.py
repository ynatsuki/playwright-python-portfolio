import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture
def product_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return ProductPage(page)


@pytest.fixture
def cart_page(product_page):
    product_page.add_to_cart()
    return product_page.go_to_cart()


@pytest.fixture
def checkout_page(product_page):
    product_page.add_to_cart()
    cart_page = product_page.go_to_cart()
    return cart_page.go_to_checkout()
