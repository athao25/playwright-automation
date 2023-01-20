Feature: Login Feature

    Scenario: Verify login with valid user
    Given I am on the saucedemo login page
    When I enter my username and password
    Then I should be logged in