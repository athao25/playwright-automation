import pytest
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.navigate_to_homepage = self.page.goto("https://www.saucedemo.com/")
        self.username_locator = "[data-test='username']"
        self.password_locator = "[data-test='password']"
        self.login_button_locator = "[data-test='login-button']"
        self.product_page = "Products"
        
    def enter_username_password(self,username:str,password:str):
        self.page.locator(self.username_locator).click()
        self.page.locator(self.username_locator).fill(username)
        self.page.locator(self.password_locator).click()
        self.page.locator(self.password_locator).fill(password)
        self.page.locator(self.login_button_locator).click()

    def check_logged_in(self):
        self.page.get_by_text(self.product_page).click()
