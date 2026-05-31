from pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.get_by_text("Checkout")
        self.your_cart_text = page.get_by_text("Your Cart")

    def click_checkout(self):
        self.checkout_button.click()

    def go_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)

    def is_displayed(self):
        return self.your_cart_text.is_visible()
