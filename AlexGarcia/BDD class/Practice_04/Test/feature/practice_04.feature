@any
Feature:Withdraw Fixed Amount

    Scenario: API
      Given I have a connection to http://todo.ly
        When I GET
      Then I receive status code 200

