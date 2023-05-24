Feature: Test functionality of SwagLabs Mobile Application

  Scenario: Validate access as standard_user
    Given I am able to open the application
    When I enter using standard_user credentials
    And I click the login button
    And I add to cart the first item
    And go to cart
    And click hamburger and choose logout
    Then I am able to test SwagLabs Mobile

  Scenario: Validate access as locked_out_user
    Given I am able to open the application
    When I enter using locked_out_user credentials
    And I click the login button
    Then I am able to test SwagLabs Mobile

  Scenario: Validate access for as problem_user
    Given I am able to open the application
    When I enter using problem_user credentials
    And I click the login button
    And I add to cart the first item
    And go to cart
    And click hamburger and choose logout
    Then I am able to test SwagLabs Mobile
#
#  Scenario: Login, Add to Cart and Logout in SwagLabs Mobile Application
#    Given I am able to open the application
#    When I enter using standard_user credentials
#    And I click the login button
#    And I add to cart the first item
#    And go to cart
#    And click hamburger and choose logout
#    Then I am able to test SwagLabs Mobile