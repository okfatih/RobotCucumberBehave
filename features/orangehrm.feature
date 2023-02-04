Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHTM home Page
    Given launch browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser