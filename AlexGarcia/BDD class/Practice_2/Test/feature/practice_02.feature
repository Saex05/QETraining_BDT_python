@any
Feature:Withdraw Fixed Amount

    Scenario Outline: Withdraw fixed amount
      Given I have <Balance> in my account
        When I choose to withdraw the fixed amount of <Withdrawl>
      Then I should receive <Received> cash
        And the balance of my account should be <Remaining>


    Scenario: ejemplo 00


    Scenario: ejemplo 01

    Examples:
    |Balance|Withdrawl|Received|Remaining|
    |$500|$50|$50|$450|
    |$500|$100|$100|$400|
    |$500|$200|$200|$300|