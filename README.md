# Python Pytest BDD Automation Framework

Comprehensive BDD (Behavior Driven Development) test automation framework built with Python, Pytest, Selenium WebDriver, and Allure reporting for readable, maintainable test automation.

## Features

- **Pytest Framework** - Powerful testing with fixtures and plugins
- **BDD with Pytest-BDD** - Gherkin syntax for behavior-driven tests
- **Selenium WebDriver** - Cross-browser automation
- **Page Object Model** - Clean, maintainable test architecture
- **Allure Reports** - Beautiful, detailed HTML reports
- **WebDriver Manager** - Automatic driver management
- **Parallel Execution** - Fast test runs with pytest-xdist
- **Data-Driven Testing** - Faker integration for test data
- **API Testing** - Requests library integration

## Project Structure

```
python-pytest-bdd-framework/
├── features/
│   └── login.feature         # BDD feature files
├── pages/
│   ├── base_page.py         # Base Page Object
│   └── login_page.py        # Login Page Object
├── step_defs/
│   └── test_login_steps.py  # Step definitions
├── tests/
│   └── test_example.py      # Regular pytest tests
├── utils/
│   ├── config.py            # Configuration
│   └── helpers.py           # Helper functions
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Chrome/Firefox browser

## Installation

```bash
# Clone the repository
git clone https://github.com/Cheetahrevive/python-pytest-bdd-framework.git

# Navigate to project directory
cd python-pytest-bdd-framework

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run BDD tests
```bash
pytest --gherkin-terminal-reporter
```

### Run tests in parallel
```bash
pytest -n 4
```

### Run specific test file
```bash
pytest tests/test_example.py
```

### Run with HTML report
```bash
pytest --html=report.html --self-contained-html
```

### Run with Allure report
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Run tests by marker
```bash
pytest -m smoke
pytest -m regression
```

## Writing BDD Tests

### Feature File (login.feature)
```gherkin
Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "user@example.com"
    And I enter password "password123"
    And I click the login button
    Then I should be redirected to the dashboard
```

### Step Definitions (test_login_steps.py)
```python
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios('../features/login.feature')

@given('I am on the login page')
def navigate_to_login(browser):
    login_page = LoginPage(browser)
    login_page.navigate()

@when('I enter username "<username>"')
def enter_username(browser, username):
    login_page = LoginPage(browser)
    login_page.enter_username(username)

@then('I should be redirected to the dashboard')
def verify_dashboard(browser):
    assert 'dashboard' in browser.current_url
```

## Page Object Example

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
```

## Configuration

### pytest.ini
```ini
[pytest]
markers =
    smoke: Smoke tests
    regression: Regression tests
    api: API tests
```

## Allure Reports

To generate and view Allure reports:
```bash
# Generate reports
pytest --alluredir=allure-results

# Serve reports
allure serve allure-results
```

## CI/CD Integration

This framework is ready for CI/CD with:
- GitHub Actions
- Jenkins
- GitLab CI
- CircleCI

## Best Practices

1. Use Page Object Model for UI interactions
2. Write clear, readable Gherkin scenarios
3. Keep step definitions simple and reusable
4. Use fixtures for test setup/teardown
5. Implement proper waits (explicit over implicit)
6. Use markers to organize tests
7. Generate reports for every test run

## Author

**Cheetahrevive** - Senior QA Automation Engineer

## License

MIT
