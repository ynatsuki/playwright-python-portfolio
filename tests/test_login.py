from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_successful_login(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert product_page.is_loaded()


def test_failed_login(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert not product_page.is_loaded()


def test_add_and_remove_item_from_cart(product_page):
    product_page.add_to_cart()
    product_page.expect_cart_count(1)

    product_page.remove_from_cart()
    product_page.expect_cart_count(0)


def test_checkout(product_page):
    product_page.add_to_cart()

    cart_page = product_page.go_to_cart()
    checkout_page = cart_page.click_checkout()

    checkout_page.set_first_name("John")
    checkout_page.set_last_name("Doe")
    checkout_page.set_zip_code("12345")
    checkout_overview_page = checkout_page.click_continue()
    checkout_complete_page = checkout_overview_page.click_finish()

    assert checkout_complete_page.is_complete_message_displayed()

    product_page = checkout_complete_page.click_back_home()
    assert product_page.is_loaded()
