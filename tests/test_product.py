import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize(
    ("sort_value", "reverse"),
    [
        ("az", False),
        ("za", True),
    ],
)
def test_sort_items_by_name(
    product_page: ProductPage, sort_value: str, reverse: bool
) -> None:
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
def test_sort_items_by_price(
    product_page: ProductPage, sort_value: str, reverse: bool
) -> None:
    product_page.select_sort(sort_value)
    actual_prices = product_page.get_item_prices()
    expected_prices = sorted(actual_prices, reverse=reverse)
    assert actual_prices == expected_prices


def test_add_and_remove_item_from_cart(product_page: ProductPage) -> None:
    product_page.add_to_cart()
    assert product_page.get_cart_count() == 1

    product_page.remove_from_cart()
    assert product_page.get_cart_count() == 0
