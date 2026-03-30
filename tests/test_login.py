import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
import allure

# Link feature file
scenarios('../features/login.feature')


@given("I am on the login page")
def open_login_page(login_page):
    """Open the login page"""
    login_page.open()


@when(parsers.parse('I enter username "{username}"'))
def enter_username(login_page, username):
    """Enter username in the login form"""
    from selenium.webdriver.common.by import By
    login_page.type_text((By.ID, "username"), username)


@when(parsers.parse('I enter password "{password}"'))
def enter_password(login_page, password):
    """Enter password in the login form"""
    from selenium.webdriver.common.by import By
    login_page.type_text((By.ID, "password"), password)


@when("I click the login button")
def click_login_button(login_page):
    """Click the login button"""
    from selenium.webdriver.common.by import By
    login_page.click((By.ID, "login-button"))


@then("I should see the success message")
def verify_success_message(login_page):
    """Verify success message is displayed"""
    message = login_page.get_success_message()
    assert "success" in message.lower(), f"Expected success message, got: {message}"


@then("I should be logged in")
def verify_logged_in(login_page):
    """Verify user is logged in"""
    assert login_page.is_logged_in(), "User is not logged in"


@then("I should see an error message")
def verify_error_message(login_page):
    """Verify error message is displayed"""
    message = login_page.get_error_message()
    assert "error" in message.lower() or "invalid" in message.lower(), f"Expected error message, got: {message}"


@then("I should not be logged in")
def verify_not_logged_in(login_page):
    """Verify user is not logged in"""
    assert not login_page.is_logged_in(), "User should not be logged in"


@then(parsers.parse('I should see "{expected_result}"'))
def verify_result(login_page, expected_result):
    """Verify expected result"""
    if expected_result == "success":
        message = login_page.get_success_message()
        assert "success" in message.lower()
    elif expected_result == "error":
        message = login_page.get_error_message()
        assert "error" in message.lower() or "invalid" in message.lower()
