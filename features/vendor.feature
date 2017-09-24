Feature: Vendor Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders a coke
    Given I am a vendor
    When I order a "Coke"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order a "Coke" for "1" dollar
    When I insert "1" dollar
    Then the displays says "Thank you"