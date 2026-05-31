import pytest

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


@pytest.mark.parametrize(
    ("sort_value", "reverse"),
    [
        ("az", False),
        ("za", True),
    ],
)
def test_sort_items_by_name(product_page, sort_value, reverse):
    product_page.select_sort(sort_value)
    actual_names = product_page.get_item_names()
    expected_names = sorted(actual_names, reverse=reverse)
    assert actual_names == expected_names


@pytest.mark.parametrize(
    ("sort_value", "reverse"),
    [
        ("lohi", False),
        ("hilo", True),
    ],
)
def test_sort_items_by_price(product_page, sort_value, reverse):
    product_page.select_sort(sort_value)
    actual_prices = product_page.get_item_prices()
    expected_prices = sorted(actual_prices, reverse=reverse)
    assert actual_prices == expected_prices


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
