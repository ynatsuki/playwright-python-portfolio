import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return ProductPage(page)


@pytest.fixture
def product_page_object(page: Page) -> ProductPage:
    return ProductPage(page)


@pytest.fixture
def cart_page(product_page: ProductPage) -> CartPage:
    product_page.add_to_cart()
    return product_page.go_to_cart()


@pytest.fixture
def cart_page_object(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(product_page: ProductPage) -> CheckoutPage:
    product_page.add_to_cart()
    cart_page = product_page.go_to_cart()
    return cart_page.go_to_checkout()
