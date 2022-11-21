# Path: features/product.feature

from behave import given, when, then
from src.vending_machine import VendingMachine

"""
Feature: Product Feature
  Acceptance criteria for selecting various products from the vending machine

  Scenario: Customer orders Chips
    Given I order "Chips" for ".50"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Cola
    Given I order "Cola" for "1.00"
    When I select the respective button
    And I have inserted "4" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Candy
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    And I have inserted "1" "Dime"
    And I have inserted "1" "Nickle"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer does not have enough coins to complete transaction
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the machine displays "Insert Coins"
"""

@given('I order "{product}" for "{price}"')
def step_impl(context, product, price):
    context.product = product
    context.price = price

@when('I select the respective button')
def step_impl(context):
    context.vending_machine = VendingMachine()
    context.vending_machine.order_item(context.product, context.price)

@when('I have inserted "{quantity}" "{coin}"')
def step_impl(context, quantity, coin):
    for i in range(int(quantity)):
        context.vending_machine.insert_coin(coin)

@then('the product is dispensed')
def step_impl(context):
    assert context.vending_machine.dispense_product(context.product)

@then('the machine displays "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == "Thank you"

@then('the machine displays "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == "Insert Coins"

