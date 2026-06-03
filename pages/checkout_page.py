from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def set_first_name(self, name: str) -> None:
        self.first_name_input.fill(name)

    def set_last_name(self, name: str) -> None:
        self.last_name_input.fill(name)

    def set_zip_code(self, code: str) -> None:
        self.zip_code_input.fill(code)

    def click_continue(self) -> None:
        self.continue_button.click()

    def go_to_checkout_overview(self) -> CheckoutOverviewPage:
        self.continue_button.click()
        return CheckoutOverviewPage(self.page)

    def is_error_message_displayed(self, error_type: str) -> bool:
        error_type = error_type.strip().lower()

        if error_type == "first_name":
            return self.page.get_by_text("Error: First Name is required").is_visible()
        elif error_type == "last_name":
            return self.page.get_by_text("Error: Last Name is required").is_visible()
        elif error_type == "zip_code":
            return self.page.get_by_text("Error: Postal Code is required").is_visible()
        return False
