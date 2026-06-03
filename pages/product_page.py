from playwright.sync_api import Page, expect

from pages.cart_page import CartPage


class ProductPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_to_cart_button = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_from_cart_button = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_icon = page.locator('[data-test="shopping-cart-badge"]')
        self.sort_dropdown = self.page.locator('[data-test="product-sort-container"]')

    def is_loaded(self) -> bool:
        return self.page.get_by_text("Product").is_visible()

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def remove_from_cart(self) -> None:
        self.remove_from_cart_button.click()

    def expect_cart_count(self, count: int) -> None:
        if count == 0:
            expect(self.cart_icon).not_to_be_visible()
        else:
            expect(self.cart_icon).to_have_text(str(count))

    def get_cart_count(self) -> int:
        if not self.cart_icon.is_visible():
            return 0

        text = self.cart_icon.text_content()
        assert text is not None

        return int(text)

    def go_to_cart(self) -> CartPage:
        self.cart_icon.click()
        return CartPage(self.page)

    def select_sort(self, sort_option: str) -> None:
        self.sort_dropdown.select_option(sort_option)

    def get_item_names(self) -> list[str]:
        return self.page.locator(
            '[data-test="inventory-item-name"]'
        ).all_text_contents()

    def get_item_prices(self) -> list[float]:
        prices = self.page.locator(
            '[data-test="inventory-item-price"]'
        ).all_text_contents()
        return [float(price.replace("$", "")) for price in prices]
