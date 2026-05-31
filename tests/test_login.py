from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_successful_login(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert product_page.is_loaded()


def test_failed_login_incorrect_password(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert not product_page.is_loaded()


def test_failed_login_incorrect_username(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("wrong_username", "secret_sauce")

    assert not product_page.is_loaded()


def test_failed_login_empty_username(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("", "secret_sauce")

    assert login_page.get_error_message() == "Epic sadface: Username is required"
    assert not product_page.is_loaded()


def test_failed_login_empty_password(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "")

    assert login_page.get_error_message() == "Epic sadface: Password is required"
    assert not product_page.is_loaded()


def test_failed_login_locked_out(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert (
        login_page.get_error_message()
        == "Epic sadface: Sorry, this user has been locked out."
    )
    assert not product_page.is_loaded()
