from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """Login Page Object with locators and methods"""

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
    LOGOUT_BUTTON = (By.ID, "logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://example.com/login"

    @allure.step("Open login page")
    def open(self):
        """Navigate to login page"""
        self.navigate_to(self.url)

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        """Perform login with credentials"""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Get error message")
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    @allure.step("Get success message")
    def get_success_message(self):
        """Get success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)

    @allure.step("Check if user is logged in")
    def is_logged_in(self):
        """Check if logout button is visible"""
        return self.is_visible(self.LOGOUT_BUTTON)

    @allure.step("Logout")
    def logout(self):
        """Click logout button"""
        self.click(self.LOGOUT_BUTTON)
