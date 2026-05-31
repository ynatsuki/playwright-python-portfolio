class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.thank_you_message = page.get_by_text("Thank you for your order!")
        self.back_home_button = page.get_by_role("button", name="Back Home")

    def is_complete_message_displayed(self):
        return self.thank_you_message.is_visible()

    def click_back_home(self):
        # Import here to avoid circular imports
        from pages.product_page import ProductPage

        self.back_home_button.click()
        return ProductPage(self.page)
