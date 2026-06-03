from typing import Optional

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> Optional[str]:
        return self.error_message.text_content()
