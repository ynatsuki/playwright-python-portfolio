from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage


def test_checkout(product_page: ProductPage) -> None:
    product_page.add_to_cart()

    cart_page = product_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_page.set_first_name("John")
    checkout_page.set_last_name("Doe")
    checkout_page.set_zip_code("12345")
    checkout_overview_page = checkout_page.go_to_checkout_overview()
    checkout_complete_page = checkout_overview_page.click_finish()

    assert checkout_complete_page.is_complete_message_displayed()

    product_page = checkout_complete_page.click_back_home()
    assert product_page.is_loaded()


def test_failed_checkout_empty_first_name(checkout_page: CheckoutPage) -> None:
    checkout_page.set_first_name("")
    checkout_page.set_last_name("Doe")
    checkout_page.set_zip_code("12345")
    checkout_page.click_continue()

    assert checkout_page.is_error_message_displayed("first_name")


def test_failed_checkout_empty_last_name(checkout_page: CheckoutPage) -> None:
    checkout_page.set_first_name("John")
    checkout_page.set_last_name("")
    checkout_page.set_zip_code("12345")
    checkout_page.click_continue()

    assert checkout_page.is_error_message_displayed("last_name")


def test_failed_checkout_empty_zip_code(checkout_page: CheckoutPage) -> None:
    checkout_page.set_first_name("John")
    checkout_page.set_last_name("Doe")
    checkout_page.set_zip_code("")
    checkout_page.click_continue()

    assert checkout_page.is_error_message_displayed("zip_code")
