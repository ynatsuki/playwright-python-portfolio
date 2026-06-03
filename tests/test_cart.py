from pages.cart_page import CartPage


def test_card_page_displayed(cart_page: CartPage) -> None:
    assert cart_page.is_displayed()


def test_go_to_continue_shopping(cart_page: CartPage) -> None:
    product_page = cart_page.go_to_continue_shopping()
    assert product_page.is_loaded()


def test_remove_products(cart_page: CartPage) -> None:
    cart_page.remove_products()
    assert not cart_page.is_product_in_cart()
