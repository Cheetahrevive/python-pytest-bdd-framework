from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Base Page class with common methods for all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Navigate to {url}")
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)

    @allure.step("Find element by {locator}")
    def find_element(self, locator, timeout=10):
        """Find a single element with explicit wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="element_not_found",
                          attachment_type=allure.attachment_type.PNG)
            raise

    @allure.step("Find elements by {locator}")
    def find_elements(self, locator, timeout=10):
        """Find multiple elements with explicit wait"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Click element {locator}")
    def click(self, locator):
        """Click on an element"""
        element = self.find_element(locator)
        element.click()

    @allure.step("Type '{text}' into {locator}")
    def type_text(self, locator, text):
        """Type text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Get text from {locator}")
    def get_text(self, locator):
        """Get text from an element"""
        return self.find_element(locator).text

    @allure.step("Check if element {locator} is visible")
    def is_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name="screenshot"):
        """Take screenshot and attach to Allure report"""
        allure.attach(self.driver.get_screenshot_as_png(), name=name,
                      attachment_type=allure.attachment_type.PNG)

    def get_page_title(self):
        """Get current page title"""
        return self.driver.title
