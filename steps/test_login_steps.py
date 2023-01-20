from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("I am on the saucedemo login page")
def navigate_to_homepage(login_page: LoginPage):
    login_page.navigate_to_homepage()


@when("I enter my username and password")
def enter_username_password(page: Page):
    login_page = LoginPage(page)
    login_page.enter_username_password()

@then("I should be logged in")
def check_logged_in(page: Page):
    login_page = LoginPage(page)
    login_page.check_logged_in()