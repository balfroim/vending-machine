"""
Feature: Vending Machine accepts Quarters, Dimes, and Nickles. It does not accept pennies

  Scenario: Vending Machine accepts quarters
    Given I have a "Quarter"
    When I insert a "Quarter" into the vending machine
    Then the vending machine accepts the "Quarter"

  Scenario: Vending Machine accepts Dimes
    Given I have a "Dime"
    When I insert a "Dime" into the vending machine
    Then the vending machine accepts the "Dime"

  Scenario: Vending Machine accepts Nickels
    Given I have a "Nickel"
    When I insert a "Nickel" into the vending machine
    Then the vending machine accepts the "Nickel"

  Scenario: Vending Machine does not accept Pennies
    Given I have a "Penny"
    When I insert a "Penny" into the vending machine
    Then the vending machine does not accepts the coin

Feature: Payment Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders an item
    Given I am a vendor
    When I go to order an item
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".25" dollar
    When I insert ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".50" dollar
    When I insert ".25"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".25"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".30"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"
    And ".05" cents is returned

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
from behave import given, when, then
from src.vending_machine import VendingMachine
from src.coin_validator import CoinValidator
from src.model.dime import Dime
from src.model.nickel import Nickel
from src.model.penny import Penny
from src.model.quarter import Quarter
from src.model.coin import Coin
from src.model.product import Product


@given('I have a "{coin}"')
def step_impl(context, coin):
    context.coin = coin
      
@when('I insert a "{payment}" into the vending machine')
def step_impl(context, payment):
    product = Product('item', context.coin.value)
    context.vending_machine = VendingMachine(product, CoinValidator(), product.price)
    context.vending_machine.insert_coins(context.coin)

@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
    assert context.vending_machine.accepted_coins == [context.coin]

@then('the vending machine does not accepts the coin')
def step_impl(context):
    assert context.vending_machine.accepted_coins == []

@given('I am a vendor')
def step_impl(context):
    pass

@when('I go to order an item')
def step_impl(context):
    context.vending_machine = VendingMachine(None, CoinValidator(), 0)

@then('the displays says "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == 'Insert Coins'

@given('order an item for "{price}" dollar')
def step_impl(context, price):
    context.price = float(price)

@when('I insert "{payment}"')
def step_impl(context, payment):
    product = Product('item', context.price)
    context.vending_machine = VendingMachine(product, CoinValidator(), product.price)
    context.vending_machine.insert_coins(Coin(float(payment)))

@then('the displays says "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == 'Thank You'

@then('"{change}" cents is returned')
def step_impl(context, change):
    assert context.vending_machine.change == float(change)

@given('I order "{product}" for "{price}"')
def step_impl(context, product, price):
    context.product = Product(product, float(price))

@when('I select the respective button')
def step_impl(context):
    pass

@then('the product is dispensed')
def step_impl(context):
    assert context.vending_machine.product == context.product

@then('the machine displays "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == 'Insert Coins'

@then('the machine displays "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == 'Thank You'

@when('I have inserted "{quantity}" "{coin}"')
def step_impl(context, quantity, coin):
    for i in range(int(quantity)):
        context.vending_machine.insert_coins(Coin(float(coin)))

@given('I purchase an item for "{price}"')
def step_impl(context, price):
    context.price = float(price)

@given('I have inserted "{payment}"')
def step_impl(context, payment):
    context.payment = float(payment)

@when('I insert another "{payment}"')
def step_impl(context, payment):
    context.vending_machine.insert_coins(Coin(float(payment)))