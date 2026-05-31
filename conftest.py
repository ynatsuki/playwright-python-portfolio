import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture
def product_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return ProductPage(page)
