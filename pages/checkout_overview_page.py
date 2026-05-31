from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.get_by_role("button", name="Finish")

    def click_finish(self):
        self.finish_button.click()
        return CheckoutCompletePage(self.page)
