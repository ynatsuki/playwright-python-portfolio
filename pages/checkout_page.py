from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def set_first_name(self, name):
        self.first_name_input.fill(name)

    def set_last_name(self, name):
        self.last_name_input.fill(name)

    def set_zip_code(self, code):
        self.zip_code_input.fill(code)

    def click_continue(self):
        self.continue_button.click()
        return CheckoutOverviewPage(self.page)
