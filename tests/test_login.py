from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_successful_login(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert product_page.is_loaded()
