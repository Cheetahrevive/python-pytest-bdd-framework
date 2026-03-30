Feature: User Login
  As a user
  I want to login to the application
  So that I can access protected features

  Background:
    Given I am on the login page

  @smoke @login
  Scenario: Successful login with valid credentials
    When I enter username "testuser"
    And I enter password "testpass123"
    And I click the login button
    Then I should see the success message
    And I should be logged in

  @regression @login
  Scenario: Failed login with invalid credentials
    When I enter username "invaliduser"
    And I enter password "wrongpass"
    And I click the login button
    Then I should see an error message
    And I should not be logged in

  @regression @login
  Scenario Outline: Login with multiple credentials
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see "<expected_result>"

    Examples:
      | username    | password    | expected_result |
      | validuser   | validpass   | success         |
      | invaliduser | invalidpass | error           |
      | emptyuser   |             | error           |
      |             | emptypass   | error           |
