from playwright.sync_api import expect

from pages.cart_page import CartPage


class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_from_cart_button = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_icon = page.locator('[data-test="shopping-cart-badge"]')
        self.sort_dropdown = self.page.locator('[data-test="product-sort-container"]')

    def is_loaded(self):
        return self.page.get_by_text("Product").is_visible()

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def remove_from_cart(self):
        self.remove_from_cart_button.click()

    def expect_cart_count(self, count):
        if count == 0:
            expect(self.cart_icon).not_to_be_visible()
        else:
            expect(self.cart_icon).to_have_text(str(count))

    def get_cart_count(self):
        if not self.cart_icon.is_visible():
            return 0

        return int(self.cart_icon.text_content())

    def go_to_cart(self):
        self.cart_icon.click()
        return CartPage(self.page)

    def select_sort(self, sort_option):
        self.sort_dropdown.select_option(sort_option)

    def get_item_names(self):
        return self.page.locator(
            '[data-test="inventory-item-name"]'
        ).all_text_contents()

    def get_item_prices(self):
        prices = self.page.locator(
            '[data-test="inventory-item-price"]'
        ).all_text_contents()
        return [float(price.replace("$", "")) for price in prices]
