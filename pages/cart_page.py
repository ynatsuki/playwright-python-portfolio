from pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.get_by_text("Checkout")

    def click_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)
