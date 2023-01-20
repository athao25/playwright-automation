from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page


scenarios("../features/login.feature")

@given("I am on the saucedemo login page")
def navigate_to_homepage(page: Page):
    page.goto("https://www.saucedemo.com/")

@when("I enter my username and password")
def enter_username_password(page: Page):
    page.locator("[data-test='username']").click()
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").click()
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

@then("I should be logged in")
def check_logged_in(page: Page):
    page.get_by_text("Products").click()
