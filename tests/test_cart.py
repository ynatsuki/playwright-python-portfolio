from pages.cart_page import CartPage


def test_card_page_displayed(cart_page: CartPage) -> None:
    assert cart_page.is_displayed()
