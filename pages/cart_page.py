from typing import TYPE_CHECKING

from playwright.sync_api import Page, expect

from pages.checkout_page import CheckoutPage

if TYPE_CHECKING:
    from pages.product_page import ProductPage


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.get_by_text("Checkout")
        self.your_cart_text = page.get_by_text("Your Cart")
        self.click_continue_shopping_button = page.get_by_text("Continue Shopping")
        self.product_name = page.locator('[data-test="inventory-item-name"]')

    def click_checkout(self) -> None:
        self.checkout_button.click()

    def go_to_checkout(self) -> CheckoutPage:
        self.checkout_button.click()
        return CheckoutPage(self.page)

    def is_displayed(self) -> bool:
        return self.your_cart_text.is_visible()

    def click_continue_shopping(self) -> None:
        self.click_continue_shopping_button.click()

    def go_to_continue_shopping(self) -> "ProductPage":
        from pages.product_page import ProductPage

        self.click_continue_shopping_button.click()
        return ProductPage(self.page)

    def remove_products(self) -> None:
        remove_buttons = self.page.get_by_role("button", name="Remove").all()

        for button in remove_buttons:
            button.click()
            expect(button).not_to_be_visible()

    def is_product_in_cart(self) -> bool:
        return self.product_name.is_visible()
