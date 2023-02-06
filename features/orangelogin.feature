Feature: OrangeHRM Login
  Scenario: Login to OrangeHrm with valid parameters
    Given I launch Chrome browser
    When  I open homepage
    And   I enter username "admin" and password "admin123"
    And   I click on login button
    Then  User must successfully login to dashboard